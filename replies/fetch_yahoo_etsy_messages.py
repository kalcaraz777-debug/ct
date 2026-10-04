#!/usr/bin/env python3
"""Read Etsy notification emails from the shop's Yahoo inbox, read-only, and print them as JSON.

- Opens INBOX with IMAP EXAMINE (read-only): nothing is marked read, moved or deleted.
- Only emails from an etsy.com sender are returned; everything else in the mailbox is ignored.
- Credentials come from the environment, never from code or chat:
    YAHOO_EMAIL          the shop's Yahoo address
    YAHOO_APP_PASSWORD   a Yahoo app password (Yahoo Account security → Generate app password);
                         revoke it there at any time.
- Works through the HTTPS CONNECT proxy in HTTPS_PROXY when set (cloud sessions), else direct.

Usage:
  python3 fetch_yahoo_etsy_messages.py --since-days 3
  python3 fetch_yahoo_etsy_messages.py --check-connection   # no login; verifies the server is reachable
"""
import argparse, base64, email, imaplib, json, os, re, socket, ssl, sys, urllib.parse
from datetime import datetime, timedelta, timezone
from email.header import decode_header, make_header
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser

HOST, PORT = "imap.mail.yahoo.com", 993


def proxied_socket(host, port, timeout=30):
    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    if not proxy:
        return socket.create_connection((host, port), timeout)
    u = urllib.parse.urlparse(proxy if "://" in proxy else "http://" + proxy)
    s = socket.create_connection((u.hostname, u.port or 80), timeout)
    req = f"CONNECT {host}:{port} HTTP/1.1\r\nHost: {host}:{port}\r\n"
    if u.username:
        cred = base64.b64encode(f"{urllib.parse.unquote(u.username)}:{urllib.parse.unquote(u.password or '')}".encode()).decode()
        req += f"Proxy-Authorization: Basic {cred}\r\n"
    s.sendall((req + "\r\n").encode())
    resp = b""
    while b"\r\n\r\n" not in resp:
        chunk = s.recv(4096)
        if not chunk:
            break
        resp += chunk
    status = resp.split(b"\r\n", 1)[0]
    if b" 200" not in status:
        s.close()
        raise OSError(f"proxy refused CONNECT: {status.decode(errors='replace')}")
    return s


class IMAP(imaplib.IMAP4_SSL):
    def _create_socket(self, timeout):
        ctx = ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE") or None)
        if os.path.exists("/root/.ccr/ca-bundle.crt"):
            ctx.load_verify_locations("/root/.ccr/ca-bundle.crt")
        return ctx.wrap_socket(proxied_socket(self.host, self.port, timeout or 30), server_hostname=self.host)


class _Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts = []; self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ("style", "script"): self.skip += 1
        if tag in ("br", "p", "div", "tr", "li"): self.parts.append("\n")
    def handle_endtag(self, tag):
        if tag in ("style", "script") and self.skip: self.skip -= 1
    def handle_data(self, d):
        if not self.skip: self.parts.append(d)


def body_text(msg):
    plain, html = None, None
    for part in msg.walk():
        ctype = part.get_content_type()
        if part.get_content_maintype() == "multipart" or part.get("Content-Disposition", "").startswith("attachment"):
            continue
        try:
            payload = part.get_payload(decode=True)
            text = payload.decode(part.get_content_charset() or "utf-8", "replace") if payload else ""
        except Exception:
            continue
        if ctype == "text/plain" and plain is None: plain = text
        elif ctype == "text/html" and html is None: html = text
    if plain is None and html:
        p = _Text(); p.feed(html); plain = "".join(p.parts)
    text = re.sub(r"[ \t]+", " ", plain or "")
    return re.sub(r"\n\s*\n+", "\n\n", text).strip()[:4000]


def hdr(v):
    try: return str(make_header(decode_header(v or "")))
    except Exception: return v or ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since-days", type=float, default=3)
    ap.add_argument("--check-connection", action="store_true")
    a = ap.parse_args()

    M = IMAP(HOST, PORT)
    if a.check_connection:
        print("connected:", M.welcome.decode(errors="replace")[:80]); M.logout(); return

    user, pw = os.environ.get("YAHOO_EMAIL"), os.environ.get("YAHOO_APP_PASSWORD")
    if not user or not pw:
        sys.exit("YAHOO_EMAIL / YAHOO_APP_PASSWORD are not set in this environment.")
    M.login(user, pw)
    M.select("INBOX", readonly=True)
    since = (datetime.now(timezone.utc) - timedelta(days=a.since_days)).strftime("%d-%b-%Y")
    typ, data = M.search(None, "SINCE", since, "FROM", "etsy.com")
    out = []
    for num in (data[0].split() if data and data[0] else []):
        typ, msgdata = M.fetch(num, "(BODY.PEEK[])")
        raw = next((x[1] for x in msgdata if isinstance(x, tuple)), None)
        if not raw:
            continue
        msg = email.message_from_bytes(raw)
        sender = hdr(msg.get("From"))
        if "etsy.com" not in sender.lower():
            continue
        try: received = parsedate_to_datetime(msg.get("Date")).astimezone(timezone.utc).isoformat()
        except Exception: received = None
        out.append({
            "message_id": (msg.get("Message-ID") or "").strip("<> "),
            "from": sender, "subject": hdr(msg.get("Subject")), "received": received,
            "reply_to": hdr(msg.get("Reply-To")), "body": body_text(msg),
        })
    M.logout()
    print(json.dumps({"fetched_at": datetime.now(timezone.utc).isoformat(), "count": len(out), "emails": out}, indent=1))


if __name__ == "__main__":
    main()

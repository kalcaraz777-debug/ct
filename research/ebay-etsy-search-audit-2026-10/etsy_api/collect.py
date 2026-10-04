#!/usr/bin/env python3
"""
etsy_market_api_quickstart.py  --  READ-ONLY Etsy Open API v3 collector for the Riverside Greenhouses study.

Uses ONLY endpoints that the live OpenAPI spec (https://www.etsy.com/openapi/generated/oas/3.0.0.json, Last-Modified 2026-10-02)
marks as API-key-only (no OAuth):
    GET /v3/application/openapi-ping
    GET /v3/application/shops?shop_name=...                      (findShops)
    GET /v3/application/shops/{shop_id}                          (getShop)
    GET /v3/application/shops/{shop_id}/listings/active          (findAllActiveListingsByShop)
    GET /v3/application/shops/{shop_id}/reviews                  (getReviewsByShop)
    GET /v3/application/listings/active?keywords=..&sort_on=score  (findAllListingsActive)
    GET /v3/application/listings/batch?listing_ids=..&includes=Images,Shop   (getListingsByListingIds)

Auth (since 2026-02-09): header  x-api-key: <keystring>:<shared_secret>   (both values from https://www.etsy.com/developers/your-apps)
Credentials are read from the environment (ETSY_KEYSTRING, ETSY_SHARED_SECRET); never hard-code or commit them.

Usage
    python3 etsy_market_api_quickstart.py --selftest                 # offline logic test with a fake transport, no network, no key
    ETSY_KEYSTRING=... ETSY_SHARED_SECRET=... python3 etsy_market_api_quickstart.py --ping
    ETSY_KEYSTRING=... ETSY_SHARED_SECRET=... python3 etsy_market_api_quickstart.py --run --out ./etsy_api_out

Politeness: sleeps to honour x-remaining-this-second / x-remaining-today, backs off on 429 using retry-after, ~1 request/second by default.
Nothing here has been run against the live API (no key was available); --selftest exercises the parsing and ranking code on mock data shaped like the spec.
"""
import argparse, csv, json, os, sys, time, urllib.parse, urllib.request, urllib.error

BASE = "https://openapi.etsy.com"
OWNER_SHOP_NAME = "RvsdGreenhouses"
PLANT_KEYWORDS = ["hoya sunrise", "hoya kerrii", "hoya australis lisa", "hoya carnosa compacta", "syngonium chiapense", "syngonium pink splash", "syngonium mojito",
                  "raven zz plant", "monstera peru", "rhaphidophora tetrasperma", "philodendron pink princess", "philodendron micans", "philodendron brasil",
                  "monstera siltepecana", "peperomia hope", "watermelon peperomia", "pilea peperomioides", "calathea setosa", "calathea rattlesnake", "satin pothos",
                  "cebu blue pothos", "christmas cactus", "sansevieria moonshine", "texas ebony plant", "hoya cummingiana"]


class Etsy:
    def __init__(self, keystring, secret, min_interval=1.0, transport=None):
        self.key = "%s:%s" % (keystring, secret)          # REQUIRED format since 2026-02-09
        self.min_interval = min_interval
        self.last = 0.0
        self.transport = transport or self._http
        self.remaining_today = None

    def _http(self, url, headers):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status, dict(r.headers), r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            return e.code, dict(e.headers), e.read().decode("utf-8", "replace")

    def get(self, path, **params):
        qs = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None}, doseq=True)
        url = BASE + path + (("?" + qs) if qs else "")
        for attempt in range(5):
            wait = self.min_interval - (time.time() - self.last)
            if wait > 0: time.sleep(wait)
            self.last = time.time()
            status, hdr, body = self.transport(url, {"x-api-key": self.key, "Accept": "application/json"})
            h = {k.lower(): v for k, v in hdr.items()}
            if "x-remaining-today" in h:
                try: self.remaining_today = int(h["x-remaining-today"])
                except ValueError: pass
            if status == 429:
                time.sleep(float(h.get("retry-after", "2")) + 0.5); continue
            if status == 200:
                return json.loads(body)
            raise RuntimeError("HTTP %s for %s : %s" % (status, path, body[:300]))
        raise RuntimeError("giving up after repeated 429s: " + path)

    # ---- thin wrappers -------------------------------------------------
    def ping(self): return self.get("/v3/application/openapi-ping")
    def find_shop(self, name): return self.get("/v3/application/shops", shop_name=name, limit=10)
    def shop(self, shop_id): return self.get("/v3/application/shops/%d" % shop_id)
    def shop_listings(self, shop_id, limit=100, offset=0): return self.get("/v3/application/shops/%d/listings/active" % shop_id, limit=limit, offset=offset)
    def shop_reviews(self, shop_id, limit=100, offset=0): return self.get("/v3/application/shops/%d/reviews" % shop_id, limit=limit, offset=offset)
    def search(self, keywords, limit=100, offset=0): return self.get("/v3/application/listings/active", keywords=keywords, sort_on="score", limit=limit, offset=offset)
    def batch(self, ids): return self.get("/v3/application/listings/batch", listing_ids=",".join(str(i) for i in ids), includes="Images,Shop")


def price_of(l):
    p = l.get("price") or {}
    try: return round(p["amount"] / p["divisor"], 2)
    except Exception: return None


def rank_keyword(api, keyword, owner_shop_id, pages=3):
    """Return rows for the top pages*100 results of a score-sorted keyword search + owner's best rank."""
    rows, owner_ranks = [], []
    for pg in range(pages):
        d = api.search(keyword, limit=100, offset=pg * 100)
        for i, l in enumerate(d.get("results", [])):
            rank = pg * 100 + i + 1
            rows.append(dict(keyword=keyword, rank=rank, listing_id=l["listing_id"], shop_id=l["shop_id"], title=l.get("title"), price=price_of(l), quantity=l.get("quantity"),
                             num_favorers=l.get("num_favorers"), tags="|".join(l.get("tags") or []), created_ts=l.get("created_timestamp") or l.get("creation_timestamp"),
                             updated_ts=l.get("updated_timestamp") or l.get("last_modified_timestamp"), taxonomy_id=l.get("taxonomy_id"), has_variations=l.get("has_variations"),
                             shipping_profile_id=l.get("shipping_profile_id"), is_owner=(l["shop_id"] == owner_shop_id), url=l.get("url")))
            if l["shop_id"] == owner_shop_id: owner_ranks.append(rank)
        if len(d.get("results", [])) < 100: break
    return rows, owner_ranks


def collect(api, outdir):
    os.makedirs(outdir, exist_ok=True)
    print("ping:", api.ping())
    shops = api.find_shop(OWNER_SHOP_NAME)
    me = next(s for s in shops["results"] if s["shop_name"].lower() == OWNER_SHOP_NAME.lower())
    sid = me["shop_id"]
    shop = api.shop(sid)
    json.dump(shop, open(os.path.join(outdir, "owner_shop.json"), "w"), indent=1)
    print("owner shop: id=%s active_listings=%s sold=%s review_count(past year)=%s review_average=%s" % (sid, shop.get("listing_active_count"), shop.get("transaction_sold_count"), shop.get("review_count"), shop.get("review_average")))
    # owner's active listings
    own, off = [], 0
    while True:
        d = api.shop_listings(sid, 100, off); own += d["results"]
        if len(d["results"]) < 100: break
        off += 100
    json.dump(own, open(os.path.join(outdir, "owner_active_listings.json"), "w"), indent=1)
    # keyword rank sweeps
    allrows, summary, shop_ids = [], [], set()
    for kw in PLANT_KEYWORDS:
        rows, oranks = rank_keyword(api, kw, sid)
        allrows += rows; shop_ids |= {r["shop_id"] for r in rows[:30]}
        summary.append(dict(keyword=kw, results_scanned=len(rows), owner_best_rank=min(oranks) if oranks else "", owner_listings_in_scan=len(oranks)))
        print("%-28s scanned=%3d owner_best_rank=%s" % (kw, len(rows), min(oranks) if oranks else "-"))
    for name, rows in (("keyword_ranks.csv", allrows), ("keyword_summary.csv", summary)):
        with open(os.path.join(outdir, name), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    # shop-level facts for the shops that appear in the top 30 of any keyword
    srows = []
    for s in sorted(shop_ids):
        d = api.shop(s)
        srows.append(dict(shop_id=s, shop_name=d.get("shop_name"), created=d.get("create_date") or d.get("created_timestamp"), listing_active_count=d.get("listing_active_count"),
                          transaction_sold_count=d.get("transaction_sold_count"), review_count_past_year=d.get("review_count"), review_average_past_year=d.get("review_average"),
                          num_favorers=d.get("num_favorers"), is_vacation=d.get("is_vacation"), shop_location_country_iso=d.get("shop_location_country_iso")))
    with open(os.path.join(outdir, "top_shops.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(srows[0].keys())); w.writeheader(); w.writerows(srows)
    print("done; remaining_today =", api.remaining_today)


def selftest():
    """Offline test with a fake transport that returns spec-shaped JSON. Proves URL building, header format, paging and rank logic only."""
    calls = []
    def fake(url, headers):
        calls.append((url, headers))
        assert headers["x-api-key"] == "KEY:SECRET", "x-api-key must be keystring:shared_secret"
        u = urllib.parse.urlparse(url); q = urllib.parse.parse_qs(u.query)
        if u.path.endswith("/openapi-ping"): return 200, {"x-remaining-today": "99999"}, json.dumps({"application_id": 1})
        if u.path == "/v3/application/shops": return 200, {}, json.dumps({"count": 1, "results": [{"shop_id": 42, "shop_name": "RvsdGreenhouses"}]})
        if u.path == "/v3/application/shops/42": return 200, {}, json.dumps({"shop_id": 42, "shop_name": "RvsdGreenhouses", "listing_active_count": 2, "transaction_sold_count": 89, "review_count": 35, "review_average": 4.9})
        if u.path.endswith("/listings/active") and "/shops/" in u.path: return 200, {}, json.dumps({"count": 1, "results": [{"listing_id": 7, "shop_id": 42, "title": "x"}]})
        if u.path == "/v3/application/listings/active":
            assert q["sort_on"] == ["score"] and q["limit"] == ["100"]
            off = int(q.get("offset", ["0"])[0])
            res = [{"listing_id": 1000 + off + i, "shop_id": 42 if (off + i) == 7 else 9, "title": "t", "price": {"amount": 1899, "divisor": 100, "currency_code": "USD"}, "tags": ["a", "b"], "num_favorers": 3} for i in range(100 if off < 100 else 40)]
            return 200, {"x-remaining-this-second": "5"}, json.dumps({"count": 140, "results": res})
        return 404, {}, "{}"
    api = Etsy("KEY", "SECRET", min_interval=0, transport=fake)
    assert api.ping()["application_id"] == 1
    me = api.find_shop("RvsdGreenhouses")["results"][0]; assert me["shop_id"] == 42
    rows, oranks = rank_keyword(api, "hoya sunrise", 42, pages=3)
    assert len(rows) == 140 and oranks == [8], (len(rows), oranks)
    assert rows[0]["price"] == 18.99
    print("selftest OK:", len(calls), "mock calls; owner rank detection and x-api-key format verified")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true"); ap.add_argument("--ping", action="store_true"); ap.add_argument("--run", action="store_true"); ap.add_argument("--out", default="./etsy_api_out")
    a = ap.parse_args()
    if a.selftest: selftest(); sys.exit(0)
    ks, sec = os.environ.get("ETSY_KEYSTRING"), os.environ.get("ETSY_SHARED_SECRET")
    if not ks or not sec: sys.exit("Set ETSY_KEYSTRING and ETSY_SHARED_SECRET (from https://www.etsy.com/developers/your-apps). Not running.")
    api = Etsy(ks, sec)
    if a.ping: print(api.ping()); sys.exit(0)
    if a.run: collect(api, a.out); sys.exit(0)
    ap.print_help()

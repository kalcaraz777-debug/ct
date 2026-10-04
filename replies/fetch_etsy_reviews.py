#!/usr/bin/env python3
"""Fetch recent reviews for the RvsdGreenhouses Etsy shop as JSON (read-only).

Needs only an Etsy API key (no OAuth). Credentials come from the environment:
  ETSY_KEYSTRING, ETSY_SHARED_SECRET   (sent as x-api-key: keystring:shared_secret, required since 2026-02-09)

Usage:
  python3 fetch_etsy_reviews.py --since-days 7          # reviews created in the last 7 days
  python3 fetch_etsy_reviews.py --since 1791000000      # reviews created after a unix timestamp
Prints one JSON object: {"shop_id", "fetched_at", "reviews": [...]} where each review has
review_key, transaction_id, listing_id, listing_title, rating, review, language, created (ISO).
"""
import argparse, json, os, sys, time, urllib.error, urllib.parse, urllib.request
from datetime import datetime, timezone

BASE = "https://openapi.etsy.com"
SHOP_NAME = "RvsdGreenhouses"


def get(path, key, **params):
    qs = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    url = BASE + path + ("?" + qs if qs else "")
    for _ in range(4):
        req = urllib.request.Request(url, headers={"x-api-key": key, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(float(e.headers.get("retry-after", "2")) + 0.5)
                continue
            sys.exit(f"Etsy API error {e.code} on {path}: {e.read().decode('utf-8', 'replace')[:300]}")
    sys.exit(f"Etsy API kept rate-limiting {path}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", type=int, help="unix timestamp; only reviews created after it")
    ap.add_argument("--since-days", type=float, default=7)
    a = ap.parse_args()
    ks, sec = os.environ.get("ETSY_KEYSTRING"), os.environ.get("ETSY_SHARED_SECRET")
    if not ks or not sec:
        sys.exit("ETSY_KEYSTRING / ETSY_SHARED_SECRET are not set in this environment.")
    key = f"{ks}:{sec}"
    since = a.since or int(time.time() - a.since_days * 86400)

    shops = get("/v3/application/shops", key, shop_name=SHOP_NAME, limit=10)
    shop = next((s for s in shops.get("results", []) if s.get("shop_name", "").lower() == SHOP_NAME.lower()), None)
    if not shop:
        sys.exit(f"Shop {SHOP_NAME} not found via the API.")
    sid = shop["shop_id"]

    reviews, offset = [], 0
    while True:
        page = get(f"/v3/application/shops/{sid}/reviews", key, limit=100, offset=offset, min_created=since)
        reviews += page.get("results", [])
        if len(page.get("results", [])) < 100:
            break
        offset += 100
        time.sleep(1)

    titles = {}
    ids = sorted({r["listing_id"] for r in reviews if r.get("listing_id")})
    for i in range(0, len(ids), 100):
        batch = get("/v3/application/listings/batch", key, listing_ids=",".join(map(str, ids[i:i + 100])))
        for l in batch.get("results", []):
            titles[l["listing_id"]] = l.get("title")
        time.sleep(1)

    out = []
    for r in reviews:
        ts = r.get("created_timestamp") or r.get("create_timestamp")
        out.append({
            "review_key": f"etsy-review-{r.get('transaction_id') or r.get('listing_id')}-{ts}",
            "transaction_id": r.get("transaction_id"),
            "listing_id": r.get("listing_id"),
            "listing_title": titles.get(r.get("listing_id")),
            "rating": r.get("rating"),
            "review": r.get("review") or "",
            "language": r.get("language"),
            "created": datetime.fromtimestamp(ts, timezone.utc).isoformat() if ts else None,
        })
    print(json.dumps({"shop_id": sid, "fetched_at": datetime.now(timezone.utc).isoformat(), "reviews": out}, indent=1))


if __name__ == "__main__":
    main()

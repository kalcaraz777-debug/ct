# Etsy side on real data — handoff

Status (4 Oct 2026): waiting on the shop owner's Etsy API key. Nothing here has been run against Etsy yet.

## Owner's answers so far
- Not running eBay Promoted Listings. Watermelon Peperomia (168578976274) still rendered "Sponsored" at position 3 in both captures; owner to check Seller Hub → Marketing → Advertising.
- Checking duplicate pairs (see report fix list) for which listing holds sales/watchers.
- Grows and propagates the plants (Etsy Creativity Standards: OK; say so in listings).
- Wants the Etsy side measured on real data.

## Before running
1. Owner reads Etsy's API Terms of Use (https://www.etsy.com/legal/api; blocked from the cloud container) and confirms that using public listing-search endpoints for this study is allowed. Summaries suggest the terms limit collecting Etsy content "for analytics" without authorization. If in doubt, skip step 3 and use only the owner's own Shop Manager data.
2. Owner registers a Seller App at https://www.etsy.com/developers/register and adds two environment variables in the cloud environment settings (never in chat or in the repo):
   - `ETSY_KEYSTRING`
   - `ETSY_SHARED_SECRET`
   Since 9 Feb 2026 the API needs `x-api-key: keystring:shared_secret`. A new session picks the variables up.
3. In the new session:
   ```
   python3 collect.py --selftest      # offline check
   python3 collect.py --ping          # verifies the key
   python3 collect.py --run --out ./etsy_api_out
   ```
   It pulls the owner's shop, active listings, reviews, top-300 relevance ("score") results for the 25 plant keywords, and shop facts for every shop in a top 30. About 1 request/second, honouring Etsy's rate-limit headers.

## Owner-side data that needs no key (first-party, safest)
- Shop Manager → Marketing → Search analytics: queries, impressions, visits, orders per listing.
- Shop Manager → Stats → search terms and traffic sources (last 30 days).
- Shop Manager → Settings → Options → Download data → Currently for sale listings (CSV: titles, tags, photos).

## Caveat
API "score" order is Etsy's relevance sort without a shopper's personalization or ads, so it approximates — but is not identical to — what a logged-in buyer sees. Compare it with Search analytics positions.

# eBay + Etsy search audit — Riverside Greenhouses (4 Oct 2026)

Why the eBay store `riversidegreenhouses` and the Etsy shop `RvsdGreenhouses` rank where they do across 25 plant searches, compared with the small sellers ranking above them.

- `report.html` — the full report (open in a browser). Also published as a private claude.ai artifact.
- `agent-reports/` — written reports on documented ranking factors (eBay + Etsy) and the Etsy market.
- `data/` — the evidence:
  - `ebay_search_results_snapshot1.json`: 23 eBay Best Match searches, parsed result cards.
  - `ebay_serp_sellers_*`: second capture with ad (Sponsored) detection, rank correlations, seller profiles.
  - `ebay_listings_*`: 292 item pages (all 131 owner listings + competitors), duplicates, vague titles, title rewrites.
  - `etsy_market_*`: owner Etsy catalog and competitor shops, from Google / Google Shopping (Etsy blocks automated access).

## Headline findings
1. eBay positions 2–4 (and 13–16, 29–32, 39–40) were paid ads in all 23 searches checked.
2. Owner titles already contain every search word (22/22) and delivered price matches the unpaid top 3 ($25.98 vs $25.99).
3. Seller feedback count had no measurable link to rank (ρ ≈ +0.02); sellers with 8–60 feedback held #1 spots.
4. Unpaid top 3 vs owner: watchers 84% vs 30%, ≥1 sale 52% vs 13%, listed/revised ≤30 days 59% vs 0%, ≥5 photos 55% vs 4%.
5. 15 duplicate pairs, 29 vague titles, several descriptions that describe a different plant.
6. Etsy: 89 sales / 35 reviews (4.9★); page 1 of Etsy keyword pages for several plants; titles 118 chars vs 61 for shops Google surfaces.

Method: logged-out public pages, ship-to ZIP 94104, low request rate; correlations from one day of data, not proof of cause.

# Etsy market data for RvsdGreenhouses (scope `etsy_market`)

Generated 2026-10-04 by the plant-market-analyst (Etsy slice). Every figure below is regenerated from the files in `SCRATCH/data/etsy_market*` by `SCRATCH/etsy_market_report_build.py`; raw dumps are in `SCRATCH/etsy_market_raw/`.

## 0. Read this first

* **This is a PROXY, not Etsy's ranking.** etsy.com page requests from this container hit a DataDome interstitial (`SCRATCH/etsy_shop.html` is the captured wall, `geo.captcha-delivery.com`); two `help.etsy.com` articles and `etsy.com/legal/api` also returned HTTP 403 to a single plain fetch each (Seller Handbook URLs showed up in search results but were never fetched). I did **not** try to get around any of it (no unblockers, no caches/archives, no scraper actors, no `SERPER_SCRAPE_WEBPAGE`). Everything about Etsy listings and shops below is what **Google surfaces**: Google Shopping rows ("<plant> etsy", 25 queries, 942 rows, 824 from Etsy) and Google web-result snippets of etsy.com pages (about 1,000 queries, 5,170 snippets, 1,299 distinct listing IDs, 621 shop names). Position in those lists is Google's order, **not** Etsy's search order. The one place Etsy's own ordering leaks through is Etsy's keyword landing pages (`etsy.com/market/<keyword>?page=N`), which Google indexes; I only see the owner's cards on them (section 3.4), and I am assuming those pages mirror Etsy's search results for the keyword at crawl time (plausible, not verified).
* Snapshot dates are unknown and differ per page (weeks to months old). Shop counters (sales, reviews) only grow, so I always use the largest/latest snapshot and show the series where it matters.
* Etsy API host `openapi.etsy.com` is **not** walled: the published OpenAPI spec (`https://www.etsy.com/openapi/generated/oas/3.0.0.json`, Last-Modified 2 Oct 2026) and a key-less ping were reachable. That is why section 5 is exact rather than paraphrased.

## 1. Key findings, ranked by likely usefulness to the owner

1. **[MEASURED] Etsy is already the owner's stronger channel.** Latest public snapshot of the shop block: **4.9 stars, 35 reviews, 89 sales, "4 months on Etsy"** (owner Angel, Riverside CA, ships from Mira Loma CA). First listings went live 29 May 2026 (ID range 4513271075+; 13 of the 24 listings with a visible date are 1 Jun 2026). eBay shows 8 items sold in about 7 months. The series climbs 1 → 89 sales over 16 distinct snapshots (table in 3.2). No snippet shows a Star Seller badge for the shop (not proof of absence).
2. **[MEASURED] On Etsy's own keyword pages the owner's cards sit on page 1 for most of the plants.** 146 distinct `etsy.com/market/...` pages show an owner card (69 of 159 sightings are on page 1). Per plant, relevant keyword pages with the owner on page 1 / all relevant pages found: all on page 1: Hoya Australis Lisa (7/7), Hoya Sunrise (6/6), Syngonium Chiapense (2/2), Monstera Siltepecana (2/2); mostly: Sansevieria Moonshine (5/7), Rhaphidophora Tetrasperma (Mini Monstera) (4/6), Monstera Peru (3/5), Hoya Kerrii (2/4), Syngonium Mojito (3/4), Peperomia Hope (3/4), Watermelon Peperomia (3/4); weak: **Pilea Peperomioides (Chinese Money Plant) (0/7), Satin Pothos (0/1), Philodendron Brasil (2/5)**; owner listing exists but no relevant keyword page found: Syngonium Pink Splash, Christmas Cactus.
3. **[MEASURED] Google Shopping, the proxy I can query at scale, shows the owner for only 4 of 25 plants** (Hoya Sunrise #8, Syngonium Chiapense #24, Watermelon Peperomia #29, Pilea #39 of 40). So Google-side visibility and Etsy-side visibility differ a lot; do not read the Shopping position as the owner's Etsy rank.
4. **[MEASURED] The owner's title template is unlike the competition.** 65 owner titles: median **118 characters** (IQR 114-123), 98% pipe-delimited, 100% carry the pot size and "Live", 94% say "Easy Care", and **100% end with the brand phrase "from Riverside Greenhouses" (27 characters, 23% of the title)**. Google Shopping Etsy titles in positions 1-10 (n=209): median 61 chars, 11% pipes, 2% brand suffix; positions 11-40 (n=615): median 72 chars, 20% pipes. The "<plant> from <Shop>" suffix is used by two of the biggest recurring shops (CaliforniaTropicals, TropicalAmbiance), so it is probably copied, not proven helpful.
5. **[MEASURED; trend inferred] Pricing and shipping.** Owner Etsy prices seen: $12.99-$27.99 (median $18.49, n=38 titles). Listings show **FREE shipping** where checked (60 of 106 owner card sightings carry the label, the rest are mostly truncated snippets; Google Shopping tags "Free delivery" on 9 of 20 owner products). On eBay the same items charge $6.99/$9.99 shipping. Etsy price equals the eBay price for 27 of 38 matched titles and is higher for 11 (never lower): the owner appears to have been **raising Etsy prices by $1-$5 since June** (inferred from older vs newer card sightings, ordered by the shop review count printed on each card; e.g. Hoya Australis Lisa $16.99 → $18.99, Hindu Rope $13.99 → $16.99, Sansevieria Moonshine 6" $18.99 → $21.99 → $23.99) while sales kept rising. Against Google's Etsy rows (non-cutting, any size) the owner is **below the median for 17 of 21 plants**; at/above for pilea peperomioides, philodendron brasil, syngonium mojito, watermelon peperomia (Chinese Money Plant is the stark case: $21.99 vs median $12.00, 72% of comps cheaper).
6. **[MEASURED] Coverage gap = the old eBay listings.** 21 of the 25 plants have an Etsy listing; the 4 with none found (Raven ZZ, Philodendron Pink Princess, Texas Ebony, Hoya Cummingiana) are exactly the four that exist on eBay only in the old "- Live Houseplant - N-inch Pot" format. The Etsy catalog closely mirrors the 64 new-format eBay listings (an Etsy twin with the same title was found for 62 of them) plus extras such as a Heat Pack add-on.
7. **[MEASURED] The competitors Google repeats most are large, but not all.** PlantVers (16 of 25 plants; 136k sales), CaliforniaTropicals (14; 166k), TheGreenEscape (10; 875k), RareFoliagePlantCo (9; 17k, Star Seller), NYCitySucculents (9; 69k), LasOrquideasRamos (8; 3.7k, Star Seller, 1 year) ... and young shops get through too (HausOfRootsLLC: "3 months on Etsy", 157 sales, Star Seller). A same-city rival exists: MyPlantsShopLLC, Riverside CA, 6.1k sales, Star Seller. See 4.4.
8. **[INFERENCE, weak] What correlates with Google Shopping position (824 Etsy rows).** Having a product rating is the strongest: Spearman rho(position, has-rating) = -0.30 pooled and negative in 22 of 25 plants (rated items sit higher); more reviews also higher (rho -0.19). Longer titles sit slightly lower (rho +0.14; positive in 20 of 25 plants), higher price slightly lower (rho +0.15); "Free delivery" shows no relationship (rho -0.003, but only 25% of rows carry a shipping label). This describes Google, not Etsy.
9. **[MEASURED] API facts that matter.** Since 9 Feb 2026 the header must be `x-api-key: <keystring>:<shared_secret>`; a key-less call today returns `403 {"error":"Invalid API key: should be in the format 'keystring:shared_secret'."}`. Relevance search is `GET /v3/application/listings/active?keywords=..&sort_on=score` (API key only, no OAuth). **Composio has no Etsy toolkit.** Details and the step-by-step key procedure are in section 5; an offline-tested collector script is `SCRATCH/data/etsy_market_api_quickstart.py`.
10. **[MEASURED] The hinted listing IDs.** `4487242670` is **not** the owner's (seller ChambersPlants, Gatlinburg TN, listed 11 Apr 2026, $16.00). `4514468379` **is** the owner's ZZ Plant 2". The owner's real Hoya Sunrise 4" is `4513836738` ($18.99, free shipping).

## 2. Access, tools and method

| Route | Result |
|---|---|
| etsy.com pages from the container | DataDome interstitial (`SCRATCH/etsy_shop.html`); not pursued |
| help.etsy.com (2 articles) and etsy.com/legal/api (WebFetch) | HTTP 403 on the single attempt each; not pursued. Content taken from search-engine snippets of those pages and from Alura's public seller docs instead |
| developers.etsy.com docs (WebFetch) | readable (authentication, requests, rate-limits, landing/app types) |
| Published OpenAPI spec file | plain GET OK: 911,340 bytes, OpenAPI 3.0.2, 76 paths, 105 operations (saved, parsed, extract in `data/etsy_market_openapi_extract.json`) |
| `openapi.etsy.com` key-less ping | HTTP 403 with the new key-format message (proves reachability and the format rule) |
| Google Shopping (Composio `COMPOSIO_SEARCH_SHOPPING`, SerpApi, `gl=us`) | 54 queries: 25 x "<plant> etsy" (40 rows max), 28 owner-title queries, 1 test. Rows carry `source` ("Etsy - <shop>" names the shop for only 142 of 942 rows; "Etsy - Seller"/"Etsy" otherwise), price, "Free delivery", product-level rating/reviews. No listing URL or ID is returned |
| Google web results (Composio `SERPER_SEARCH_WEB` / `SERPER_BATCH_SEARCH_WEB`, free instant account) | about 1,000 queries; free tier refuses result_count>10 on `site:` queries so I paged by cursor. Snippets of etsy.com listing pages expose "This House Plants item is sold by <shop>. Ships from <city>. Listed on <date>" and the "Meet your seller" block ("<shop> · Owned by <name> | <place>. 4.9 (35). 89 sales. 4 months on Etsy") |
| Third-party stats pages | MakerWords: loads without login but is a keyword-tool directory with thin coverage (owner shop and `keyword/hoya-sunrise` not present, 404); not used for numbers |
| Composio Etsy toolkit | does not exist (9 Etsy-focused queries in 3 `COMPOSIO_SEARCH_TOOLS` calls); see 5.6 |

Shop attribution caveat: Google labels most Etsy Shopping rows "Etsy - Seller", so only 210 rows have a shop (142 from Google's own label, 68 from long, unique title matches to a listing page). The shop-level tables use the web-snippet blocks (the same shop numbers Etsy prints on each listing page).

## 3. The owner's Etsy shop (RvsdGreenhouses)

### 3.1 The two hinted listings

| Listing | Verdict | Evidence |
|---|---|---|
| `etsy.com/listing/4487242670` "Hoya Sunrise" | **Not the owner's.** Seller ChambersPlants (Carolyn Chambers), ships from Gatlinburg TN, listed 11 Apr 2026, price $16.00 | Snippets of that URL: "This Plants item is sold by ChambersPlants. Ships from Gatlinburg, TN. Listed on Apr 11, 2026", "Meet your seller. ChambersPlants · Owned by Carolyn Chambers", "Price:$16.00". The ID also pre-dates the owner's first listing (29 May 2026 = ID 4513271075) |
| `etsy.com/listing/4514468379` "ZZ Plant 2"" | **The owner's.** Title "ZZ Plant 2" Live Houseplant \| Zamioculcas Zamiifolia \| Easy Care Low Light Indoor Plant from Riverside Greenhouses", snippet names RvsdGreenhouses, "Listed on 01 Jun, 2026" | Localised pages show CA$18.81, AU$19.37, 14,42 EUR; USD price not shown (inference only: those three conversions are mutually consistent with about $13.99). A second ZZ 2" listing exists (4526371121, $12.99 card). eBay twin $12.99 |
| owner's real Hoya Sunrise 4" | `4513836738`, $18.99, free shipping, on page 1 of 6 Etsy keyword pages | cards: "Hoya Sunrise 4" Live Houseplant \| Rare Hoya \| Easy Care Indoor Vining Plant from Riverside Greenhouses. ($18.99) FREE shipping" |

### 3.2 Shop facts and growth (snippets of the "Meet your seller" block)

Shop name RvsdGreenhouses, owner Angel, Riverside, California; listings say "Ships from Mira Loma, CA"; About text: "Proudly growers of beautiful and healthy plants ... located in Riverside, California"; categories House Plants, Cold & Heat Packs. Returns accepted appears on at least one listing. Listing "Listed on" dates: 29 May (2), 30 May (1), 1 Jun (13), 12 Jun (1), 22 Jun (4), 23 Jun (1), 7 Jul (1), 19 Sep (1, Hoya Australis Lisa: renewed or relisted).

| Snapshot (ordered by sales) | Sales | Reviews | Rating | Age text |
|---|---|---|---|---|
| #1 | 1 | 0 | - | New on Etsy |
| #2 | 2 | 0 | - | New on Etsy |
| #3 | 3 | 0 | - | 1 month on Etsy |
| #4 | 3 | 1 | 5.0 | 1 month on Etsy |
| #5 | 6 | 1 | 5.0 | 1 month on Etsy |
| #6 | 8 | 1 | 5.0 | 1 month on Etsy |
| #7 | 8 | 2 | 5.0 | 1 month on Etsy |
| #8 | 9 | 2 | 5.0 | 1 month on Etsy |
| #9 | 9 | 3 | 5.0 | 2 months on Etsy |
| #10 | 11 | 3 | 5.0 | 2 months on Etsy |
| #11 | 13 | 3 | 5.0 | 2 months on Etsy |
| #12 | 32 | 5 | 5.0 | 2 months on Etsy |
| #13 | 46 | 13 | 5.0 | 3 months on Etsy |
| #14 | 82 | 29 | 4.9 | 4 months on Etsy |
| #15 | 89 | 32 | 4.9 | 4 months on Etsy |
| #16 | 89 | 35 | 4.9 | 4 months on Etsy |

Latest = #16: 4.9 / 35 reviews / 89 sales / 4 months (listing 4514475992). Reviews/sales per snapshot are internally consistent (monotonic), which is why I treat the series as a time axis. Etsy's listing cards print the same shop-level review count (2, 3, 5, 13, 21 ... 35) next to every owner item. The sales count has probably moved on since the last crawl.

### 3.3 Catalog reconstruction (67 titles, 57 with a listing ID)

Method: owner titles all end with "from Riverside Greenhouses", listing pages say "sold by RvsdGreenhouses" / "RvsdGreenhouses · Owned by Angel", and Etsy keyword pages print the owner's cards. Full CSV: `data/etsy_market_owner_catalog.csv` (title, IDs, prices seen, free-shipping flag, listed-on, ships-from, Google Shopping position, number of Etsy keyword pages, eBay twin). Duplicated titles: Satin Pothos 4" (4514470150, 4526450542) and Syngonium Pink Splash 4" (4526372903, 4526520636). Hoya Kerrii 4" (4513275018) was retitled after creation (URL slug still shows the earlier title). One "Sale Price" sighting (Snake Plant Black Gold 4": $13.59 vs $16.99, and a "Sale ends in 3 days" Red Bromeliad card), so the owner has used Etsy sales.

| Plant in study | Title (without the ' from Riverside Greenhouses' suffix) | Listing ID | Etsy price(s) seen | Free shipping seen | eBay twin price |
|---|---|---|---|---|---|
| calathea rattlesnake | Calathea Rattlesnake 4" Live Houseplant \| Lancifolia Prayer Plant \| Easy Care Tropical Indoor Plant | 4514507750 | 17.99 | - | $17.99 |
| calathea setosa | Calathea Setosa Grey Star 4" Live Houseplant \| Prayer Plant \| Easy Care Tropical Indoor Plant | 4514503686 | 18.99 | - | $18.99 |
| cebu blue pothos | Cebu Blue Pothos 3" Live Houseplant \| Epipremnum Pinnatum \| Easy Care Rare Vining Indoor Plant | 4526450139 | 12.79 → 15.99 | - | $15.99 |
| christmas cactus | Christmas Cactus 4" Live Flowering Cactus \| Surprise Color \| Unique Holiday Plant | 4513281172 | 17.99 | yes | $17.99 |
| hoya australis lisa | Hoya Australis Lisa 4" Live Houseplant \| Variegated Hoya \| Easy Care Vining Indoor Plant | 4514471164 | 16.99 → 18.99 | yes | $16.99 |
| hoya carnosa compacta | Hoya Hindu Rope Variegated 2" Live Houseplant \| Hoya Carnosa Compacta \| Rare Vining Plant | 4514468966 | 13.99 → 16.99 | - | $13.99 |
| hoya kerrii | Hoya Kerrii 4" Variegated 1 Heart Leaf Live Succulent Heart Plant Easy Care Indoor Plant | 4513275018 | 21.99 | yes | $21.99 |
| hoya sunrise | Hoya Sunrise 4" Live Houseplant \| Rare Hoya \| Easy Care Indoor Vining Plant | 4513836738 | 18.99 | yes | $18.99 |
| monstera peru | Monstera Peru 3" Live Houseplant \| Monstera Karstenianum \| Easy Care Rare Tropical Indoor Plant | 4526572073 | 17.5 | - | $17.50 |
| monstera siltepecana | Monstera Siltepecana 4" Live Houseplant \| Silver Monstera \| Easy Care Rare Tropical Indoor Plant | 4526367313 | 21.99 | yes | $21.99 |
| peperomia hope | Peperomia Hope 4" Live Houseplant \| Trailing Peperomia \| Easy Care Indoor Plant | 4514509657 | 16.99 → 17.99 | - | $16.99 |
| philodendron brasil | Philodendron Brasil 6" Live Houseplant \| Variegated Heartleaf Philodendron \| Easy Care Vining Indoor Plant | 4514512537 | 18.99 | - | $18.99 |
| philodendron micans | Philodendron Micans 4" Live Houseplant \| Velvet Leaf Philodendron \| Easy Care Vining Indoor Plant | 4514475175 | 15.99 | - | $15.99 |
| pilea peperomioides | Chinese Money Plant 4" Live Houseplant \| Pilea Peperomioides \| Easy Care Indoor Plant | 4513826476 | 21.99 | yes | $21.99 |
| rhaphidophora tetrasperma | Mini Monstera 4" Live Houseplant \| Rhaphidophora Tetrasperma \| Easy Care Vining Indoor Plant | 4526354083 | 16.99 → 17.99 | yes | $16.99 |
| rhaphidophora tetrasperma | Mini Monstera 8" Live Houseplant \| Rhaphidophora Tetrasperma \| Easy Care Vining Indoor Plant | 4526509173 | 27.99 | - | $27.99 |
| sansevieria moonshine | Sansevieria Moonshine 6" Live Houseplant \| Silver Snake Plant \| Easy Care Low Light Indoor Plant | 4526378226 | 18.99 → 21.99 → 23.99 | yes | $18.99 |
| satin pothos | Satin Pothos 4" Live Houseplant \| Scindapsus Pictus \| Easy Care Vining Indoor Plant | 4514470150, 4526450542 | 16.99 → 17.99 | yes | $16.99 |
| syngonium chiapense | Syngonium Chiapense 4" Live Houseplant \| Rare Arrowhead Plant \| Easy Care Tropical Indoor Plant | 4526358599 | 21.99 | yes | $21.99 |
| syngonium mojito | Syngonium Mojito 4" Live Houseplant \| Rare Variegated Arrowhead Plant \| Easy Care Tropical Indoor Plant | 4526455050 | 23.99 | yes | $23.99 |
| syngonium pink splash | Syngonium Pink Splash 4" Live Houseplant \| Arrowhead Plant \| Easy Care Tropical Indoor Plant | 4526372903, 4526520636 | 24.99 | yes | $24.99 |
| watermelon peperomia | Watermelon Peperomia (Stilt) 4" Live Houseplant \| Peperomia Argyreia \| Easy Care Tropical Indoor Plant | - | 18.99 | - | $18.99 |
| watermelon peperomia | Watermelon Peperomia 4" Live Houseplant \| Peperomia Argyreia \| Easy Care Tropical Indoor Plant | 4514496451 | - | - | - |
| - | Anthurium Plant 4" Live Houseplant \| Flamingo Flower \| Easy Care Tropical Indoor Plant | 4514452319 | - | - | - |
| - | Birkin Philodendron Variegated 4" Live Houseplant Rare Variegated Philodendron \| Easy Care Tropical Indoor Plant | 4514513158 | - | - | $16.99 |
| - | Calathea Peacock Makoyana 4" Live Houseplant \| Cathedral Windows Plant \| Easy Care Tropical Indoor Plant | 4514504880 | - | - | $16.99 |
| - | Chinese Evergreen Lady Valentine 4" Live Houseplant \| Aglaonema \| Easy Care Tropical Indoor Plant | 4514502582 | 20.99 | - | $20.99 |
| - | Creamsicle Plant 4" Live Houseplant \| Rare Tropical Indoor Plant \| Easy Care Plant | 4526361168 | 16.99 → 17.99 | yes | $16.99 |
| - | Curly Sue 4" Live Houseplant \| Unique Curly Leaf Plant \| Easy Care Indoor Plant | 4513292468 | 22.99 | yes | $22.99 |
| - | Dieffenbachia Compacta 4" Live Houseplant \| Dumb Cane \| Easy Care Tropical Indoor Plant | 4514475992 | 18.99 | - | $18.99 |
| - | Dwarf Fiddle Leaf Fig 4" Live Houseplant \| Ficus Lyrata Bambino \| Easy Care Indoor Tree | - | - | - | - |
| - | Everblooming Gardenia 4" Live Houseplant \| Gardenia Jasminoides \| Fragrant Flowering Indoor Plant | 4514497649 | - | - | $12.99 |
| - | Golden Pothos 4" Live Houseplant \| Epipremnum Aureum \| Easy Care Vining Indoor Plant | 4526514343 | - | - | $16.99 |
| - | Green Queen Pothos 6" Live Houseplant \| Epipremnum Aureum \| Easy Care Vining Indoor Plant | 4526589241 | 25.99 | - | $23.99 |
| - | Haworthia Zebra 4" Live Houseplant \| Zebra Cactus \| Easy Care Succulent Indoor Plant | 4514508898 | 17.99 | - | $15.99 |
| - | Heat Pack Add-on \| Cold Weather Plant Protection \| Safe Winter ... [partial] | 4513271075 | - | - | - |
| - | Hoya Carnosa (Jade Wax) 4" Live Houseplant \| Wax Plant \| Easy Care Indoor Vining Plant | - | 17.99 | yes | $17.99 |
| - | Hoya Carnosa 4" Live Houseplant \| Wax Plant \| Easy Care Indoor Vining Plant | 4513834850 | - | - | - |
| - | Lemon Lime Maranta Prayer Plant 3" Live Houseplant \| Maranta Leuconeura \| Easy Care Indoor Plant | 4514473668 | 16.99 | - | $10.99 |
| - | Marble Queen Pothos 4" Live Houseplant \| Epipremnum Aureum \| Easy Care Vining Indoor Plant | 4514510438 | 17.99 | - | $15.99 |
| - | Ming Aralia Variegated 4" Live Houseplant \| Polyscias Fruticosa \| Rare Indoor Plant | - | 20.99 → 26.99 | yes | $26.99 |
| - | Monstera Laniata 3" Live Houseplant \| Rare Monstera \| Easy Care Tropical Indoor Plant | 4526359466 | - | - | $13.99 |
| - | Monstera Split Leaf 6" Live Houseplant \| Monstera Deliciosa \| Easy Care Tropical Indoor Plant | 4526571468 | 25.99 | - | $17.99 |
| - | Neon Pothos 4" Live Houseplant \| Epipremnum Aureum Neon \| Easy Care Vining Indoor Plant | 4526578669 | 16.49 | yes | $16.49 |
| - | Peperomia Rosso 4" Live Houseplant \| Emerald Ripple Peperomia \| Easy Care Tropical Indoor Plant | 4514500931 | - | - | $16.99 |
| - | Philodendron Burgundy Princess 4" Live Houseplant Rare ... [partial] | 4514506174 | - | - | - |
| - | Philodendron Emerald Red 6" Live Houseplant \| Rare Philodendron \| Easy Care Tropical Indoor Plant | 4514499807 | - | - | $25.99 |
| - | Philodendron Red Back 4" Live Houseplant \| Rare Philodendron \| Easy Care Tropical Indoor Plant | 4514511929 | - | - | $17.99 |
| - | Pink Fittonia 3" Live Houseplant \| Nerve Plant \| Easy Care Tropical Indoor Plant | 4514506906 | 12.99 → 16.99 | - | $12.99 |
| - | Pothos Devils Ivy Queen 4" Live Houseplant \| Epipremnum Aureum \| Easy Care Vining Indoor Plant | 4526358124 | - | - | $15.99 |
| - | Purple Anthurium 4" Live Houseplant \| Flamingo Flower \| Easy Care Tropical Indoor Plant | 4514454689 | - | - | $18.99 |
| - | Purple Bromeliad 4" Live Houseplant \| Tropical Flowering Plant \| Easy Care Indoor Plant | - | 18 | yes | $18.00 |
| - | Rainbow Anthurium 4" Live Houseplant \| Flamingo Flower \| Easy Care Tropical Indoor Plant | - | - | - | $18.99 |
| - | Rat Tail Succulent 3" Live Houseplant \| Aporocactus Flagelliformis \| Easy Care Trailing Cactus | 4514511083 | 12.99 | - | $12.99 |
| - | Red Anthurium Plant 4" Live Houseplant \| Flamingo Flower \| Easy Care Tropical Indoor Plant | - | 18.99 | yes | $18.99 |
| - | Red Bromeliad 4" Live Houseplant \| Tropical Flowering Plant \| Easy Care Indoor Plant | 4526514028 | 17.5 | yes | $17.50 |
| - | Red Maranta Prayer Plant 4" Live Houseplant \| Maranta Leuconeura \| Easy Care Indoor Plant | 4514472233 | 18.99 | - | $12.99 |
| - | Sansevieria Sol Radiante 4" Live Houseplant \| Rare Snake Plant \| Easy Care Low Light Indoor Plant | - | 17.99 | - | $16.99 |
| - | Sansevieria Superba 4" Live Houseplant \| Snake Plant \| Easy Care Low Light Indoor Plant | - | 17.99 | - | $16.99 |
| - | Sansevieria Zeylanica 6" Live Houseplant \| Bowstring Hemp Snake Plant \| Easy Care Low Light Indoor Plant | 4526383000 | - | - | $23.99 |
| - | Snake Plant Sansevieria Black Gold 4" Live Houseplant \| Dracaena Trifasciata \| Easy Care Low Light Indoor Plant | 4526357109 | - | - | - |
| - | Strawberry Syngonium 3" Live Houseplant \| Arrowhead Plant \| Easy Care Tropical Indoor Plant | - | - | - | $12.99 |
| - | Syngonium Aurea 4" Live Houseplant \| Rare Variegated Arrowhead Plant \| Easy Care Tropical Indoor Plant | 4526582277 | - | - | $34.99 |
| - | Syngonium Batik 4" Live Houseplant \| Rare Arrowhead Plant \| Easy Care Tropical Indoor Plant | 4526584832 | - | - | $25.99 |
| - | Yellow Bromeliad 4" Live Houseplant \| Tropical Flowering Plant \| Easy Care Indoor Plant | 4526363574 | 18.99 | yes | $18.99 |
| - | ZZ Plant 2" Live Houseplant \| Zamioculcas Zamiifolia \| Easy Care Low Light Indoor Plant | 4526371121 | 12.99 → 16.99 | - | $12.99 |
| - | ZZ Plant Zamifolia 8" Live Houseplant \| Zamioculcas Zamiifolia \| Easy Care Low Light Indoor Plant | 4526360543 | - | - | $34.99 |

Prices with several values were seen at different crawl dates; values rise with the shop's review count on the same card, i.e. the owner repriced upward. A blank means no price text was found for that title.

### 3.4 Where the owner appears (two different lenses)

* **Etsy keyword landing pages (closest thing to Etsy's own order):** per plant, page-1/all relevant pages with an owner card are in the last column of the table in 4.1; the full list is `data/etsy_market_owner_relevant_market_pages.csv` and all 159 sightings are in `data/etsy_market_owner_on_market_pages.csv`. The exact-slug pages `etsy.com/market/calathea_setosa` and `etsy.com/market/syngonium_mojito` have an owner listing as the first card text in their Google snippet (suggestive of top placement, not proof). Caveats: none of the 227 snippets containing an owner card carries an "Ad by" label, but a label may not survive in a snippet, so promoted (Etsy Ads) placement cannot be excluded; check Shop Manager > Marketing for ads.
* **Google Shopping:** owner rows only for Hoya Sunrise #8 ($18.99, Free delivery, product rating 5.0/2 reviews), Syngonium Chiapense #24, Watermelon Peperomia #29, Pilea #39.

## 4. Competitors per plant (proxy for what Etsy shows)

### 4.1 Per-plant table (Google Shopping "<plant> etsy", up to 40 rows each)

"Share of comps cheaper" is the percent of non-cutting Etsy rows for that plant that are cheaper than the owner's highest price seen; sizes in comps are mixed (2" starters to 8"), so treat as crude. Shipping is only known when Google prints "Free delivery" (25% of Etsy rows); the owner's price already includes shipping.

| Plant | Etsy rows seen | cutting-type % | 'Free delivery' % | median non-cutting $ | Owner Etsy listings | Owner price(s) seen (share of comps cheaper) | Owner in Google Shopping | Owner cards on Etsy keyword pages (page 1 / all) |
|---|---|---|---|---|---|---|---|---|
| hoya sunrise | 40 | 18 | 20 | 29.84 | 1 | $18.99 (22%) | #8 | 6 / 6 |
| hoya kerrii | 37 | 16 | 24 | 28.74 | 1 | $21.99 (39%) | - | 2 / 4 |
| hoya australis lisa | 40 | 25 | 15 | 36.72 | 1 | $16.99 → 18.99 (23%) | - | 7 / 7 |
| hoya carnosa compacta | 34 | 3 | 32 | 39.95 | 1 | $13.99 → 16.99 (9%) | - | 1 / 1 |
| syngonium chiapense | 40 | 0 | 8 | 40.93 | 1 | $21.99 (18%) | #24 | 2 / 2 |
| syngonium pink splash | 26 | 0 | 27 | 30.0 | 1 | $24.99 (46%) | - | 0 / 0 |
| syngonium mojito | 20 | 10 | 25 | 22.84 | 1 | $23.99 (56%) | - | 3 / 4 |
| raven zz plant | 40 | 10 | 20 | 30.0 | none found | - | - | 0 / 0 |
| monstera peru | 34 | 12 | 35 | 33.49 | 1 | $17.5 (23%) | - | 3 / 5 |
| rhaphidophora tetrasperma | 40 | 5 | 8 | 67.5 | 2 | $16.99 → 17.99 (13%) | - | 4 / 6 |
| philodendron pink princess | 32 | 0 | 28 | 30.11 | none found | - | - | 0 / 0 |
| philodendron micans | 28 | 7 | 18 | 55.0 | 1 | $15.99 (12%) | - | 1 / 2 |
| philodendron brasil | 40 | 38 | 2 | 15.6 | 1 | $18.99 (56%) | - | 2 / 5 |
| monstera siltepecana | 26 | 19 | 35 | 29.99 | 1 | $21.99 (24%) | - | 2 / 2 |
| peperomia hope | 27 | 0 | 33 | 21.98 | 1 | $16.99 → 17.99 (30%) | - | 3 / 4 |
| watermelon peperomia | 34 | 12 | 35 | 16.99 | 2 | $18.99 (55%) | #29 | 3 / 4 |
| pilea peperomioides | 40 | 0 | 52 | 12.0 | 1 | $21.99 (72%) | #39 | 0 / 7 |
| calathea setosa | 17 | 6 | 12 | 33.6 | 1 | $18.99 (25%) | - | 1 / 1 |
| calathea rattlesnake | 40 | 12 | 35 | 19.2 | 1 | $17.99 (46%) | - | 1 / 2 |
| satin pothos | 38 | 45 | 21 | 19.48 | 1 | $16.99 → 17.99 (43%) | - | 0 / 1 |
| cebu blue pothos | 24 | 17 | 42 | 16.29 | 1 | $12.79 → 15.99 (45%) | - | 1 / 2 |
| christmas cactus | 34 | 3 | 65 | 42.74 | 1 | $17.99 (21%) | - | 0 / 0 |
| sansevieria moonshine | 40 | 2 | 10 | 30.0 | 1 | $18.99 → 21.99 → 23.99 (28%) | - | 5 / 7 |
| texas ebony plant | 13 | 38 | 15 | 32.99 | none found | - | - | 0 / 0 |
| hoya cummingiana | 40 | 28 | 20 | 28.0 | none found | - | - | 0 / 0 |

Full rows, top-10 per plant with shop facts where known: `data/etsy_market_per_plant_gshopping_top10.csv`, `data/etsy_market_gshopping_enriched.csv`, Google organic top listings `data/etsy_market_per_plant_google_organic.csv`, matrix `data/etsy_market_plant_matrix.csv`.

Examples (top rows, Google Shopping order):

* Hoya Sunrise
  - #1: Hoya Sunrise \| Rare Hoya Plant; $18; product rating 4.6 (62)
  - #2: Hoya Sunrise; $30; product rating 4.6 (81)
  - #3: Hoya 'Sunrise' 6; $16
  - #4: Hoya Sunrise Cutting: Rare Vining Wax Plant, Unrooted cutting 2-Leaf/2-Node; $7.24; product rating 5 (29)
* Pilea peperomioides (Chinese Money Plant)
  - #1: Pilea Peperomioides, Planta de Pilea, Planta de Pilea peperomia en maceta de 4" - Planta del dinero ; $17.6; Free delivery; product rating 4.7 (25)
  - #2: Pilea Peperomioides; $23.95; product rating 4.4 (329)
  - #3: Pilea peperomioides, Planta del Dinero China, Planta OVNI, Maceta de 4"; $29.99; Free delivery; product rating 4.7 (34)
  - #4: Potted Pilea Peperomioides 1 Count 6-inch pot; $29.32; product rating 5 (4)
* Satin Pothos
  - #1: Satin Pothos - 6'' from California Tropicals; $24.99; product rating 4 (105); shop CaliforniaTropicals
  - #2: Satin Pothos Scindapsus ‘Argyraeus’; $14.99; Free delivery; product rating 4.7 (650)
  - #3: Pothos Njoy RARO, maceta completa de 4 pulgadas, enredadera de interior abigarrada blanca, planta de; $19.47; product rating 5 (680); shop PlantVers
  - #4: IVORY KNIGHT Pothos hanging basket CULTIVAR Epipremnum Aurea; $52.95
* Sansevieria Moonshine
  - #1: Sansevieria Moonshine Live Plant \| Moonshine Snake Plants \| Mother in Laws Tongue Houseplants \| Easy; $18.55; product rating 4.8 (13); shop NYCitySucculents
  - #2: Sansevieria Trifasciata Moonshine; $14; product rating 4.6 (75)
  - #3: LIVE PLANT Snake Plant Moonshine Sansevieria Rooted Cutting; $4.99; shop ReadyLimited
  - #4: Sanseveria-Snake Plant--Moonshine; $18; product rating 4.4 (5)

### 4.2 Title structure (Etsy rows in Google Shopping vs the owner)

| Group | n | median chars | IQR | pipes | has size | "Live" | "Rare" | "Easy care" | brand suffix "from <Shop>" | cutting words |
|---|---|---|---|---|---|---|---|---|---|---|
| Google Shopping positions 1-10 | 209 | 61 | 35-93 | 11% | 19% | 11% | 17% | 4% | 2% | 10% |
| Google Shopping positions 11-40 | 615 | 72 | 51.5-107.5 | 20% | 21% | 19% | 20% | 6% | 1% | 14% |
| Owner Etsy titles | 65 | 118 | 114-123 | 98% | 100% | 100% | 25% | 94% | 100% | 0% |

Competitor top-10 titles are often the plain buyer query ("Hoya Sunrise | Rare Hoya Plant", "Pilea Peperomioides", "Hoya Sunrise"), often with a synonym ("Tequila Sunrise", "UFO plant", "Chinese Money Plant"); "Exact plant" appears in only 2.8% of rows and "US seller" in 2-4%; about 8% of the Etsy rows are Spanish-language titles (Etsy's translated/duplicated listings show up as separate Shopping rows). The owner's titles are longer, uniform and carry a brand tail; Etsy cards only show the first part of long titles.

### 4.3 What Google's order correlates with (exploratory, 824 Etsy rows, n by plant 13-40)

Spearman rho of Google Shopping position (1 = best) with: has product rating -0.303; title length +0.143; price +0.147; cutting-type +0.044; on sale +0.037; "Free delivery" -0.003. Product-level rating/review counts in Shopping rows are not the shop's lifetime counts (e.g. PlantVers listing shows 5.0/680 while the shop block says 4.7/41.8k). Saved: `data/etsy_market_gshopping_position_correlations.json`. Weak effects, one search engine, one day: use only to decide which Etsy-side tests to run.

### 4.4 The shops that recur most (top 12 by number of the 25 plants they appear for, Google Shopping labels + web snippets)

| # | Shop | Plants (of 25) | Listings seen | Best Google Shopping pos. | Sales | Shop reviews (rating) | Years on Etsy | Location (per listing page) | Star Seller badge in snippets |
|---|---|---|---|---|---|---|---|---|---|
| 1 | PlantVers | 16 | 55 | 3 | 136,300 | 41,800 (4.7) | 6.0 | Lake Orion, Michigan | yes |
| 2 | CaliforniaTropicals | 14 | 10 | 1 | 165,900 | 54,300 (4.8) | 7.0 | United States | not seen |
| 3 | TheGreenEscape | 10 | 31 | 1 | 875,000 | 266,100 (4.7) | 6.0 | Florida, United States | not seen |
| 4 | RareFoliagePlantCo | 9 | 32 | - | 17,200 | 6,600 (4.9) | 3.0 | Winter Garden, Florida | yes |
| 5 | NYCitySucculents | 9 | 14 | 1 | 69,200 | 19,100 (4.4) | 6.0 | New York, United States | not seen |
| 6 | LasOrquideasRamos | 8 | 24 | - | 3,700 | 1,300 (4.8) | - | Miami, Florida | yes |
| 7 | plantproperco | 7 | 19 | - | 14,200 | 6,000 (4.9) | 5.0 | Homestead, Florida | yes |
| 8 | CanopyGems | 7 | 17 | 12 | 10,800 | 3,800 (4.9) | 16.0 | United States | not seen |
| 9 | TropicalAmbiance | 7 | 15 | - | 38,800 | 14,700 (4.8) | 6.0 | United States | not seen |
| 10 | FreshFromGreenhouse | 7 | 13 | 6 | 51,700 | 16,800 (4.8) | 5.0 | Umatilla, Florida | not seen |
| 11 | AnnasPlantlings | 7 | 8 | - | 70 | 10 (5.0) | 3.0 | United States | not seen |
| 12 | IshysPlants | 7 | 7 | - | 1,200 | 347 (4.4) | 1.0 | Brooklyn, New York | not seen |

Shop numbers are the latest "Meet your seller" snapshot found (sales, reviews and rating always from one snapshot). "Star Seller badge in snippets" = the page text says "<shop> is a star seller" / "<shop>. Star Seller."; "not seen" is not proof of absence. Observations: (a) ratings are 4.4-5.0 and most of these shops have thousands of reviews, so the owner's 35 reviews is the biggest visible gap; (b) the field is not only veterans: HausOfRootsLLC ("3 months on Etsy", 157 sales, 60 reviews, Star Seller) and KayKaysplanties ("3 months", 16.8k sales, Star Seller; implausibly fast, possibly a re-opened shop) appear next to 6-16-year-old shops; (c) Florida dominates the location column (Winter Garden, Miami, Homestead, Umatilla), California is CaliforniaTropicals, LasOrquideasRamos competes from Miami, and **MyPlantsShopLLC (Riverside CA, 6.1k sales, 4.8, Star Seller, 3 years)** is a local rival; (d) the large shops use short, query-like titles, the "<Plant> - 6'' from California Tropicals" style, or "Exact plant" collector titles. The full 621-shop table is `data/etsy_market_shops_all.csv`.

## 5. Etsy Open API v3: what the owner needs

Source: developers.etsy.com (authentication, requests, rate-limits, landing page) plus the live OpenAPI spec file (parsed). Machine-readable version: `data/etsy_market_api_requirements.json`, `data/etsy_market_openapi_extract.json`.

### 5.1 Authentication (verified)
* Header on **every** request: `x-api-key: <keystring>:<shared_secret>`. This changed on **9 Feb 2026** (announced 2 Feb 2026, github.com/etsy/open-api/discussions/1529: requests with only the keystring "will be rejected"). Verified live on 2026-10-04: key-less `GET https://openapi.etsy.com/v3/application/openapi-ping` → `403 {"error":"Invalid API key: should be in the format 'keystring:shared_secret'."}`.
* OAuth 2.0 (`Authorization: Bearer <user_id>.<access_token>`) is only needed for private/write endpoints. **32 of the 105 operations are API-key-only, including every endpoint below.**
* Base URL `https://openapi.etsy.com` (docs also list `https://api.etsy.com/v3/`).

### 5.2 The two jobs
**(a) Keyword search, relevance sort**
`GET https://openapi.etsy.com/v3/application/listings/active?keywords=hoya%20sunrise&sort_on=score&limit=100&offset=0`
Parameters: `limit` 1-100 (default 25), `offset`, `keywords`, `sort_on` ∈ created | price | updated | **score**, `sort_order`, `min_price`, `max_price`, `taxonomy_id`, `shop_location`, `is_safe`, `currency`, `buyer_country`. Spec notes: `sort_on` only works with a search option such as `keywords`; with `score` results are always descending. Returns `{count, results[]}`; each result is a ShopListing (57 fields) including **`title`, `tags[]` (the 13 tags), `materials[]`, `price{amount,divisor,currency_code}`, `quantity`, `num_favorers`, `created/updated timestamps`, `shop_id`, `taxonomy_id`, `has_variations`, `should_auto_renew`, `shipping_profile_id`, `url`, `listing_type`**. There is no `includes` parameter on this endpoint and shipping *cost* is not in the listing. Add images, shop and the `views` field with `GET /v3/application/listings/batch?listing_ids=1,2,3&includes=Images,Shop`. `score` is Etsy's relevance score; it may not equal the order a logged-in shopper sees (personalisation, ads, location).

**(b) A shop, its listings, its reviews**
* find the ID: `GET /v3/application/shops?shop_name=RvsdGreenhouses`
* shop: `GET /v3/application/shops/{shop_id}` → `shop_name`, `create_date`, `listing_active_count`, **`transaction_sold_count`** (lifetime sales), `num_favorers`, **`review_count` and `review_average` (reviews in the past year per the spec)**, `is_vacation`, `currency_code`, `shop_location_country_iso`, policies (47 fields)
* active listings: `GET /v3/application/shops/{shop_id}/listings/active?limit=100&offset=N` (also supports `keywords`, `sort_on`)
* reviews: `GET /v3/application/shops/{shop_id}/reviews?limit=100&offset=N&min_created=..&max_created=..` → `rating` 1-5, `review` text, `listing_id`, `transaction_id`, timestamps, optional `image_url_fullxfull`; per item: `GET /v3/application/listings/{listing_id}/reviews`

### 5.3 Rate limits
Per API key (public and private alike): QPS and QPD with a sliding 24 h window. Your numbers are shown per app in the Developer Portal (the docs print only an example: 150 QPS / 100,000 QPD). Response headers `x-limit-per-second`, `x-remaining-this-second`, `x-limit-per-day`, `x-remaining-today`; HTTP 429 carries `retry-after`; more quota by emailing developer@etsy.com. Third-party posts quote 5-10 QPS / 5,000-10,000 QPD defaults for new apps: unconfirmed. The full study needs fewer than 300 calls (25 keywords x 3 pages, about 150 getShop calls).

### 5.4 How the owner gets a key (about 10 minutes)
1. Sign in to etsy.com with the account that owns RvsdGreenhouses (shop active and in good standing, no app registered yet).
2. Open `https://www.etsy.com/developers/register`, fill in the form (app name, short description). Pick **Seller App** (own-shop tools, "approved within minutes, with no manual review queue"); Personal App is the deeper-review path; Commercial Access needs an approved Personal App first.
3. Accept the API Terms of Use (`etsy.com/legal/api`: my fetch got HTTP 403, so I could not read it; the owner should check the clauses on storing/caching Etsy content and competitive use before collecting other shops' data).
4. Wait for approval ("Your API key is not active until it has been approved").
5. `https://www.etsy.com/developers/your-apps`: click the eye icon beside the shared secret; copy **both** keystring and shared secret.
6. Test: `curl -H 'x-api-key: KEYSTRING:SHARED_SECRET' https://openapi.etsy.com/v3/application/openapi-ping` (expect 200).
7. Export `ETSY_KEYSTRING` and `ETSY_SHARED_SECRET`, run `python3 SCRATCH/data/etsy_market_api_quickstart.py --ping` then `--run --out ./etsy_api_out`. Do not paste the secret into chat or git.

Open question for step 2: the docs restrict a Seller App's **OAuth** to the owner's own shop; they do not say whether its key may read **public** data about other shops. The spec lists those endpoints as API-key-only, so it should; the first competitor search tells.

### 5.5 What the script does (tested offline only)
`data/etsy_market_api_quickstart.py`: ping → find shop id → getShop → owner's active listings → for each of the 25 keywords three pages of `sort_on=score` (300 listings) with the owner's best rank → `getShop` for every shop in any top 30 → CSVs. `--selftest` passes (mock transport, checks header format, paging, rank detection). It has **not** been run against Etsy because no key exists.

### 5.6 Composio
Nine Etsy-focused queries in three `COMPOSIO_SEARCH_TOOLS` calls (auto and tool_search strategies) returned **no Etsy toolkit**. The only Etsy-named tools belong to `benchmark_email` (`BENCHMARK_EMAIL_GET_ETSY_STORE_NAME`, `..._TEST_ETSY_INTEGRATION`, `..._CONNECT_SERVICE` with AuthSite ETSY/EBAY/SHOPIFY/SALESFORCE, `..._DISCONNECT_ETSY_INTEGRATION`): Benchmark Email's own e-mail-marketing integration, useless for listings, search or reviews. Nothing needs connecting for Etsy; run the script with the owner's key, or add a custom HTTP/MCP connection in the Composio dashboard. No connection was started. Active toolkits seen: shopify (`shopify_kilim-melic`, unused), and instant accounts for serpapi, serper, just_one_api, composio_search (used read-only for search results).

## 6. What the owner can export, and what finishes the comparison

Full list with paths: `data/etsy_market_exports.json`. (Menu paths come from Etsy Help titles/snippets and Alura's seller docs; Etsy's own help pages were blocked to me.)

| Export / screen | Where | Gives us |
|---|---|---|
| Listings CSV | Shop Manager > Settings > Options > Download Data > Listings | current titles, description, price, quantity, **tags**, materials, image URLs (photo count), SKU. No traffic data |
| Order Items / Orders CSV | same tab > Orders (CSV type, month, year) | sales per listing and date, shipping destinations |
| Reviews CSV | same tab > Take your data with you > Download Your Reviews | review timing and text per listing |
| Stats > How shoppers found you > Etsy search | Shop Manager > Stats | search terms with visits, traffic-source split (Etsy search / Etsy Ads / Offsite Ads / social / direct); CSV for search terms not confirmed |
| **Marketing > Search Analytics** | Shop Manager > Marketing | per query: impressions, visits, orders, conversion, revenue and **position**; listing drill-down. The only first-party source of the owner's own rank per query |
| Etsy Search Visibility page | Shop Manager | Etsy's own diagnosis in three areas (shop, listing, customer-service quality) |
| Marketplace Insights | Shop Manager > Stats | search data/trends for any keyword the owner types |
| Star Seller dashboard / Customer Service Standards | Shop Manager | response rate (95% in 24 h), on-time shipping with tracking (95%), average rating; tells whether the badge is held |
| Etsy Ads search terms | Marketing > Etsy Ads | separates paid from organic placement |
| Owner-run logged-out searches | owner's browser, private window, "Save page" for 25 queries x 2 pages | the real Etsy result order today, with ad labels and badges |

**Minimum set to finish the Etsy comparison properly:** (A) API key + the collector script → relevance-sorted top 300 per keyword with tags, prices, favorites, listing age and shop review/sales counts, plus the owner's rank in each; (B) Listings CSV + Search Analytics (position per query) + Stats search terms; (C) Reviews CSV + Order Items CSV. (A) answers "who is above me and what do they have", (B) answers "where am I and why", (C) answers "which listings convert".

## 7. Suggested next steps (hypotheses to test, ordered by expected value)

1. Get the API key (5.4) and run the script: replaces all proxies in this report with Etsy's own relevance order and tag lists.
2. Capture Search Analytics for the 25 plant terms (position, impressions, orders): finds the queries where the owner is on page 1 but not converting, and vice versa.
3. Test titles on the weakest placements first: Chinese Money Plant (page 2-6), Satin Pothos (page 3), Syngonium Pink Splash, Hoya Kerrii, Christmas Cactus. Hypothesis: drop the 27-character brand tail and the generic "Easy Care ... Indoor Plant", and spend the first ~60 characters on the buyer query plus synonyms that appear in competitors' titles. Examples (use only if true of what you ship; change one group at a time and read the result in Search Analytics after about two weeks):
   * now: `Chinese Money Plant 4" Live Houseplant | Pilea Peperomioides | Easy Care Indoor Plant from Riverside Greenhouses`
   * test: `Chinese Money Plant Pilea Peperomioides 4" Live Plant | UFO Plant | Free Shipping | Ships from California`
   * now: `Hoya Sunrise 4" Live Houseplant | Rare Hoya | Easy Care Indoor Vining Plant from Riverside Greenhouses`
   * test: `Hoya Sunrise (Tequila Sunrise) 4" Live Hoya Plant | Rare Wax Plant | Free Shipping`
4. Price: Chinese Money Plant ($21.99) sits above 72% of Google's Etsy rows and the field is 52% "Free delivery"; the four plants where the owner is at/above the median are the ones to look at first. Elsewhere the owner is below the median and has been raising prices without losing sales, so there is probably room; watch conversion in Search Analytics.
5. Consolidate or differentiate the duplicate listings (Satin Pothos x2, Syngonium Pink Splash x2) so they do not split reviews and relevance. List Raven ZZ, Pink Princess, Hoya Cummingiana and Texas Ebony on Etsy only if stock exists.
6. Check the Star Seller dashboard: 89 sales and 4.9 stars are in the range where many recurring shops hold the badge; a Star Seller mention is visible for 4 of the 12 recurring shops.

## 8. Files

Reports: `SCRATCH/reports/etsy_market.md`. Data (`SCRATCH/data/`): `etsy_market_summary.json`, `etsy_market_owner_catalog.csv|json`, `etsy_market_owner_shop_snapshots.csv`, `etsy_market_owner_on_market_pages.csv`, `etsy_market_owner_relevant_market_pages.csv`, `etsy_market_owner_price_position.csv`, `etsy_market_plant_matrix.csv`, `etsy_market_per_plant_summary.csv`, `etsy_market_per_plant_gshopping_top10.csv`, `etsy_market_per_plant_google_organic.csv`, `etsy_market_gshopping_all.csv`, `etsy_market_gshopping_enriched.csv|json`, `etsy_market_gshopping_position_correlations.json`, `etsy_market_title_structure.csv`, `etsy_market_listings_web.csv|json` (1,299 listing IDs), `etsy_market_shops_all.csv`, `etsy_market_recurring_shops_top12.csv`, `etsy_market_api_requirements.json`, `etsy_market_openapi_extract.json`, `etsy_market_exports.json`, `etsy_market_api_quickstart.py`. Raw dumps and builders: `SCRATCH/etsy_market_raw/` (Google Shopping JSON, Serper JSON, Etsy OpenAPI spec) and `SCRATCH/etsy_market_*.py` (`etsy_market_build_all.sh` rebuilds everything offline).

## 9. Limits and honesty notes

* No etsy.com listing or shop page was fetched by this project. The only successful requests to Etsy-operated hosts were the public OpenAPI spec file, developers.etsy.com doc pages, one key-less API ping, and github.com discussion #1529; three plain fetches (legal/api and two help articles) were refused with 403 and not retried. All shop/listing facts are search-engine snippets of unknown age; the shop block is printed by Etsy for logged-out visitors, so it matches what a shopper sees.
* Only a minority of Shopping rows could be tied to a shop or listing ID; competitor shop tables rest mostly on the web-snippet data, not on Shopping rows.
* Google Shopping rating/review fields are product-level; Etsy keyword-page cards show shop-level review counts.
* The correlations in 4.3 and 1.8 are exploratory and describe Google. Etsy's actual algorithm is not recoverable from these sources.
* I used about 1,000 Serper queries and 54 Shopping queries from Composio's shared instant accounts (free tier). That is more than my first estimate; no further bulk querying is needed.

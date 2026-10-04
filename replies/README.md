# Riverside Reply Desk

Drafts replies to Etsy reviews and buyer messages; you copy, paste into Etsy and send. Nothing is ever sent automatically.

- **Queue page (private):** https://claude.ai/artifact/V3ozFFjatMF8z6UWW85KS9
  - "Draft a reply now": paste any message or review and get a draft that follows your playbook.
  - Queue: each item shows the buyer's words, an editable draft, Copy reply / Mark sent / Skip / Redo draft.
  - Shop playbook: your policies, tone and sign-off. Fix the [confirm] items.
- **Scheduled assistant:** a Claude routine runs `routine_prompt.md` a few times a day, pulls new reviews (`fetch_etsy_reviews.py`, Etsy API) and new message notifications (your shop email), drafts replies and adds them to the queue.

## Setup checklist
- [x] Queue page and playbook
- [x] Etsy review fetcher (`fetch_etsy_reviews.py`) — tested without a key only
- [ ] Owner confirms the playbook's [confirm] items
- [ ] Etsy approves the API app → add `ETSY_KEYSTRING` and `ETSY_SHARED_SECRET` in the cloud environment settings (environment menu in the session title bar → Edit). Never paste them in chat.
- [ ] Messages: the shop email is Yahoo. There is no claude.ai Yahoo connector, and the cloud environment cannot reach Yahoo's IMAP port (993; only 443 is allowed through the proxy).
      Options: (a) paste messages into the Reply Desk (works now); (b) send Etsy notifications to a Gmail address and connect Gmail at https://claude.ai/customize/connectors;
      (c) run `fetch_yahoo_etsy_messages.py` on a computer you own (needs YAHOO_EMAIL + YAHOO_APP_PASSWORD there).
- [ ] CHOSEN: owner forwards the Yahoo inbox to a dedicated Riverside Greenhouses Gmail and connects that Gmail at https://claude.ai/customize/connectors (fallback if Yahoo forwarding needs Yahoo Mail Plus: change the Etsy account email to the new Gmail).
- [ ] In a new session (connectors load at session start): confirm Etsy's "new message" emails include the message text, then create the routine with the Gmail connector — it can draft messages before the Etsy API key arrives (reviews are skipped until then)
- [ ] Create the routine (3×/day) with the email connector attached
- [ ] Next: eBay (Feedback API respond_to_feedback; Trading API member messages). Negative feedback is never auto-answered (eBay policy).

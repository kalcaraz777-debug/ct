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
- [ ] Owner connects the shop email as a claude.ai connector
- [ ] Check that Etsy's "new message" emails include the message text
- [ ] Create the routine (3×/day) with the email connector attached
- [ ] Next: eBay (Feedback API respond_to_feedback; Trading API member messages). Negative feedback is never auto-answered (eBay policy).

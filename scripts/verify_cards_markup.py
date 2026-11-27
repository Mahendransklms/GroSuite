with open('pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for prod, p_id in [('GROHRMS', 'grohrms-pricing'), ('GROLOG', 'grolog-pricing'), ('GROINN', 'groinn-pricing')]:
    print(f"\n==================== {prod} ====================")
    sec_idx = text.find(f'id="{p_id}"')
    sec_end = text.find('</section>', sec_idx)
    sec_text = text[sec_idx:sec_end]
    cards = re.findall(r'<article class="pricing-card[^"]*">([\s\S]*?)</article>', sec_text)
    for i, c in enumerate(cards):
        h3 = re.search(r'<h3>([^<]+)</h3>', c)
        title = h3.group(1) if h3 else f"Card {i+1}"
        price_box = re.search(r'<div class="pricing-card__price-box[^"]*">([\s\S]*?)</div>', c)
        note_box = re.search(r'<p class="pricing-card__billing-note"[^>]*>([\s\S]*?)</p>', c)
        p_clean = re.sub(r'\s+', ' ', price_box.group(0).strip()) if price_box else "N/A"
        n_clean = re.sub(r'\s+', ' ', note_box.group(0).strip()) if note_box else "N/A"
        print(f"[{title}]")
        print(f"  Price box: {p_clean}")
        print(f"  Note pill: {n_clean}")

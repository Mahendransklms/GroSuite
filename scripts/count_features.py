import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

groinn_match = re.search(r'<section class="pricing-section" id="groinn-pricing"[\s\S]*?</section>', html)
if groinn_match:
    groinn_sec = groinn_match.group(0)
    cards = re.findall(r'<article class="pricing-card[\s\S]*?</article>', groinn_sec)
    for idx, c in enumerate(cards):
        title_m = re.search(r'<h3>(.*?)</h3>', c)
        title = title_m.group(1) if title_m else "Unknown"
        lis = re.findall(r'<li>[\s\S]*?</li>', c)
        print(f"Card {idx+1} ({title}): {len(lis)} features")

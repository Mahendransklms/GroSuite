with open('pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Remove any consecutive duplicate pricing-card__original-price elements
text = re.sub(
    r'(<span class="pricing-card__original-price"[^>]*>.*?</span>\s*)+',
    lambda m: m.group(1),
    text
)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Duplicates cleaned.")

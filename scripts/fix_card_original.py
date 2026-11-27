with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Fix any occurrences of >number">number</span>
html = re.sub(r'(style="display: inline;">)\d[\d,]*">(\d[\d,]*)</span>', r'\g<1>\g<2></span>', html)
# Let's inspect all cardOriginal elements in html
origs = re.findall(r'<span class="pricing-card__original-price"[^>]*>[^<]*</span>', html)
print("Before clean:")
for o in origs:
    print(o)

# Let's do exact clean replacements for cardOriginal:
html = re.sub(
    r'<span class="pricing-card__original-price" id="cardOriginalBasic"[^>]*>[^<]*</span>',
    r'<span class="pricing-card__original-price" id="cardOriginalBasic" style="display: none;">180</span>',
    html
)
html = re.sub(
    r'<span class="pricing-card__original-price" id="cardOriginalStandard"[^>]*>[^<]*</span>',
    r'<span class="pricing-card__original-price" id="cardOriginalStandard" style="display: inline;">360</span>',
    html
)
html = re.sub(
    r'<span class="pricing-card__original-price" id="cardOriginalPrime"[^>]*>[^<]*</span>',
    r'<span class="pricing-card__original-price" id="cardOriginalPrime" style="display: inline;">720</span>',
    html
)

html = re.sub(
    r'<span class="pricing-card__original-price" id="cardOriginalGrolog1"[^>]*>[^<]*</span>',
    r'<span class="pricing-card__original-price" id="cardOriginalGrolog1" style="display: inline;">4,200</span>',
    html
)
html = re.sub(
    r'<span class="pricing-card__original-price" id="cardOriginalGrolog2"[^>]*>[^<]*</span>',
    r'<span class="pricing-card__original-price" id="cardOriginalGrolog2" style="display: inline;">4,200</span>',
    html
)
html = re.sub(
    r'<span class="pricing-card__original-price" id="cardOriginalGrolog3"[^>]*>[^<]*</span>',
    r'<span class="pricing-card__original-price" id="cardOriginalGrolog3" style="display: inline;">4,200</span>',
    html
)

html = re.sub(
    r'<span class="pricing-card__original-price" id="cardOriginalGroinn1"[^>]*>[^<]*</span>',
    r'<span class="pricing-card__original-price" id="cardOriginalGroinn1" style="display: none;">12,000</span>',
    html
)
html = re.sub(
    r'<span class="pricing-card__original-price" id="cardOriginalGroinn2"[^>]*>[^<]*</span>',
    r'<span class="pricing-card__original-price" id="cardOriginalGroinn2" style="display: inline;">24,000</span>',
    html
)
html = re.sub(
    r'<span class="pricing-card__original-price" id="cardOriginalGroinn3"[^>]*>[^<]*</span>',
    r'<span class="pricing-card__original-price" id="cardOriginalGroinn3" style="display: inline;">36,000</span>',
    html
)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nAfter clean:")
origs2 = re.findall(r'<span class="pricing-card__original-price"[^>]*>[^<]*</span>', html)
for o in origs2:
    print(o)

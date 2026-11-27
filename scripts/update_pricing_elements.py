import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Grohrms price boxes
# Basic
html = re.sub(
    r'(<span class="pricing-card__amount" id="cardAmountBasic"[^>]*>15</span>\s*)(<span class="pricing-card__period" id="cardPeriodBasic">)',
    r'\1<span class="pricing-card__original-price" id="cardOriginalBasic" style="display: none;">15</span>\n                  \2',
    html
)

# Standard
html = re.sub(
    r'(<span class="pricing-card__amount" id="cardAmountStandard"[^>]*>30</span>\s*)(<span class="pricing-card__period" id="cardPeriodStandard">)',
    r'\1<span class="pricing-card__original-price" id="cardOriginalStandard" style="display: none;">30</span>\n                  \2',
    html
)

# Prime
html = re.sub(
    r'(<span class="pricing-card__amount" id="cardAmountPrime"[^>]*>60</span>\s*)(<span class="pricing-card__period" id="cardPeriodPrime">)',
    r'\1<span class="pricing-card__original-price" id="cardOriginalPrime" style="display: none;">60</span>\n                  \2',
    html
)

# 2. Update Grolog price boxes
# Tier 1
html = re.sub(
    r'(<span class="pricing-card__amount" id="cardAmountGrolog1"[^>]*>350</span>\s*)(<span class="pricing-card__period" id="cardPeriodGrolog1">)',
    r'\1<span class="pricing-card__original-price" id="cardOriginalGrolog1" style="display: none;">350</span>\n                  \2',
    html
)

# Tier 2
html = re.sub(
    r'(<span class="pricing-card__amount" id="cardAmountGrolog2"[^>]*>300</span>\s*)(<span class="pricing-card__period" id="cardPeriodGrolog2">)',
    r'\1<span class="pricing-card__original-price" id="cardOriginalGrolog2" style="display: none;">300</span>\n                  \2',
    html
)

# Tier 3
html = re.sub(
    r'(<span class="pricing-card__amount" id="cardAmountGrolog3"[^>]*>250</span>\s*)(<span class="pricing-card__period" id="cardPeriodGrolog3">)',
    r'\1<span class="pricing-card__original-price" id="cardOriginalGrolog3" style="display: none;">250</span>\n                  \2',
    html
)

# 3. Update Groinn price boxes
# Tier 1
html = re.sub(
    r'(<span class="pricing-card__amount" id="cardAmountGroinn1"[^>]*>1000</span>\s*)(<span class="pricing-card__period" id="cardPeriodGroinn1">)',
    r'\1<span class="pricing-card__original-price" id="cardOriginalGroinn1" style="display: none;">1000</span>\n                \2',
    html
)

# Tier 2
html = re.sub(
    r'(<span class="pricing-card__amount" id="cardAmountGroinn2"[^>]*>1000</span>\s*)(<span class="pricing-card__period" id="cardPeriodGroinn2">)',
    r'\1<span class="pricing-card__original-price" id="cardOriginalGroinn2" style="display: none;">1000</span>\n                \2',
    html
)

# Tier 3
html = re.sub(
    r'(<span class="pricing-card__amount" id="cardAmountGroinn3"[^>]*>1000</span>\s*)(<span class="pricing-card__period" id="cardPeriodGroinn3">)',
    r'\1<span class="pricing-card__original-price" id="cardOriginalGroinn3" style="display: none;">1000</span>\n                \2',
    html
)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated HTML markup successfully.")

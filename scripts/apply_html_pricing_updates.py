import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Grohrms price boxes in HTML
# Basic
html = re.sub(
    r'(<div class="pricing-card__price-box">\s*<span class="pricing-card__currency" id="cardCurrencyBasic">[^<]*</span>\s*<span class="pricing-card__amount" id="cardAmountBasic"[^>]*>)[^<]*(</span>\s*<span class="pricing-card__original-price" id="cardOriginalBasic"[^>]*>)[^<]*(</span>\s*<span class="pricing-card__period" id="cardPeriodBasic">)[^<]*(</span>\s*</div>\s*<p class="pricing-card__billing-note" id="cardNoteBasic"[^>]*>)[^<]*(</p>)',
    r'\g<1>180\g<2>180\g<3>/ user / yr\g<4>Monthly Pack: ₹15 / user / mo\g<5>',
    html
)

# Standard
html = re.sub(
    r'(<div class="pricing-card__price-box">\s*<span class="pricing-card__currency" id="cardCurrencyStandard">[^<]*</span>\s*<span class="pricing-card__amount" id="cardAmountStandard"[^>]*>)[^<]*(</span>\s*<span class="pricing-card__original-price" id="cardOriginalStandard"[^>]*style=")[^"]*(">[^<]*</span>\s*<span class="pricing-card__period" id="cardPeriodStandard">)[^<]*(</span>\s*</div>\s*<p class="pricing-card__billing-note" id="cardNoteStandard"[^>]*>)[^<]*(</p>)',
    r'\g<1>324</span><span class="pricing-card__original-price" id="cardOriginalStandard" style="display: inline;">360\g<3>/ user / yr\g<4>Monthly Pack: ₹30 / user / mo\g<5>',
    html
)

# Prime
html = re.sub(
    r'(<div class="pricing-card__price-box">\s*<span class="pricing-card__currency" id="cardCurrencyPrime">[^<]*</span>\s*<span class="pricing-card__amount" id="cardAmountPrime"[^>]*>)[^<]*(</span>\s*<span class="pricing-card__original-price" id="cardOriginalPrime"[^>]*style=")[^"]*(">[^<]*</span>\s*<span class="pricing-card__period" id="cardPeriodPrime">)[^<]*(</span>\s*</div>\s*<p class="pricing-card__billing-note" id="cardNotePrime"[^>]*>)[^<]*(</p>)',
    r'\g<1>576</span><span class="pricing-card__original-price" id="cardOriginalPrime" style="display: inline;">720\g<3>/ user / yr\g<4>Monthly Pack: ₹60 / user / mo\g<5>',
    html
)

# 2. Update Grolog price boxes in HTML
# Tier 1
html = re.sub(
    r'(<div class="pricing-card__price-box">\s*<span class="pricing-card__currency" id="cardCurrencyGrolog1">[^<]*</span>\s*<span class="pricing-card__amount" id="cardAmountGrolog1"[^>]*>)[^<]*(</span>\s*<span class="pricing-card__original-price" id="cardOriginalGrolog1"[^>]*style=")[^"]*(">[^<]*</span>\s*<span class="pricing-card__period" id="cardPeriodGrolog1">)[^<]*(</span>\s*</div>\s*<p class="pricing-card__billing-note" id="cardNoteGrolog1"[^>]*>)[^<]*(</p>)',
    r'\g<1>3,990</span><span class="pricing-card__original-price" id="cardOriginalGrolog1" style="display: inline;">4,200\g<3>/ user / yr\g<4>Monthly Pack: ₹350 / user / mo\g<5>',
    html
)

# Tier 2
html = re.sub(
    r'(<div class="pricing-card__price-box">\s*<span class="pricing-card__currency" id="cardCurrencyGrolog2">[^<]*</span>\s*<span class="pricing-card__amount" id="cardAmountGrolog2"[^>]*>)[^<]*(</span>\s*<span class="pricing-card__original-price" id="cardOriginalGrolog2"[^>]*style=")[^"]*(">[^<]*</span>\s*<span class="pricing-card__period" id="cardPeriodGrolog2">)[^<]*(</span>\s*</div>\s*<p class="pricing-card__billing-note" id="cardNoteGrolog2"[^>]*>)[^<]*(</p>)',
    r'\g<1>3,780</span><span class="pricing-card__original-price" id="cardOriginalGrolog2" style="display: inline;">4,200\g<3>/ user / yr\g<4>Monthly Pack: ₹350 / user / mo\g<5>',
    html
)

# Tier 3
html = re.sub(
    r'(<div class="pricing-card__price-box">\s*<span class="pricing-card__currency" id="cardCurrencyGrolog3">[^<]*</span>\s*<span class="pricing-card__amount" id="cardAmountGrolog3"[^>]*>)[^<]*(</span>\s*<span class="pricing-card__original-price" id="cardOriginalGrolog3"[^>]*style=")[^"]*(">[^<]*</span>\s*<span class="pricing-card__period" id="cardPeriodGrolog3">)[^<]*(</span>\s*</div>\s*<p class="pricing-card__billing-note" id="cardNoteGrolog3"[^>]*>)[^<]*(</p>)',
    r'\g<1>3,570</span><span class="pricing-card__original-price" id="cardOriginalGrolog3" style="display: inline;">4,200\g<3>/ user / yr\g<4>Monthly Pack: ₹350 / user / mo\g<5>',
    html
)

# 3. Update Groinn price boxes in HTML
# Tier 1 - Basic: 12000/year, Monthly pack: 1000/month
html = re.sub(
    r'(<div class="pricing-card__price-box">\s*<span class="pricing-card__currency" id="cardCurrencyGroinn1">[^<]*</span>\s*<span class="pricing-card__amount" id="cardAmountGroinn1"[^>]*>)[^<]*(</span>\s*<span class="pricing-card__original-price" id="cardOriginalGroinn1"[^>]*>)[^<]*(</span>\s*<span class="pricing-card__period" id="cardPeriodGroinn1">)[^<]*(</span>\s*</div>\s*<p class="pricing-card__billing-note" id="cardNoteGroinn1"[^>]*>)[^<]*(</p>)',
    r'\g<1>12,000\g<2>12,000\g<3>/ year\g<4>Monthly Pack: ₹1,000 / month\g<5>',
    html
)

# Tier 2 - Standard: 20000/year, Monthly pack: 2000/month
html = re.sub(
    r'(<div class="pricing-card__price-box">\s*<span class="pricing-card__currency" id="cardCurrencyGroinn2">[^<]*</span>\s*<span class="pricing-card__amount" id="cardAmountGroinn2"[^>]*>)[^<]*(</span>\s*<span class="pricing-card__original-price" id="cardOriginalGroinn2"[^>]*style=")[^"]*(">[^<]*</span>\s*<span class="pricing-card__period" id="cardPeriodGroinn2">)[^<]*(</span>\s*</div>\s*<p class="pricing-card__billing-note" id="cardNoteGroinn2"[^>]*>)[^<]*(</p>)',
    r'\g<1>20,000</span><span class="pricing-card__original-price" id="cardOriginalGroinn2" style="display: inline;">24,000\g<3>/ year\g<4>Monthly Pack: ₹2,000 / month\g<5>',
    html
)

# Tier 3 - Prime: 30000/year, Monthly pack: 3000/month
html = re.sub(
    r'(<div class="pricing-card__price-box">\s*<span class="pricing-card__currency" id="cardCurrencyGroinn3">[^<]*</span>\s*<span class="pricing-card__amount" id="cardAmountGroinn3"[^>]*>)[^<]*(</span>\s*<span class="pricing-card__original-price" id="cardOriginalGroinn3"[^>]*style=")[^"]*(">[^<]*</span>\s*<span class="pricing-card__period" id="cardPeriodGroinn3">)[^<]*(</span>\s*</div>\s*<p class="pricing-card__billing-note" id="cardNoteGroinn3"[^>]*>)[^<]*(</p>)',
    r'\g<1>30,000</span><span class="pricing-card__original-price" id="cardOriginalGroinn3" style="display: inline;">36,000\g<3>/ year\g<4>Monthly Pack: ₹3,000 / month\g<5>',
    html
)

# Update data-annual and data-monthly on Groinn cards
html = html.replace('id="cardAmountGroinn1" data-monthly="1000"\n                  data-annual="12000"', 'id="cardAmountGroinn1" data-monthly="1000" data-annual="12000"')
html = html.replace('id="cardAmountGroinn2" data-monthly="1000"\n                  data-annual="12000"', 'id="cardAmountGroinn2" data-monthly="2000" data-annual="20000"')
html = html.replace('id="cardAmountGroinn3" data-monthly="1000"\n                  data-annual="12000"', 'id="cardAmountGroinn3" data-monthly="3000" data-annual="30000"')

# Hide product-billing-control cleanly
html = re.sub(
    r'<div class="product-billing-control">',
    r'<div class="product-billing-control" style="display: none;">',
    html
)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML price boxes updated successfully!")

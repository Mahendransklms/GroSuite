with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update cardAmountGroinn3 HTML markup
html = html.replace('data-annual="30000">30,000</span>', 'data-annual="28000">28,000</span>')

# 2. Update currencyRates.INR.groinn.tier3
html = html.replace(
    'tier3: { monthly: 3000, annual: 30000, originalAnnual: 36000 }',
    'tier3: { monthly: 3000, annual: 28000, originalAnnual: 36000 }'
)

# 3. Update comments and fallback in renderPricingGroinn
html = html.replace(
    '// Tier 3: Prime (30000/year, Monthly pack: 3000/month, Regular: 36000/year)',
    '// Tier 3: Prime (28000/year, Monthly pack: 3000/month, Regular: 36000/year)'
)
html = html.replace(
    'const groinn3Annual = (cur.groinn && cur.groinn.tier3) ? cur.groinn.tier3.annual : 30000;',
    'const groinn3Annual = (cur.groinn && cur.groinn.tier3) ? cur.groinn.tier3.annual : 28000;'
)
html = html.replace(
    '// Tier 3 - Prime: Show Annually plan amount in main price (30,000 / year with 36,000 struck), Monthly pack in marked box (3,000 / month)',
    '// Tier 3 - Prime: Show Annually plan amount in main price (28,000 / year with 36,000 struck), Monthly pack in marked box (3,000 / month)'
)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated Groinn Prime pack rate from 30,000 to 28,000 successfully!")

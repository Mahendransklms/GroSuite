with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_quote = """              <div class="pricing-card__price-box">
                <span class="pricing-card__amount" style="font-size: 2.1rem; line-height: 1.2;">Custom Quote</span>
              </div>"""

new_quote = """              <div class="pricing-card__price-box pricing-card__price-box--quote">
                <span class="pricing-card__amount pricing-card__amount--quote">Custom Quote</span>
              </div>"""

html = html.replace(old_quote, new_quote)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated Custom Quote markup.")

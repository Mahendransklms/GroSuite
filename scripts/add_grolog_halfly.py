import re

# 1. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_hide = """#grolog-pricing .product-billing-control,
#groinn-pricing .product-billing-control {
  display: none !important;
}"""

new_hide = """#groinn-pricing .product-billing-control {
  display: none !important;
}"""

if old_hide in css:
    css = css.replace(old_hide, new_hide)
    print("Replaced hide rule in css/style.css!")
else:
    css = re.sub(
        r'#grolog-pricing\s*\.product-billing-control\s*,\s*#groinn-pricing\s*\.product-billing-control\s*\{[^}]*\}',
        new_hide,
        css
    )
    print("Regex replaced hide rule in css/style.css!")

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update pricing.html
with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate Grolog section
grolog_idx = html.find('id="grolog-pricing"')
groinn_idx = html.find('id="groinn-pricing"')

grolog_part = html[grolog_idx:groinn_idx]

# Remove style="display: none;" from Grolog product-billing-control
old_grolog_btn_group = """            <div class="product-billing-control" style="display: none;">
              <div class="billing-btn-group" role="group" aria-label="Grolog billing frequency">
                <button type="button" class="billing-btn active" id="btnMonthlyGrolog" data-product="grolog"
                  data-period="monthly" aria-pressed="true">
                  <span>Monthly</span>
                </button>
                <button type="button" class="billing-btn" id="btnAnnualGrolog" data-product="grolog"
                  data-period="annual" aria-pressed="false">
                  <span>Annually</span>
                  <span class="billing-discount-badge">Up to 15% Off</span>
                </button>
              </div>
            </div>"""

new_grolog_btn_group = """            <div class="product-billing-control">
              <div class="billing-btn-group" role="group" aria-label="Grolog billing frequency">
                <button type="button" class="billing-btn" id="btnMonthlyGrolog" data-product="grolog"
                  data-period="monthly" aria-pressed="false" style="display: none;">
                  <span>Monthly</span>
                </button>
                <button type="button" class="billing-btn" id="btnHalflyGrolog" data-product="grolog"
                  data-period="halfly" aria-pressed="false">
                  <span>Half-Yearly</span>
                  <span class="billing-discount-badge">Save up to 15%</span>
                </button>
                <button type="button" class="billing-btn active" id="btnAnnualGrolog" data-product="grolog"
                  data-period="annual" aria-pressed="true">
                  <span>Annually</span>
                  <span class="billing-discount-badge">Up to 15% Off</span>
                </button>
              </div>
            </div>"""

assert old_grolog_btn_group in grolog_part, "old_grolog_btn_group not found!"
grolog_part_new = grolog_part.replace(old_grolog_btn_group, new_grolog_btn_group)
html = html[:grolog_idx] + grolog_part_new + html[groinn_idx:]
print("Updated Grolog switcher HTML!")

# 3. Add grologBillingCycle in JS
old_grolog_var = "let isAnnualGrolog = true;"
new_grolog_var = "let isAnnualGrolog = true;\n      let grologBillingCycle = 'annual';"
html = html.replace(old_grolog_var, new_grolog_var, 1)

# 4. Update renderPricingGrolog in JS
start_marker = "function renderPricingGrolog() {"
end_marker = "function renderPricingGroinn() {"

idx_start = html.find(start_marker)
idx_end = html.find(end_marker)

assert idx_start != -1 and idx_end != -1, "renderPricingGrolog markers not found!"

new_render_grolog = """function renderPricingGrolog() {
        const cur = currencyRates[currentCurrency] || currencyRates.INR;
        const sym = cur.symbol.trim();

        // Tier 1: Up to 5 users (350/mo, 2100/6mo base, 5% discount => 1995/6mo; 4200/yr base, 5% discount => 3990/yr)
        const grolog1Monthly = cur.grolog.tier1.monthly;
        const grolog1HalflyTotal = (cur.code === 'INR') ? Math.round(grolog1Monthly * 6) : +(grolog1Monthly * 6).toFixed(2);
        const grolog1HalflyDiscounted = (cur.code === 'INR') ? Math.round(grolog1HalflyTotal * 0.95) : +(grolog1HalflyTotal * 0.95).toFixed(2);
        const grolog1AnnualTotal = (cur.code === 'INR') ? Math.round(grolog1Monthly * 12) : +(grolog1Monthly * 12).toFixed(2);
        const grolog1AnnualDiscounted = (cur.code === 'INR') ? Math.round(grolog1AnnualTotal * 0.95) : +(grolog1AnnualTotal * 0.95).toFixed(2);

        // Tier 2: 10 users (350/mo, 2100/6mo base, 10% discount => 1890/6mo; 4200/yr base, 10% discount => 3780/yr)
        const grolog2Monthly = cur.grolog.tier2.monthly;
        const grolog2HalflyTotal = (cur.code === 'INR') ? Math.round(grolog2Monthly * 6) : +(grolog2Monthly * 6).toFixed(2);
        const grolog2HalflyDiscounted = (cur.code === 'INR') ? Math.round(grolog2HalflyTotal * 0.90) : +(grolog2HalflyTotal * 0.90).toFixed(2);
        const grolog2AnnualTotal = (cur.code === 'INR') ? Math.round(grolog2Monthly * 12) : +(grolog2Monthly * 12).toFixed(2);
        const grolog2AnnualDiscounted = (cur.code === 'INR') ? Math.round(grolog2AnnualTotal * 0.90) : +(grolog2AnnualTotal * 0.90).toFixed(2);

        // Tier 3: 15 users (350/mo, 2100/6mo base, 15% discount => 1785/6mo; 4200/yr base, 15% discount => 3570/yr)
        const grolog3Monthly = cur.grolog.tier3.monthly;
        const grolog3HalflyTotal = (cur.code === 'INR') ? Math.round(grolog3Monthly * 6) : +(grolog3Monthly * 6).toFixed(2);
        const grolog3HalflyDiscounted = (cur.code === 'INR') ? Math.round(grolog3HalflyTotal * 0.85) : +(grolog3HalflyTotal * 0.85).toFixed(2);
        const grolog3AnnualTotal = (cur.code === 'INR') ? Math.round(grolog3Monthly * 12) : +(grolog3Monthly * 12).toFixed(2);
        const grolog3AnnualDiscounted = (cur.code === 'INR') ? Math.round(grolog3AnnualTotal * 0.85) : +(grolog3AnnualTotal * 0.85).toFixed(2);

        if (grologBillingCycle === 'halfly') {
          // Tier 1 - Halfly (1,995 with 2,100 struck)
          if (cardCurrencyGrolog1) cardCurrencyGrolog1.textContent = sym;
          if (cardAmountGrolog1) cardAmountGrolog1.textContent = formatNum(grolog1HalflyDiscounted);
          if (cardOriginalGrolog1) {
            cardOriginalGrolog1.textContent = formatNum(grolog1HalflyTotal);
            cardOriginalGrolog1.style.display = 'inline';
          }
          if (cardPeriodGrolog1) cardPeriodGrolog1.textContent = '/ user / 6 mo';
          if (cardNoteGrolog1) cardNoteGrolog1.textContent = `Monthly Pack: ${sym}${formatNum(grolog1Monthly)} / user / mo`;

          // Tier 2 - Halfly (1,890 with 2,100 struck)
          if (cardCurrencyGrolog2) cardCurrencyGrolog2.textContent = sym;
          if (cardAmountGrolog2) cardAmountGrolog2.textContent = formatNum(grolog2HalflyDiscounted);
          if (cardOriginalGrolog2) {
            cardOriginalGrolog2.textContent = formatNum(grolog2HalflyTotal);
            cardOriginalGrolog2.style.display = 'inline';
          }
          if (cardPeriodGrolog2) cardPeriodGrolog2.textContent = '/ user / 6 mo';
          if (cardNoteGrolog2) cardNoteGrolog2.textContent = `Monthly Pack: ${sym}${formatNum(grolog2Monthly)} / user / mo`;

          // Tier 3 - Halfly (1,785 with 2,100 struck)
          if (cardCurrencyGrolog3) cardCurrencyGrolog3.textContent = sym;
          if (cardAmountGrolog3) cardAmountGrolog3.textContent = formatNum(grolog3HalflyDiscounted);
          if (cardOriginalGrolog3) {
            cardOriginalGrolog3.textContent = formatNum(grolog3HalflyTotal);
            cardOriginalGrolog3.style.display = 'inline';
          }
          if (cardPeriodGrolog3) cardPeriodGrolog3.textContent = '/ user / 6 mo';
          if (cardNoteGrolog3) cardNoteGrolog3.textContent = `Monthly Pack: ${sym}${formatNum(grolog3Monthly)} / user / mo`;

        } else if (grologBillingCycle === 'monthly') {
          // Tier 1 - Monthly
          if (cardCurrencyGrolog1) cardCurrencyGrolog1.textContent = sym;
          if (cardAmountGrolog1) cardAmountGrolog1.textContent = formatNum(grolog1Monthly);
          if (cardOriginalGrolog1) cardOriginalGrolog1.style.display = 'none';
          if (cardPeriodGrolog1) cardPeriodGrolog1.textContent = '/ user / mo';
          if (cardNoteGrolog1) cardNoteGrolog1.textContent = `Monthly Pack: ${sym}${formatNum(grolog1Monthly)} / user / mo`;

          // Tier 2 - Monthly
          if (cardCurrencyGrolog2) cardCurrencyGrolog2.textContent = sym;
          if (cardAmountGrolog2) cardAmountGrolog2.textContent = formatNum(grolog2Monthly);
          if (cardOriginalGrolog2) cardOriginalGrolog2.style.display = 'none';
          if (cardPeriodGrolog2) cardPeriodGrolog2.textContent = '/ user / mo';
          if (cardNoteGrolog2) cardNoteGrolog2.textContent = `Monthly Pack: ${sym}${formatNum(grolog2Monthly)} / user / mo`;

          // Tier 3 - Monthly
          if (cardCurrencyGrolog3) cardCurrencyGrolog3.textContent = sym;
          if (cardAmountGrolog3) cardAmountGrolog3.textContent = formatNum(grolog3Monthly);
          if (cardOriginalGrolog3) cardOriginalGrolog3.style.display = 'none';
          if (cardPeriodGrolog3) cardPeriodGrolog3.textContent = '/ user / mo';
          if (cardNoteGrolog3) cardNoteGrolog3.textContent = `Monthly Pack: ${sym}${formatNum(grolog3Monthly)} / user / mo`;

        } else {
          // Annual (default)
          // Tier 1 - Annually (3,990 with 4,200 struck)
          if (cardCurrencyGrolog1) cardCurrencyGrolog1.textContent = sym;
          if (cardAmountGrolog1) cardAmountGrolog1.textContent = formatNum(grolog1AnnualDiscounted);
          if (cardOriginalGrolog1) {
            cardOriginalGrolog1.textContent = formatNum(grolog1AnnualTotal);
            cardOriginalGrolog1.style.display = 'inline';
          }
          if (cardPeriodGrolog1) cardPeriodGrolog1.textContent = '/ user / yr';
          if (cardNoteGrolog1) cardNoteGrolog1.textContent = `Monthly Pack: ${sym}${formatNum(grolog1Monthly)} / user / mo`;

          // Tier 2 - Annually (3,780 with 4,200 struck)
          if (cardCurrencyGrolog2) cardCurrencyGrolog2.textContent = sym;
          if (cardAmountGrolog2) cardAmountGrolog2.textContent = formatNum(grolog2AnnualDiscounted);
          if (cardOriginalGrolog2) {
            cardOriginalGrolog2.textContent = formatNum(grolog2AnnualTotal);
            cardOriginalGrolog2.style.display = 'inline';
          }
          if (cardPeriodGrolog2) cardPeriodGrolog2.textContent = '/ user / yr';
          if (cardNoteGrolog2) cardNoteGrolog2.textContent = `Monthly Pack: ${sym}${formatNum(grolog2Monthly)} / user / mo`;

          // Tier 3 - Annually (3,570 with 4,200 struck)
          if (cardCurrencyGrolog3) cardCurrencyGrolog3.textContent = sym;
          if (cardAmountGrolog3) cardAmountGrolog3.textContent = formatNum(grolog3AnnualDiscounted);
          if (cardOriginalGrolog3) {
            cardOriginalGrolog3.textContent = formatNum(grolog3AnnualTotal);
            cardOriginalGrolog3.style.display = 'inline';
          }
          if (cardPeriodGrolog3) cardPeriodGrolog3.textContent = '/ user / yr';
          if (cardNoteGrolog3) cardNoteGrolog3.textContent = `Monthly Pack: ${sym}${formatNum(grolog3Monthly)} / user / mo`;
        }
      }

      """

html = html[:idx_start] + new_render_grolog + html[idx_end:]

# 5. Update setGrologBilling in JS
old_set_grolog = """      function setGrologBilling(annual) {
        isAnnualGrolog = annual;
        const btnM = document.getElementById('btnMonthlyGrolog');
        const btnA = document.getElementById('btnAnnualGrolog');
        if (btnM) { btnM.classList.toggle('active', !annual); btnM.setAttribute('aria-pressed', !annual); }
        if (btnA) { btnA.classList.toggle('active', annual); btnA.setAttribute('aria-pressed', annual); }
        renderPricingGrolog();
      }"""

new_set_grolog = """      function setGrologBilling(cycle) {
        if (cycle === true) grologBillingCycle = 'annual';
        else if (cycle === false) grologBillingCycle = 'monthly';
        else grologBillingCycle = cycle;

        isAnnualGrolog = (grologBillingCycle === 'annual');

        const btnM = document.getElementById('btnMonthlyGrolog');
        const btnH = document.getElementById('btnHalflyGrolog');
        const btnA = document.getElementById('btnAnnualGrolog');

        if (btnM) { 
          btnM.classList.toggle('active', grologBillingCycle === 'monthly'); 
          btnM.setAttribute('aria-pressed', grologBillingCycle === 'monthly'); 
        }
        if (btnH) { 
          btnH.classList.toggle('active', grologBillingCycle === 'halfly'); 
          btnH.setAttribute('aria-pressed', grologBillingCycle === 'halfly'); 
        }
        if (btnA) { 
          btnA.classList.toggle('active', grologBillingCycle === 'annual'); 
          btnA.setAttribute('aria-pressed', grologBillingCycle === 'annual'); 
        }
        renderPricingGrolog();
      }"""

assert old_set_grolog in html, "old_set_grolog not found in pricing.html!"
html = html.replace(old_set_grolog, new_set_grolog)

# 6. Add event listeners for Grolog buttons
old_grolog_listeners = """      const btnMGrolog = document.getElementById('btnMonthlyGrolog');
      const btnAGrolog = document.getElementById('btnAnnualGrolog');
      if (btnMGrolog) btnMGrolog.addEventListener('click', () => setGrologBilling(false));
      if (btnAGrolog) btnAGrolog.addEventListener('click', () => setGrologBilling(true));"""

new_grolog_listeners = """      const btnMGrolog = document.getElementById('btnMonthlyGrolog');
      const btnHGrolog = document.getElementById('btnHalflyGrolog');
      const btnAGrolog = document.getElementById('btnAnnualGrolog');
      if (btnMGrolog) btnMGrolog.addEventListener('click', () => setGrologBilling('monthly'));
      if (btnHGrolog) btnHGrolog.addEventListener('click', () => setGrologBilling('halfly'));
      if (btnAGrolog) btnAGrolog.addEventListener('click', () => setGrologBilling('annual'));"""

assert old_grolog_listeners in html, "old_grolog_listeners not found in pricing.html!"
html = html.replace(old_grolog_listeners, new_grolog_listeners)

# 7. Update URL param handling for halfly in Grolog
old_url_param = """} else if (urlParams.get('billing') === 'halfly' || urlParams.get('billing') === 'half-yearly') {
          setGrohrmsBilling('halfly');
        }"""

new_url_param = """} else if (urlParams.get('billing') === 'halfly' || urlParams.get('billing') === 'half-yearly') {
          setGrohrmsBilling('halfly');
          setGrologBilling('halfly');
        }"""

html = html.replace(old_url_param, new_url_param)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully added halfly plan to Grolog!")

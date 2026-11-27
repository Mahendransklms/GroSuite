import re

# 1. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .product-billing-control rule
old_pbc = """.product-billing-control {
  display: none !important;
}"""

new_pbc = """.product-billing-control {
  display: flex !important;
  justify-content: center !important;
  align-items: center !important;
  margin: 1.25rem auto 1.6rem !important;
  width: 100% !important;
}

#grolog-pricing .product-billing-control,
#groinn-pricing .product-billing-control {
  display: none !important;
}"""

if old_pbc in css:
    css = css.replace(old_pbc, new_pbc)
    print("Replaced .product-billing-control in css/style.css!")
else:
    # Use regex
    css = re.sub(
        r'\.product-billing-control\s*\{[^}]*\}',
        new_pbc,
        css
    )
    print("Regex replaced .product-billing-control in css/style.css!")

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update pricing.html
with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove style="display: none;" from Grohrms product-billing-control
grohrms_sec_idx = html.find('id="grohrms-pricing"')
grohrms_sec_end = html.find('id="grolog-pricing"')

grohrms_part = html[grohrms_sec_idx:grohrms_sec_end]
grohrms_part_new = grohrms_part.replace(
    '<div class="product-billing-control" style="display: none;">',
    '<div class="product-billing-control">'
)

# Update Grohrms cards HTML to monthly initial state:
# Basic
grohrms_part_new = re.sub(
    r'(<span class="pricing-card__amount" id="cardAmountBasic"[^>]*>)[^<]*(</span>\s*<span class="pricing-card__original-price" id="cardOriginalBasic"[^>]*>)[^<]*(</span>\s*<span class="pricing-card__period" id="cardPeriodBasic">)[^<]*(</span>\s*</div>\s*<p class="pricing-card__billing-note" id="cardNoteBasic"[^>]*>)[^<]*(</p>)',
    r'\g<1>15\g<2>15\g<3>/ user / mo\g<4>Yearly: ₹180 / user / yr (Billed monthly)\g<5>',
    grohrms_part_new
)
# Standard
grohrms_part_new = re.sub(
    r'(<span class="pricing-card__amount" id="cardAmountStandard"[^>]*>)[^<]*(</span>\s*<span class="pricing-card__original-price" id="cardOriginalStandard"[^>]*style=")[^"]*(">[^<]*</span>\s*<span class="pricing-card__period" id="cardPeriodStandard">)[^<]*(</span>\s*</div>\s*<p class="pricing-card__billing-note" id="cardNoteStandard"[^>]*>)[^<]*(</p>)',
    r'\g<1>30</span><span class="pricing-card__original-price" id="cardOriginalStandard" style="display: none;">360\g<3>/ user / mo\g<4>Yearly: ₹360 / user / yr (Billed monthly)\g<5>',
    grohrms_part_new
)
# Prime
grohrms_part_new = re.sub(
    r'(<span class="pricing-card__amount" id="cardAmountPrime"[^>]*>)[^<]*(</span>\s*<span class="pricing-card__original-price" id="cardOriginalPrime"[^>]*style=")[^"]*(">[^<]*</span>\s*<span class="pricing-card__period" id="cardPeriodPrime">)[^<]*(</span>\s*</div>\s*<p class="pricing-card__billing-note" id="cardNotePrime"[^>]*>)[^<]*(</p>)',
    r'\g<1>60</span><span class="pricing-card__original-price" id="cardOriginalPrime" style="display: none;">720\g<3>/ user / mo\g<4>Yearly: ₹720 / user / yr (Billed monthly)\g<5>',
    grohrms_part_new
)

html = html[:grohrms_sec_idx] + grohrms_part_new + html[grohrms_sec_end:]

# Update JS isAnnualGrohrms = false
html = html.replace('let isAnnualGrohrms = true;', 'let isAnnualGrohrms = false;')

# Update renderPricingGrohrms in JS
start_marker = "function renderPricingGrohrms() {"
end_marker = "function renderPricingGrolog() {"

idx_start = html.find(start_marker)
idx_end = html.find(end_marker)

assert idx_start != -1, "start_marker not found!"
assert idx_end != -1, "end_marker not found!"

new_hrms_js = """function renderPricingGrohrms() {
        const cur = currencyRates[currentCurrency] || currencyRates.INR;
        const sym = cur.symbol.trim();

        // Basic: No discount (monthly = annual)
        const hrmsBasicMonthly = cur.hrms.basic.monthly;
        const hrmsBasicMonthlyTotal = (cur.code === 'INR') ? Math.round(hrmsBasicMonthly * 12) : +(hrmsBasicMonthly * 12).toFixed(2);
        const hrmsBasicAnnualTotal = hrmsBasicMonthlyTotal;

        // Standard: 10% discount on annual plan
        const hrmsStdMonthly = cur.hrms.standard.monthly;
        const hrmsStdMonthlyTotal = (cur.code === 'INR') ? Math.round(hrmsStdMonthly * 12) : +(hrmsStdMonthly * 12).toFixed(2);
        const hrmsStdAnnualTotal = (cur.code === 'INR') ? Math.round(hrmsStdMonthlyTotal * 0.90) : +(hrmsStdMonthlyTotal * 0.90).toFixed(2);

        // Prime: 20% discount on annual plan
        const hrmsPrimeMonthly = cur.hrms.prime.monthly;
        const hrmsPrimeMonthlyTotal = (cur.code === 'INR') ? Math.round(hrmsPrimeMonthly * 12) : +(hrmsPrimeMonthly * 12).toFixed(2);
        const hrmsPrimeAnnualTotal = (cur.code === 'INR') ? Math.round(hrmsPrimeMonthlyTotal * 0.80) : +(hrmsPrimeMonthlyTotal * 0.80).toFixed(2);

        if (isAnnualGrohrms) {
          // Basic Plan - Annually
          if (cardCurrencyBasic) cardCurrencyBasic.textContent = sym;
          if (cardAmountBasic) cardAmountBasic.textContent = formatNum(hrmsBasicAnnualTotal);
          if (cardOriginalBasic) cardOriginalBasic.style.display = 'none';
          if (cardPeriodBasic) cardPeriodBasic.textContent = '/ user / yr';
          if (cardNoteBasic) {
            cardNoteBasic.textContent = `Yearly: ${sym}${formatNum(hrmsBasicAnnualTotal)} / user / yr (Billed Annually)`;
          }

          // Standard Plan - Annually (10% discount: 324 with 360 struck)
          if (cardCurrencyStandard) cardCurrencyStandard.textContent = sym;
          if (cardAmountStandard) cardAmountStandard.textContent = formatNum(hrmsStdAnnualTotal);
          if (cardOriginalStandard) {
            cardOriginalStandard.textContent = formatNum(hrmsStdMonthlyTotal);
            cardOriginalStandard.style.display = 'inline';
          }
          if (cardPeriodStandard) cardPeriodStandard.textContent = '/ user / yr';
          if (cardNoteStandard) {
            cardNoteStandard.textContent = `Yearly: ${sym}${formatNum(hrmsStdAnnualTotal)} / user / yr (Save 10% Billed Annually)`;
          }

          // Prime Plan - Annually (20% discount: 576 with 720 struck)
          if (cardCurrencyPrime) cardCurrencyPrime.textContent = sym;
          if (cardAmountPrime) cardAmountPrime.textContent = formatNum(hrmsPrimeAnnualTotal);
          if (cardOriginalPrime) {
            cardOriginalPrime.textContent = formatNum(hrmsPrimeMonthlyTotal);
            cardOriginalPrime.style.display = 'inline';
          }
          if (cardPeriodPrime) cardPeriodPrime.textContent = '/ user / yr';
          if (cardNotePrime) {
            cardNotePrime.textContent = `Yearly: ${sym}${formatNum(hrmsPrimeAnnualTotal)} / user / yr (Save 20% Billed Annually)`;
          }
        } else {
          // Basic Plan - Monthly (15 / user / mo)
          if (cardCurrencyBasic) cardCurrencyBasic.textContent = sym;
          if (cardAmountBasic) cardAmountBasic.textContent = formatNum(hrmsBasicMonthly);
          if (cardOriginalBasic) cardOriginalBasic.style.display = 'none';
          if (cardPeriodBasic) cardPeriodBasic.textContent = '/ user / mo';
          if (cardNoteBasic) {
            cardNoteBasic.textContent = `Yearly: ${sym}${formatNum(hrmsBasicMonthlyTotal)} / user / yr (Billed monthly)`;
          }

          // Standard Plan - Monthly (30 / user / mo)
          if (cardCurrencyStandard) cardCurrencyStandard.textContent = sym;
          if (cardAmountStandard) cardAmountStandard.textContent = formatNum(hrmsStdMonthly);
          if (cardOriginalStandard) cardOriginalStandard.style.display = 'none';
          if (cardPeriodStandard) cardPeriodStandard.textContent = '/ user / mo';
          if (cardNoteStandard) {
            cardNoteStandard.textContent = `Yearly: ${sym}${formatNum(hrmsStdMonthlyTotal)} / user / yr (Billed monthly)`;
          }

          // Prime Plan - Monthly (60 / user / mo)
          if (cardCurrencyPrime) cardCurrencyPrime.textContent = sym;
          if (cardAmountPrime) cardAmountPrime.textContent = formatNum(hrmsPrimeMonthly);
          if (cardOriginalPrime) cardOriginalPrime.style.display = 'none';
          if (cardPeriodPrime) cardPeriodPrime.textContent = '/ user / mo';
          if (cardNotePrime) {
            cardNotePrime.textContent = `Yearly: ${sym}${formatNum(hrmsPrimeMonthlyTotal)} / user / yr (Billed monthly)`;
          }
        }
      }

      """

html = html[:idx_start] + new_hrms_js + html[idx_end:]

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated Grohrms monthly plan successfully!")

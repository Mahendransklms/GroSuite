import re

# 1. Update css/style.css to hide .product-billing-control
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(
    r'\.product-billing-control\s*\{[^}]*\}',
    '''.product-billing-control {
  display: none !important;
}''',
    css
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated css/style.css to hide .product-billing-control!")

# 2. Update pricing.html JS render functions
with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = "function renderPricingGrohrms() {"
end_marker = "function renderPricing() {"

idx_start = html.find(start_marker)
idx_end = html.find(end_marker)

assert idx_start != -1, "start_marker not found!"
assert idx_end != -1, "end_marker not found!"

new_js = """function renderPricingGrohrms() {
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

        // Basic Plan - Show only Annually plan amount in main price, Monthly pack in marked note box
        if (cardCurrencyBasic) cardCurrencyBasic.textContent = sym;
        if (cardAmountBasic) cardAmountBasic.textContent = formatNum(hrmsBasicAnnualTotal);
        if (cardOriginalBasic) cardOriginalBasic.style.display = 'none';
        if (cardPeriodBasic) cardPeriodBasic.textContent = '/ user / yr';
        if (cardNoteBasic) {
          cardNoteBasic.textContent = `Monthly Pack: ${sym}${formatNum(hrmsBasicMonthly)} / user / mo`;
        }

        // Standard Plan - Show only Annually plan amount in main price (324 with 360 struck), Monthly pack in marked note box (30)
        if (cardCurrencyStandard) cardCurrencyStandard.textContent = sym;
        if (cardAmountStandard) cardAmountStandard.textContent = formatNum(hrmsStdAnnualTotal);
        if (cardOriginalStandard) {
          cardOriginalStandard.textContent = formatNum(hrmsStdMonthlyTotal);
          cardOriginalStandard.style.display = 'inline';
        }
        if (cardPeriodStandard) cardPeriodStandard.textContent = '/ user / yr';
        if (cardNoteStandard) {
          cardNoteStandard.textContent = `Monthly Pack: ${sym}${formatNum(hrmsStdMonthly)} / user / mo`;
        }

        // Prime Plan - Show only Annually plan amount in main price (576 with 720 struck), Monthly pack in marked note box (60)
        if (cardCurrencyPrime) cardCurrencyPrime.textContent = sym;
        if (cardAmountPrime) cardAmountPrime.textContent = formatNum(hrmsPrimeAnnualTotal);
        if (cardOriginalPrime) {
          cardOriginalPrime.textContent = formatNum(hrmsPrimeMonthlyTotal);
          cardOriginalPrime.style.display = 'inline';
        }
        if (cardPeriodPrime) cardPeriodPrime.textContent = '/ user / yr';
        if (cardNotePrime) {
          cardNotePrime.textContent = `Monthly Pack: ${sym}${formatNum(hrmsPrimeMonthly)} / user / mo`;
        }
      }

      function renderPricingGrolog() {
        const cur = currencyRates[currentCurrency] || currencyRates.INR;
        const sym = cur.symbol.trim();

        // Tier 1: Up to 5 users (350/mo, 4200/yr total, 5% discount => 3990/yr)
        const grolog1Monthly = cur.grolog.tier1.monthly;
        const grolog1MonthlyTotal = (cur.code === 'INR') ? Math.round(grolog1Monthly * 12) : +(grolog1Monthly * 12).toFixed(2);
        const grolog1AnnualTotal = (cur.code === 'INR') ? Math.round(grolog1MonthlyTotal * 0.95) : +(grolog1MonthlyTotal * 0.95).toFixed(2);

        // Tier 2: 5 - 10 users (350/mo, 4200/yr total, 10% discount => 3780/yr)
        const grolog2Monthly = cur.grolog.tier2.monthly;
        const grolog2MonthlyTotal = (cur.code === 'INR') ? Math.round(grolog2Monthly * 12) : +(grolog2Monthly * 12).toFixed(2);
        const grolog2AnnualTotal = (cur.code === 'INR') ? Math.round(grolog2MonthlyTotal * 0.90) : +(grolog2MonthlyTotal * 0.90).toFixed(2);

        // Tier 3: 10 - 15 users (350/mo, 4200/yr total, 15% discount => 3570/yr)
        const grolog3Monthly = cur.grolog.tier3.monthly;
        const grolog3MonthlyTotal = (cur.code === 'INR') ? Math.round(grolog3Monthly * 12) : +(grolog3Monthly * 12).toFixed(2);
        const grolog3AnnualTotal = (cur.code === 'INR') ? Math.round(grolog3MonthlyTotal * 0.85) : +(grolog3MonthlyTotal * 0.85).toFixed(2);

        // Tier 1 - Annually in main box (3990 with 4200 struck), Monthly pack in marked box (350)
        if (cardCurrencyGrolog1) cardCurrencyGrolog1.textContent = sym;
        if (cardAmountGrolog1) cardAmountGrolog1.textContent = formatNum(grolog1AnnualTotal);
        if (cardOriginalGrolog1) {
          cardOriginalGrolog1.textContent = formatNum(grolog1MonthlyTotal);
          cardOriginalGrolog1.style.display = 'inline';
        }
        if (cardPeriodGrolog1) cardPeriodGrolog1.textContent = '/ user / yr';
        if (cardNoteGrolog1) {
          cardNoteGrolog1.textContent = `Monthly Pack: ${sym}${formatNum(grolog1Monthly)} / user / mo`;
        }

        // Tier 2 - Annually in main box (3780 with 4200 struck), Monthly pack in marked box (350)
        if (cardCurrencyGrolog2) cardCurrencyGrolog2.textContent = sym;
        if (cardAmountGrolog2) cardAmountGrolog2.textContent = formatNum(grolog2AnnualTotal);
        if (cardOriginalGrolog2) {
          cardOriginalGrolog2.textContent = formatNum(grolog2MonthlyTotal);
          cardOriginalGrolog2.style.display = 'inline';
        }
        if (cardPeriodGrolog2) cardPeriodGrolog2.textContent = '/ user / yr';
        if (cardNoteGrolog2) {
          cardNoteGrolog2.textContent = `Monthly Pack: ${sym}${formatNum(grolog2Monthly)} / user / mo`;
        }

        // Tier 3 - Annually in main box (3570 with 4200 struck), Monthly pack in marked box (350)
        if (cardCurrencyGrolog3) cardCurrencyGrolog3.textContent = sym;
        if (cardAmountGrolog3) cardAmountGrolog3.textContent = formatNum(grolog3AnnualTotal);
        if (cardOriginalGrolog3) {
          cardOriginalGrolog3.textContent = formatNum(grolog3MonthlyTotal);
          cardOriginalGrolog3.style.display = 'inline';
        }
        if (cardPeriodGrolog3) cardPeriodGrolog3.textContent = '/ user / yr';
        if (cardNoteGrolog3) {
          cardNoteGrolog3.textContent = `Monthly Pack: ${sym}${formatNum(grolog3Monthly)} / user / mo`;
        }
      }

      function renderPricingGroinn() {
        const cur = currencyRates[currentCurrency] || currencyRates.INR;
        const sym = cur.symbol.trim();

        // Tier 1: Basic (12000/year, Monthly pack: 1000/month)
        const groinn1Monthly = (cur.groinn && cur.groinn.tier1) ? cur.groinn.tier1.monthly : 1000;
        const groinn1Annual = (cur.groinn && cur.groinn.tier1) ? cur.groinn.tier1.annual : 12000;

        // Tier 2: Standard (20000/year, Monthly pack: 2000/month, Regular: 24000/year)
        const groinn2Monthly = (cur.groinn && cur.groinn.tier2) ? cur.groinn.tier2.monthly : 2000;
        const groinn2Annual = (cur.groinn && cur.groinn.tier2) ? cur.groinn.tier2.annual : 20000;
        const groinn2RegularAnnual = (cur.groinn && cur.groinn.tier2 && cur.groinn.tier2.originalAnnual) 
          ? cur.groinn.tier2.originalAnnual 
          : ((cur.code === 'INR') ? Math.round(groinn2Monthly * 12) : +(groinn2Monthly * 12).toFixed(2));

        // Tier 3: Prime (30000/year, Monthly pack: 3000/month, Regular: 36000/year)
        const groinn3Monthly = (cur.groinn && cur.groinn.tier3) ? cur.groinn.tier3.monthly : 3000;
        const groinn3Annual = (cur.groinn && cur.groinn.tier3) ? cur.groinn.tier3.annual : 30000;
        const groinn3RegularAnnual = (cur.groinn && cur.groinn.tier3 && cur.groinn.tier3.originalAnnual) 
          ? cur.groinn.tier3.originalAnnual 
          : ((cur.code === 'INR') ? Math.round(groinn3Monthly * 12) : +(groinn3Monthly * 12).toFixed(2));

        // Tier 1 - Basic: Show Annually plan amount in main price (12,000 / year), Monthly pack in marked box (1,000 / month)
        if (cardCurrencyGroinn1) cardCurrencyGroinn1.textContent = sym;
        if (cardAmountGroinn1) cardAmountGroinn1.textContent = formatNum(groinn1Annual);
        if (cardOriginalGroinn1) cardOriginalGroinn1.style.display = 'none';
        if (cardPeriodGroinn1) cardPeriodGroinn1.textContent = '/ year';
        if (cardNoteGroinn1) cardNoteGroinn1.textContent = `Monthly Pack: ${sym}${formatNum(groinn1Monthly)} / month`;

        // Tier 2 - Standard: Show Annually plan amount in main price (20,000 / year with 24,000 struck), Monthly pack in marked box (2,000 / month)
        if (cardCurrencyGroinn2) cardCurrencyGroinn2.textContent = sym;
        if (cardAmountGroinn2) cardAmountGroinn2.textContent = formatNum(groinn2Annual);
        if (cardOriginalGroinn2) {
          cardOriginalGroinn2.textContent = formatNum(groinn2RegularAnnual);
          cardOriginalGroinn2.style.display = 'inline';
        }
        if (cardPeriodGroinn2) cardPeriodGroinn2.textContent = '/ year';
        if (cardNoteGroinn2) cardNoteGroinn2.textContent = `Monthly Pack: ${sym}${formatNum(groinn2Monthly)} / month`;

        // Tier 3 - Prime: Show Annually plan amount in main price (30,000 / year with 36,000 struck), Monthly pack in marked box (3,000 / month)
        if (cardCurrencyGroinn3) cardCurrencyGroinn3.textContent = sym;
        if (cardAmountGroinn3) cardAmountGroinn3.textContent = formatNum(groinn3Annual);
        if (cardOriginalGroinn3) {
          cardOriginalGroinn3.textContent = formatNum(groinn3RegularAnnual);
          cardOriginalGroinn3.style.display = 'inline';
        }
        if (cardPeriodGroinn3) cardPeriodGroinn3.textContent = '/ year';
        if (cardNoteGroinn3) cardNoteGroinn3.textContent = `Monthly Pack: ${sym}${formatNum(groinn3Monthly)} / month`;
      }

      """

html = html[:idx_start] + new_js + html[idx_end:]

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated pricing.html JS render functions successfully!")

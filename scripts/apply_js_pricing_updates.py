import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update currencyRates for groinn
old_inr_groinn = """          groinn: {
            tier1: { monthly: 1000, annual: 1000 },
            tier2: { monthly: 1000, annual: 1000 },
            tier3: { monthly: 1000, annual: 1000 }
          },"""

new_inr_groinn = """          groinn: {
            tier1: { monthly: 1000, annual: 12000 },
            tier2: { monthly: 2000, annual: 20000, originalAnnual: 24000 },
            tier3: { monthly: 3000, annual: 30000, originalAnnual: 36000 }
          },"""

if old_inr_groinn in html:
    html = html.replace(old_inr_groinn, new_inr_groinn)
    print("Replaced INR groinn rates!")
else:
    print("Warning: old_inr_groinn not found!")

# Update other currencies in currencyRates
old_usd_groinn = """          groinn: {
            tier1: { monthly: 15.00, annual: 15.00 },
            tier2: { monthly: 15.00, annual: 15.00 },
            tier3: { monthly: 15.00, annual: 15.00 }
          },"""
new_usd_groinn = """          groinn: {
            tier1: { monthly: 15.00, annual: 150.00 },
            tier2: { monthly: 25.00, annual: 250.00, originalAnnual: 300.00 },
            tier3: { monthly: 40.00, annual: 400.00, originalAnnual: 480.00 }
          },"""
if old_usd_groinn in html:
    html = html.replace(old_usd_groinn, new_usd_groinn)
    print("Replaced USD groinn rates!")

old_gbp_groinn = """          groinn: {
            tier1: { monthly: 12.00, annual: 12.00 },
            tier2: { monthly: 12.00, annual: 12.00 },
            tier3: { monthly: 12.00, annual: 12.00 }
          },"""
new_gbp_groinn = """          groinn: {
            tier1: { monthly: 12.00, annual: 120.00 },
            tier2: { monthly: 20.00, annual: 200.00, originalAnnual: 240.00 },
            tier3: { monthly: 32.00, annual: 320.00, originalAnnual: 384.00 }
          },"""
if old_gbp_groinn in html:
    html = html.replace(old_gbp_groinn, new_gbp_groinn)
    print("Replaced GBP groinn rates!")

old_eur_groinn = """          groinn: {
            tier1: { monthly: 14.00, annual: 14.00 },
            tier2: { monthly: 14.00, annual: 14.00 },
            tier3: { monthly: 14.00, annual: 14.00 }
          },"""
new_eur_groinn = """          groinn: {
            tier1: { monthly: 14.00, annual: 140.00 },
            tier2: { monthly: 24.00, annual: 240.00, originalAnnual: 288.00 },
            tier3: { monthly: 36.00, annual: 360.00, originalAnnual: 432.00 }
          },"""
if old_eur_groinn in html:
    html = html.replace(old_eur_groinn, new_eur_groinn)
    print("Replaced EUR groinn rates!")

old_aed_groinn = """          groinn: {
            tier1: { monthly: 55.00, annual: 55.00 },
            tier2: { monthly: 55.00, annual: 55.00 },
            tier3: { monthly: 55.00, annual: 55.00 }
          },"""
new_aed_groinn = """          groinn: {
            tier1: { monthly: 55.00, annual: 550.00 },
            tier2: { monthly: 95.00, annual: 950.00, originalAnnual: 1140.00 },
            tier3: { monthly: 145.00, annual: 1450.00, originalAnnual: 1740.00 }
          },"""
if old_aed_groinn in html:
    html = html.replace(old_aed_groinn, new_aed_groinn)
    print("Replaced AED groinn rates!")

old_sgd_groinn = """          groinn: {
            tier1: { monthly: 20.00, annual: 20.00 },
            tier2: { monthly: 20.00, annual: 20.00 },
            tier3: { monthly: 20.00, annual: 20.00 }
          },"""
new_sgd_groinn = """          groinn: {
            tier1: { monthly: 20.00, annual: 200.00 },
            tier2: { monthly: 35.00, annual: 350.00, originalAnnual: 420.00 },
            tier3: { monthly: 55.00, annual: 550.00, originalAnnual: 660.00 }
          },"""
if old_sgd_groinn in html:
    html = html.replace(old_sgd_groinn, new_sgd_groinn)
    print("Replaced SGD groinn rates!")

old_aud_groinn = """          groinn: {
            tier1: { monthly: 22.00, annual: 22.00 },
            tier2: { monthly: 22.00, annual: 22.00 },
            tier3: { monthly: 22.00, annual: 22.00 }
          },"""
new_aud_groinn = """          groinn: {
            tier1: { monthly: 22.00, annual: 220.00 },
            tier2: { monthly: 38.00, annual: 380.00, originalAnnual: 456.00 },
            tier3: { monthly: 60.00, annual: 600.00, originalAnnual: 720.00 }
          },"""
if old_aud_groinn in html:
    html = html.replace(old_aud_groinn, new_aud_groinn)
    print("Replaced AUD groinn rates!")

old_cad_groinn = """          groinn: {
            tier1: { monthly: 20.00, annual: 20.00 },
            tier2: { monthly: 20.00, annual: 20.00 },
            tier3: { monthly: 20.00, annual: 20.00 }
          },"""
new_cad_groinn = """          groinn: {
            tier1: { monthly: 20.00, annual: 200.00 },
            tier2: { monthly: 35.00, annual: 350.00, originalAnnual: 420.00 },
            tier3: { monthly: 55.00, annual: 550.00, originalAnnual: 660.00 }
          },"""
if old_cad_groinn in html:
    html = html.replace(old_cad_groinn, new_cad_groinn)
    print("Replaced CAD groinn rates!")

# 2. Update isAnnual initial values to true
html = html.replace('let isAnnualGrohrms = false;', 'let isAnnualGrohrms = true;')
html = html.replace('let isAnnualGrolog = false;', 'let isAnnualGrolog = true;')
html = html.replace('let isAnnualGroinn = false;', 'let isAnnualGroinn = true;')

# 3. Replace renderPricingGrohrms, renderPricingGrolog, renderPricingGroinn
new_render_hrms = """      function renderPricingGrohrms() {
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
      }"""

new_render_grolog = """      function renderPricingGrolog() {
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
      }"""

new_render_groinn = """      function renderPricingGroinn() {
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
      }"""

# Replace all 3 functions
pattern = r'function renderPricingGrohrms\(\)\s*\{[\s\S]*?function renderPricingAddons'
replacement = new_render_hrms + "\n\n" + new_render_grolog + "\n\n" + new_render_groinn + "\n\n      function renderPricingAddons"

html = re.sub(pattern, replacement, html)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("JS pricing render functions updated successfully!")

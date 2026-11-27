import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update data attributes in HTML for Grolog
code = re.sub(
    r'(id="cardAmountGrolog1"[^>]*data-monthly="350"[^>]*)data-annual="333"',
    r'\1data-annual="3990"',
    code
)
code = re.sub(
    r'(id="cardAmountGrolog2"[^>]*data-monthly="300"[^>]*)data-annual="270"',
    r'\1data-annual="3240"',
    code
)
code = re.sub(
    r'(id="cardAmountGrolog3"[^>]*data-monthly="250"[^>]*)data-annual="200"',
    r'\1data-annual="2400"',
    code
)

# Grohrms data-annual
code = re.sub(
    r'(id="cardAmountBasic"[^>]*data-monthly="15"[^>]*)data-annual="15"',
    r'\1data-annual="180"',
    code
)
code = re.sub(
    r'(id="cardAmountStandard"[^>]*data-monthly="30"[^>]*)data-annual="27"',
    r'\1data-annual="324"',
    code
)
code = re.sub(
    r'(id="cardAmountPrime"[^>]*data-monthly="60"[^>]*)data-annual="48"',
    r'\1data-annual="576"',
    code
)

# Groinn data-annual
code = re.sub(
    r'(id="cardAmountGroinn1"[^>]*data-monthly="1000"[^>]*)data-annual="1000"',
    r'\1data-annual="12000"',
    code
)
code = re.sub(
    r'(id="cardAmountGroinn2"[^>]*data-monthly="1000"[^>]*)data-annual="1000"',
    r'\1data-annual="12000"',
    code
)
code = re.sub(
    r'(id="cardAmountGroinn3"[^>]*data-monthly="1000"[^>]*)data-annual="1000"',
    r'\1data-annual="12000"',
    code
)

# 2. Add cardPeriod DOM queries in JS
dom_old = """      // Grohrms Card Elements
      const cardCurrencyBasic = document.getElementById('cardCurrencyBasic');
      const cardAmountBasic = document.getElementById('cardAmountBasic');
      const cardOriginalBasic = document.getElementById('cardOriginalBasic');
      const cardNoteBasic = document.getElementById('cardNoteBasic');

      const cardCurrencyStandard = document.getElementById('cardCurrencyStandard');
      const cardAmountStandard = document.getElementById('cardAmountStandard');
      const cardOriginalStandard = document.getElementById('cardOriginalStandard');
      const cardNoteStandard = document.getElementById('cardNoteStandard');

      const cardCurrencyPrime = document.getElementById('cardCurrencyPrime');
      const cardAmountPrime = document.getElementById('cardAmountPrime');
      const cardOriginalPrime = document.getElementById('cardOriginalPrime');
      const cardNotePrime = document.getElementById('cardNotePrime');

      // Groinn Card Elements
      const cardCurrencyGroinn1 = document.getElementById('cardCurrencyGroinn1');
      const cardAmountGroinn1 = document.getElementById('cardAmountGroinn1');
      const cardOriginalGroinn1 = document.getElementById('cardOriginalGroinn1');
      const cardNoteGroinn1 = document.getElementById('cardNoteGroinn1');

      const cardCurrencyGroinn2 = document.getElementById('cardCurrencyGroinn2');
      const cardAmountGroinn2 = document.getElementById('cardAmountGroinn2');
      const cardOriginalGroinn2 = document.getElementById('cardOriginalGroinn2');
      const cardNoteGroinn2 = document.getElementById('cardNoteGroinn2');

      const cardCurrencyGroinn3 = document.getElementById('cardCurrencyGroinn3');
      const cardAmountGroinn3 = document.getElementById('cardAmountGroinn3');
      const cardOriginalGroinn3 = document.getElementById('cardOriginalGroinn3');
      const cardNoteGroinn3 = document.getElementById('cardNoteGroinn3');

      // Compatibility fallback
      const cardCurrencyGroinn = cardCurrencyGroinn1;
      const cardAmountGroinn = cardAmountGroinn1;
      const cardNoteGroinn = cardNoteGroinn1;

      // Grolog Card Elements
      const cardCurrencyGrolog1 = document.getElementById('cardCurrencyGrolog1');
      const cardAmountGrolog1 = document.getElementById('cardAmountGrolog1');
      const cardOriginalGrolog1 = document.getElementById('cardOriginalGrolog1');
      const cardNoteGrolog1 = document.getElementById('cardNoteGrolog1');

      const cardCurrencyGrolog2 = document.getElementById('cardCurrencyGrolog2');
      const cardAmountGrolog2 = document.getElementById('cardAmountGrolog2');
      const cardOriginalGrolog2 = document.getElementById('cardOriginalGrolog2');
      const cardNoteGrolog2 = document.getElementById('cardNoteGrolog2');

      const cardCurrencyGrolog3 = document.getElementById('cardCurrencyGrolog3');
      const cardAmountGrolog3 = document.getElementById('cardAmountGrolog3');
      const cardOriginalGrolog3 = document.getElementById('cardOriginalGrolog3');
      const cardNoteGrolog3 = document.getElementById('cardNoteGrolog3');"""

dom_new = """      // Grohrms Card Elements
      const cardCurrencyBasic = document.getElementById('cardCurrencyBasic');
      const cardAmountBasic = document.getElementById('cardAmountBasic');
      const cardOriginalBasic = document.getElementById('cardOriginalBasic');
      const cardPeriodBasic = document.getElementById('cardPeriodBasic');
      const cardNoteBasic = document.getElementById('cardNoteBasic');

      const cardCurrencyStandard = document.getElementById('cardCurrencyStandard');
      const cardAmountStandard = document.getElementById('cardAmountStandard');
      const cardOriginalStandard = document.getElementById('cardOriginalStandard');
      const cardPeriodStandard = document.getElementById('cardPeriodStandard');
      const cardNoteStandard = document.getElementById('cardNoteStandard');

      const cardCurrencyPrime = document.getElementById('cardCurrencyPrime');
      const cardAmountPrime = document.getElementById('cardAmountPrime');
      const cardOriginalPrime = document.getElementById('cardOriginalPrime');
      const cardPeriodPrime = document.getElementById('cardPeriodPrime');
      const cardNotePrime = document.getElementById('cardNotePrime');

      // Groinn Card Elements
      const cardCurrencyGroinn1 = document.getElementById('cardCurrencyGroinn1');
      const cardAmountGroinn1 = document.getElementById('cardAmountGroinn1');
      const cardOriginalGroinn1 = document.getElementById('cardOriginalGroinn1');
      const cardPeriodGroinn1 = document.getElementById('cardPeriodGroinn1');
      const cardNoteGroinn1 = document.getElementById('cardNoteGroinn1');

      const cardCurrencyGroinn2 = document.getElementById('cardCurrencyGroinn2');
      const cardAmountGroinn2 = document.getElementById('cardAmountGroinn2');
      const cardOriginalGroinn2 = document.getElementById('cardOriginalGroinn2');
      const cardPeriodGroinn2 = document.getElementById('cardPeriodGroinn2');
      const cardNoteGroinn2 = document.getElementById('cardNoteGroinn2');

      const cardCurrencyGroinn3 = document.getElementById('cardCurrencyGroinn3');
      const cardAmountGroinn3 = document.getElementById('cardAmountGroinn3');
      const cardOriginalGroinn3 = document.getElementById('cardOriginalGroinn3');
      const cardPeriodGroinn3 = document.getElementById('cardPeriodGroinn3');
      const cardNoteGroinn3 = document.getElementById('cardNoteGroinn3');

      // Compatibility fallback
      const cardCurrencyGroinn = cardCurrencyGroinn1;
      const cardAmountGroinn = cardAmountGroinn1;
      const cardNoteGroinn = cardNoteGroinn1;

      // Grolog Card Elements
      const cardCurrencyGrolog1 = document.getElementById('cardCurrencyGrolog1');
      const cardAmountGrolog1 = document.getElementById('cardAmountGrolog1');
      const cardOriginalGrolog1 = document.getElementById('cardOriginalGrolog1');
      const cardPeriodGrolog1 = document.getElementById('cardPeriodGrolog1');
      const cardNoteGrolog1 = document.getElementById('cardNoteGrolog1');

      const cardCurrencyGrolog2 = document.getElementById('cardCurrencyGrolog2');
      const cardAmountGrolog2 = document.getElementById('cardAmountGrolog2');
      const cardOriginalGrolog2 = document.getElementById('cardOriginalGrolog2');
      const cardPeriodGrolog2 = document.getElementById('cardPeriodGrolog2');
      const cardNoteGrolog2 = document.getElementById('cardNoteGrolog2');

      const cardCurrencyGrolog3 = document.getElementById('cardCurrencyGrolog3');
      const cardAmountGrolog3 = document.getElementById('cardAmountGrolog3');
      const cardOriginalGrolog3 = document.getElementById('cardOriginalGrolog3');
      const cardPeriodGrolog3 = document.getElementById('cardPeriodGrolog3');
      const cardNoteGrolog3 = document.getElementById('cardNoteGrolog3');"""

assert dom_old in code, "DOM old declarations not found"
code = code.replace(dom_old, dom_new)

# 3. Update renderPricingGrohrms
hrms_render_pattern = r'function renderPricingGrohrms\(\)\s*\{[\s\S]*?\}\s*function renderPricingGrolog'
hrms_render_new = """function renderPricingGrohrms() {
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
          // Basic Plan - Annually (No discount)
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
          // Basic Plan - Monthly
          if (cardCurrencyBasic) cardCurrencyBasic.textContent = sym;
          if (cardAmountBasic) cardAmountBasic.textContent = formatNum(hrmsBasicMonthly);
          if (cardOriginalBasic) cardOriginalBasic.style.display = 'none';
          if (cardPeriodBasic) cardPeriodBasic.textContent = '/ user / mo';
          if (cardNoteBasic) {
            cardNoteBasic.textContent = `Yearly: ${sym}${formatNum(hrmsBasicMonthlyTotal)} / user / yr (Billed monthly)`;
          }

          // Standard Plan - Monthly
          if (cardCurrencyStandard) cardCurrencyStandard.textContent = sym;
          if (cardAmountStandard) cardAmountStandard.textContent = formatNum(hrmsStdMonthly);
          if (cardOriginalStandard) cardOriginalStandard.style.display = 'none';
          if (cardPeriodStandard) cardPeriodStandard.textContent = '/ user / mo';
          if (cardNoteStandard) {
            cardNoteStandard.textContent = `Yearly: ${sym}${formatNum(hrmsStdMonthlyTotal)} / user / yr (Billed monthly)`;
          }

          // Prime Plan - Monthly
          if (cardCurrencyPrime) cardCurrencyPrime.textContent = sym;
          if (cardAmountPrime) cardAmountPrime.textContent = formatNum(hrmsPrimeMonthly);
          if (cardOriginalPrime) cardOriginalPrime.style.display = 'none';
          if (cardPeriodPrime) cardPeriodPrime.textContent = '/ user / mo';
          if (cardNotePrime) {
            cardNotePrime.textContent = `Yearly: ${sym}${formatNum(hrmsPrimeMonthlyTotal)} / user / yr (Billed monthly)`;
          }
        }
      }

      function renderPricingGrolog"""

code = re.sub(hrms_render_pattern, hrms_render_new, code)

# 4. Update renderPricingGrolog
grolog_render_pattern = r'function renderPricingGrolog\(\)\s*\{[\s\S]*?\}\s*function renderPricingGroinn'
grolog_render_new = """function renderPricingGrolog() {
        const cur = currencyRates[currentCurrency] || currencyRates.INR;
        const sym = cur.symbol.trim();

        // Tier 1: 5 users plan (350/mo, 4200/yr total, 5% discount => 3990/yr)
        const grolog1Monthly = cur.grolog.tier1.monthly;
        const grolog1MonthlyTotal = (cur.code === 'INR') ? Math.round(grolog1Monthly * 12) : +(grolog1Monthly * 12).toFixed(2);
        const grolog1AnnualTotal = (cur.code === 'INR') ? Math.round(grolog1MonthlyTotal * 0.95) : +(grolog1MonthlyTotal * 0.95).toFixed(2);

        // Tier 2: 5 - 10 users plan (300/mo, 3600/yr total, 10% discount => 3240/yr)
        const grolog2Monthly = cur.grolog.tier2.monthly;
        const grolog2MonthlyTotal = (cur.code === 'INR') ? Math.round(grolog2Monthly * 12) : +(grolog2Monthly * 12).toFixed(2);
        const grolog2AnnualTotal = (cur.code === 'INR') ? Math.round(grolog2MonthlyTotal * 0.90) : +(grolog2MonthlyTotal * 0.90).toFixed(2);

        // Tier 3: 10 - 25 users plan (250/mo, 3000/yr total, 20% discount => 2400/yr)
        const grolog3Monthly = cur.grolog.tier3.monthly;
        const grolog3MonthlyTotal = (cur.code === 'INR') ? Math.round(grolog3Monthly * 12) : +(grolog3Monthly * 12).toFixed(2);
        const grolog3AnnualTotal = (cur.code === 'INR') ? Math.round(grolog3MonthlyTotal * 0.80) : +(grolog3MonthlyTotal * 0.80).toFixed(2);

        if (isAnnualGrolog) {
          // Tier 1 - Annually (3990 with 4200 struck)
          if (cardCurrencyGrolog1) cardCurrencyGrolog1.textContent = sym;
          if (cardAmountGrolog1) cardAmountGrolog1.textContent = formatNum(grolog1AnnualTotal);
          if (cardOriginalGrolog1) {
            cardOriginalGrolog1.textContent = formatNum(grolog1MonthlyTotal);
            cardOriginalGrolog1.style.display = 'inline';
          }
          if (cardPeriodGrolog1) cardPeriodGrolog1.textContent = '/ user / yr';
          if (cardNoteGrolog1) {
            cardNoteGrolog1.textContent = `Yearly: ${sym}${formatNum(grolog1AnnualTotal)} / user / yr (Save 5% Billed Annually)`;
          }

          // Tier 2 - Annually (3240 with 3600 struck)
          if (cardCurrencyGrolog2) cardCurrencyGrolog2.textContent = sym;
          if (cardAmountGrolog2) cardAmountGrolog2.textContent = formatNum(grolog2AnnualTotal);
          if (cardOriginalGrolog2) {
            cardOriginalGrolog2.textContent = formatNum(grolog2MonthlyTotal);
            cardOriginalGrolog2.style.display = 'inline';
          }
          if (cardPeriodGrolog2) cardPeriodGrolog2.textContent = '/ user / yr';
          if (cardNoteGrolog2) {
            cardNoteGrolog2.textContent = `Yearly: ${sym}${formatNum(grolog2AnnualTotal)} / user / yr (Save 10% Billed Annually)`;
          }

          // Tier 3 - Annually (2400 with 3000 struck)
          if (cardCurrencyGrolog3) cardCurrencyGrolog3.textContent = sym;
          if (cardAmountGrolog3) cardAmountGrolog3.textContent = formatNum(grolog3AnnualTotal);
          if (cardOriginalGrolog3) {
            cardOriginalGrolog3.textContent = formatNum(grolog3MonthlyTotal);
            cardOriginalGrolog3.style.display = 'inline';
          }
          if (cardPeriodGrolog3) cardPeriodGrolog3.textContent = '/ user / yr';
          if (cardNoteGrolog3) {
            cardNoteGrolog3.textContent = `Yearly: ${sym}${formatNum(grolog3AnnualTotal)} / user / yr (Save 20% Billed Annually)`;
          }
        } else {
          // Tier 1 - Monthly
          if (cardCurrencyGrolog1) cardCurrencyGrolog1.textContent = sym;
          if (cardAmountGrolog1) cardAmountGrolog1.textContent = formatNum(grolog1Monthly);
          if (cardOriginalGrolog1) cardOriginalGrolog1.style.display = 'none';
          if (cardPeriodGrolog1) cardPeriodGrolog1.textContent = '/ user / mo';
          if (cardNoteGrolog1) {
            cardNoteGrolog1.textContent = `Yearly: ${sym}${formatNum(grolog1MonthlyTotal)} / user / yr (Billed monthly)`;
          }

          // Tier 2 - Monthly
          if (cardCurrencyGrolog2) cardCurrencyGrolog2.textContent = sym;
          if (cardAmountGrolog2) cardAmountGrolog2.textContent = formatNum(grolog2Monthly);
          if (cardOriginalGrolog2) cardOriginalGrolog2.style.display = 'none';
          if (cardPeriodGrolog2) cardPeriodGrolog2.textContent = '/ user / mo';
          if (cardNoteGrolog2) {
            cardNoteGrolog2.textContent = `Yearly: ${sym}${formatNum(grolog2MonthlyTotal)} / user / yr (Billed monthly)`;
          }

          // Tier 3 - Monthly
          if (cardCurrencyGrolog3) cardCurrencyGrolog3.textContent = sym;
          if (cardAmountGrolog3) cardAmountGrolog3.textContent = formatNum(grolog3Monthly);
          if (cardOriginalGrolog3) cardOriginalGrolog3.style.display = 'none';
          if (cardPeriodGrolog3) cardPeriodGrolog3.textContent = '/ user / mo';
          if (cardNoteGrolog3) {
            cardNoteGrolog3.textContent = `Yearly: ${sym}${formatNum(grolog3MonthlyTotal)} / user / yr (Billed monthly)`;
          }
        }
      }

      function renderPricingGroinn"""

code = re.sub(grolog_render_pattern, grolog_render_new, code)

# 5. Update renderPricingGroinn
groinn_render_pattern = r'function renderPricingGroinn\(\)\s*\{[\s\S]*?\}\s*function renderPricing\(\)'
groinn_render_new = """function renderPricingGroinn() {
        const cur = currencyRates[currentCurrency] || currencyRates.INR;
        const sym = cur.symbol.trim();

        const groinn1Monthly = (cur.groinn.tier1 ? cur.groinn.tier1.monthly : cur.groinn.monthly);
        const groinn1Annual = (cur.groinn.tier1 ? cur.groinn.tier1.annual : cur.groinn.annual);
        const groinn1MonthlyTotal = (cur.code === 'INR') ? Math.round(groinn1Monthly * 12) : +(groinn1Monthly * 12).toFixed(2);
        const groinn1AnnualTotal = (cur.code === 'INR') ? Math.round(groinn1Annual * 12) : +(groinn1Annual * 12).toFixed(2);

        const groinn2Monthly = (cur.groinn.tier2 ? cur.groinn.tier2.monthly : cur.groinn.monthly);
        const groinn2Annual = (cur.groinn.tier2 ? cur.groinn.tier2.annual : cur.groinn.annual);
        const groinn2MonthlyTotal = (cur.code === 'INR') ? Math.round(groinn2Monthly * 12) : +(groinn2Monthly * 12).toFixed(2);
        const groinn2AnnualTotal = (cur.code === 'INR') ? Math.round(groinn2Annual * 12) : +(groinn2Annual * 12).toFixed(2);

        const groinn3Monthly = (cur.groinn.tier3 ? cur.groinn.tier3.monthly : cur.groinn.monthly);
        const groinn3Annual = (cur.groinn.tier3 ? cur.groinn.tier3.annual : cur.groinn.annual);
        const groinn3MonthlyTotal = (cur.code === 'INR') ? Math.round(groinn3Monthly * 12) : +(groinn3Monthly * 12).toFixed(2);
        const groinn3AnnualTotal = (cur.code === 'INR') ? Math.round(groinn3Annual * 12) : +(groinn3Annual * 12).toFixed(2);

        if (isAnnualGroinn) {
          // Tier 1 - Annually (12000)
          if (cardCurrencyGroinn1) cardCurrencyGroinn1.textContent = sym;
          if (cardAmountGroinn1) cardAmountGroinn1.textContent = formatNum(groinn1AnnualTotal);
          if (cardOriginalGroinn1) cardOriginalGroinn1.style.display = 'none';
          if (cardPeriodGroinn1) cardPeriodGroinn1.textContent = '/ year';
          if (cardNoteGroinn1) cardNoteGroinn1.textContent = `Yearly: ${sym}${formatNum(groinn1AnnualTotal)} / year (Billed Annually)`;

          // Tier 2 - Annually (12000)
          if (cardCurrencyGroinn2) cardCurrencyGroinn2.textContent = sym;
          if (cardAmountGroinn2) cardAmountGroinn2.textContent = formatNum(groinn2AnnualTotal);
          if (cardOriginalGroinn2) cardOriginalGroinn2.style.display = 'none';
          if (cardPeriodGroinn2) cardPeriodGroinn2.textContent = '/ year';
          if (cardNoteGroinn2) cardNoteGroinn2.textContent = `Yearly: ${sym}${formatNum(groinn2AnnualTotal)} / year (Billed Annually)`;

          // Tier 3 - Annually (12000)
          if (cardCurrencyGroinn3) cardCurrencyGroinn3.textContent = sym;
          if (cardAmountGroinn3) cardAmountGroinn3.textContent = formatNum(groinn3AnnualTotal);
          if (cardOriginalGroinn3) cardOriginalGroinn3.style.display = 'none';
          if (cardPeriodGroinn3) cardPeriodGroinn3.textContent = '/ year';
          if (cardNoteGroinn3) cardNoteGroinn3.textContent = `Yearly: ${sym}${formatNum(groinn3AnnualTotal)} / year (Billed Annually)`;
        } else {
          // Tier 1 - Monthly (1000)
          if (cardCurrencyGroinn1) cardCurrencyGroinn1.textContent = sym;
          if (cardAmountGroinn1) cardAmountGroinn1.textContent = formatNum(groinn1Monthly);
          if (cardOriginalGroinn1) cardOriginalGroinn1.style.display = 'none';
          if (cardPeriodGroinn1) cardPeriodGroinn1.textContent = '/ month';
          if (cardNoteGroinn1) cardNoteGroinn1.textContent = `Yearly: ${sym}${formatNum(groinn1MonthlyTotal)} / year (Billed monthly)`;

          // Tier 2 - Monthly (1000)
          if (cardCurrencyGroinn2) cardCurrencyGroinn2.textContent = sym;
          if (cardAmountGroinn2) cardAmountGroinn2.textContent = formatNum(groinn2Monthly);
          if (cardOriginalGroinn2) cardOriginalGroinn2.style.display = 'none';
          if (cardPeriodGroinn2) cardPeriodGroinn2.textContent = '/ month';
          if (cardNoteGroinn2) cardNoteGroinn2.textContent = `Yearly: ${sym}${formatNum(groinn2MonthlyTotal)} / year (Billed monthly)`;

          // Tier 3 - Monthly (1000)
          if (cardCurrencyGroinn3) cardCurrencyGroinn3.textContent = sym;
          if (cardAmountGroinn3) cardAmountGroinn3.textContent = formatNum(groinn3Monthly);
          if (cardOriginalGroinn3) cardOriginalGroinn3.style.display = 'none';
          if (cardPeriodGroinn3) cardPeriodGroinn3.textContent = '/ month';
          if (cardNoteGroinn3) cardNoteGroinn3.textContent = `Yearly: ${sym}${formatNum(groinn3MonthlyTotal)} / year (Billed monthly)`;
        }
      }

      function renderPricing()"""

code = re.sub(groinn_render_pattern, groinn_render_new, code)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated pricing.html to show yearly plan in main pricing details!")

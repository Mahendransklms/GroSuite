import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Insert btnHalflyGrohrms between btnMonthlyGrohrms and btnAnnualGrohrms
old_btn_group = """                <button type="button" class="billing-btn active" id="btnMonthlyGrohrms" data-product="grohrms"
                  data-period="monthly" aria-pressed="true">
                  <span>Monthly</span>
                </button>
                <button type="button" class="billing-btn" id="btnAnnualGrohrms" data-product="grohrms"
                  data-period="annual" aria-pressed="false">
                  <span>Annually</span>
                  <span class="billing-discount-badge">Up to 20% Off</span>
                </button>"""

new_btn_group = """                <button type="button" class="billing-btn active" id="btnMonthlyGrohrms" data-product="grohrms"
                  data-period="monthly" aria-pressed="true">
                  <span>Monthly</span>
                </button>
                <button type="button" class="billing-btn" id="btnHalflyGrohrms" data-product="grohrms"
                  data-period="halfly" aria-pressed="false">
                  <span>Half-Yearly</span>
                  <span class="billing-discount-badge">Save up to 10%</span>
                </button>
                <button type="button" class="billing-btn" id="btnAnnualGrohrms" data-product="grohrms"
                  data-period="annual" aria-pressed="false">
                  <span>Annually</span>
                  <span class="billing-discount-badge">Up to 20% Off</span>
                </button>"""

assert old_btn_group in html, "old_btn_group not found in pricing.html!"
html = html.replace(old_btn_group, new_btn_group)
print("Inserted btnHalflyGrohrms into HTML!")

# 2. Add grohrmsBillingCycle variable in JS
old_var = "let isAnnualGrohrms = false;"
new_var = "let isAnnualGrohrms = false;\n      let grohrmsBillingCycle = 'monthly';"
html = html.replace(old_var, new_var, 1)

# 3. Update renderPricingGrohrms function in JS
start_marker = "function renderPricingGrohrms() {"
end_marker = "function renderPricingGrolog() {"

idx_start = html.find(start_marker)
idx_end = html.find(end_marker)

assert idx_start != -1 and idx_end != -1, "renderPricing markers not found!"

new_render_hrms = """function renderPricingGrohrms() {
        const cur = currencyRates[currentCurrency] || currencyRates.INR;
        const sym = cur.symbol.trim();

        // Basic: No discount (15 / mo, 90 / 6 mo, 180 / yr)
        const hrmsBasicMonthly = cur.hrms.basic.monthly;
        const hrmsBasicHalfly = (cur.code === 'INR') ? Math.round(hrmsBasicMonthly * 6) : +(hrmsBasicMonthly * 6).toFixed(2);
        const hrmsBasicAnnual = (cur.code === 'INR') ? Math.round(hrmsBasicMonthly * 12) : +(hrmsBasicMonthly * 12).toFixed(2);

        // Standard: 5% discount on halfly, 10% discount on annual
        const hrmsStdMonthly = cur.hrms.standard.monthly;
        const hrmsStdHalflyTotal = (cur.code === 'INR') ? Math.round(hrmsStdMonthly * 6) : +(hrmsStdMonthly * 6).toFixed(2);
        const hrmsStdHalflyDiscounted = (cur.code === 'INR') ? Math.round(hrmsStdHalflyTotal * 0.95) : +(hrmsStdHalflyTotal * 0.95).toFixed(2);
        const hrmsStdAnnualTotal = (cur.code === 'INR') ? Math.round(hrmsStdMonthly * 12) : +(hrmsStdMonthly * 12).toFixed(2);
        const hrmsStdAnnualDiscounted = (cur.code === 'INR') ? Math.round(hrmsStdAnnualTotal * 0.90) : +(hrmsStdAnnualTotal * 0.90).toFixed(2);

        // Prime: 10% discount on halfly, 20% discount on annual
        const hrmsPrimeMonthly = cur.hrms.prime.monthly;
        const hrmsPrimeHalflyTotal = (cur.code === 'INR') ? Math.round(hrmsPrimeMonthly * 6) : +(hrmsPrimeMonthly * 6).toFixed(2);
        const hrmsPrimeHalflyDiscounted = (cur.code === 'INR') ? Math.round(hrmsPrimeHalflyTotal * 0.90) : +(hrmsPrimeHalflyTotal * 0.90).toFixed(2);
        const hrmsPrimeAnnualTotal = (cur.code === 'INR') ? Math.round(hrmsPrimeMonthly * 12) : +(hrmsPrimeMonthly * 12).toFixed(2);
        const hrmsPrimeAnnualDiscounted = (cur.code === 'INR') ? Math.round(hrmsPrimeAnnualTotal * 0.80) : +(hrmsPrimeAnnualTotal * 0.80).toFixed(2);

        if (grohrmsBillingCycle === 'annual') {
          // Basic Plan - Annually (180 / user / yr)
          if (cardCurrencyBasic) cardCurrencyBasic.textContent = sym;
          if (cardAmountBasic) cardAmountBasic.textContent = formatNum(hrmsBasicAnnual);
          if (cardOriginalBasic) cardOriginalBasic.style.display = 'none';
          if (cardPeriodBasic) cardPeriodBasic.textContent = '/ user / yr';
          if (cardNoteBasic) {
            cardNoteBasic.textContent = `Yearly: ${sym}${formatNum(hrmsBasicAnnual)} / user / yr (Billed Annually)`;
          }

          // Standard Plan - Annually (324 with 360 struck)
          if (cardCurrencyStandard) cardCurrencyStandard.textContent = sym;
          if (cardAmountStandard) cardAmountStandard.textContent = formatNum(hrmsStdAnnualDiscounted);
          if (cardOriginalStandard) {
            cardOriginalStandard.textContent = formatNum(hrmsStdAnnualTotal);
            cardOriginalStandard.style.display = 'inline';
          }
          if (cardPeriodStandard) cardPeriodStandard.textContent = '/ user / yr';
          if (cardNoteStandard) {
            cardNoteStandard.textContent = `Yearly: ${sym}${formatNum(hrmsStdAnnualDiscounted)} / user / yr (Save 10% Billed Annually)`;
          }

          // Prime Plan - Annually (576 with 720 struck)
          if (cardCurrencyPrime) cardCurrencyPrime.textContent = sym;
          if (cardAmountPrime) cardAmountPrime.textContent = formatNum(hrmsPrimeAnnualDiscounted);
          if (cardOriginalPrime) {
            cardOriginalPrime.textContent = formatNum(hrmsPrimeAnnualTotal);
            cardOriginalPrime.style.display = 'inline';
          }
          if (cardPeriodPrime) cardPeriodPrime.textContent = '/ user / yr';
          if (cardNotePrime) {
            cardNotePrime.textContent = `Yearly: ${sym}${formatNum(hrmsPrimeAnnualDiscounted)} / user / yr (Save 20% Billed Annually)`;
          }
        } else if (grohrmsBillingCycle === 'halfly') {
          // Basic Plan - Half-Yearly (90 / user / 6 mo)
          if (cardCurrencyBasic) cardCurrencyBasic.textContent = sym;
          if (cardAmountBasic) cardAmountBasic.textContent = formatNum(hrmsBasicHalfly);
          if (cardOriginalBasic) cardOriginalBasic.style.display = 'none';
          if (cardPeriodBasic) cardPeriodBasic.textContent = '/ user / 6 mo';
          if (cardNoteBasic) {
            cardNoteBasic.textContent = `Half-Yearly: ${sym}${formatNum(hrmsBasicHalfly)} / user / 6 mo (Billed half-yearly)`;
          }

          // Standard Plan - Half-Yearly (171 with 180 struck)
          if (cardCurrencyStandard) cardCurrencyStandard.textContent = sym;
          if (cardAmountStandard) cardAmountStandard.textContent = formatNum(hrmsStdHalflyDiscounted);
          if (cardOriginalStandard) {
            cardOriginalStandard.textContent = formatNum(hrmsStdHalflyTotal);
            cardOriginalStandard.style.display = 'inline';
          }
          if (cardPeriodStandard) cardPeriodStandard.textContent = '/ user / 6 mo';
          if (cardNoteStandard) {
            cardNoteStandard.textContent = `Half-Yearly: ${sym}${formatNum(hrmsStdHalflyDiscounted)} / user / 6 mo (Save 5% Billed Half-Yearly)`;
          }

          // Prime Plan - Half-Yearly (324 with 360 struck)
          if (cardCurrencyPrime) cardCurrencyPrime.textContent = sym;
          if (cardAmountPrime) cardAmountPrime.textContent = formatNum(hrmsPrimeHalflyDiscounted);
          if (cardOriginalPrime) {
            cardOriginalPrime.textContent = formatNum(hrmsPrimeHalflyTotal);
            cardOriginalPrime.style.display = 'inline';
          }
          if (cardPeriodPrime) cardPeriodPrime.textContent = '/ user / 6 mo';
          if (cardNotePrime) {
            cardNotePrime.textContent = `Half-Yearly: ${sym}${formatNum(hrmsPrimeHalflyDiscounted)} / user / 6 mo (Save 10% Billed Half-Yearly)`;
          }
        } else {
          // Basic Plan - Monthly (15 / user / mo)
          if (cardCurrencyBasic) cardCurrencyBasic.textContent = sym;
          if (cardAmountBasic) cardAmountBasic.textContent = formatNum(hrmsBasicMonthly);
          if (cardOriginalBasic) cardOriginalBasic.style.display = 'none';
          if (cardPeriodBasic) cardPeriodBasic.textContent = '/ user / mo';
          if (cardNoteBasic) {
            cardNoteBasic.textContent = `Yearly: ${sym}${formatNum(hrmsBasicAnnual)} / user / yr (Billed monthly)`;
          }

          // Standard Plan - Monthly (30 / user / mo)
          if (cardCurrencyStandard) cardCurrencyStandard.textContent = sym;
          if (cardAmountStandard) cardAmountStandard.textContent = formatNum(hrmsStdMonthly);
          if (cardOriginalStandard) cardOriginalStandard.style.display = 'none';
          if (cardPeriodStandard) cardPeriodStandard.textContent = '/ user / mo';
          if (cardNoteStandard) {
            cardNoteStandard.textContent = `Yearly: ${sym}${formatNum(hrmsStdAnnualTotal)} / user / yr (Billed monthly)`;
          }

          // Prime Plan - Monthly (60 / user / mo)
          if (cardCurrencyPrime) cardCurrencyPrime.textContent = sym;
          if (cardAmountPrime) cardAmountPrime.textContent = formatNum(hrmsPrimeMonthly);
          if (cardOriginalPrime) cardOriginalPrime.style.display = 'none';
          if (cardPeriodPrime) cardPeriodPrime.textContent = '/ user / mo';
          if (cardNotePrime) {
            cardNotePrime.textContent = `Yearly: ${sym}${formatNum(hrmsPrimeAnnualTotal)} / user / yr (Billed monthly)`;
          }
        }
      }

      """

html = html[:idx_start] + new_render_hrms + html[idx_end:]

# 4. Update setGrohrmsBilling function
old_set_grohrms = """      function setGrohrmsBilling(annual) {
        isAnnualGrohrms = annual;
        const btnM = document.getElementById('btnMonthlyGrohrms');
        const btnA = document.getElementById('btnAnnualGrohrms');
        if (btnM) { btnM.classList.toggle('active', !annual); btnM.setAttribute('aria-pressed', !annual); }
        if (btnA) { btnA.classList.toggle('active', annual); btnA.setAttribute('aria-pressed', annual); }
        renderPricingGrohrms();
      }"""

new_set_grohrms = """      function setGrohrmsBilling(cycle) {
        if (cycle === true) grohrmsBillingCycle = 'annual';
        else if (cycle === false) grohrmsBillingCycle = 'monthly';
        else grohrmsBillingCycle = cycle;

        isAnnualGrohrms = (grohrmsBillingCycle === 'annual');

        const btnM = document.getElementById('btnMonthlyGrohrms');
        const btnH = document.getElementById('btnHalflyGrohrms');
        const btnA = document.getElementById('btnAnnualGrohrms');

        if (btnM) { 
          btnM.classList.toggle('active', grohrmsBillingCycle === 'monthly'); 
          btnM.setAttribute('aria-pressed', grohrmsBillingCycle === 'monthly'); 
        }
        if (btnH) { 
          btnH.classList.toggle('active', grohrmsBillingCycle === 'halfly'); 
          btnH.setAttribute('aria-pressed', grohrmsBillingCycle === 'halfly'); 
        }
        if (btnA) { 
          btnA.classList.toggle('active', grohrmsBillingCycle === 'annual'); 
          btnA.setAttribute('aria-pressed', grohrmsBillingCycle === 'annual'); 
        }
        renderPricingGrohrms();
      }"""

assert old_set_grohrms in html, "old_set_grohrms not found in pricing.html!"
html = html.replace(old_set_grohrms, new_set_grohrms)

# 5. Add event listener for btnHalflyGrohrms
old_listeners = """      const btnMGrohrms = document.getElementById('btnMonthlyGrohrms');
      const btnAGrohrms = document.getElementById('btnAnnualGrohrms');
      if (btnMGrohrms) btnMGrohrms.addEventListener('click', () => setGrohrmsBilling(false));
      if (btnAGrohrms) btnAGrohrms.addEventListener('click', () => setGrohrmsBilling(true));"""

new_listeners = """      const btnMGrohrms = document.getElementById('btnMonthlyGrohrms');
      const btnHGrohrms = document.getElementById('btnHalflyGrohrms');
      const btnAGrohrms = document.getElementById('btnAnnualGrohrms');
      if (btnMGrohrms) btnMGrohrms.addEventListener('click', () => setGrohrmsBilling('monthly'));
      if (btnHGrohrms) btnHGrohrms.addEventListener('click', () => setGrohrmsBilling('halfly'));
      if (btnAGrohrms) btnAGrohrms.addEventListener('click', () => setGrohrmsBilling('annual'));"""

assert old_listeners in html, "old_listeners not found in pricing.html!"
html = html.replace(old_listeners, new_listeners)

# 6. Update URL param handling for halfly
old_url_param = """        if (urlParams.get('billing') === 'annual') {
          setGrohrmsBilling(true);
          setGrologBilling(true);
          setGroinnBilling(true);
        }"""

new_url_param = """        if (urlParams.get('billing') === 'annual') {
          setGrohrmsBilling('annual');
          setGrologBilling(true);
          setGroinnBilling(true);
        } else if (urlParams.get('billing') === 'halfly' || urlParams.get('billing') === 'half-yearly') {
          setGrohrmsBilling('halfly');
        }"""

if old_url_param in html:
    html = html.replace(old_url_param, new_url_param)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully added halfly plan to Grohrms!")

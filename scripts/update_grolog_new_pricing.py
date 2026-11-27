import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Grolog Annually Discount Badge: "Up to 20% Off" -> "Up to 15% Off"
content = re.sub(
    r'(<button type="button" class="billing-btn" id="btnAnnualGrolog"[^>]*>[\s\S]*?<span class="billing-discount-badge">)Up to 20% Off(</span>)',
    r'\g<1>Up to 15% Off\2',
    content
)

# 2. Update Card 2 HTML
# Monthly 350, Annual 3780
content = re.sub(
    r'(id="cardAmountGrolog2" data-monthly=")[^"]*(" data-annual=")[^"]*(">\s*)[^<]*',
    r'\g<1>350\g<2>3780\g<3>350',
    content
)
content = re.sub(
    r'(id="cardOriginalGrolog2" style="display: none;">)[^<]*',
    r'\g<1>350',
    content
)
content = re.sub(
    r'(id="cardNoteGrolog2"[\s\S]*?data-monthly-note=")[^"]*("[\s\S]*?data-annual-note=")[^"]*(">\s*)[\s\S]*?(</p>)',
    r'\g<1>Yearly: ₹4,200 / user / yr (Billed monthly)\g<2>Yearly: ₹3,780 / user / yr (Billed Annually)\g<3>Yearly: ₹4,200 / user / yr (Billed monthly)\g<4>',
    content
)

# 3. Update Card 3 HTML
# 10 - 25 Users -> 10 - 15 Users
content = re.sub(
    r'<h3>10 – 25 Users</h3>',
    r'<h3>10 – 15 Users</h3>',
    content
)
content = re.sub(
    r'(id="cardAmountGrolog3" data-monthly=")[^"]*(" data-annual=")[^"]*(">\s*)[^<]*',
    r'\g<1>350\g<2>3570\g<3>350',
    content
)
content = re.sub(
    r'(id="cardOriginalGrolog3" style="display: none;">)[^<]*',
    r'\g<1>350',
    content
)
content = re.sub(
    r'(id="cardNoteGrolog3"[\s\S]*?data-monthly-note=")[^"]*("[\s\S]*?data-annual-note=")[^"]*(">\s*)[\s\S]*?(</p>)',
    r'\g<1>Yearly: ₹4,200 / user / yr (Billed monthly)\g<2>Yearly: ₹3,570 / user / yr (Billed Annually)\g<3>Yearly: ₹4,200 / user / yr (Billed monthly)\g<4>',
    content
)
content = re.sub(
    r'<span><b>10 to 25 active agents &amp; multi-SIM tracking</b></span>',
    r'<span><b>10 to 15 active agents &amp; multi-SIM tracking</b></span>',
    content
)
content = re.sub(
    r'href="enquire\.html\?plan=grolog-25users"',
    r'href="enquire.html?plan=grolog-15users"',
    content
)

# 4. Update Card 4 HTML
# 25+ Users / Enterprise -> 15+ Users / Enterprise
content = re.sub(
    r'<h3>25\+ Users / Enterprise</h3>',
    r'<h3>15+ Users / Enterprise</h3>',
    content
)

# 5. Update currencyRates for Grolog
# INR
old_inr_grolog = """          grolog: {
            tier1: { monthly: 350, annual: 332.5 },
            tier2: { monthly: 300, annual: 270 },
            tier3: { monthly: 250, annual: 200 }
          },"""

new_inr_grolog = """          grolog: {
            tier1: { monthly: 350, annual: 332.5 },
            tier2: { monthly: 350, annual: 315 },
            tier3: { monthly: 350, annual: 297.5 }
          },"""

content = content.replace(old_inr_grolog, new_inr_grolog)

# 6. Update renderPricingGrolog()
old_render_grolog = """function renderPricingGrolog() {
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
      }"""

new_render_grolog = """function renderPricingGrolog() {
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

          // Tier 2 - Annually (3780 with 4200 struck)
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

          // Tier 3 - Annually (3570 with 4200 struck)
          if (cardCurrencyGrolog3) cardCurrencyGrolog3.textContent = sym;
          if (cardAmountGrolog3) cardAmountGrolog3.textContent = formatNum(grolog3AnnualTotal);
          if (cardOriginalGrolog3) {
            cardOriginalGrolog3.textContent = formatNum(grolog3MonthlyTotal);
            cardOriginalGrolog3.style.display = 'inline';
          }
          if (cardPeriodGrolog3) cardPeriodGrolog3.textContent = '/ user / yr';
          if (cardNoteGrolog3) {
            cardNoteGrolog3.textContent = `Yearly: ${sym}${formatNum(grolog3AnnualTotal)} / user / yr (Save 15% Billed Annually)`;
          }
        } else {
          // Tier 1 - Monthly (350/mo)
          if (cardCurrencyGrolog1) cardCurrencyGrolog1.textContent = sym;
          if (cardAmountGrolog1) cardAmountGrolog1.textContent = formatNum(grolog1Monthly);
          if (cardOriginalGrolog1) cardOriginalGrolog1.style.display = 'none';
          if (cardPeriodGrolog1) cardPeriodGrolog1.textContent = '/ user / mo';
          if (cardNoteGrolog1) {
            cardNoteGrolog1.textContent = `Yearly: ${sym}${formatNum(grolog1MonthlyTotal)} / user / yr (Billed monthly)`;
          }

          // Tier 2 - Monthly (350/mo)
          if (cardCurrencyGrolog2) cardCurrencyGrolog2.textContent = sym;
          if (cardAmountGrolog2) cardAmountGrolog2.textContent = formatNum(grolog2Monthly);
          if (cardOriginalGrolog2) cardOriginalGrolog2.style.display = 'none';
          if (cardPeriodGrolog2) cardPeriodGrolog2.textContent = '/ user / mo';
          if (cardNoteGrolog2) {
            cardNoteGrolog2.textContent = `Yearly: ${sym}${formatNum(grolog2MonthlyTotal)} / user / yr (Billed monthly)`;
          }

          // Tier 3 - Monthly (350/mo)
          if (cardCurrencyGrolog3) cardCurrencyGrolog3.textContent = sym;
          if (cardAmountGrolog3) cardAmountGrolog3.textContent = formatNum(grolog3Monthly);
          if (cardOriginalGrolog3) cardOriginalGrolog3.style.display = 'none';
          if (cardPeriodGrolog3) cardPeriodGrolog3.textContent = '/ user / mo';
          if (cardNoteGrolog3) {
            cardNoteGrolog3.textContent = `Yearly: ${sym}${formatNum(grolog3MonthlyTotal)} / user / yr (Billed monthly)`;
          }
        }
      }"""

assert old_render_grolog in content, "old_render_grolog not found"
content = content.replace(old_render_grolog, new_render_grolog)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Grolog new pricing successfully!")

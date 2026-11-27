import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    js_code = f.read()

# 1. Update element declarations
old_decl = """      // Grohrms Card Elements
      const cardCurrencyBasic = document.getElementById('cardCurrencyBasic');
      const cardAmountBasic = document.getElementById('cardAmountBasic');
      const cardNoteBasic = document.getElementById('cardNoteBasic');

      const cardCurrencyStandard = document.getElementById('cardCurrencyStandard');
      const cardAmountStandard = document.getElementById('cardAmountStandard');
      const cardNoteStandard = document.getElementById('cardNoteStandard');

      const cardCurrencyPrime = document.getElementById('cardCurrencyPrime');
      const cardAmountPrime = document.getElementById('cardAmountPrime');
      const cardNotePrime = document.getElementById('cardNotePrime');

      // Groinn Card Elements
      const cardCurrencyGroinn1 = document.getElementById('cardCurrencyGroinn1');
      const cardAmountGroinn1 = document.getElementById('cardAmountGroinn1');
      const cardNoteGroinn1 = document.getElementById('cardNoteGroinn1');

      const cardCurrencyGroinn2 = document.getElementById('cardCurrencyGroinn2');
      const cardAmountGroinn2 = document.getElementById('cardAmountGroinn2');
      const cardNoteGroinn2 = document.getElementById('cardNoteGroinn2');

      const cardCurrencyGroinn3 = document.getElementById('cardCurrencyGroinn3');
      const cardAmountGroinn3 = document.getElementById('cardAmountGroinn3');
      const cardNoteGroinn3 = document.getElementById('cardNoteGroinn3');

      // Compatibility fallback
      const cardCurrencyGroinn = cardCurrencyGroinn1;
      const cardAmountGroinn = cardAmountGroinn1;
      const cardNoteGroinn = cardNoteGroinn1;

      // Grolog Card Elements
      const cardCurrencyGrolog1 = document.getElementById('cardCurrencyGrolog1');
      const cardAmountGrolog1 = document.getElementById('cardAmountGrolog1');
      const cardNoteGrolog1 = document.getElementById('cardNoteGrolog1');

      const cardCurrencyGrolog2 = document.getElementById('cardCurrencyGrolog2');
      const cardAmountGrolog2 = document.getElementById('cardAmountGrolog2');
      const cardNoteGrolog2 = document.getElementById('cardNoteGrolog2');

      const cardCurrencyGrolog3 = document.getElementById('cardCurrencyGrolog3');
      const cardAmountGrolog3 = document.getElementById('cardAmountGrolog3');
      const cardNoteGrolog3 = document.getElementById('cardNoteGrolog3');"""

new_decl = """      // Grohrms Card Elements
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

assert old_decl in js_code, "Could not find old_decl"
js_code = js_code.replace(old_decl, new_decl)

# 2. Update renderPricingGrohrms
old_hrms = """        if (cardCurrencyBasic) cardCurrencyBasic.textContent = sym;
        if (cardAmountBasic) cardAmountBasic.textContent = formatNum(hrmsBasicActive);
        if (cardNoteBasic) {
          const yearlyTotal = formatNum(hrmsBasicActive * 12);
          cardNoteBasic.textContent = isAnnualGrohrms
            ? `Yearly: ${sym}${yearlyTotal} / user / yr (Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / user / yr (Billed monthly)`;
        }

        if (cardCurrencyStandard) cardCurrencyStandard.textContent = sym;
        if (cardAmountStandard) cardAmountStandard.textContent = formatNum(hrmsStdActive);
        if (cardNoteStandard) {
          const yearlyTotal = formatNum(hrmsStdActive * 12);
          cardNoteStandard.textContent = isAnnualGrohrms
            ? `Yearly: ${sym}${yearlyTotal} / user / yr (Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / user / yr (Billed monthly)`;
        }

        if (cardCurrencyPrime) cardCurrencyPrime.textContent = sym;
        if (cardAmountPrime) cardAmountPrime.textContent = formatNum(hrmsPrimeActive);
        if (cardNotePrime) {
          const yearlyTotal = formatNum(hrmsPrimeActive * 12);
          cardNotePrime.textContent = isAnnualGrohrms
            ? `Yearly: ${sym}${yearlyTotal} / user / yr (Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / user / yr (Billed monthly)`;
        }"""

new_hrms = """        if (cardCurrencyBasic) cardCurrencyBasic.textContent = sym;
        if (cardAmountBasic) cardAmountBasic.textContent = formatNum(hrmsBasicActive);
        if (cardOriginalBasic) {
          if (isAnnualGrohrms && hrmsBasicAnnual < hrmsBasicMonthly) {
            cardOriginalBasic.textContent = formatNum(hrmsBasicMonthly);
            cardOriginalBasic.style.display = 'inline';
          } else {
            cardOriginalBasic.style.display = 'none';
          }
        }
        if (cardNoteBasic) {
          const yearlyTotal = formatNum(hrmsBasicActive * 12);
          cardNoteBasic.textContent = isAnnualGrohrms
            ? `Yearly: ${sym}${yearlyTotal} / user / yr (Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / user / yr (Billed monthly)`;
        }

        if (cardCurrencyStandard) cardCurrencyStandard.textContent = sym;
        if (cardAmountStandard) cardAmountStandard.textContent = formatNum(hrmsStdActive);
        if (cardOriginalStandard) {
          if (isAnnualGrohrms && hrmsStdAnnual < hrmsStdMonthly) {
            cardOriginalStandard.textContent = formatNum(hrmsStdMonthly);
            cardOriginalStandard.style.display = 'inline';
          } else {
            cardOriginalStandard.style.display = 'none';
          }
        }
        if (cardNoteStandard) {
          const yearlyTotal = formatNum(hrmsStdActive * 12);
          cardNoteStandard.textContent = isAnnualGrohrms
            ? `Yearly: ${sym}${yearlyTotal} / user / yr (Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / user / yr (Billed monthly)`;
        }

        if (cardCurrencyPrime) cardCurrencyPrime.textContent = sym;
        if (cardAmountPrime) cardAmountPrime.textContent = formatNum(hrmsPrimeActive);
        if (cardOriginalPrime) {
          if (isAnnualGrohrms && hrmsPrimeAnnual < hrmsPrimeMonthly) {
            cardOriginalPrime.textContent = formatNum(hrmsPrimeMonthly);
            cardOriginalPrime.style.display = 'inline';
          } else {
            cardOriginalPrime.style.display = 'none';
          }
        }
        if (cardNotePrime) {
          const yearlyTotal = formatNum(hrmsPrimeActive * 12);
          cardNotePrime.textContent = isAnnualGrohrms
            ? `Yearly: ${sym}${yearlyTotal} / user / yr (Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / user / yr (Billed monthly)`;
        }"""

assert old_hrms in js_code, "Could not find old_hrms"
js_code = js_code.replace(old_hrms, new_hrms)

# 3. Update renderPricingGrolog
old_grolog = """        if (cardCurrencyGrolog1) cardCurrencyGrolog1.textContent = sym;
        if (cardAmountGrolog1) {
          const displayVal = (cur.code === 'INR' && isAnnualGrolog) ? Math.round(grolog1Active) : grolog1Active;
          cardAmountGrolog1.textContent = formatNum(displayVal);
        }
        if (cardNoteGrolog1) {
          const yearlyTotal = formatNum(grolog1Active * 12);
          cardNoteGrolog1.textContent = isAnnualGrolog
            ? `Yearly: ${sym}${yearlyTotal} / user / yr (Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / user / yr (Billed monthly)`;
        }

        if (cardCurrencyGrolog2) cardCurrencyGrolog2.textContent = sym;
        if (cardAmountGrolog2) cardAmountGrolog2.textContent = formatNum(grolog2Active);
        if (cardNoteGrolog2) {
          const yearlyTotal = formatNum(grolog2Active * 12);
          cardNoteGrolog2.textContent = isAnnualGrolog
            ? `Yearly: ${sym}${yearlyTotal} / user / yr (Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / user / yr (Billed monthly)`;
        }

        if (cardCurrencyGrolog3) cardCurrencyGrolog3.textContent = sym;
        if (cardAmountGrolog3) cardAmountGrolog3.textContent = formatNum(grolog3Active);
        if (cardNoteGrolog3) {
          const yearlyTotal = formatNum(grolog3Active * 12);
          cardNoteGrolog3.textContent = isAnnualGrolog
            ? `Yearly: ${sym}${yearlyTotal} / user / yr (Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / user / yr (Billed monthly)`;
        }"""

new_grolog = """        if (cardCurrencyGrolog1) cardCurrencyGrolog1.textContent = sym;
        if (cardAmountGrolog1) {
          const displayVal = (cur.code === 'INR' && isAnnualGrolog) ? Math.round(grolog1Active) : grolog1Active;
          cardAmountGrolog1.textContent = formatNum(displayVal);
        }
        if (cardOriginalGrolog1) {
          if (isAnnualGrolog && grolog1Annual < grolog1Monthly) {
            cardOriginalGrolog1.textContent = formatNum(grolog1Monthly);
            cardOriginalGrolog1.style.display = 'inline';
          } else {
            cardOriginalGrolog1.style.display = 'none';
          }
        }
        if (cardNoteGrolog1) {
          const yearlyTotal = formatNum(grolog1Active * 12);
          cardNoteGrolog1.textContent = isAnnualGrolog
            ? `Yearly: ${sym}${yearlyTotal} / user / yr (Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / user / yr (Billed monthly)`;
        }

        if (cardCurrencyGrolog2) cardCurrencyGrolog2.textContent = sym;
        if (cardAmountGrolog2) cardAmountGrolog2.textContent = formatNum(grolog2Active);
        if (cardOriginalGrolog2) {
          if (isAnnualGrolog && grolog2Annual < grolog2Monthly) {
            cardOriginalGrolog2.textContent = formatNum(grolog2Monthly);
            cardOriginalGrolog2.style.display = 'inline';
          } else {
            cardOriginalGrolog2.style.display = 'none';
          }
        }
        if (cardNoteGrolog2) {
          const yearlyTotal = formatNum(grolog2Active * 12);
          cardNoteGrolog2.textContent = isAnnualGrolog
            ? `Yearly: ${sym}${yearlyTotal} / user / yr (Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / user / yr (Billed monthly)`;
        }

        if (cardCurrencyGrolog3) cardCurrencyGrolog3.textContent = sym;
        if (cardAmountGrolog3) cardAmountGrolog3.textContent = formatNum(grolog3Active);
        if (cardOriginalGrolog3) {
          if (isAnnualGrolog && grolog3Annual < grolog3Monthly) {
            cardOriginalGrolog3.textContent = formatNum(grolog3Monthly);
            cardOriginalGrolog3.style.display = 'inline';
          } else {
            cardOriginalGrolog3.style.display = 'none';
          }
        }
        if (cardNoteGrolog3) {
          const yearlyTotal = formatNum(grolog3Active * 12);
          cardNoteGrolog3.textContent = isAnnualGrolog
            ? `Yearly: ${sym}${yearlyTotal} / user / yr (Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / user / yr (Billed monthly)`;
        }"""

assert old_grolog in js_code, "Could not find old_grolog"
js_code = js_code.replace(old_grolog, new_grolog)

# 4. Update renderPricingGroinn
old_groinn = """        // Tier 1
        if (cardCurrencyGroinn1) cardCurrencyGroinn1.textContent = sym;
        if (cardAmountGroinn1) {
          const displayVal = (cur.code === 'INR' && isAnnualGroinn) ? Math.round(groinn1Active) : groinn1Active;
          cardAmountGroinn1.textContent = formatNum(displayVal);
        }
        if (cardNoteGroinn1) {
          const yearlyTotal = formatNum(Math.round(groinn1Active * 12));
          cardNoteGroinn1.textContent = isAnnualGroinn
            ? `Yearly: ${sym}${yearlyTotal} / year (Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / year (Billed monthly)`;
        }

        // Tier 2
        if (cardCurrencyGroinn2) cardCurrencyGroinn2.textContent = sym;
        if (cardAmountGroinn2) {
          const displayVal = (cur.code === 'INR' && isAnnualGroinn) ? Math.round(groinn2Active) : groinn2Active;
          cardAmountGroinn2.textContent = formatNum(displayVal);
        }
        if (cardNoteGroinn2) {
          const yearlyTotal = formatNum(Math.round(groinn2Active * 12));
          cardNoteGroinn2.textContent = isAnnualGroinn
            ? `Yearly: ${sym}${yearlyTotal} / year (Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / year (Billed monthly)`;
        }

        // Tier 3
        if (cardCurrencyGroinn3) cardCurrencyGroinn3.textContent = sym;
        if (cardAmountGroinn3) {
          const displayVal = (cur.code === 'INR' && isAnnualGroinn) ? Math.round(groinn3Active) : groinn3Active;
          cardAmountGroinn3.textContent = formatNum(displayVal);
        }
        if (cardNoteGroinn3) {
          const yearlyTotal = formatNum(Math.round(groinn3Active * 12));
          cardNoteGroinn3.textContent = isAnnualGroinn
            ? `Yearly: ${sym}${yearlyTotal} / year (Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / year (Billed monthly)`;
        }"""

new_groinn = """        // Tier 1
        if (cardCurrencyGroinn1) cardCurrencyGroinn1.textContent = sym;
        if (cardAmountGroinn1) {
          const displayVal = (cur.code === 'INR' && isAnnualGroinn) ? Math.round(groinn1Active) : groinn1Active;
          cardAmountGroinn1.textContent = formatNum(displayVal);
        }
        if (cardOriginalGroinn1) {
          if (isAnnualGroinn && groinn1Annual < groinn1Monthly) {
            cardOriginalGroinn1.textContent = formatNum(groinn1Monthly);
            cardOriginalGroinn1.style.display = 'inline';
          } else {
            cardOriginalGroinn1.style.display = 'none';
          }
        }
        if (cardNoteGroinn1) {
          const yearlyTotal = formatNum(Math.round(groinn1Active * 12));
          cardNoteGroinn1.textContent = isAnnualGroinn
            ? `Yearly: ${sym}${yearlyTotal} / year (Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / year (Billed monthly)`;
        }

        // Tier 2
        if (cardCurrencyGroinn2) cardCurrencyGroinn2.textContent = sym;
        if (cardAmountGroinn2) {
          const displayVal = (cur.code === 'INR' && isAnnualGroinn) ? Math.round(groinn2Active) : groinn2Active;
          cardAmountGroinn2.textContent = formatNum(displayVal);
        }
        if (cardOriginalGroinn2) {
          if (isAnnualGroinn && groinn2Annual < groinn2Monthly) {
            cardOriginalGroinn2.textContent = formatNum(groinn2Monthly);
            cardOriginalGroinn2.style.display = 'inline';
          } else {
            cardOriginalGroinn2.style.display = 'none';
          }
        }
        if (cardNoteGroinn2) {
          const yearlyTotal = formatNum(Math.round(groinn2Active * 12));
          cardNoteGroinn2.textContent = isAnnualGroinn
            ? `Yearly: ${sym}${yearlyTotal} / year (Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / year (Billed monthly)`;
        }

        // Tier 3
        if (cardCurrencyGroinn3) cardCurrencyGroinn3.textContent = sym;
        if (cardAmountGroinn3) {
          const displayVal = (cur.code === 'INR' && isAnnualGroinn) ? Math.round(groinn3Active) : groinn3Active;
          cardAmountGroinn3.textContent = formatNum(displayVal);
        }
        if (cardOriginalGroinn3) {
          if (isAnnualGroinn && groinn3Annual < groinn3Monthly) {
            cardOriginalGroinn3.textContent = formatNum(groinn3Monthly);
            cardOriginalGroinn3.style.display = 'inline';
          } else {
            cardOriginalGroinn3.style.display = 'none';
          }
        }
        if (cardNoteGroinn3) {
          const yearlyTotal = formatNum(Math.round(groinn3Active * 12));
          cardNoteGroinn3.textContent = isAnnualGroinn
            ? `Yearly: ${sym}${yearlyTotal} / year (Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / year (Billed monthly)`;
        }"""

assert old_groinn in js_code, "Could not find old_groinn"
js_code = js_code.replace(old_groinn, new_groinn)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(js_code)

print("Updated JavaScript in pricing.html successfully.")

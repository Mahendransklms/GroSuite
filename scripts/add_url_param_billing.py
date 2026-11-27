import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    code = f.read()

pattern = r'(\s*// Initial Render Pricing\s*renderPricing\(\);)'
replacement = r'''\1

      // Check URL Query Parameters (e.g. ?billing=annual)
      try {
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.get('billing') === 'annual') {
          setGrohrmsBilling(true);
          setGrologBilling(true);
          setGroinnBilling(true);
        }
      } catch (e) {
        console.warn('URL params parsing failed', e);
      }'''

code = re.sub(pattern, replacement, code, count=1)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(code)

print("Added URL param billing support.")

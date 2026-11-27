import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    code = f.read()

pattern = r'''      // Check URL Query Parameters \(e\.g\. \?billing=annual\)
      try \{
        const urlParams = new URLSearchParams\(window\.location\.search\);
        if \(urlParams\.get\('billing'\) === 'annual'\) \{
          setGrohrmsBilling\(true\);
          setGrologBilling\(true\);
          setGroinnBilling\(true\);
        \}
      \} catch \(e\) \{
        console\.warn\('URL params parsing failed', e\);
      \}'''

replacement = '''      // Check URL Query Parameters (e.g. ?billing=annual or ?unlocked=1)
      try {
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.get('unlocked') === '1' || urlParams.get('billing')) {
          if (pricingGateForm) pricingGateForm.style.display = 'none';
          if (pricingDetailsContainer) pricingDetailsContainer.style.display = 'block';
        }
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

print("Updated URL query param handling to unlock pricing when needed.")

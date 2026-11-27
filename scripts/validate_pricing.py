with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Check tag balances
stack = []
for idx, line in enumerate(html.splitlines()):
    clean = re.sub(r'<!--.*?-->', '', line)
    for tag in re.finditer(r'<(/)?([a-zA-Z0-9]+)[^>]*>', clean):
        is_close = tag.group(1) == '/'
        name = tag.group(2).lower()
        if name in ['meta', 'link', 'br', 'hr', 'img', 'input', 'source', 'path', 'circle', 'rect', 'line', 'polyline', 'polygon']:
            continue
        if tag.group(0).endswith('/>'):
            continue
        if is_close:
            if stack and stack[-1] == name:
                stack.pop()
        else:
            stack.append(name)

print("Unclosed tags:", "All valid!" if not stack else stack)

# Check elements
tabs = re.findall(r'id=["\']tab(.*?)["\']', html)
print("Tabs in pricing.html:", tabs)

discount_badges = re.findall(r'class=["\']card-annual-discount["\']', html)
print("Card annual discount badges count:", len(discount_badges))

billing_discount = 'billing-discount-badge' in html
print("Any billing discount badges on buttons:", billing_discount)

btn_ids = [
    'btnMonthlyGrohrms', 'btnAnnualGrohrms',
    'btnMonthlyGrolog', 'btnAnnualGrolog',
    'btnMonthlyGroinn', 'btnAnnualGroinn'
]
missing_btns = [b for b in btn_ids if f'id="{b}"' not in html]
print("Missing separate product buttons:", missing_btns if missing_btns else "None! All 6 buttons present.")

sections = re.findall(r'<section\s+class=["\']pricing-section["\']\s+id=["\'](.*?)["\']', html)
print("Pricing sections:", sections)

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

opens = css.count('{')
closes = css.count('}')
print(f"CSS braces diff: {opens - closes}")

orig_ids = [
    'cardOriginalBasic', 'cardOriginalStandard', 'cardOriginalPrime',
    'cardOriginalGrolog1', 'cardOriginalGrolog2', 'cardOriginalGrolog3',
    'cardOriginalGroinn1', 'cardOriginalGroinn2', 'cardOriginalGroinn3'
]

counts = {oid: len(re.findall(r'id=["\']' + oid + r'["\']', html)) for oid in orig_ids}
print("Original price element counts (should be exactly 1 each in HTML markup):", counts)
assert all(c == 1 for c in counts.values()), "Some elements are duplicated or missing!"

js_refs = {oid: len(re.findall(r'\b' + oid + r'\b', html)) for oid in orig_ids}
print("JS references count:", js_refs)
assert all(c >= 2 for c in js_refs.values()), "Some elements are not referenced in JS!"
print("ALL CHECKS PASSED PERFECTLY!")

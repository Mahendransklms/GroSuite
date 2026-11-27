with open('pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

print("=== SEARCH FOR SWITCHER BUTTONS ===")
for m in re.finditer(r'<div class="[^"]*billing[^"]*"[\s\S]*?</div>', text):
    print(m.group(0)[:300])
    print("---")

print("\n=== SEARCH FOR cardAmountBasic IN HTML ===")
idx = text.find('id="cardAmountBasic"')
if idx != -1:
    print(text[idx-200:idx+400])

print("\n=== SEARCH FOR cardAmountGroinn1 IN HTML ===")
idx2 = text.find('id="cardAmountGroinn1"')
if idx2 != -1:
    print(text[idx2-200:idx2+400])

print("\n=== SEARCH FOR cardAmountGrolog1 IN HTML ===")
idx3 = text.find('id="cardAmountGrolog1"')
if idx3 != -1:
    print(text[idx3-200:idx3+400])

print("\n=== SEARCH FOR BUTTON EVENT LISTENERS FOR BILLING ===")
for m in re.finditer(r'btn(Annual|Monthly)[a-zA-Z]*\.addEventListener[\s\S]*?\}\);', text):
    print(m.group(0)[:200])

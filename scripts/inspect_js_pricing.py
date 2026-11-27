with open('pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

idx1 = text.find('const currencyRates = {')
idx2 = text.find('// Step Navigation Functions', idx1)
print("=== currencyRates TO Step Navigation Functions ===")
print(text[idx1:idx1+1500])

idx3 = text.find('let isAnnualGrohrms =')
idx4 = text.find('// Billing Toggle Switchers', idx3)
print("\n=== isAnnual TO Switchers ===")
print(text[idx3:idx4])

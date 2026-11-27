with open('pricing.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

def find_lines(pattern):
    import re
    res = []
    for i, l in enumerate(lines):
        if re.search(pattern, l):
            res.append(i)
    return res

print("Grohrms cards around:", find_lines(r'cardAmountBasic'))
print("Grolog cards around:", find_lines(r'cardAmountGrolog1'))
print("Groinn cards around:", find_lines(r'cardAmountGroinn1'))
print("currencyRates around:", find_lines(r'const currencyRates ='))
print("renderPricing around:", find_lines(r'function renderPricingGrohrms'))

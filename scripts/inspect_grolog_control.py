with open('pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="grolog-pricing"')
print(text[idx:idx+1500])

with open('pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="groinn-pricing"')
if idx != -1:
    print(text[idx+2500:idx+6500])

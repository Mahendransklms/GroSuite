with open('pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="grohrms-pricing"')
end = text.find('id="grolog-pricing"')
print(text[idx:end])

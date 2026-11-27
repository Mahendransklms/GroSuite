with open('pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('id="cardAmountBasic" data-monthly="15" data-annual="12"', 'id="cardAmountBasic" data-monthly="15" data-annual="15"')
text = text.replace('id="cardAmountStandard" data-monthly="30" data-annual="24"', 'id="cardAmountStandard" data-monthly="30" data-annual="27"')

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated data-annual attributes in pricing.html successfully.")

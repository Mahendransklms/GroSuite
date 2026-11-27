with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="solutions"')
if idx != -1:
    print(text[idx:idx+3000])
else:
    print("id='solutions' not found")

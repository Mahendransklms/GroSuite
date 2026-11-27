with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
items = re.findall(r'<div[^>]*>\s*<h3>(Gro[a-z]+)[^<]*</h3>\s*<p>(.*?)</p>', text)
for name, desc in items:
    print(f"{name}: {desc}")

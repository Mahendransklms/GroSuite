with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<h3[^>]*>(Gro[a-z]+)[^<]*</h3>', text, re.IGNORECASE)
print("Products in index.html:", matches)

# Find solution titles/subtitles
cards = re.findall(r'(Gro[a-z]+)</h3>\s*<p[^>]*>(.*?)</p>', text, re.IGNORECASE)
for name, desc in cards[:12]:
    print(f"{name}: {desc[:80]}")

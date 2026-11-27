import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    c = f.read()

matches = re.findall(r'id=["\'](cardOriginal[a-zA-Z0-9]+)["\']', c)
print('Count of cardOriginal IDs:', len(matches))
print('Unique cardOriginal IDs:', len(set(matches)))
print('IDs found:', matches)

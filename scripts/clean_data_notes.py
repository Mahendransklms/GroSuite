with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Remove any data-monthly-note and data-annual-note attributes from cardNote elements
html = re.sub(r'\s+data-monthly-note="[^"]*"', '', html)
html = re.sub(r'\s+data-annual-note="[^"]*"', '', html)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Removed outdated data-*-note attributes successfully!")

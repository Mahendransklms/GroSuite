with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

html = html.replace('id="cardOriginalStandard" style="display: none;">360">360</span>', 'id="cardOriginalStandard" style="display: none;">360</span>')
html = html.replace('id="cardOriginalPrime" style="display: none;">720">720</span>', 'id="cardOriginalPrime" style="display: none;">720</span>')

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed tag typo!")

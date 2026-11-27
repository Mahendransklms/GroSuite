with open('enquire.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
selects = re.findall(r'<select[^>]*>.*?</select>', text, re.DOTALL)
for s in selects:
    print(s[:500])

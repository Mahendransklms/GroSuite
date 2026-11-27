with open('pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'// Prepare FormData for FormSubmit\.app.*?formData\.append\(\'_ts\'.*?\);', text, re.DOTALL)
if match:
    print(match.group(0))
else:
    print("formData block not found")

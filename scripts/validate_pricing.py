from html.parser import HTMLParser

class Validator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.void_tags = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
    def handle_starttag(self, tag, attrs):
        if tag not in self.void_tags:
            self.tags.append(tag)
    def handle_endtag(self, tag):
        if tag not in self.void_tags:
            if self.tags and self.tags[-1] == tag:
                self.tags.pop()

v = Validator()
with open('pricing.html', 'r', encoding='utf-8') as f:
    content = f.read()
    v.feed(content)

print('Unclosed tags:', v.tags[-10:] if v.tags else 'All valid!')

targets = [
    'ESTIMATE YOUR INVESTMENT',
    'Interactive Team Size Cost Calculator',
    'MODULAR ADD-ONS',
    'Supercharge your workflow with specialized modules',
    'DETAILED COMPARISON',
    'Compare all plan features side by side'
]

for t in targets:
    print(f'Remaining "{t}":', t.lower() in content.lower())

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

print('CSS brace diff:', css.count('{') - css.count('}'))

with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace with "Employee Count: 20", "60", "120", "120+"
html = html.replace('<span>Employee Count: <strong>Up to 20</strong></span>', '<span>Employee Count: <strong>20</strong></span>')
html = html.replace('<span>Employee Count: <strong>Up to 60</strong></span>', '<span>Employee Count: <strong>60</strong></span>')
html = html.replace('<span>Employee Count: <strong>Up to 120</strong></span>', '<span>Employee Count: <strong>120</strong></span>')
html = html.replace('<span>Employee Count: <strong>120+ / Custom</strong></span>', '<span>Employee Count: <strong>120+</strong></span>')

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

# Update .pricing-card__employee-count in css/style.css with justify-content: center and white-space: nowrap
css = re.sub(
    r'\.pricing-card__employee-count\s*\{[^}]*\}',
    '''.pricing-card__employee-count {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  font-size: 0.84rem;
  font-weight: 600;
  color: #38bdf8;
  background: rgba(56, 189, 248, 0.08);
  border: 1px solid rgba(56, 189, 248, 0.22);
  border-radius: 8px;
  padding: 0.45rem 0.65rem;
  margin-top: -0.35rem;
  margin-bottom: 1.25rem;
  line-height: 1.3;
  white-space: nowrap;
}''',
    css
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated employee count styles and text!")

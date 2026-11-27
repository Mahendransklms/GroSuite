import re
import subprocess
import os
from PIL import Image

with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove all existing .pricing-card__employee-count elements from pricing.html first to avoid duplicates
html = re.sub(r'\s*<div class="pricing-card__employee-count">[\s\S]*?</div>', '', html)

# Define SVG icon
icon_svg = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>'

# Card 1: Basic (20)
emp_basic = f'''              <div class="pricing-card__employee-count">
                {icon_svg}
                <span>Employee Count: <strong>20</strong></span>
              </div>'''

# Card 2: Standard (60)
emp_standard = f'''              <div class="pricing-card__employee-count">
                {icon_svg}
                <span>Employee Count: <strong>60</strong></span>
              </div>'''

# Card 3: Prime (120)
emp_prime = f'''              <div class="pricing-card__employee-count">
                {icon_svg}
                <span>Employee Count: <strong>120</strong></span>
              </div>'''

# Card 4: Custom (120+)
emp_custom = f'''              <div class="pricing-card__employee-count">
                {icon_svg}
                <span>Employee Count: <strong>120+</strong></span>
              </div>'''

# Insert after cardNoteBasic
html = re.sub(
    r'(<p class="pricing-card__billing-note" id="cardNoteBasic"[^>]*>.*?</p>)',
    r'\g<1>\n' + emp_basic,
    html
)

# Insert after cardNoteStandard
html = re.sub(
    r'(<p class="pricing-card__billing-note" id="cardNoteStandard"[^>]*>.*?</p>)',
    r'\g<1>\n' + emp_standard,
    html
)

# Insert after cardNotePrime
html = re.sub(
    r'(<p class="pricing-card__billing-note" id="cardNotePrime"[^>]*>.*?</p>)',
    r'\g<1>\n' + emp_prime,
    html
)

# Insert in Grohrms card 4 after billing note
grohrms_idx = html.find('id="grohrms-pricing"')
grohrms_end = html.find('id="grolog-pricing"')
grohrms_text = html[grohrms_idx:grohrms_end]

card4_pattern = r'(<div class="pricing-card__price-box pricing-card__price-box--quote">\s*<span class="pricing-card__amount pricing-card__amount--quote">Client Requirement</span>\s*</div>\s*<p class="pricing-card__billing-note">Tailored project scope &amp; milestones</p>)'
assert re.search(card4_pattern, grohrms_text), "Card 4 pattern not found!"

grohrms_text_new = re.sub(card4_pattern, r'\g<1>\n' + emp_custom, grohrms_text)
html = html[:grohrms_idx] + grohrms_text_new + html[grohrms_end:]

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated pricing.html cleanly with employee counts!")

# 2. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

clean_emp_css = """.pricing-card__employee-count {
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
}
.pricing-card__employee-count svg {
  flex-shrink: 0;
  color: #38bdf8;
}
.pricing-card__employee-count strong {
  color: #ffffff;
  font-weight: 700;
}"""

if '.pricing-card__employee-count' in css:
    css = re.sub(r'\.pricing-card__employee-count\s*\{[^}]*\}', clean_emp_css, css)
else:
    css += "\n" + clean_emp_css

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated css/style.css with clean employee count styles!")

# 3. Capture screenshot
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\Mahendran K\.gemini\antigravity\brain\286be14e-9558-4fc1-b5d3-e5e458ba4ddc"
url = "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/pricing.html?unlocked=1"
out_full = os.path.join(artifact_dir, "pricing_emp_count_clean.png")

subprocess.run([
    chrome_path, "--headless=new", f"--screenshot={out_full}",
    "--window-size=1280,4500", "--hide-scrollbars", url
], check=True)

im = Image.open(out_full)
crop_hrms = im.crop((50, 750, 1230, 1800))
crop_hrms_path = os.path.join(artifact_dir, "crop_grohrms_emp_count_final.png")
crop_hrms.save(crop_hrms_path)
print("Saved final crop screenshot:", crop_hrms_path)

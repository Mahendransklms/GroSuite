import re
import subprocess
import os
from PIL import Image

# 1. Update css/style.css to include .pricing-card__employee-count
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

emp_css = """.pricing-card__employee-count {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.84rem;
  font-weight: 600;
  color: #38bdf8;
  background: rgba(56, 189, 248, 0.08);
  border: 1px solid rgba(56, 189, 248, 0.22);
  border-radius: 8px;
  padding: 0.45rem 0.75rem;
  margin-top: -0.35rem;
  margin-bottom: 1.25rem;
  line-height: 1.3;
}
.pricing-card__employee-count svg {
  flex-shrink: 0;
  color: #38bdf8;
}
.pricing-card__employee-count strong {
  color: #ffffff;
  font-weight: 700;
}
"""

if '.pricing-card__employee-count' not in css:
    css += "\n" + emp_css
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Added .pricing-card__employee-count to css/style.css!")

# 2. Add employee count in pricing.html under Grohrms billing note
with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define SVG icon
icon_svg = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>'

# Card 1: Basic
emp_box_basic = f'''              <div class="pricing-card__employee-count">
                {icon_svg}
                <span>Employee Count: <strong>Up to 20</strong></span>
              </div>'''

# Card 2: Standard
emp_box_standard = f'''              <div class="pricing-card__employee-count">
                {icon_svg}
                <span>Employee Count: <strong>Up to 60</strong></span>
              </div>'''

# Card 3: Prime
emp_box_prime = f'''              <div class="pricing-card__employee-count">
                {icon_svg}
                <span>Employee Count: <strong>Up to 120</strong></span>
              </div>'''

# Card 4: Custom
emp_box_custom = f'''              <div class="pricing-card__employee-count">
                {icon_svg}
                <span>Employee Count: <strong>120+ / Custom</strong></span>
              </div>'''

# Insert after cardNoteBasic
html = re.sub(
    r'(<p class="pricing-card__billing-note" id="cardNoteBasic"[^>]*>.*?</p>)',
    r'\g<1>\n' + emp_box_basic,
    html
)

# Insert after cardNoteStandard
html = re.sub(
    r'(<p class="pricing-card__billing-note" id="cardNoteStandard"[^>]*>.*?</p>)',
    r'\g<1>\n' + emp_box_standard,
    html
)

# Insert after cardNotePrime
html = re.sub(
    r'(<p class="pricing-card__billing-note" id="cardNotePrime"[^>]*>.*?</p>)',
    r'\g<1>\n' + emp_box_prime,
    html
)

# Insert after card 4 billing note in grohrms
grohrms_idx = html.find('id="grohrms-pricing"')
grohrms_end = html.find('id="grolog-pricing"')
grohrms_text = html[grohrms_idx:grohrms_end]

card4_note_pattern = r'(<div class="pricing-card__price-box pricing-card__price-box--quote">\s*<span class="pricing-card__amount pricing-card__amount--quote">Client Requirement</span>\s*</div>\s*<p class="pricing-card__billing-note">Tailored project scope &amp; milestones</p>)'
assert re.search(card4_note_pattern, grohrms_text), "Card 4 note not found in grohrms!"

grohrms_text_new = re.sub(
    card4_note_pattern,
    r'\g<1>\n' + emp_box_custom,
    grohrms_text
)

html = html[:grohrms_idx] + grohrms_text_new + html[grohrms_end:]

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated pricing.html with employee counts!")

# 3. Capture screenshot
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\Mahendran K\.gemini\antigravity\brain\286be14e-9558-4fc1-b5d3-e5e458ba4ddc"

url = "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/pricing.html?unlocked=1"
out_full = os.path.join(artifact_dir, "pricing_emp_count_full.png")

subprocess.run([
    chrome_path, "--headless=new", f"--screenshot={out_full}",
    "--window-size=1280,4500", "--hide-scrollbars", url
], check=True)

im = Image.open(out_full)
crop_hrms = im.crop((50, 750, 1230, 1800))
crop_hrms_path = os.path.join(artifact_dir, "crop_grohrms_emp_count.png")
crop_hrms.save(crop_hrms_path)
print("Saved crop:", crop_hrms_path)

import subprocess
import os
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\Mahendran K\.gemini\antigravity\brain\286be14e-9558-4fc1-b5d3-e5e458ba4ddc"

with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

step2_test_html = html.replace('id="pricingStep1Block" class="pricing-step-container"', 'id="pricingStep1Block" class="pricing-step-container" style="display: none;"')
step2_test_html = step2_test_html.replace('id="pricingStep2Block" class="pricing-step-container" style="display: none;"', 'id="pricingStep2Block" class="pricing-step-container" style="display: block;"')
step2_test_html = step2_test_html.replace('id="stepIndicator1" class="pricing-step-item active"', 'id="stepIndicator1" class="pricing-step-item completed"')
step2_test_html = step2_test_html.replace('id="stepIndicator2" class="pricing-step-item"', 'id="stepIndicator2" class="pricing-step-item active"')
step2_test_html = step2_test_html.replace('id="circleStep1">1<', 'id="circleStep1">✓<')
step2_test_html = step2_test_html.replace('id="stepLine1" class="pricing-step-line"', 'id="stepLine1" class="pricing-step-line completed"')

with open('temp_step2_test.html', 'w', encoding='utf-8') as f:
    f.write(step2_test_html)

url_step2 = "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/temp_step2_test.html"
out_step2 = os.path.join(artifact_dir, "pricing_step2_full_card.png")

subprocess.run([
    chrome_path, "--headless=new", f"--screenshot={out_step2}",
    "--window-size=1280,1400", "--hide-scrollbars", url_step2
], check=True)

im = Image.open(out_step2)
crop_full = im.crop((120, 520, 1160, 1340))
crop_full.save(os.path.join(artifact_dir, "crop_step2_full_form.png"))
print("Saved full Step 2 form crop!")

if os.path.exists('temp_step2_test.html'):
    os.remove('temp_step2_test.html')

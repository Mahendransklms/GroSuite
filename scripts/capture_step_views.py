import subprocess
import os
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\Mahendran K\.gemini\antigravity\brain\286be14e-9558-4fc1-b5d3-e5e458ba4ddc"

# 1. Capture Step 1 (Default Gate view)
url_step1 = "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/pricing.html"
out_step1 = os.path.join(artifact_dir, "pricing_step1_raw.png")

subprocess.run([
    chrome_path, "--headless=new", f"--screenshot={out_step1}",
    "--window-size=1280,1000", "--hide-scrollbars", url_step1
], check=True)

# Crop Step 1 Card
im = Image.open(out_step1)
# Header + Gate card area
crop_step1 = im.crop((0, 0, 1280, 850))
crop_step1.save(os.path.join(artifact_dir, "crop_pricing_step1.png"))
print("Captured and cropped Step 1 view!")

# 2. Check if we can create a temporary file or check Step 2 view
# Create a test view where Step 2 is active
with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make step 2 active initially for screenshot verification
step2_test_html = html.replace('id="pricingStep1Block" class="pricing-step-container"', 'id="pricingStep1Block" class="pricing-step-container" style="display: none;"')
step2_test_html = step2_test_html.replace('id="pricingStep2Block" class="pricing-step-container" style="display: none;"', 'id="pricingStep2Block" class="pricing-step-container" style="display: block;"')
step2_test_html = step2_test_html.replace('id="stepIndicator1" class="pricing-step-item active"', 'id="stepIndicator1" class="pricing-step-item completed"')
step2_test_html = step2_test_html.replace('id="stepIndicator2" class="pricing-step-item"', 'id="stepIndicator2" class="pricing-step-item active"')
step2_test_html = step2_test_html.replace('id="circleStep1">1<', 'id="circleStep1">✓<')
step2_test_html = step2_test_html.replace('id="stepLine1" class="pricing-step-line"', 'id="stepLine1" class="pricing-step-line completed"')

with open('temp_step2_test.html', 'w', encoding='utf-8') as f:
    f.write(step2_test_html)

url_step2 = "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/temp_step2_test.html"
out_step2 = os.path.join(artifact_dir, "pricing_step2_raw.png")

subprocess.run([
    chrome_path, "--headless=new", f"--screenshot={out_step2}",
    "--window-size=1280,1100", "--hide-scrollbars", url_step2
], check=True)

im2 = Image.open(out_step2)
crop_step2 = im2.crop((0, 0, 1280, 950))
crop_step2.save(os.path.join(artifact_dir, "crop_pricing_step2.png"))
print("Captured and cropped Step 2 view!")

if os.path.exists('temp_step2_test.html'):
    os.remove('temp_step2_test.html')

import re
import subprocess
import os
from PIL import Image

# Read css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update .pricing-card__amount color to #38bdf8 !important
# Also update .pricing-card__amount--quote
# And let's see about .pricing-card__currency: let's set .pricing-card__currency to #38bdf8 as well, or #38bdf8 for amount and currency!
css_updated = re.sub(
    r'\.pricing-card__currency\s*\{([^}]*?)color:[^;!]+(!important)?;\s*',
    r'.pricing-card__currency {\1color: #38bdf8 !important; ',
    css
)

css_updated = re.sub(
    r'\.pricing-card__amount\s*\{([^}]*?)color:[^;!]+(!important)?;\s*',
    r'.pricing-card__amount {\1color: #38bdf8 !important; ',
    css_updated
)

css_updated = re.sub(
    r'\.pricing-card__amount--quote\s*\{([^}]*?)color:[^;!]+(!important)?;\s*',
    r'.pricing-card__amount--quote {\1color: #38bdf8 !important; ',
    css_updated
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_updated)

print("Updated style.css with #38bdf8 for amount & currency!")

# Capture screenshot
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\Mahendran K\.gemini\antigravity\brain\286be14e-9558-4fc1-b5d3-e5e458ba4ddc"
url = "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/pricing.html?unlocked=1"
out_full = os.path.join(artifact_dir, "pricing_color_test_full.png")

subprocess.run([
    chrome_path,
    "--headless=new",
    f"--screenshot={out_full}",
    "--window-size=1280,5000",
    "--hide-scrollbars",
    url
], check=True)

im = Image.open(out_full)

# Crop Groinn cards
crop_groinn = im.crop((50, 2700, 1230, 3750))
crop_groinn_path = os.path.join(artifact_dir, "crop_color_test_groinn.png")
crop_groinn.save(crop_groinn_path)

# Crop Grolog cards
crop_grolog = im.crop((50, 1850, 1230, 2750))
crop_grolog_path = os.path.join(artifact_dir, "crop_color_test_grolog.png")
crop_grolog.save(crop_grolog_path)

print("Screenshots saved successfully!")

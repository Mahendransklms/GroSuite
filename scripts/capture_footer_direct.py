import subprocess
import os
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\Mahendran K\.gemini\antigravity\brain\286be14e-9558-4fc1-b5d3-e5e458ba4ddc"

# We can capture a page like partnership.html or enquire.html which is shorter, or pricing.html with window-size=1280,10000
out_pricing = os.path.join(artifact_dir, "pricing_full_10k.png")
subprocess.run([
    chrome_path,
    "--headless=new",
    f"--screenshot={out_pricing}",
    "--window-size=1280,8500",
    "--hide-scrollbars",
    "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/pricing.html?unlocked=1"
], check=True)

# Also capture a concise page like partnership.html
out_part = os.path.join(artifact_dir, "partnership_full.png")
subprocess.run([
    chrome_path,
    "--headless=new",
    f"--screenshot={out_part}",
    "--window-size=1280,4500",
    "--hide-scrollbars",
    "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/partnership.html"
], check=True)

im_p = Image.open(out_pricing)
# Let's find where footer is by cropping the bottom 1200px of pricing
crop_p_bottom = im_p.crop((0, im_p.height - 1200, im_p.width, im_p.height))
crop_p_bottom.save(os.path.join(artifact_dir, "crop_pricing_bottom.png"))

im_part = Image.open(out_part)
crop_part_bottom = im_part.crop((0, im_part.height - 1200, im_part.width, im_part.height))
crop_part_bottom.save(os.path.join(artifact_dir, "crop_part_bottom.png"))

print("Captured!")

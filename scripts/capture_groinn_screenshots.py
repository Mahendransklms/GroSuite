import subprocess
import os
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\Mahendran K\.gemini\antigravity\brain\286be14e-9558-4fc1-b5d3-e5e458ba4ddc"

# 1. Capture Monthly Screenshot
url_monthly = "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/pricing.html?unlocked=1"
out_monthly = os.path.join(artifact_dir, "pricing_verify_monthly.png")
subprocess.run([
    chrome_path,
    "--headless=new",
    f"--screenshot={out_monthly}",
    "--window-size=1280,5500",
    "--hide-scrollbars",
    url_monthly
], check=True)

# 2. Capture Annual Screenshot
url_annual = "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/pricing.html?billing=annual"
out_annual = os.path.join(artifact_dir, "pricing_verify_annual.png")
subprocess.run([
    chrome_path,
    "--headless=new",
    f"--screenshot={out_annual}",
    "--window-size=1280,5500",
    "--hide-scrollbars",
    url_annual
], check=True)

print("Screenshots captured successfully.")

im_m = Image.open(out_monthly)
im_a = Image.open(out_annual)
print(f"Image dimensions: {im_a.size}")

# Groinn cards: let's crop from y=1900 to bottom of Groinn (approx 3400)
crop_m_groinn = im_m.crop((60, 1900, 1220, 3400))
crop_m_groinn.save(os.path.join(artifact_dir, "crop_groinn_new_monthly.png"))

crop_a_groinn = im_a.crop((60, 1900, 1220, 3400))
crop_a_groinn.save(os.path.join(artifact_dir, "crop_groinn_new_annual.png"))

print("Cropped Groinn screenshots generated successfully!")

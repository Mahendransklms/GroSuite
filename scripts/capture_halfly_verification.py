import subprocess
import os
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\Mahendran K\.gemini\antigravity\brain\286be14e-9558-4fc1-b5d3-e5e458ba4ddc"

# 1. Capture Grohrms Monthly
url_monthly = "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/pricing.html?unlocked=1"
out_monthly = os.path.join(artifact_dir, "pricing_grohrms_monthly.png")
subprocess.run([
    chrome_path, "--headless=new", f"--screenshot={out_monthly}",
    "--window-size=1280,4500", "--hide-scrollbars", url_monthly
], check=True)
im_m = Image.open(out_monthly)
crop_m = im_m.crop((50, 750, 1230, 1750))
crop_m.save(os.path.join(artifact_dir, "crop_grohrms_monthly_3btn.png"))
print("Saved Grohrms Monthly screenshot")

# 2. Capture Grohrms Halfly
url_halfly = "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/pricing.html?unlocked=1&billing=halfly"
out_halfly = os.path.join(artifact_dir, "pricing_grohrms_halfly.png")
subprocess.run([
    chrome_path, "--headless=new", f"--screenshot={out_halfly}",
    "--window-size=1280,4500", "--hide-scrollbars", url_halfly
], check=True)
im_h = Image.open(out_halfly)
crop_h = im_h.crop((50, 750, 1230, 1750))
crop_h.save(os.path.join(artifact_dir, "crop_grohrms_halfly_active.png"))
print("Saved Grohrms Halfly screenshot")

# 3. Capture Grohrms Annually
url_annual = "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/pricing.html?unlocked=1&billing=annual"
out_annual = os.path.join(artifact_dir, "pricing_grohrms_annual.png")
subprocess.run([
    chrome_path, "--headless=new", f"--screenshot={out_annual}",
    "--window-size=1280,4500", "--hide-scrollbars", url_annual
], check=True)
im_a = Image.open(out_annual)
crop_a = im_a.crop((50, 750, 1230, 1750))
crop_a.save(os.path.join(artifact_dir, "crop_grohrms_annual_3btn.png"))
print("Saved Grohrms Annually screenshot")

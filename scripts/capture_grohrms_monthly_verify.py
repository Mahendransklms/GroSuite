import subprocess
import os
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\Mahendran K\.gemini\antigravity\brain\286be14e-9558-4fc1-b5d3-e5e458ba4ddc"

# 1. Capture Grohrms Monthly view (default on load)
url_monthly = "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/pricing.html?unlocked=1"
out_monthly = os.path.join(artifact_dir, "pricing_grohrms_monthly_full.png")

subprocess.run([
    chrome_path,
    "--headless=new",
    f"--screenshot={out_monthly}",
    "--window-size=1280,5000",
    "--hide-scrollbars",
    url_monthly
], check=True)

im_m = Image.open(out_monthly)

# Crop Grohrms Monthly
crop_hrms_m = im_m.crop((50, 750, 1230, 1750))
crop_hrms_m_path = os.path.join(artifact_dir, "crop_hrms_monthly_active.png")
crop_hrms_m.save(crop_hrms_m_path)
print("Saved Grohrms Monthly crop:", crop_hrms_m_path)

# Crop Grolog
crop_grolog = im_m.crop((50, 1750, 1230, 2650))
crop_grolog_path = os.path.join(artifact_dir, "crop_grolog_verify_noswitcher.png")
crop_grolog.save(crop_grolog_path)
print("Saved Grolog crop:", crop_grolog_path)

# Crop Groinn
crop_groinn = im_m.crop((50, 2650, 1230, 3650))
crop_groinn_path = os.path.join(artifact_dir, "crop_groinn_verify_noswitcher.png")
crop_groinn.save(crop_groinn_path)
print("Saved Groinn crop:", crop_groinn_path)

# 2. Capture Grohrms Annual view
url_annual = "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/pricing.html?unlocked=1&billing=annual"
out_annual = os.path.join(artifact_dir, "pricing_grohrms_annual_full.png")

subprocess.run([
    chrome_path,
    "--headless=new",
    f"--screenshot={out_annual}",
    "--window-size=1280,5000",
    "--hide-scrollbars",
    url_annual
], check=True)

im_a = Image.open(out_annual)
crop_hrms_a = im_a.crop((50, 750, 1230, 1750))
crop_hrms_a_path = os.path.join(artifact_dir, "crop_hrms_annual_active.png")
crop_hrms_a.save(crop_hrms_a_path)
print("Saved Grohrms Annual crop:", crop_hrms_a_path)

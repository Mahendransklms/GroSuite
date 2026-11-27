import subprocess
import os
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\Mahendran K\.gemini\antigravity\brain\286be14e-9558-4fc1-b5d3-e5e458ba4ddc"

url = "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/pricing.html?unlocked=1"
out_full = os.path.join(artifact_dir, "pricing_verify_updated_full.png")

subprocess.run([
    chrome_path,
    "--headless=new",
    f"--screenshot={out_full}",
    "--window-size=1280,5000",
    "--hide-scrollbars",
    url
], check=True)

print("Full screenshot captured:", out_full)

im = Image.open(out_full)
print("Image dimensions:", im.size)

# Crop sections:
# Grohrms: around y=200 to 1100
crop_hrms = im.crop((50, 200, 1230, 1100))
crop_hrms_path = os.path.join(artifact_dir, "crop_hrms_annual_only.png")
crop_hrms.save(crop_hrms_path)
print("Saved Grohrms crop:", crop_hrms_path)

# Grolog: around y=1050 to 1950
crop_grolog = im.crop((50, 1050, 1230, 1950))
crop_grolog_path = os.path.join(artifact_dir, "crop_grolog_annual_only.png")
crop_grolog.save(crop_grolog_path)
print("Saved Grolog crop:", crop_grolog_path)

# Groinn: around y=1900 to 2950
crop_groinn = im.crop((50, 1900, 1230, 2950))
crop_groinn_path = os.path.join(artifact_dir, "crop_groinn_annual_only.png")
crop_groinn.save(crop_groinn_path)
print("Saved Groinn crop:", crop_groinn_path)

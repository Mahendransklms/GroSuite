import subprocess
import os
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\Mahendran K\.gemini\antigravity\brain\286be14e-9558-4fc1-b5d3-e5e458ba4ddc"

# 1. Capture Grolog Annual (default)
url_annual = "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/pricing.html?unlocked=1"
out_annual = os.path.join(artifact_dir, "pricing_grolog_annual_view.png")

subprocess.run([
    chrome_path, "--headless=new", f"--screenshot={out_annual}",
    "--window-size=1280,5000", "--hide-scrollbars", url_annual
], check=True)

im_a = Image.open(out_annual)
crop_grolog_a = im_a.crop((50, 1850, 1230, 2850))
crop_grolog_a.save(os.path.join(artifact_dir, "crop_grolog_annual_view.png"))
print("Saved Grolog Annual screenshot")

# Crop Groinn to confirm no switcher
crop_groinn = im_a.crop((50, 3100, 1230, 4100))
crop_groinn.save(os.path.join(artifact_dir, "crop_groinn_still_noswitcher.png"))
print("Saved Groinn screenshot")

# 2. Capture Grolog Halfly
url_halfly = "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/pricing.html?unlocked=1&billing=halfly"
out_halfly = os.path.join(artifact_dir, "pricing_grolog_halfly_view.png")

subprocess.run([
    chrome_path, "--headless=new", f"--screenshot={out_halfly}",
    "--window-size=1280,5000", "--hide-scrollbars", url_halfly
], check=True)

im_h = Image.open(out_halfly)
crop_grolog_h = im_h.crop((50, 1850, 1230, 2850))
crop_grolog_h.save(os.path.join(artifact_dir, "crop_grolog_halfly_view.png"))
print("Saved Grolog Halfly screenshot")

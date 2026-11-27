import subprocess
import os
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\Mahendran K\.gemini\antigravity\brain\286be14e-9558-4fc1-b5d3-e5e458ba4ddc"

# 1. Capture pricing.html full page
out_pricing = os.path.join(artifact_dir, "footer_verify_pricing_full.png")
subprocess.run([
    chrome_path,
    "--headless=new",
    f"--screenshot={out_pricing}",
    "--window-size=1280,6000",
    "--hide-scrollbars",
    "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/pricing.html?unlocked=1"
], check=True)

# 2. Capture index.html full page
out_index = os.path.join(artifact_dir, "footer_verify_index_full.png")
subprocess.run([
    chrome_path,
    "--headless=new",
    f"--screenshot={out_index}",
    "--window-size=1280,6000",
    "--hide-scrollbars",
    "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/index.html"
], check=True)

print("Screenshots captured.")

# Crop the footer region from pricing.html
im_p = Image.open(out_pricing)
w, h = im_p.size
print("Pricing size:", w, h)
crop_p_footer = im_p.crop((0, h - 850, w, h))
crop_p_footer.save(os.path.join(artifact_dir, "crop_footer_pricing.png"))

# Crop the footer region from index.html
im_i = Image.open(out_index)
wi, hi = im_i.size
print("Index size:", wi, hi)
crop_i_footer = im_i.crop((0, hi - 850, wi, hi))
crop_i_footer.save(os.path.join(artifact_dir, "crop_footer_index.png"))

print("Cropped footer screenshots generated successfully!")

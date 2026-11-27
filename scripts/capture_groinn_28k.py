import subprocess
import os
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifact_dir = r"C:\Users\Mahendran K\.gemini\antigravity\brain\286be14e-9558-4fc1-b5d3-e5e458ba4ddc"

url = "file:///C:/Users/Mahendran%20K/OneDrive/Documents/GitHub/GroSuite/pricing.html?unlocked=1"
out_path = os.path.join(artifact_dir, "pricing_groinn_28k_full.png")

subprocess.run([
    chrome_path, "--headless=new", f"--screenshot={out_path}",
    "--window-size=1280,4500", "--hide-scrollbars", url
], check=True)

im = Image.open(out_path)
crop_groinn = im.crop((50, 2600, 1230, 3600))
crop_groinn_path = os.path.join(artifact_dir, "crop_groinn_28k.png")
crop_groinn.save(crop_groinn_path)
print("Saved Groinn crop:", crop_groinn_path)

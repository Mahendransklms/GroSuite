import os
from PIL import Image

artifact_dir = r"C:\Users\Mahendran K\.gemini\antigravity\brain\286be14e-9558-4fc1-b5d3-e5e458ba4ddc"
out_full = os.path.join(artifact_dir, "pricing_color_test_full.png")

im = Image.open(out_full)

# Grohrms is around y=950 to 1850
crop_hrms = im.crop((50, 950, 1230, 1850))
crop_hrms_path = os.path.join(artifact_dir, "crop_color_test_hrms.png")
crop_hrms.save(crop_hrms_path)
print("Saved Grohrms crop:", crop_hrms_path)

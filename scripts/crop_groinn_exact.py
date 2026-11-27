import os
from PIL import Image

artifact_dir = r"C:\Users\Mahendran K\.gemini\antigravity\brain\286be14e-9558-4fc1-b5d3-e5e458ba4ddc"
out_full = os.path.join(artifact_dir, "pricing_verify_updated_full.png")

im = Image.open(out_full)
print("Image dimensions:", im.size)

# Groinn is below Grolog: around y=2700 to 3700
crop_groinn_actual = im.crop((50, 2700, 1230, 3750))
crop_groinn_actual_path = os.path.join(artifact_dir, "crop_groinn_exact.png")
crop_groinn_actual.save(crop_groinn_actual_path)
print("Saved Groinn crop:", crop_groinn_actual_path)

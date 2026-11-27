import os
from PIL import Image

artifact_dir = r"C:\Users\Mahendran K\.gemini\antigravity\brain\286be14e-9558-4fc1-b5d3-e5e458ba4ddc"
out_path = os.path.join(artifact_dir, "pricing_groinn_28k_full.png")

im = Image.open(out_path)
crop_groinn = im.crop((50, 3100, 1230, 3950))
crop_groinn_path = os.path.join(artifact_dir, "crop_groinn_28k_visible.png")
crop_groinn.save(crop_groinn_path)
print("Saved Groinn visible crop:", crop_groinn_path)

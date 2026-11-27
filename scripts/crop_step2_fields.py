from PIL import Image
import os

artifact_dir = r"C:\Users\Mahendran K\.gemini\antigravity\brain\286be14e-9558-4fc1-b5d3-e5e458ba4ddc"
im = Image.open(os.path.join(artifact_dir, "pricing_step2_raw.png"))

# Crop the full card
crop_full_card = im.crop((120, 520, 1160, 1100))
crop_full_card.save(os.path.join(artifact_dir, "crop_step2_card_fields.png"))
print("Saved Step 2 card fields crop!")

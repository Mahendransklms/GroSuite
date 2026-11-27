import os, subprocess
from PIL import Image

artifact_dir = r"C:\Users\Mahendran K\.gemini\antigravity\brain\286be14e-9558-4fc1-b5d3-e5e458ba4ddc"

with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make details container visible
base_preview = html.replace(
    'id="pricingDetailsContainer" class="pricing-details-container" style="display: none;"',
    'id="pricingDetailsContainer" class="pricing-details-container" style="display: block;"'
)

# 1. Monthly (Default on load)
with open('preview_monthly.html', 'w', encoding='utf-8') as f:
    f.write(base_preview)

# 2. Annually (Trigger annual clicks on load)
annual_script = """<script>
  window.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
      const bH = document.getElementById('btnAnnualGrohrms');
      const bL = document.getElementById('btnAnnualGrolog');
      const bI = document.getElementById('btnAnnualGroinn');
      if (bH) bH.click();
      if (bL) bL.click();
      if (bI) bI.click();
    }, 50);
  });
</script></body>"""

annual_html = base_preview.replace('</body>', annual_script)

with open('preview_annual.html', 'w', encoding='utf-8') as f:
    f.write(annual_html)

chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Capture Monthly
img_monthly_path = os.path.join(artifact_dir, "pricing_preview_monthly.png")
subprocess.run([
    chrome_exe,
    '--headless=new', '--disable-gpu', '--no-sandbox',
    '--window-size=1280,4500',
    '--screenshot=' + img_monthly_path,
    'file:///' + os.path.abspath('preview_monthly.html').replace('\\', '/')
], check=True)

# Capture Annual
img_annual_path = os.path.join(artifact_dir, "pricing_preview_annual.png")
subprocess.run([
    chrome_exe,
    '--headless=new', '--disable-gpu', '--no-sandbox',
    '--window-size=1280,4500',
    '--screenshot=' + img_annual_path,
    'file:///' + os.path.abspath('preview_annual.html').replace('\\', '/')
], check=True)

if os.path.exists('preview_monthly.html'):
    os.remove('preview_monthly.html')
if os.path.exists('preview_annual.html'):
    os.remove('preview_annual.html')

im_ann = Image.open(img_annual_path)
im_mon = Image.open(img_monthly_path)
print("Image dimensions:", im_ann.size)

# Find coordinates for grohrms and grolog cards
# Grohrms cards typically appear between Y=500 and 1300
im_ann.crop((100, 500, 1180, 1200)).save(os.path.join(artifact_dir, "crop_grohrms_annual_strikethrough.png"))
im_mon.crop((100, 500, 1180, 1200)).save(os.path.join(artifact_dir, "crop_grohrms_monthly.png"))

# Grolog cards appear between Y=1600 and 2400
im_ann.crop((100, 1600, 1180, 2350)).save(os.path.join(artifact_dir, "crop_grolog_annual_strikethrough.png"))
im_mon.crop((100, 1600, 1180, 2350)).save(os.path.join(artifact_dir, "crop_grolog_monthly.png"))

print("Cropped comparison screenshots generated successfully!")

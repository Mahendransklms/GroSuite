with open('pricing.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("=== GROHRMS CARDS PRICE BOXES ===")
for i in range(400, 600):
    if 'pricing-card__price-box' in lines[i] or 'pricing-card__billing-note' in lines[i]:
        print(f"L{i+1}: " + "".join(lines[i:i+12]))

print("\n=== GROLOG CARDS PRICE BOXES ===")
for i in range(690, 950):
    if 'pricing-card__price-box' in lines[i] or 'pricing-card__billing-note' in lines[i]:
        print(f"L{i+1}: " + "".join(lines[i:i+12]))

print("\n=== GROINN CARDS PRICE BOXES ===")
for i in range(990, 1300):
    if 'pricing-card__price-box' in lines[i] or 'pricing-card__billing-note' in lines[i]:
        print(f"L{i+1}: " + "".join(lines[i:i+12]))

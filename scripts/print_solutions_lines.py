with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="solutions"' in line:
        for j in range(i, min(i+120, len(lines))):
            print(f"{j+1}: {lines[j].strip()}")
        break

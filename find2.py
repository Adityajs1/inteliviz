with open('site3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'cx="9.5"' in line or 'cards-grid' in line:
        print(f'{i+1}: {line.strip()[:100]}')

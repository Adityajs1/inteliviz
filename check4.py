with open('site3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start = -1
for i, line in enumerate(lines):
    if '<div class="cards-grid">' in line:
        start = i
        break

if start != -1:
    print(''.join(lines[start:start+40]))

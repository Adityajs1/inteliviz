import re
with open('site3.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'<div class="cards-grid">.*?</section>', content, re.DOTALL)
if m:
    print(m.group(0)[:500])
    cards = re.findall(r'<h3 class="card-title">(.*?)</h3>', m.group(0))
    print('Cards:', cards)
else:
    print('Not found')

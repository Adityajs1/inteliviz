import re
with open('site3.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'<div class="cards-grid">.*?</section>', content, re.DOTALL)
if m:
    cards = re.findall(r'(<div class="feature-card">.*?</div>)', m.group(0), re.DOTALL)
    for i, c in enumerate(cards):
        print(f"Card {i}:")
        print(c[:150])
        print("...")

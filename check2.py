import re
with open('site3.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'<div class="cards-grid">.*?</section>', content, re.DOTALL)
if m:
    cards = re.findall(r'(<div class="feature-card">.*?</div>\n\s*)', m.group(0), re.DOTALL)
    print('Num feature-card blocks:', len(cards))
    if len(cards) == 0:
        # try without trailing whitespace
        cards = re.findall(r'<div class="feature-card">.*?</div>', m.group(0), re.DOTALL)
        print('Num feature-card blocks (no trailing spaces):', len(cards))

    titles = re.findall(r'<h3 class="card-title">(.*?)</h3>', m.group(0))
    print('Titles:', titles)

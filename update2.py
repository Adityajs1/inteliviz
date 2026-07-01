import re

def main():
    with open('site3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update font to Inter
    content = re.sub(
        r"--font-display: 'Syne', sans-serif;",
        r"--font-display: 'Inter', sans-serif;",
        content
    )

    # 2. Update feature-card background
    content = re.sub(
        r"background: linear-gradient\(180deg, rgba\(30, 30, 30, 0\.4\) 0%, rgba\(15, 15, 15, 0\.8\) 100%\);",
        r"background: #0C0C0C;",
        content
    )

    # 3 & 4. Swap cards and update section to Content
    old_section = re.search(r'(<!-- CONTENT FOCUS CARDS -->.*?<!-- SERVICES -->)', content, re.DOTALL)
    if old_section:
        section_text = old_section.group(1)
        
        # Add eyebrow and change id
        section_text = section_text.replace(
            '<section id="content-focus" style="padding-top: 64px; padding-bottom: 64px;">',
            '''<section id="content" style="padding-top: 64px; padding-bottom: 64px;">
  <div class="eyebrow" style="justify-content:center">
    <div class="eyebrow-line"></div>
    <span class="eyebrow-text">Content</span>
    <div class="eyebrow-line"></div>
  </div>'''
        )

        # Extract the cards
        cards = re.findall(r'(<div class="feature-card">.*?</div>\n    )', section_text, re.DOTALL)
        if len(cards) >= 4:
            # cards[1] is Value-Driven, cards[3] is AI Relevant
            # Swap them
            temp = cards[1]
            cards[1] = cards[3]
            cards[3] = temp

            # Reconstruct the cards-grid
            new_cards_grid = '<div class="cards-grid">\n    ' + ''.join(cards) + '</div>\n</section>\n\n<!-- SERVICES -->'
            section_text = re.sub(r'<div class="cards-grid">.*?</section>\n\n<!-- SERVICES -->', new_cards_grid, section_text, flags=re.DOTALL)
            
            content = content.replace(old_section.group(1), section_text)

    with open('site3.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()

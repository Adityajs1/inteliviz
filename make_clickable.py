import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the <div class="channel-card"> for each and replace it with:
# <div class="channel-card" onclick="window.open('url', '_blank')" style="cursor: pointer;" ...>

# Card 1: artificialintelligence.co (Instagram) - We know it has "400K+" soon after.
# Since regex can be tricky with HTML, let's just find the indexes.

def add_click(html, handle, url, hint=""):
    # Find all channel-cards
    idx = 0
    while True:
        card_start = html.find('<div class="channel-card"', idx)
        if card_start == -1: break
        card_end = html.find('</div>\n      </div>', card_start) # Rough end of card
        if card_end == -1: break
        
        card_html = html[card_start:card_end]
        if handle in card_html and hint in card_html:
            # Inject onclick
            new_div = '<div class="channel-card" onclick="window.open(\'' + url + '\', \'_blank\')" style="cursor: pointer;"'
            new_card_html = card_html.replace('<div class="channel-card"', new_div, 1)
            
            html = html[:card_start] + new_card_html + html[card_end:]
            return html
        idx = card_start + 1
    return html

content = add_click(content, 'artificialintelligence.co', 'https://www.instagram.com/artificialintelligence.co/', hint='400K+')
content = add_click(content, 'inteliviz', 'https://www.instagram.com/inteliviz/', hint='43K+')
content = add_click(content, 'artificialintelligence.co', 'https://www.facebook.com/profile.php?id=61557410417163', hint='100K+')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added click handlers to channel cards")

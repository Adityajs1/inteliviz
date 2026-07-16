import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the remaining rocket logo(s)
# The rocket logo has alt="rocket"
pattern_rocket = r'<div class="partner-logo-item">.*?alt="rocket".*?</div>'
content = re.sub(pattern_rocket, '', content, flags=re.DOTALL)

# Increase size of the Adobe Firefly logo (which was the second one)
# It currently has style="transform: scale(1.7);" alt="Adobe Firefly"
# We can just replace scale(1.7) with scale(2.2) for the Adobe Firefly image.
# The exact string from earlier:
# <img style="transform: scale(1.7);"  style="transform: scale(1.7);" ... alt="Adobe Firefly"
# Wait, let's just do a regex replace on the scale for Adobe Firefly.

def firefly_replacer(match):
    text = match.group(0)
    text = text.replace('scale(1.7)', 'scale(2.2)')
    return text

pattern_firefly = r'<div class="partner-logo-item">.*?alt="Adobe Firefly".*?</div>'
content = re.sub(pattern_firefly, firefly_replacer, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modifications done.")

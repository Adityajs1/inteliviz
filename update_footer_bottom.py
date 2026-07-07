import re

with open('site3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace footer-bottom
start_str = '<div class="footer-bottom">'
end_str = '<div class="footer-copy-new">'
start_idx = content.find(start_str)
end_idx = content.find(end_str)
if start_idx != -1 and end_idx != -1:
    new_bottom = '''<div class="footer-bottom" style="display: flex; justify-content: flex-start; border-bottom: none; padding-bottom: 0; margin-bottom: 16px;">
      <div style="font-size: 14px;"><strong style="color: var(--white); font-family: var(--font-display);">Contact:</strong> <a href="mailto:collabaico@gmail.com" style="color: var(--mid); text-decoration: none;">collabaico@gmail.com</a></div>
    </div>
    '''
    content = content[:start_idx] + new_bottom + content[end_idx:]

# 2. Adjust collaboration section spacing
# The section is <section id="partnerships">
content = content.replace('<section id="partnerships">', '<section id="partnerships" style="padding-top: 32px; padding-bottom: 16px;">')

with open('site3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Success')

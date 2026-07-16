import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove text labels from footer-social-links
content = re.sub(r'<span>Instagram</span>', '', content)
content = re.sub(r'<span>Telegram</span>', '', content)
content = re.sub(r'<span>Facebook</span>', '', content)

# 2. Update footer-right-col css
content = content.replace(
    '.footer-right-col {\n      display: flex;\n      flex-direction: column;\n      align-items: flex-start;\n    }',
    '.footer-right-col {\n      display: flex;\n      flex-direction: column;\n      align-items: center;\n    }'
)

# 3. Update footer-social-links justify-content
content = content.replace(
    'justify-content: flex-start;\n      width: 100%;\n      flex-wrap: wrap;\n      margin-bottom: 32px;',
    'justify-content: center;\n      width: 100%;\n      flex-wrap: wrap;\n      margin-bottom: 24px;'
)

# 4. Update the footer-info-blocks HTML that we modified earlier
old_footer_info = """<div class="footer-info-blocks" style="justify-content: flex-end;">
            <div class="footer-info-block" style="align-items: flex-end; text-align: right;">
              <span class="footer-info-label">Email</span>
              <a href="mailto:collabaico@gmail.com" class="footer-info-value">collabaico@gmail.com</a>
            </div>
          </div>"""

new_footer_info = """<div class="footer-info-blocks" style="justify-content: center; margin-bottom: 24px;">
            <div class="footer-info-block" style="align-items: center; text-align: center;">
              <span class="footer-info-label">Email</span>
              <a href="mailto:collabaico@gmail.com" class="footer-info-value">collabaico@gmail.com</a>
            </div>
          </div>"""

content = content.replace(old_footer_info, new_footer_info)

# 5. Ensure the copyright line is centered
content = content.replace(
    '<p class="footer-copy">',
    '<p class="footer-copy" style="text-align: center;">'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated footer alignment")

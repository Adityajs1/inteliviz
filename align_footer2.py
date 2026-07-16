import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the 'Email' label
content = content.replace('<span class="footer-info-label">Email</span>', '')

# 2. Right align social links
content = content.replace(
    'justify-content: center;\n      width: 100%;\n      flex-wrap: wrap;\n      margin-bottom: 24px;',
    'justify-content: flex-end;\n      width: 100%;\n      flex-wrap: wrap;\n      margin-bottom: 24px;'
)

# 3. Right align email info block
old_info_block = """<div class="footer-info-blocks" style="justify-content: center; margin-bottom: 24px;">
            <div class="footer-info-block" style="align-items: center; text-align: center;">
              
              <a href="mailto:collabaico@gmail.com" class="footer-info-value">collabaico@gmail.com</a>
            </div>
          </div>"""

new_info_block = """<div class="footer-info-blocks" style="justify-content: flex-end; width: 100%; margin-bottom: 24px;">
            <div class="footer-info-block" style="align-items: flex-end; text-align: right;">
              <a href="mailto:collabaico@gmail.com" class="footer-info-value">collabaico@gmail.com</a>
            </div>
          </div>"""

# Ensure the label is gone from old block string if the first replace worked
old_info_block_fallback = """<div class="footer-info-blocks" style="justify-content: center; margin-bottom: 24px;">
            <div class="footer-info-block" style="align-items: center; text-align: center;">
              <a href="mailto:collabaico@gmail.com" class="footer-info-value">collabaico@gmail.com</a>
            </div>
          </div>"""

content = content.replace(old_info_block, new_info_block)
content = content.replace(old_info_block_fallback, new_info_block)

# 4. Make sure the right column allows full width stretching
content = content.replace(
    '.footer-right-col {\n      display: flex;\n      flex-direction: column;\n      align-items: center;\n    }',
    '.footer-right-col {\n      display: flex;\n      flex-direction: column;\n      align-items: stretch;\n    }'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied final alignment.")

import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_html = """<div class="footer-info-blocks">
            <div class="footer-info-block">
              <span class="footer-info-label">Email</span>
              <a href="mailto:collabaico@gmail.com" class="footer-info-value">collabaico@gmail.com</a>
            </div>
            <div class="footer-info-block">
              <span class="footer-info-label">Operating Hours</span>
              <span class="footer-info-value">24/7</span>
            </div>
          </div>"""

new_html = """<div class="footer-info-blocks" style="justify-content: flex-end;">
            <div class="footer-info-block" style="align-items: flex-end; text-align: right;">
              <span class="footer-info-label">Email</span>
              <a href="mailto:collabaico@gmail.com" class="footer-info-value">collabaico@gmail.com</a>
            </div>
          </div>"""

content = content.replace(old_html, new_html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated footer layout")

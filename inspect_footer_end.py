import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('<div class="footer-social-links">')
if idx != -1:
    print(content[idx:idx+1500])
else:
    print("Social links not found")

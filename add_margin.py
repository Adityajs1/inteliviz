import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add margin-bottom to the Content heading to restore spacing above cards
content = content.replace('<h2 class="reveal">Content</h2>', '<h2 class="reveal" style="margin-bottom: 40px;">Content</h2>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added margin to Content heading")

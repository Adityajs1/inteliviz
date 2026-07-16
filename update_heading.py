import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Our Services with Content
content = content.replace('<h2 class="reveal">Our Services</h2>', '<h2 class="reveal">Content</h2>')

# Remove the paragraph
p_tag = '<p class="lead reveal" style="max-width: 600px; margin-bottom: 32px;">Delivering high-impact, trend-aware content and visually elite solutions tailored for your success.</p>'
content = content.replace(p_tag, '')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated headings")

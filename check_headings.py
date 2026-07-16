import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find all eyebrows and print the next 200 characters
matches = re.finditer(r'<div class="eyebrow reveal">', content)
for match in matches:
    idx = match.start()
    print("----- EYEBROW -----")
    print(content[idx:idx+300])


import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the specific robust_style from previous script with a fill-container style
old_style = r'style="height: 56px !important; width: auto !important; max-height: none !important; transform: none !important; object-fit: contain !important; flex-shrink: 0 !important;"'
new_style = 'style="height: 100% !important; width: 100% !important; max-height: 100px !important; transform: none !important; object-fit: contain !important; flex-shrink: 0 !important;"'

content = re.sub(old_style, new_style, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated logos to 100% height/width of container.")

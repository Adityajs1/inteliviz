import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace transform: none with transform: scale(1.25) to visually bump them up a bit
old_style = r'style="height: 100% !important; width: 100% !important; max-height: 100px !important; transform: none !important; object-fit: contain !important; flex-shrink: 0 !important;"'
new_style = 'style="height: 100% !important; width: 100% !important; max-height: 100px !important; transform: scale(1.25) !important; object-fit: contain !important; flex-shrink: 0 !important;"'

content = re.sub(old_style, new_style, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Scaled up logos by 1.25x")

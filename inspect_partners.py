import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# find partners-glass
match = re.search(r'<section class="partners-glass">.*?</section>', content, flags=re.DOTALL)
if match:
    print(match.group(0)[:500])
else:
    print("Could not find partners-glass")

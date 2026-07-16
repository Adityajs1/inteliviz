import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# let's just find marquee-wrapper and print 500 chars before it
idx = content.find('<div class="marquee-wrapper">')
if idx != -1:
    print(content[max(0, idx-500):idx])
else:
    print("marquee-wrapper not found")

import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find "artificialintelligence.co" and print the surrounding HTML
idx = content.find('artificialintelligence.co')
if idx != -1:
    print(content[max(0, idx-500):idx+500])
else:
    print("artificialintelligence.co not found")

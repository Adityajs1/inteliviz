import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Rocket
content = content.replace('src="IMG_6456.PNG" alt="rocket" loading="lazy" style="height: 80px; width: auto;"', 
                          'src="IMG_6456.PNG" alt="rocket" loading="lazy" style="transform: scale(4.0);" ')

content = content.replace('src="IMG_6456.PNG" alt="Partner Logo" loading="lazy" style="height: 45px; width: auto;"', 
                          'src="IMG_6456.PNG" alt="rocket" loading="lazy" style="transform: scale(4.0);" ')

# Adobe Firefly
# The previous script might have left it as style="height: 45px; width: auto;"
content = re.sub(r'style="height: 45px; width: auto;"\s+src="data:image/png.*?alt="Adobe Firefly"', 
                 lambda m: m.group(0).replace('style="height: 45px; width: auto;"', 'style="transform: scale(0.9);"'),
                 content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated logos")

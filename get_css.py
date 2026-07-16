import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract styles block
styles = re.findall(r'<style>(.*?)</style>', content, flags=re.DOTALL)
if not styles:
    styles = re.findall(r'<style.*?>.*?</style>', content, flags=re.DOTALL)

for style in styles:
    if 'marquee' in style:
        print("FOUND MARQUEE CSS:")
        for line in style.split('\n'):
            if 'marquee' in line or 'keyframes' in line or 'transform' in line or 'animation' in line:
                print(line)

# Extract scripts
scripts = re.findall(r'<script>(.*?)</script>', content, flags=re.DOTALL)
for script in scripts:
    if 'marquee' in script:
        print("FOUND MARQUEE JS:")
        print(script)

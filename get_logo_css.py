import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

styles = re.findall(r'<style.*?>(.*?)</style>', content, flags=re.DOTALL)
for style in styles:
    if 'partner-logo-item' in style:
        lines = style.split('\n')
        in_block = False
        for line in lines:
            if 'partner-logo-item' in line or in_block:
                print(line)
                in_block = True
                if '}' in line:
                    in_block = False

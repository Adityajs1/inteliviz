import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

styles = re.findall(r'<style>(.*?)</style>', content, flags=re.DOTALL)
css_content = '\n'.join(styles)

# find footer classes
matches = re.findall(r'(\.footer-[^{]+{[^}]+})', css_content)
for match in matches:
    print(match)

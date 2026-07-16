import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

styles = re.findall(r'<style.*?>(.*?)</style>', content, flags=re.DOTALL)
with open('extracted_styles.css', 'w', encoding='utf-8') as out:
    for i, style in enumerate(styles):
        out.write(f"/* Style Block {i+1} */\n")
        out.write(style)
        out.write("\n\n")

print("CSS extracted to extracted_styles.css")

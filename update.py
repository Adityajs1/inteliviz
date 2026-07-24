import re
import os

# Update script.js
with open('script.js', 'r', encoding='utf-8') as f:
    js_content = f.read()
js_content = re.sub(r'const embeddedImages = \{.*?\};\n\ndocument\.querySelectorAll\(\'img\[data-b64-id\]\'\)\.forEach\(img => \{\n    img\.src = embeddedImages\[img\.getAttribute\(\'data-b64-id\'\)\];\n\}\);', '', js_content, flags=re.DOTALL)
with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# Update HTML files
for html_file in ['index.html', 'combined.html']:
    if not os.path.exists(html_file):
        continue
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace src="" data-b64-id="filename" with src="filename"
    html = re.sub(r'src=""\s*data-b64-id="([^"]+)"', r'src="\1"', html)
    html = re.sub(r'src=""\s+data-b64-id="([^"]+)"', r'src="\1"', html)
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {html_file}")

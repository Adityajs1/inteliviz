import re

with open(r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all partner-logo-item divs
pattern = r'<div class="partner-logo-item">.*?</div>'
matches = re.finditer(pattern, content, flags=re.DOTALL)

for i, match in enumerate(matches):
    match_str = match.group(0)
    if 'rocket' in match_str or 'base64' in match_str:
        print(f"Match {i+1}: length {len(match_str)}, contains 'rocket': {'rocket' in match_str}")
        print(match_str[-100:])
        print("---")

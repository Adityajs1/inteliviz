import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find all partner-logo-item divs
pattern = r'(<div class="partner-logo-item">.*?</div>)'

def replacer(match):
    match_str = match.group(1)
    # Check if this is the first rocket logo (we use a global flag)
    global rocket_removed
    if not rocket_removed and 'rocket' in match_str and len(match_str) > 1000000:
        rocket_removed = True
        return '' # Remove it
    return match_str

rocket_removed = False
new_content = re.sub(pattern, replacer, content, count=0, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Rocket removed: {rocket_removed}")

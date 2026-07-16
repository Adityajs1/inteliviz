import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's fix the keyframes for marquee-scroll
# We want to replace whatever is in @keyframes marquee-scroll { ... } with a seamless translation.
# Wait, gap is 72px. The seamless translation is calc(-50% - 36px)

pattern = r'(@keyframes marquee-scroll\s*\{)(.*?)(\})'
# wait, keyframes block has nested braces.
# @keyframes marquee-scroll { from { ... } to { ... } }
pattern = r'(@keyframes marquee-scroll\s*\{)(.*?from.*?to.*?\})(\s*)'

match = re.search(r'@keyframes marquee-scroll\s*\{.*?\}', content, flags=re.DOTALL)
# Actually, since it has nested braces, regex `\{.*?\}` will stop at the first `}` which is end of `from {}`
# Let's do string manipulation
start_idx = content.find('@keyframes marquee-scroll')
if start_idx != -1:
    end_idx = content.find('}', start_idx) # end of from
    end_idx = content.find('}', end_idx + 1) # end of to
    end_idx = content.find('}', end_idx + 1) # end of keyframes
    
    print("Found keyframes block:")
    print(content[start_idx:end_idx+1])
    
    # Replace it!
    new_keyframes = """@keyframes marquee-scroll {
      0% { transform: translateX(0); }
      100% { transform: translateX(calc(-50% - 36px)); }
    }"""
    
    content = content[:start_idx] + new_keyframes + content[end_idx+1:]
    
    # What about @keyframes marquee?
    start_idx2 = content.find('@keyframes marquee {')
    if start_idx2 != -1:
        end_idx2 = content.find('}', start_idx2)
        end_idx2 = content.find('}', end_idx2 + 1)
        end_idx2 = content.find('}', end_idx2 + 1)
        
        new_keyframes2 = """@keyframes marquee {
      0% { transform: translateX(0); }
      100% { transform: translateX(calc(-50% - 36px)); }
    }"""
        content = content[:start_idx2] + new_keyframes2 + content[end_idx2+1:]
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated CSS.")
else:
    print("Not found.")


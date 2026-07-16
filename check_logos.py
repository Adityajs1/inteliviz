import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract marquee-track
track_pattern = r'(<div class="marquee-track" id="marqueeTrack">)(.*?)(</div>\s*</div>\s*</section>)'
match = re.search(track_pattern, content, flags=re.DOTALL)
if match:
    track_content = match.group(2)
    items = re.findall(r'<div class="partner-logo-item">(.*?)</div>', track_content, flags=re.DOTALL)
    
    for i, item in enumerate(items[:4]):
        print(f"--- Item {i+1} ---")
        print(item[:200].replace('\n', ' '))
else:
    print("Could not find marquee-track!")

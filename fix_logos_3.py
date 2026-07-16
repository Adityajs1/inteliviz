import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix CSS
# Remove nth-child(1) scaling
content = re.sub(r'\.partner-logo-item:nth-child\(1\)\s*img\s*\{\s*transform:\s*scale\([^)]+\);\s*\}', '', content, flags=re.DOTALL)
content = re.sub(r'\.partner-logo-item:nth-child\(1\):hover\s*img\s*\{\s*transform:\s*scale\([^)]+\);\s*\}', '', content, flags=re.DOTALL)

# Change max-height: 64px to max-height: 100px in .partner-logo-item img
content = re.sub(r'max-height:\s*64px;', 'max-height: 100px;', content)

# 2. Fix HTML inline styles
# Remove transform: scale(...) and replace with fixed height for Rocket
content = re.sub(r'src="IMG_6456\.PNG" alt="rocket" loading="lazy" style="transform:\s*scale\([\d\.]+\);"\s*', 
                 'src="IMG_6456.PNG" alt="rocket" loading="lazy" style="height: 70px; width: auto;" ', content)
content = re.sub(r'src="IMG_6456\.PNG" alt="Partner Logo" loading="lazy" style="transform:\s*scale\([\d\.]+\);"\s*', 
                 'src="IMG_6456.PNG" alt="rocket" loading="lazy" style="height: 70px; width: auto;" ', content)
content = re.sub(r'src="IMG_6456\.PNG" alt="Partner Logo" loading="lazy" style="height:\s*45px;\s*width:\s*auto;"\s*', 
                 'src="IMG_6456.PNG" alt="rocket" loading="lazy" style="height: 70px; width: auto;" ', content)

# Adobe Firefly
content = re.sub(r'style="transform:\s*scale\([\d\.]+\);"\s*src="data:image/png.*?alt="Adobe Firefly"', 
                 lambda m: m.group(0).replace(re.search(r'style="transform:\s*scale\([\d\.]+\);"', m.group(0)).group(0), 'style="height: 45px; width: auto;"'),
                 content, flags=re.DOTALL)

# Ensure no other transform scales exist on these two logos
# Let's just do a pass to replace any style="transform: scale(0.9);" with style="height: 45px; width: auto;" for Adobe Firefly
content = re.sub(r'style="transform:\s*scale\(0\.9\);"', 'style="height: 45px; width: auto;"', content)

# Ensure track duplicated items are EXACTLY the same
# Re-extract the first 6 items and duplicate them to make sure!
track_pattern = r'(<div class="marquee-track" id="marqueeTrack">)(.*?)(</div>\s*</div>\s*</section>)'
match = re.search(track_pattern, content, flags=re.DOTALL)
if match:
    track_content = match.group(2)
    items = re.findall(r'<div class="partner-logo-item">.*?</div>', track_content, flags=re.DOTALL)
    
    half = len(items) // 2
    set1 = items[:half]
    
    new_track_inner = '\n'.join(set1 + set1)
    content = content[:match.start(2)] + '\n' + new_track_inner + '\n          ' + content[match.end(2):]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS and HTML fixed for uniform sizing.")

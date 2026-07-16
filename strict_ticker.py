import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Ensure Adobe and Rocket have exact size 56px and no transforms.
# Let's strip their inline styles completely, and inject a new class or inline style that is robust.
# We will use style="height: 56px !important; width: auto !important; max-height: none; transform: none !important; object-fit: contain;"

robust_style = 'style="height: 56px !important; width: auto !important; max-height: none !important; transform: none !important; object-fit: contain !important; flex-shrink: 0 !important;"'

# Rocket
content = re.sub(r'src="IMG_6456\.PNG"\s*alt="rocket"\s*loading="lazy"\s*(?:style="[^"]*")?',
                 f'src="IMG_6456.PNG" alt="rocket" loading="lazy" {robust_style}',
                 content)

# Adobe Firefly
content = re.sub(r'(?:style="[^"]*"\s*)?src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABgAAAAQACAYAAAAn[^"]+"\s*alt="Adobe Firefly"\s*loading="lazy"(?:style="[^"]*")?',
                 f'src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABgAAAAQACAYAAAAncZJCAAAAAXNSR0IArs4c6QAAAIRlWElmTU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASg" alt="Adobe Firefly" loading="lazy" {robust_style}',
                 content)

# Actually, the base64 string for Adobe is huge, let's use a simpler regex for Adobe Firefly.
content = re.sub(r'<img[^>]*alt="Adobe Firefly"[^>]*>',
                 lambda m: m.group(0).replace(re.search(r'style="[^"]*"', m.group(0)).group(0) if re.search(r'style="[^"]*"', m.group(0)) else '', '')
                                     .replace('alt="Adobe Firefly"', f'alt="Adobe Firefly" {robust_style}'),
                 content)

content = re.sub(r'<img[^>]*alt="rocket"[^>]*>',
                 lambda m: m.group(0).replace(re.search(r'style="[^"]*"', m.group(0)).group(0) if re.search(r'style="[^"]*"', m.group(0)) else '', '')
                                     .replace('alt="rocket"', f'alt="rocket" {robust_style}'),
                 content)


# 2. Re-duplicate set1 to set2 to ensure absolute identity.
track_pattern = r'(<div class="marquee-track" id="marqueeTrack">)(.*?)(</div>\s*</div>\s*</section>)'
match = re.search(track_pattern, content, flags=re.DOTALL)
if match:
    track_content = match.group(2)
    items = re.findall(r'<div class="partner-logo-item">.*?</div>', track_content, flags=re.DOTALL)
    
    half = len(items) // 2
    set1 = items[:half]
    
    new_track_inner = '\n'.join(set1 + set1)
    content = content[:match.start(2)] + '\n' + new_track_inner + '\n          ' + content[match.end(2):]

# 3. Double check marquee-scroll animation. Ensure it is purely linear.
# We will just force linear on marquee-track.
content = re.sub(r'\.marquee-track\s*\{', '.marquee-track {\n      animation-timing-function: linear !important;', content)

# 4. Remove any rogue transform/scale from .partner-logo-item img
# We already removed nth-child(1) in the previous script. Let's make sure it's not anywhere else.
content = re.sub(r'transform:\s*scale\([^)]+\);', '', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied strict requirements.")

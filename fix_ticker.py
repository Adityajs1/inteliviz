import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract marquee-track
track_pattern = r'(<div class="marquee-track" id="marqueeTrack">)(.*?)(</div>\s*</div>\s*</section>)'
match = re.search(track_pattern, content, flags=re.DOTALL)
if match:
    track_content = match.group(2)
    # track_content contains all the partner-logo-items
    items = re.findall(r'<div class="partner-logo-item">.*?</div>', track_content, flags=re.DOTALL)
    print(f"Total items in marquee track: {len(items)}")
    
    # We should have two identical sets.
    # Let's rebuild the track content.
    # We will take the unique items, add IMG_6456.PNG at the beginning, and duplicate the whole set.
    
    # But wait, there might be exactly 24 items left (we had 26, removed 2 rockets).
    half = len(items) // 2
    set1 = items[:half]
    set2 = items[half:]
    
    print(f"Set 1 length: {len(set1)}, Set 2 length: {len(set2)}")
    
    # Let's create the new item
    new_item = '<div class="partner-logo-item"><img src="IMG_6456.PNG" alt="Partner Logo" loading="lazy" style="height: 45px; width: auto;" /></div>'
    
    # Insert it at the start of set 1
    new_set = [new_item] + set1
    
    # The marquee works by having two identical sets side by side.
    # Make sure we join them without extra spaces that might mess up inline-block gaps, 
    # though usually flexbox is used.
    new_track_inner = '\n'.join(new_set + new_set)
    
    # Replace in file
    new_content = content[:match.start(2)] + '\n' + new_track_inner + '\n          ' + content[match.end(2):]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Rebuilt marquee track successfully.")
else:
    print("Could not find marquee-track!")


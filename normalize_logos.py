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
    
    half = len(items) // 2
    set1 = items[:half]
    
    for i, item in enumerate(set1):
        # find width, height, scale, alt
        scale_match = re.search(r'scale\(([\d\.]+)\)', item)
        scale = scale_match.group(1) if scale_match else 'none'
        
        alt_match = re.search(r'alt="(.*?)"', item)
        alt = alt_match.group(1) if alt_match else 'none'
        
        w_match = re.search(r'width="(\d+)"', item)
        w = w_match.group(1) if w_match else 'none'
        
        h_match = re.search(r'height="(\d+)"', item)
        h = h_match.group(1) if h_match else 'none'
        
        is_svg = '<svg' in item
        
        print(f"Item {i+1}: SVG: {is_svg}, Alt: {alt}, Scale: {scale}, W: {w}, H: {h}")
        # print snippet
        print(item[:150].replace('\n', ' '))


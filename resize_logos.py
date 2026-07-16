import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make IMG_6456.PNG larger (rocket)
# It currently has style="height: 45px; width: auto;"
content = content.replace('src="IMG_6456.PNG" alt="Partner Logo" loading="lazy" style="height: 45px; width: auto;"', 
                          'src="IMG_6456.PNG" alt="rocket" loading="lazy" style="height: 80px; width: auto;"')

# Decrease Adobe Firefly (currently scale(2.2))
# Let's remove the transform: scale(2.2) so it's normal size.
content = content.replace('style="transform: scale(2.2);"  style="transform: scale(2.2);"', 'style="height: 45px; width: auto;"')
content = content.replace('style="transform: scale(2.2);"', 'style="height: 45px; width: auto;"')

# Save
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Logos resized")

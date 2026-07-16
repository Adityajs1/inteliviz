import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The services eyebrow is:
#     <div class="eyebrow reveal">
#       <div class="eyebrow-line"></div><span class="eyebrow-text">SERVICES</span>
#     </div>

# We will inject the h2 and p right after it.
insertion = """
    <h2 class="reveal">Our Services</h2>
    <p class="lead reveal" style="max-width: 600px; margin-bottom: 32px;">Delivering high-impact, trend-aware content and visually elite solutions tailored for your success.</p>
"""

content = re.sub(
    r'(<div class="eyebrow reveal">\s*<div class="eyebrow-line"></div><span class="eyebrow-text">SERVICES</span>\s*</div>)',
    r'\1' + insertion,
    content
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added contents text to Services section")

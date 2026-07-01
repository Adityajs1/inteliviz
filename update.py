import re

def main():
    with open('site3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    new_rocket_logo = '''<svg viewBox="0 0 240 60" width="180" height="45" fill="none">
          <path d="M40 10 Q 55 18 65 48 Q 40 40 15 48 Q 25 18 40 10 Z" fill="#111" stroke="#E0E0E0" stroke-width="2" stroke-linejoin="round"/>
          <text x="75" y="44" font-family="'Syne', sans-serif" font-weight="700" font-size="38" fill="none" stroke="#E0E0E0" stroke-width="1.5">rocket</text>
        </svg>'''

    # Replace the first instance of base64 image (which is the robot logo) with the new SVG
    content = re.sub(r'<img src="data:image/png;base64,[^"]+"[^>]*>', new_rocket_logo, content, count=1)

    with open('site3.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()

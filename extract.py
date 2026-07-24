import json
import base64
import re
import os

with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const embeddedImages = (\{.*?\});\n\ndocument\.querySelectorAll', content, re.DOTALL)
if match:
    obj_str = match.group(1)
    obj_str = re.sub(r',\s*\}', '}', obj_str) # Fix trailing comma
    try:
        images = json.loads(obj_str)
        for name, data_uri in images.items():
            if "," in data_uri:
                b64_data = data_uri.split(',', 1)[1]
                image_data = base64.b64decode(b64_data)
                with open(name, 'wb') as out_f:
                    out_f.write(image_data)
                print(f"Saved {name}")
    except Exception as e:
        print(f"Error parsing json: {e}")
else:
    print("Could not find embeddedImages object")

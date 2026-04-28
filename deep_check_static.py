import os
import re

STATIC_DIR = 'static'
CODE_DIRS = ['templates', 'vynzora_app', 'vynzora_pro', 'static/assets/css', 'static/assets/js']

# Get all files in the codebase
code_files = []
for d in CODE_DIRS:
    for root, _, files in os.walk(d):
        for f in files:
            if f.endswith(('.html', '.py', '.css', '.js')):
                code_files.append(os.path.join(root, f))

# Read all contents
code_contents = ""
for f in code_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            code_contents += file.read() + "\n"
    except Exception:
        pass

static_files = []
for root, _, files in os.walk(STATIC_DIR):
    if 'scss' in root:
        continue
    for f in files:
        if f == '.DS_Store':
            continue
        filepath = os.path.join(root, f)
        rel_path = os.path.relpath(filepath, STATIC_DIR)
        static_files.append(rel_path)

unused = []
for rel_path in static_files:
    basename = os.path.basename(rel_path)
    
    # Let's do a more robust check: does the exact basename exist in the code?
    if basename not in code_contents:
        # Also check without extension in case it's dynamically added?
        name_no_ext = os.path.splitext(basename)[0]
        # check if it might be dynamically built, e.g. "offcanvas-"
        if re.search(r'\b' + re.escape(name_no_ext) + r'\b', code_contents):
             # it is used dynamically or without ext
             pass
        else:
            unused.append(rel_path)

print(f"Deep unused count: {len(unused)}")
with open('unused_deep.txt', 'w') as out:
    for u in unused:
        out.write(u + '\n')

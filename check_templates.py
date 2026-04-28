import os
import re

TEMPLATES_DIR = 'templates'
VIEWS_FILE = 'vynzora_app/views.py'

# 1. Get all template files
template_files = []
for root, _, files in os.walk(TEMPLATES_DIR):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            rel_path = os.path.relpath(filepath, TEMPLATES_DIR)
            # normalize for windows just in case, though it's mac
            rel_path = rel_path.replace('\\', '/')
            template_files.append(rel_path)

# 2. Read all files where templates might be referenced
reference_files = [VIEWS_FILE]
for f in template_files:
    reference_files.append(os.path.join(TEMPLATES_DIR, f))

# Also read urls.py in case TemplateView is used
reference_files.append('vynzora_app/urls.py')

code_contents = ""
for f in reference_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            code_contents += file.read() + "\n"
    except Exception:
        pass

# 3. Check for usage
unused = []
for tmpl in template_files:
    if tmpl == '404.html' or tmpl == '500.html':
        continue # usually handled by django defaults implicitly or explicitly
    
    # We look for the exact string of the template path, e.g., 'admin_home/index.html'
    if repr(tmpl) in code_contents or f'"{tmpl}"' in code_contents or f"'{tmpl}'" in code_contents:
        pass
    else:
        # Maybe it's referenced with a variable or dynamic? But usually templates are hardcoded.
        unused.append(tmpl)

print("Unused templates:")
for u in unused:
    print(u)

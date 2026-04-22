import re

with open('d:/储存/WorkBuddy/plantpal-website.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all Chinese text patterns that are NOT in data-i18n attributes
# Pattern: Chinese characters inside >...< but not inside data-i18n="..."
lines = html.split('\n')
issues = []

for i, line in enumerate(lines, 1):
    # Skip lines with data-i18n (those are already translatable)
    if 'data-i18n=' in line:
        continue
    # Skip lines that are just comments or script content
    if '<!--' in line or '<script' in line or '</script>' in line or '<style' in line:
        continue
    # Find Chinese characters
    if re.search(r'[\u4e00-\u9fff]', line):
        # Extract the Chinese portion
        match = re.search(r'>([^<]*[\u4e00-\u9fff][^<]*)<', line)
        if match:
            issues.append((i, match.group(0), line.strip()[:80]))

print(f'Found {len(issues)} lines with hardcoded Chinese text:')
for line_num, content, preview in issues[:30]:
    print(f'  Line {line_num}: {content}')

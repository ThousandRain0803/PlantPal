import re

with open('d:/储存/WorkBuddy/plantpal-website.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all data-i18n keys in HTML
keys = re.findall(r'data-i18n="([^"]+)"', html)
unique_keys = sorted(set(keys))
print(f'Found {len(unique_keys)} unique i18n keys in HTML')
for k in unique_keys:
    print(f'  - {k}')

# Find all keys in translations
print('\n--- Checking translation completeness ---')

# Read the translations section
zh_pattern = r"zh:\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}"
en_pattern = r"en:\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}"

# Simpler approach - extract all key: 'value' pairs
zh_keys = re.findall(r"^\s{4}([\w_]+):", html, re.MULTILINE)
en_keys = re.findall(r"^\s{4}([\w_]+):", html[html.find("en: {"):], re.MULTILINE)

print(f'\nZH keys in translations: {len(zh_keys)}')
print(f'EN keys in translations: {len(en_keys)}')

# Find missing keys
missing_in_en = [k for k in unique_keys if k not in en_keys]
print(f'\nMissing in EN: {len(missing_in_en)}')
for k in missing_in_en[:20]:
    print(f'  - {k}')

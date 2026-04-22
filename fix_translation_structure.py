import re

with open('d:/储存/WorkBuddy/plantpal-website.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and remove the zh translations from inside the first en object
# They appear after "order_error: 'Submission failed..." and before the second "en: {"

# Pattern: from order_error line to the second en: { 
pattern = r"(order_error: 'Submission failed\. Please try again or contact 823142127@qq\.com',\n)(            // Comparison table\n            comp_patent: '专利技术'[\s\S]*?team5_initial: '马'\n)(\s+},\n)(\s+en: \{)"

match = re.search(pattern, content)
if match:
    # Keep only order_error and the closing }, then the second en: {
    new_content = content[:match.start()] + \
                  match.group(1) + \
                  "        },\n" + \
                  match.group(4) + \
                  content[match.end():]
    
    with open('d:/储存/WorkBuddy/plantpal-website.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Fixed! Removed zh translations from inside en object.')
else:
    print('Pattern not found - may already be fixed or different structure')

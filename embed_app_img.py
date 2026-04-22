import base64

# 读取图片并转为Base64 data URL
with open('d:/储存/WorkBuddy/images/app示意图.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode()

data_url = f'data:image/png;base64,{b64}'
print(f'Data URL ready, length: {len(data_url)}')

# 读取HTML文件
with open('d:/储存/WorkBuddy/plantpal-website.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 替换app示意图.png为data URL
old = 'src="images/app示意图.png"'
count = html.count(old)
print(f'Found {count} instances to replace')

html = html.replace(old, f'src="{data_url}"')

# 写回HTML文件
with open('d:/储存/WorkBuddy/plantpal-website.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done! App images replaced with data URLs.')
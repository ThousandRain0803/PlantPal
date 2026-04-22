import base64, re

# 读取新图片并转为Base64 data URL
with open('d:/储存/WorkBuddy/images/app示意图_new.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode()
new_data_url = 'data:image/png;base64,' + b64
print(f'New data URL length: {len(new_data_url)}')

# 读取HTML文件
with open('d:/储存/WorkBuddy/plantpal-website.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 找到所有src=data:image/png;base64的行并替换
pattern = r'src="data:image/png;base64,[^"]+"'
matches = re.findall(pattern, html)
print(f'Found {len(matches)} data URL images')

count = 0
def replace_func(m):
    global count
    url = m.group(0)
    if 'iVBOR' in url:
        count += 1
        return 'src="' + new_data_url + '"'
    return url

html_new = re.sub(pattern, replace_func, html)
print(f'Replaced {count} app images')

# 写回HTML文件
with open('d:/储存/WorkBuddy/plantpal-website.html', 'w', encoding='utf-8') as f:
    f.write(html_new)

print('Done!')
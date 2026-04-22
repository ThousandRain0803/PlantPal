content = open(r"d:\储存\WorkBuddy\plantpal-website.html", "r", encoding="utf-8").read()
# Add prototype nav link
old = '<a href="#app" class="nav-link" data-i18n="nav_app">App预览</a>'
new = '<a href="#prototype" class="nav-link" data-i18n="nav_proto">产品原型</a>\n                <a href="#app" class="nav-link" data-i18n="nav_app">App预览</a>'
content = content.replace(old, new)
# Add mobile menu nav
old2 = '<a href="#app" class="nav-link" onclick="toggleMobileMenu()" data-i18n="nav_app">App预览</a>'
new2 = '<a href="#prototype" class="nav-link" onclick="toggleMobileMenu()" data-i18n="nav_proto">产品原型</a>\n            <a href="#app" class="nav-link" onclick="toggleMobileMenu()" data-i18n="nav_app">App预览</a>'
content = content.replace(old2, new2)
# Add zh translations
old3 = "            nav_app: 'App预览',"
new3 = "            nav_proto: '产品原型',\n            nav_app: 'App预览',"
content = content.replace(old3, new3)
# Add en translations
old4 = "            nav_app: 'App Preview',"
new4 = "            nav_proto: 'Prototype',\n            nav_app: 'App Preview',"
content = content.replace(old4, new4)
open(r"d:\储存\WorkBuddy\plantpal-website.html", "w", encoding="utf-8").write(content)
print("Nav updated successfully")

content = open(r"d:\储存\WorkBuddy\plantpal-website.html", "r", encoding="utf-8").read()
content = content.replace('src="app示意图.png"', 'src="images/app示意图.png"')
open(r"d:\储存\WorkBuddy\plantpal-website.html", "w", encoding="utf-8").write(content)
print("Done")

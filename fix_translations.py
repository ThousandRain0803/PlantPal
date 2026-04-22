import re

with open('d:/储存/WorkBuddy/plantpal-website.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ===== FIX 1: Comparison table cells =====
# Add data-i18n to comparison table cells
replacements = [
    # Table cells with Chinese content
    ('<span class="check"><i class="fas fa-check"></i> 专利技术</span>', 
     '<span class="check" data-i18n="comp_patent"><i class="fas fa-check"></i> <span data-i18n="comp_patent_text">专利技术</span></span>'),
    
    # This is getting complex - let's simplify
]

# Actually let's do this differently - wrap each Chinese text in a span with data-i18n

# Line 1131: 专利技术
content = content.replace(
    '<span class="check"><i class="fas fa-check"></i> 专利技术</span>',
    '<span class="check"><i class="fas fa-check"></i> <span data-i18n="comp_patent">专利技术</span></span>'
)

# Line 1138: 即插即用
content = content.replace(
    '<td class="highlight-col"><span class="check">即插即用</span></td>',
    '<td class="highlight-col"><span class="check" data-i18n="comp_ease_plantpal">即插即用</span></td>'
)

# Line 1139: 简单
content = content.replace(
    '<td>简单</td>',
    '<td data-i18n="comp_ease_simple">简单</td>'
)

# Line 1140: 需App/蓝牙
content = content.replace(
    '<td>需App/蓝牙</td>',
    '<td data-i18n="comp_ease_app">需App/蓝牙</td>'
)

# Line 1141: 复杂
content = content.replace(
    '<td>复杂</td>',
    '<td data-i18n="comp_ease_complex">复杂</td>'
)

# Line 1148: 数百至千元
content = content.replace(
    '<td>数百至千元</td>',
    '<td data-i18n="comp_price_pro">数百至千元</td>'
)

# Line 1153: 极低
content = content.replace(
    '<td>极低</td>',
    '<td data-i18n="comp_acc_verylow">极低</td>'
)

# Line 1154: 低
content = content.replace(
    '<td>低</td>',
    '<td data-i18n="comp_acc_low">低</td>'
)

# Line 1155: 实验室级
content = content.replace(
    '<td>实验室级</td>',
    '<td data-i18n="comp_acc_pro">实验室级</td>'
)

# Line 1159: 阳台盆栽
content = content.replace(
    '<td class="highlight-col"><span class="check">阳台盆栽</span></td>',
    '<td class="highlight-col"><span class="check" data-i18n="comp_scene_plantpal">阳台盆栽</span></td>'
)

# Line 1160: 简单适配
content = content.replace(
    '<td>简单适配</td>',
    '<td data-i18n="comp_scene_simple">简单适配</td>'
)

# Line 1161: 差
content = content.replace(
    '<td>差</td>',
    '<td data-i18n="comp_scene_poor">差</td>'
)

# Line 1162: 不适合家用
content = content.replace(
    '<td>不适合家用</td>',
    '<td data-i18n="comp_scene_home">不适合家用</td>'
)

# ===== FIX 2: Specs values =====
content = content.replace(
    '<div class="spec-value">15cm(长) × 3cm(直径)</div>',
    '<div class="spec-value" data-i18n="spec_dim_val">15cm(长) × 3cm(直径)</div>'
)

content = content.replace(
    '<div class="spec-value">土壤氮(N)、磷(P)、钾(K)含量</div>',
    '<div class="spec-value" data-i18n="spec_detect_val">土壤氮(N)、磷(P)、钾(K)含量</div>'
)

content = content.replace(
    '<div class="spec-value">插入土壤后<span style="color:var(--accent);font-weight:700;">10秒</span>出结果</div>',
    '<div class="spec-value" data-i18n="spec_speed_val">插入土壤后<span style="color:var(--accent);font-weight:700;" data-i18n="spec_speed_val2">10秒</span>出结果</div>'
)

content = content.replace(
    '<div class="spec-value">可更换 CR2032 纽扣电池</div>',
    '<div class="spec-value" data-i18n="spec_power_val">可更换 CR2032 纽扣电池</div>'
)

content = content.replace(
    '<div class="spec-value">正常可用 <strong>≥6个月</strong>（每周10次检测）</div>',
    '<div class="spec-value" data-i18n="spec_battery_val">正常可用 <strong>≥6个月</strong>（每周10次检测）</div>'
)

content = content.replace(
    '<div class="spec-value">食品级可回收 ABS 生态塑料</div>',
    '<div class="spec-value" data-i18n="spec_mat_val">食品级可回收 ABS 生态塑料</div>'
)

content = content.replace(
    '<div class="spec-value">耐腐蚀 316 医用级不锈钢</div>',
    '<div class="spec-value" data-i18n="spec_probe_val">耐腐蚀 316 医用级不锈钢</div>'
)

content = content.replace(
    '<div class="spec-value">探头 <strong>IP67</strong> 防水</div>',
    '<div class="spec-value" data-i18n="spec_water_val">探头 <strong>IP67</strong> 防水</div>'
)

# ===== FIX 3: Prototype fallback =====
content = content.replace(
    '<span style="font-size:1.1rem;">PlantPal 设备原型</span>',
    '<span style="font-size:1.1rem;" data-i18n="proto_fallback_title">PlantPal 设备原型</span>'
)

content = content.replace(
    '<span style="font-size:0.8rem;color:var(--text-muted);font-weight:400;">15cm × 3cm · IP67防水</span>',
    '<span style="font-size:0.8rem;color:var(--text-muted);font-weight:400;" data-i18n="proto_fallback_sub">15cm × 3cm · IP67防水</span>'
)

# ===== FIX 4: App preview fallback =====
content = content.replace(
    '<span>App界面预览</span>',
    '<span data-i18n="app_fallback_preview">App界面预览</span>'
)

content = content.replace(
    '<span>数据记录界面</span>',
    '<span data-i18n="app_fallback_data">数据记录界面</span>'
)

content = content.replace(
    '<span>植物百科界面</span>',
    '<span data-i18n="app_fallback_plant">植物百科界面</span>'
)

# ===== FIX 5: Team initials =====
content = content.replace(
    '>蔡</div>',
    ' data-i18n="team1_initial">蔡</div>'
)
content = content.replace(
    '>王</div>',
    ' data-i18n="team2_initial">王</div>'
)
content = content.replace(
    '>郭</div>',
    ' data-i18n="team3_initial">郭</div>'
)
content = content.replace(
    '>林</div>',
    ' data-i18n="team4_initial">林</div>'
)
content = content.replace(
    '>马</div>',
    ' data-i18n="team5_initial">马</div>'
)

with open('d:/储存/WorkBuddy/plantpal-website.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('HTML updates done!')

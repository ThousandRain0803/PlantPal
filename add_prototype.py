content = open(r"d:\储存\WorkBuddy\plantpal-website.html", "r", encoding="utf-8").read()

prototype_section = '''
    <!-- Prototype Showcase -->
    <section class="py-20 md:py-28" id="prototype">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center mb-16 reveal">
                <div class="section-label"><i class="fas fa-cube"></i> <span data-i18n="proto_label">产品原型</span></div>
                <h2 class="section-title" data-i18n="proto_title">实物原型展示</h2>
                <p class="section-subtitle" data-i18n="proto_subtitle">基于香港城市大学专利技术打造的实体设备，已完成实验室测试</p>
            </div>
            
            <div class="grid md:grid-cols-2 gap-12 items-center">
                <div class="reveal">
                    <div style="background:linear-gradient(135deg,#f5f5f5,#e8e8e8);border-radius:24px;padding:2rem;display:flex;align-items:center;justify-content:center;min-height:400px;box-shadow:0 10px 40px rgba(0,0,0,0.08);">
                        <img src="images/原型图.png" alt="PlantPal Prototype" style="max-width:100%;max-height:360px;border-radius:16px;box-shadow:0 8px 30px rgba(0,0,0,0.12);" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';">
                        <div style="display:none;width:100%;height:360px;align-items:center;justify-content:center;flex-direction:column;gap:16px;color:var(--primary);font-weight:700;">
                            <i class="fas fa-microchip" style="font-size:5rem;opacity:0.4;"></i>
                            <span style="font-size:1.1rem;">PlantPal 设备原型</span>
                            <span style="font-size:0.8rem;color:var(--text-muted);font-weight:400;">15cm × 3cm · IP67防水</span>
                        </div>
                    </div>
                </div>
                <div class="reveal" style="transition-delay:0.15s;">
                    <h3 class="text-2xl font-bold mb-4" style="color:var(--text-dark);" data-i18n="proto_highlight">产品亮点</h3>
                    <ul style="list-style:none;padding:0;line-height:2.2;">
                        <li style="display:flex;align-items:flex-start;gap:12px;padding:0.75rem 0;border-bottom:1px solid rgba(45,90,39,0.06);">
                            <div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--primary-light));display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px;">
                                <i class="fas fa-check" style="color:#fff;font-size:0.8rem;"></i>
                            </div>
                            <div>
                                <strong data-i18n="proto_point1_title">工业级传感精度</strong>
                                <p style="color:var(--text-muted);font-size:0.88rem;margin-top:2px;" data-i18n="proto_point1_desc">NPK检测精度±5%，香港城市大学专利电化学技术</p>
                            </div>
                        </li>
                        <li style="display:flex;align-items:flex-start;gap:12px;padding:0.75rem 0;border-bottom:1px solid rgba(45,90,39,0.06);">
                            <div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--primary-light));display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px;">
                                <i class="fas fa-check" style="color:#fff;font-size:0.8rem;"></i>
                            </div>
                            <div>
                                <strong data-i18n="proto_point2_title">即插即用设计</strong>
                                <p style="color:var(--text-muted);font-size:0.88rem;margin-top:2px;" data-i18n="proto_point2_desc">无需App、无需蓝牙配对，插入土壤10秒出结果</p>
                            </div>
                        </li>
                        <li style="display:flex;align-items:flex-start;gap:12px;padding:0.75rem 0;border-bottom:1px solid rgba(45,90,39,0.06);">
                            <div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--primary-light));display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px;">
                                <i class="fas fa-check" style="color:#fff;font-size:0.8rem;"></i>
                            </div>
                            <div>
                                <strong data-i18n="proto_point3_title">LED直观状态显示</strong>
                                <p style="color:var(--text-muted);font-size:0.88rem;margin-top:2px;" data-i18n="proto_point3_desc">三色LED灯将NPK数据转化为可操作的养护建议</p>
                            </div>
                        </li>
                        <li style="display:flex;align-items:flex-start;gap:12px;padding:0.75rem 0;border-bottom:1px solid rgba(45,90,39,0.06);">
                            <div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--primary-light));display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px;">
                                <i class="fas fa-check" style="color:#fff;font-size:0.8rem;"></i>
                            </div>
                            <div>
                                <strong data-i18n="proto_point4_title">阳台专属尺寸</strong>
                                <p style="color:var(--text-muted);font-size:0.88rem;margin-top:2px;" data-i18n="proto_point4_desc">15cm×3cm，专为小盆栽和浅土设计</p>
                            </div>
                        </li>
                        <li style="display:flex;align-items:flex-start;gap:12px;padding:0.75rem 0;">
                            <div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--primary-light));display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px;">
                                <i class="fas fa-check" style="color:#fff;font-size:0.8rem;"></i>
                            </div>
                            <div>
                                <strong data-i18n="proto_point5_title">环保耐用材质</strong>
                                <p style="color:var(--text-muted);font-size:0.88rem;margin-top:2px;" data-i18n="proto_point5_desc">食品级ABS+316不锈钢探头，IP67防水，寿命3年+</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- App Preview -->
'''

content = content.replace("    <!-- App Preview -->\n", prototype_section)

# Add translations for prototype section
translations_en = '''
            proto_label: 'Prototype',
            proto_title: 'Product Prototype Showcase',
            proto_subtitle: 'Physical device built on CityU patented technology, lab tested',
            proto_highlight: 'Product Highlights',
            proto_point1_title: 'Industrial-Grade Sensing',
            proto_point1_desc: 'NPK accuracy ±5%, CityU patented electrochemical technology',
            proto_point2_title: 'Plug & Play',
            proto_point2_desc: 'No App or Bluetooth needed, results in 10 seconds',
            proto_point3_title: 'LED Intuitive Display',
            proto_point3_desc: 'Tri-color LEDs convert NPK data into actionable recommendations',
            proto_point4_title: 'Balcony-Optimized Size',
            proto_point4_desc: '15cm × 3cm, designed for small pots and shallow soil',
            proto_point5_title: 'Eco-Friendly & Durable',
            proto_point5_desc: 'Food-grade ABS + 316 steel probe, IP67 waterproof, 3+ year lifespan',
'''

translations_zh = '''
            proto_label: '产品原型',
            proto_title: '实物原型展示',
            proto_subtitle: '基于香港城市大学专利技术打造的实体设备，已完成实验室测试',
            proto_highlight: '产品亮点',
            proto_point1_title: '工业级传感精度',
            proto_point1_desc: 'NPK检测精度±5%，香港城市大学专利电化学技术',
            proto_point2_title: '即插即用设计',
            proto_point2_desc: '无需App、无需蓝牙配对，插入土壤10秒出结果',
            proto_point3_title: 'LED直观状态显示',
            proto_point3_desc: '三色LED灯将NPK数据转化为可操作的养护建议',
            proto_point4_title: '阳台专属尺寸',
            proto_point4_desc: '15cm×3cm，专为小盆栽和浅土设计',
            proto_point5_title: '环保耐用材质',
            proto_point5_desc: '食品级ABS+316不锈钢探头，IP67防水，寿命3年+',
'''

# Insert translations before the last closing brace in zh section
zh_end = content.rfind('}', 0, content.rfind('},'))
content = content[:zh_end+1] + ',' + translations_zh + content[zh_end+1:]

# Insert English translations before the last closing brace in en section  
en_end = content.rfind('}', 0, content.rfind('},\n        };'))
content = content[:en_end+1] + ',' + translations_en + content[en_end+1:]

open(r"d:\储存\WorkBuddy\plantpal-website.html", "w", encoding="utf-8").write(content)
print("Prototype section added successfully")

# -*- coding: utf-8 -*-
import re, io

path = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(path, encoding='utf-8') as f:
    html = f.read()

# ---------- 1) 药架改为静态 img src，满足发布链路扫描 ----------
# 展示元数据（no/tag）仅用于徽标，与 JS 数据一致
grid_cards = [
    ('p1', '不挂科', '考试周专用'), ('p2', '敢说话', '社恐专用'),
    ('p3', '不内耗', '卷躺纠结专用'), ('p4', '去爱吧', '心动/失恋专用'),
    ('p5', '和好如初', '宿舍/人际专用'), ('p6', '不后悔', '毕业迷茫专用'),
    ('p7', '不将就', '方向选择专用'), ('p8', '不熬夜', '健康自律专用'),
]
cards = []
for pid, name, tag in grid_cards:
    cards.append(
        '<div class="pill-card" data-id="%s" tabindex="0" role="button" aria-label="选择%s后悔药">\n'
        '        <div class="thumb"><span class="badge">%s</span><img src="assets/%s.jpg" alt="%s后悔药场景插画" loading="lazy"></div>\n'
        '        <div class="body"><div class="pname"></div><div class="ptag"></div><div class="ppromise"></div></div>\n'
        '      </div>' % (pid, name, tag, pid, name))
grid_html = '\n    '.join(cards)
old_grid = '<div class="pill-grid" id="pillGrid"></div>'
assert old_grid in html
html = html.replace(old_grid, '<div class="pill-grid" id="pillGrid">\n    ' + grid_html + '\n  </div>')

# 2) 移除 PILLS 中的 img 字段（图片引用改为从静态 DOM 读取）
html = re.sub(r"img:'assets/p\d\.jpg',\s*", "", html)
assert 'img:' not in html

# 3) renderPills -> bindPills（不再生成 img 标签，改为填充文字 + 绑定事件 + 收集 imgMap）
old_fn = """function renderPills(){
  $('pillGrid').innerHTML = PILLS.map(p=>`
    <div class="pill-card" data-id="${p.id}" tabindex="0" role="button" aria-label="选择${p.name}后悔药">
      <div class="thumb"><span class="badge">${p.no} ${p.tag}</span><img src="${p.img}" alt="${p.name}后悔药场景插画" loading="lazy"></div>
      <div class="body">
        <div class="pname">「${p.name}」后悔药</div>
        <div class="ptag">${p.tag}</div>
        <div class="ppromise">${p.promise}</div>
      </div>
    </div>`).join('');
  $('pillGrid').querySelectorAll('.pill-card').forEach(card=>{
    const act = ()=>choose(card.dataset.id);
    card.addEventListener('click', act);
    card.addEventListener('keydown', e=>{ if(e.key==='Enter'||e.key===' '){e.preventDefault();act();} });
  });
}"""
new_fn = """const imgMap = {};
function bindPills(){
  $('pillGrid').querySelectorAll('.pill-card').forEach(card=>{
    const p = PILLS.find(x=>x.id===card.dataset.id);
    if(!p) return;
    imgMap[p.id] = card.querySelector('img').src;
    card.querySelector('.pname').textContent = '「' + p.name + '」后悔药';
    card.querySelector('.ptag').textContent = p.tag;
    card.querySelector('.ppromise').textContent = p.promise;
    const act = ()=>choose(p.id);
    card.addEventListener('click', act);
    card.addEventListener('keydown', e=>{ if(e.key==='Enter'||e.key===' '){e.preventDefault();act();} });
  });
}"""
assert old_fn in html, 'renderPills not found'
html = html.replace(old_fn, new_fn)

# 4) 初始化调用与成品图引用
html = html.replace('renderPills();', 'bindPills();')
html = html.replace("$('resultImg').src = p.img;", "$('resultImg').src = imgMap[p.id];")

# 5) 去 emoji / 符号化字符
html = html.replace("'🎉 8 瓶集齐！你的「大学结业证书」已解锁'", "'8 瓶集齐！你的「大学结业证书」已解锁'")
html = html.replace("content:'✉'", "content:'信'")

with io.open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print('done, bytes:', len(html.encode('utf-8')))

# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) rankStars 函数（插在 let rankCache = null; 后）
old = "let rankCache = null;"
new = """let rankCache = null;
function rankStars(n){
  let out = '';
  for(let i=0;i<n;i++){
    out += '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l2.9 5.9 6.6.9-4.8 4.6 1.2 6.5L12 17.3 6.1 19.9l1.2-6.5L2.5 8.8l6.6-.9z"/></svg>';
  }
  return out;
}"""
assert s.count(old) == 1, 'rankCache'
s = s.replace(old, new, 1)

# 2) renderRank：徽章与账户弹窗 chip 用星星
old = """  badge.style.display = 'inline-flex';
  badge.style.background = r.tier.color;
  $('rankBadgeTxt').textContent = r.tier.name + ' ' + r.level + ' 级';
  const panel = $('rankPanel');
  panel.style.display = '';
  const chip = $('rankChip');
  chip.style.background = r.tier.color;
  chip.textContent = r.tier.name + ' ' + r.level + ' 级';"""
new = """  badge.style.display = 'inline-flex';
  badge.style.background = r.tier.color;
  $('rankBadgeTxt').innerHTML = r.tier.name + rankStars(r.level);
  const panel = $('rankPanel');
  panel.style.display = '';
  const chip = $('rankChip');
  chip.style.background = r.tier.color;
  chip.innerHTML = r.tier.name + rankStars(r.level);"""
assert s.count(old) == 1, 'renderRank'
s = s.replace(old, new)

# 3) rankAfterChange：升级弹窗 chip 用星星
old = """    const chip = $('rankupChip');
    chip.style.background = r.tier.color;
    chip.textContent = r.tier.name + ' ' + r.level + ' 级';"""
new = """    const chip = $('rankupChip');
    chip.style.background = r.tier.color;
    chip.innerHTML = r.tier.name + rankStars(r.level);"""
assert s.count(old) == 1, 'rankupChip'
s = s.replace(old, new)

# 4) 公告等级行用星星
old = """    $('noticeRankLine').textContent = '你目前是：' + r.tier.name + ' ' + r.level + ' 级，继续配药升级吧';"""
new = """    $('noticeRankLine').innerHTML = '你目前是：' + r.tier.name + rankStars(r.level) + '，继续配药升级吧';"""
assert s.count(old) == 1, 'notice rankline'
s = s.replace(old, new)

# 5) CSS：徽章/芯片内星星尺寸
old = """.rank-badge svg{width:13px;height:13px;flex:none}"""
new = """.rank-badge svg{width:11px;height:11px;flex:none}
.rank-chip{display:inline-flex;align-items:center;gap:5px}
.rank-chip svg{width:12px;height:12px;flex:none}
.rank-chip.big svg{width:15px;height:15px;flex:none}"""
assert s.count(old) == 1, 'badge svg css'
s = s.replace(old, new)

io.open(p, 'w', encoding='utf-8').write(s)
print('stars ok')

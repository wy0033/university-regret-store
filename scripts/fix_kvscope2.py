# -*- coding: utf-8 -*-
import io
p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(p, encoding='utf-8') as f:
    h = f.read()

kv_fn = """function kvTags(p, s){
  const kv = [];
  kv.push(`<span class="kv"><b>${esc(s.major||'大学')}</b></span>`);
  kv.push(`<span class="kv"><b>${esc(s.grade||'大二')}</b></span>`);
  kv.push(`<span class="kv"><b>${esc(s.gender||'保密')}</b></span>`);
  if(s.goal) kv.push(`<span class="kv">期望：${esc(s.goal)}</span>`);
  if(s.version==='pro'){
    if(s.stateInfo) kv.push(`<span class="kv">状态：${esc(s.stateInfo)}</span>`);
    if(s.mood) kv.push(`<span class="kv">心情：${esc(s.mood)}</span>`);
  }
  if(s.version==='pro' && s.nick) kv.push(`<span class="kv">致：${esc(s.nick)}</span>`);
  kv.push(`<span class="kv">正在：${esc(s.anxiety||'为一点小事烦恼')}</span>`);
  kv.push(`<span class="kv">${p.keyword[0]}</span>`);
  return kv.join('');
}"""

# 1) 从 showResult 内部移除 kvTags 定义，补回 kcardBody 调用行
old_inner = "  typeLetter(letter);\n" + kv_fn + "\n  $('actList').innerHTML = p.actions.map((a,i)=>`"
new_inner = "  typeLetter(letter);\n  $('kcardBody').innerHTML = kvTags(p, state);\n  $('actList').innerHTML = p.actions.map((a,i)=>`"
assert old_inner in h, 'inner block not found'
h = h.replace(old_inner, new_inner)

# 2) 顶层定义 kvTags（放在“成品”区块之前）
anchor = "/* ===== 成品 ===== */\nfunction showResult(){"
assert anchor in h
h = h.replace(anchor, kv_fn + "\n\n" + anchor)

with io.open(p, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(h)
print('fixed ok, bytes:', len(h.encode('utf-8')))

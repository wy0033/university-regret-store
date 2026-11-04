# -*- coding: utf-8 -*-
import io
p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(p, encoding='utf-8') as f:
    h = f.read()

# 从 showResult 内部删除 kvTags 定义，只保留调用
inner = """  typeLetter(letter);
function kvTags(p, s){
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
}
  $('kcardBody').innerHTML = kvTags(p, state);"""
assert inner in h
h = h.replace(inner, """  typeLetter(letter);
  $('kcardBody').innerHTML = kvTags(p, state);""")

# 在“成品”区块前插入顶层 kvTags
anchor = "/* ===== 成品 ===== */\nfunction showResult(){"
assert anchor in h
kv = """function kvTags(p, s){
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
}

/* ===== 成品 ===== */
function showResult(){"""
h = h.replace(anchor, kv)

with io.open(p, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(h)
print('fixed scope ok, bytes:', len(h.encode('utf-8')))

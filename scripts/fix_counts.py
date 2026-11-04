# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) 公告星星尺寸（.notice-sec 内 svg 约束）
old = """.notice-sec.warn{border-color:var(--amber);background:linear-gradient(180deg,rgba(245,201,123,.14),rgba(245,201,123,.05))}"""
new = """.notice-sec.warn{border-color:var(--amber);background:linear-gradient(180deg,rgba(245,201,123,.14),rgba(245,201,123,.05))}
.notice-sec svg{width:14px;height:14px;flex:none;vertical-align:-2px}"""
assert s.count(old) == 1, 'notice svg css'
s = s.replace(old, new)

# 2) 累计计数：getCounts + bumpCount（插在 calcRank 定义前）
old = "function calcRank(){"
new = """function getCounts(){
  let c = {};
  try{ c = JSON.parse(localStorage.getItem(acctKey('pillCounts'))||'null') || {}; }catch(e){ c = {}; }
  if(!Object.keys(c).length){
    const hist = getRecords();
    if(hist.length){
      hist.forEach(r=>{
        if(!r || !r.pillId) return;
        const k = r.pillId + (r.version==='pro' ? '_adv' : '_n');
        c[k] = (c[k]||0) + 1;
      });
      try{ localStorage.setItem(acctKey('pillCounts'), JSON.stringify(c)); }catch(e){}
    }
  }
  return c;
}
function bumpCount(pillId, ver){
  const c = getCounts();
  const k = pillId + (ver==='pro' ? '_adv' : '_n');
  c[k] = (c[k]||0) + 1;
  try{ localStorage.setItem(acctKey('pillCounts'), JSON.stringify(c)); }catch(e){}
}
function calcRank(){"""
assert s.count(old) == 1, 'calcRank anchor'
s = s.replace(old, new, 1)

# 3) calcRank 改用累计计数
old = """function calcRank(){
  const recs = getRecords();
  const per = {}, adv = {};
  PILLS.forEach(p=>{ per[p.id]=0; adv[p.id]=0; });
  recs.forEach(r=>{ if(per[r.pillId]!=null){ per[r.pillId]++; if(r.version==='pro') adv[r.pillId]++; } });"""
new = """function calcRank(){
  const c = getCounts();
  const per = {}, adv = {};
  PILLS.forEach(p=>{
    per[p.id] = (c[p.id+'_n']||0) + (c[p.id+'_adv']||0);
    adv[p.id] = c[p.id+'_adv']||0;
  });"""
assert s.count(old) == 1, 'calcRank body'
s = s.replace(old, new)

# 4) saveRecord 累计计数（记录仍保留 5 条上限用于历史展示）
old = """  localStorage.setItem(acctKey('pillRecords'), JSON.stringify(recs));
  if(state.user) rankAfterChange();
}"""
new = """  localStorage.setItem(acctKey('pillRecords'), JSON.stringify(recs));
  bumpCount(rec.pillId, rec.version);
  if(state.user) rankAfterChange();
}"""
assert s.count(old) == 1, 'saveRecord'
s = s.replace(old, new)

io.open(p, 'w', encoding='utf-8').write(s)
print('counts fix ok')

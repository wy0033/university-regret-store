# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) renderRecCard: rec-head 包 span + 删除按钮
old1 = '''    <div class="rec-head">${esc(r.time)} · ${r.version==='pro'?'进阶定制':'普通配方'} · ${esc(r.grade||'')}${esc(r.major?(' · '+r.major):'')}</div>'''
new1 = '''    <div class="rec-head"><span>${esc(r.time)} · ${r.version==='pro'?'进阶定制':'普通配方'} · ${esc(r.grade||'')}${esc(r.major?(' · '+r.major):'')}</span><button class="rec-del" type="button" title="删除这条记录">删除</button></div>'''
assert s.count(old1) == 1, 'renderRecCard head not found'
s = s.replace(old1, new1)

# 2) openHistory: 绑定 rec-del
old2 = '''    const idx = Number(card.dataset.idx);
    card.querySelectorAll('.rec-acts li').forEach(li=>{'''
new2 = '''    const idx = Number(card.dataset.idx);
    card.querySelector('.rec-del').addEventListener('click', ()=>{
      if(confirm('确定删除这条药方记录吗？删除后不可恢复。')) deleteRecord(pid, idx);
    });
    card.querySelectorAll('.rec-acts li').forEach(li=>{'''
assert s.count(old2) == 1, 'openHistory bind not found'
s = s.replace(old2, new2)

# 3) deleteRecord 函数
old3 = "$('histClose').addEventListener('click', ()=>$('historyModal').classList.remove('show'));"
new3 = '''function deleteRecord(pid, idx){
  const recs = getRecords();
  let target = -1, seen = 0;
  for(let i=0;i<recs.length;i++){
    if(recs[i].pillId===pid){
      if(seen===idx){ target=i; break; }
      seen++;
    }
  }
  if(target<0) return;
  recs.splice(target,1);
  localStorage.setItem('pillRecords', JSON.stringify(recs));
  openHistory(pid);
  toast('记录已删除');
}
$('histClose').addEventListener('click', ()=>$('historyModal').classList.remove('show'));'''
assert s.count(old3) == 1, 'histClose bind not found'
s = s.replace(old3, new3)

io.open(p, 'w', encoding='utf-8').write(s)
print('js ok')

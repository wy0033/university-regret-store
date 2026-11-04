# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# showResult：渲染资料卡
old = """  $('kcardBody').innerHTML = kvTags(p, state);
  $('actList').innerHTML = p.actions.map((a,i)=>`"""
new = """  $('kcardBody').innerHTML = kvTags(p, state);
  const mats = PILL_MATERIALS[p.id] || [];
  $('matCard').style.display = mats.length ? 'block' : 'none';
  $('matName').textContent = p.name;
  $('matBody').innerHTML = mats.map(m=>`<div class="mat-item"><b>${esc(m.t)}</b><p>${esc(m.c)}</p></div>`).join('');
  $('actList').innerHTML = p.actions.map((a,i)=>`"""
assert s.count(old) == 1, 'showResult mats'
s = s.replace(old, new)

io.open(p, 'w', encoding='utf-8').write(s)
print('materials js ok')

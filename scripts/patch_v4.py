# -*- coding: utf-8 -*-
import io

path = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(path, encoding='utf-8') as f:
    html = f.read()

def rep(old, new, must=True):
    global html
    if old not in html:
        if must:
            raise AssertionError('NOT FOUND: ' + old[:70])
        return
    html = html.replace(old, new, 1)

# ---------- 1) p6 改名：不后悔 -> 向前走 ----------
rep(" {id:'p6', no:'⑥', name:'不后悔', tag:'毕业迷茫专用', promise:'毕业那天，你不慌',",
    " {id:'p6', no:'⑥', name:'向前走', tag:'毕业迷茫专用', promise:'毕业那天，你不慌',")

# ---------- 2) p5 信中性化：她们 -> 大家 ----------
rep("原来那次你没去聚餐，她们以为你在生气；你深夜没睡，她们以为你不想理人。",
    "原来那次你没去聚餐，大家以为你在生气；你深夜没睡，大家以为你不想理人。")

# ---------- 3) CSS：行动清单勾选后才显示 ✓ ----------
rep(""".act-list li.done .tick{background:var(--amber);border-color:var(--amber)}""",
""".act-list li.done .tick{background:var(--amber);border-color:var(--amber)}
.act-list li.done .tick::after{content:'✓'}""")

# ---------- 4) 成品页行动清单渲染：tick 不再硬编码 ✓ ----------
rep("""  $('actList').innerHTML = p.actions.map((a,i)=>`
    <li data-i="${i}"><span class="tick">✓</span><span>${a}</span></li>`).join('');""",
"""  $('actList').innerHTML = p.actions.map((a,i)=>`
    <li data-i="${i}"><span class="tick"></span><span>${a}</span></li>`).join('');""")

# ---------- 5) choose：进入新药时彻底重置表单 ----------
rep("""function choose(id){
  state.pill = PILLS.find(p=>p.id===id);
  $('inputTitle').textContent = `「${state.pill.name}」· 来，把方子告诉我`;
  $('inputSub').textContent = `配药前，我需要知道三件事，然后为你研磨专属的一封`;
  $('anxietyLabel').textContent = `最近最让你焦虑的一件事（${state.pill.name}相关）`;
  $('anxietyInput').placeholder = state.pill.anxietyPh;
  resetVersion();
  state.qIndex = null;
  renderQ();
  $('gradeSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.grade===state.grade));
  $('genderSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.gender===state.gender));
  $('stateSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.state===state.stateInfo));
  $('moodSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.mood===state.mood));
  showScreen('input');
}""",
"""function choose(id){
  state.pill = PILLS.find(p=>p.id===id);
  $('inputTitle').textContent = `「${state.pill.name}」· 来，把方子告诉我`;
  $('inputSub').textContent = `配药前，选一个配方：速配，或深度定制`;
  $('anxietyLabel').textContent = `最近最让你焦虑的一件事（${state.pill.name}相关）`;
  $('anxietyInput').placeholder = state.pill.anxietyPh;
  resetVersion();
  resetForm();
  renderQ();
  $('gradeSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.grade===state.grade));
  $('genderSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.gender===state.gender));
  showScreen('input');
}
function resetForm(){
  state.qIndex = null;
  state.stateInfo = '';
  state.mood = '';
  state.answer = '';
  ['majorInput','anxietyInput','goalInput','nickInput','detailInput'].forEach(id=>{ $(id).value=''; });
  $('stateSeg').querySelectorAll('button').forEach(b=>b.classList.remove('sel'));
  $('moodSeg').querySelectorAll('button').forEach(b=>b.classList.remove('sel'));
}""")

# ---------- 6) startMix：进阶版专属问题必选 ----------
rep("""  state.answer = (state.qIndex!=null && state.pill.q) ? state.pill.q.o[state.qIndex] : '';
  if(!state.pill){ toast('请先选一瓶药'); showScreen('pick'); return; }""",
"""  state.answer = (state.qIndex!=null && state.pill.q) ? state.pill.q.o[state.qIndex] : '';
  if(!state.pill){ toast('请先选一瓶药'); showScreen('pick'); return; }
  if(state.version==='pro' && state.qIndex==null){ toast('进阶定制：请先回答这瓶药的专属问题'); return; }""")

# 写回（保持 CRLF）
with io.open(path, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(html)
print('patched ok, bytes:', len(html.encode('utf-8')))

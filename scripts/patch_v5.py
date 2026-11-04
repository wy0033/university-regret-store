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

# ---------- 1) CSS：药盒可点 + 历史弹窗样式 ----------
rep(""".modal-close:hover{opacity:.92}""",
""".modal-close:hover{opacity:.92}
.box-slot.got{cursor:pointer}
.box-slot.got:hover{transform:scale(1.05);box-shadow:var(--shadow-sm)}
.box-slot .bsub{font-size:10px;opacity:.88}
#histList{display:flex;flex-direction:column;gap:14px;max-height:52vh;overflow:auto;margin-top:6px;padding-right:4px}
.rec-card{background:var(--bg);border:1.5px solid var(--line);border-radius:16px;padding:14px 16px}
.rec-head{font-size:12.5px;color:var(--amber-deep);font-weight:600;margin-bottom:8px;letter-spacing:.5px}
.rec-letter{font-size:13.5px;line-height:1.9;color:var(--ink);white-space:pre-line}
.rec-kv{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px;border-top:1px dashed var(--line);padding-top:10px}
.rec-kv .kv{background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:3px 11px;font-size:12px}
.rec-kv .kv b{color:var(--amber-deep)}
.hist-empty{text-align:center;color:var(--ink-soft);font-size:13.5px;line-height:2.1;padding:34px 0}""")

# ---------- 2) HTML：历史弹窗 ----------
rep("""    <button class="modal-close" id="boxClose">收起药盒</button>
  </div>
</div>

<div id="toast" role="status"></div>""",
"""    <button class="modal-close" id="boxClose">收起药盒</button>
  </div>
</div>

<!-- ===== 药方历史弹窗 ===== -->
<div class="modal-mask" id="historyModal">
  <div class="modal">
    <h3 id="histTitle">药方历史</h3>
    <p class="modal-sub" id="histSub"></p>
    <div id="histList"></div>
    <button class="modal-close" id="histClose">收起</button>
  </div>
</div>

<div id="toast" role="status"></div>""")

# ---------- 3) JS：关键词卡抽成通用函数 ----------
rep("""  $('kcardBody').innerHTML = kv.join('');""",
"""  $('kcardBody').innerHTML = kvTags(p, state);""")
rep("""  const kv = [];
  kv.push(`<span class="kv"><b>${esc(state.major||'大学')}</b></span>`);
  kv.push(`<span class="kv"><b>${esc(state.grade)}</b></span>`);
  kv.push(`<span class="kv"><b>${esc(state.gender)}</b></span>`);
  if(state.goal) kv.push(`<span class="kv">期望：${esc(state.goal)}</span>`);
  if(state.version==='pro'){
    if(state.stateInfo) kv.push(`<span class="kv">状态：${esc(state.stateInfo)}</span>`);
    if(state.mood) kv.push(`<span class="kv">心情：${esc(state.mood)}</span>`);
  }
  if(state.version==='pro' && state.nick) kv.push(`<span class="kv">致：${esc(state.nick)}</span>`);
  kv.push(`<span class="kv">正在：${esc(state.anxiety||'为一点小事烦恼')}</span>`);
  kv.push(`<span class="kv">${p.keyword[0]}</span>`);
  $('kcardBody').innerHTML = kvTags(p, state);""",
"""function kvTags(p, s){
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
}""")

# ---------- 4) JS：成品页按钮文案 ----------
rep("  $('collectBtn').textContent = state.collected.includes(p.id) ? '已在药盒中' : '收进药盒';",
    "  $('collectBtn').textContent = state.collected.includes(p.id) ? '再记一次' : '收进药盒';")

# ---------- 5) JS：收藏时保存药方记录（支持重复追加） ----------
rep("""$('collectBtn').addEventListener('click', ()=>{
  const id = state.pill.id;
  if(state.collected.includes(id)){ toast('这瓶药已经在你的药盒里啦'); return; }
  state.collected.push(id); saveBox();
  toast(`「${state.pill.name}」已收进药盒（${state.collected.length}/8）`);
  $('collectBtn').textContent = '已在药盒中';
  if(state.collected.length===8){
    toast('8 瓶集齐！你的「大学结业证书」已解锁');
    openBox();
  }
});""",
"""$('collectBtn').addEventListener('click', ()=>{
  const id = state.pill.id;
  if(state.collected.includes(id)){
    saveRecord();
    toast(`已追加「${state.pill.name}」的药方记录`);
    return;
  }
  state.collected.push(id); saveBox();
  saveRecord();
  toast(`「${state.pill.name}」已收进药盒（${state.collected.length}/8）`);
  $('collectBtn').textContent = '再记一次';
  if(state.collected.length===8){
    toast('8 瓶集齐！你的「大学结业证书」已解锁');
    openBox();
  }
});
function nowStr(){
  const d = new Date();
  const p = n => String(n).padStart(2,'0');
  return `${d.getMonth()+1}-${p(d.getDate())} ${p(d.getHours())}:${p(d.getMinutes())}`;
}
function getRecords(){
  try{ return JSON.parse(localStorage.getItem('pillRecords')||'[]'); }catch(e){ return []; }
}
function saveRecord(){
  const rec = {
    pillId: state.pill.id, version: state.version, grade: state.grade,
    major: state.major, gender: state.gender, goal: state.goal,
    nick: state.nick, detail: state.detail, stateInfo: state.stateInfo,
    mood: state.mood, qIndex: state.qIndex, anxiety: state.anxiety,
    time: nowStr()
  };
  let recs = getRecords();
  recs.unshift(rec);
  const per = {};
  recs = recs.filter(r=>{ per[r.pillId]=(per[r.pillId]||0)+1; return per[r.pillId]<=5; });
  localStorage.setItem('pillRecords', JSON.stringify(recs));
}
function renderRecCard(pill, r){
  const s = Object.assign({}, r, {answer:(r.qIndex!=null && pill.q) ? pill.q.o[r.qIndex] : ''});
  const letter = buildLetter(pill, s);
  return `<div class="rec-card">
    <div class="rec-head">${esc(r.time)} · ${r.version==='pro'?'进阶定制':'普通配方'} · ${esc(r.grade||'')}${esc(r.major?(' · '+r.major):'')}</div>
    <div class="rec-letter">${esc(letter)}</div>
    <div class="rec-kv">${kvTags(pill, s)}</div>
  </div>`;
}
function openHistory(pid){
  const pill = PILLS.find(p=>p.id===pid);
  if(!pill) return;
  const recs = getRecords().filter(r=>r.pillId===pid);
  $('histTitle').textContent = `「${pill.name}」药方历史`;
  $('histSub').textContent = recs.length ? `共 ${recs.length} 次记录 · 按时间倒序` : '还没有药方记录';
  $('histList').innerHTML = recs.length
    ? recs.map(r=>renderRecCard(pill, r)).join('')
    : '<div class="hist-empty">这瓶药还没有留下药方记录。<br>去配一瓶并点「收进药盒」，就会出现在这里。</div>';
  $('historyModal').classList.add('show');
}
$('histClose').addEventListener('click', ()=>$('historyModal').classList.remove('show'));
$('historyModal').addEventListener('click', e=>{ if(e.target===$('historyModal')) $('historyModal').classList.remove('show'); });""")

# ---------- 6) JS：药盒已收集药瓶可点击查看历史 ----------
rep("""  $('boxGrid').innerHTML = PILLS.map(p=>{
    const got = state.collected.includes(p.id);
    return `<div class="box-slot ${got?'got':''}">${got?`<span class="bn">${p.no}</span><span>${p.name}</span>`:'<span class="bn">?</span><span>未集齐</span>'}</div>`;
  }).join('');""",
"""  $('boxGrid').innerHTML = PILLS.map(p=>{
    const got = state.collected.includes(p.id);
    if(got){
      return `<button class="box-slot got" data-id="${p.id}" aria-label="查看${p.name}药方历史"><span class="bn">${p.no}</span><span>${p.name}</span><span class="bsub">点按看记录</span></button>`;
    }
    return `<div class="box-slot"><span class="bn">?</span><span>未集齐</span></div>`;
  }).join('');
  $('boxGrid').querySelectorAll('.box-slot.got').forEach(btn=>{
    btn.addEventListener('click', ()=>openHistory(btn.dataset.id));
  });""")

# 写回（保持 CRLF）
with io.open(path, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(html)
print('patched ok, bytes:', len(html.encode('utf-8')))

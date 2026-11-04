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

# ---------- 1) CSS：历史记录里的行动清单 ----------
rep(""".hist-empty{text-align:center;color:var(--ink-soft);font-size:13.5px;line-height:2.1;padding:34px 0}""",
""".hist-empty{text-align:center;color:var(--ink-soft);font-size:13.5px;line-height:2.1;padding:34px 0}
.rec-acts{margin-top:12px;border-top:1px dashed var(--line);padding-top:11px}
.rec-acts .ra-head{font-size:12.5px;font-weight:700;color:var(--ink);margin-bottom:8px;letter-spacing:.5px}
.rec-acts ul{list-style:none;display:flex;flex-direction:column;gap:8px}
.rec-acts li{display:flex;gap:9px;align-items:flex-start;font-size:13px;color:var(--ink);cursor:pointer;line-height:1.7}
.rec-acts .tick{width:17px;height:17px;flex:none;border-radius:6px;border:1.5px solid var(--amber-deep);margin-top:2px;display:flex;align-items:center;justify-content:center;position:relative}
.rec-acts li.done > span:last-child{text-decoration:line-through;opacity:.6}
.rec-acts li.done .tick{background:var(--amber);border-color:var(--amber)}
.rec-acts li.done .tick::after{content:'✓'}""")

# ---------- 2) JS：保存记录时带上清单勾选状态 ----------
rep("""    mood: state.mood, qIndex: state.qIndex, anxiety: state.anxiety,
    time: nowStr()
  };""",
"""    mood: state.mood, qIndex: state.qIndex, anxiety: state.anxiety,
    time: nowStr(),
    done: Array.from(document.querySelectorAll('#actList li')).map(li=>li.classList.contains('done'))
  };""")

# ---------- 3) JS：历史卡渲染加入行动清单 + 记录索引 ----------
rep("""function renderRecCard(pill, r){
  const s = Object.assign({}, r, {answer:(r.qIndex!=null && pill.q) ? pill.q.o[r.qIndex] : ''});
  const letter = buildLetter(pill, s);
  return `<div class="rec-card">
    <div class="rec-head">${esc(r.time)} · ${r.version==='pro'?'进阶定制':'普通配方'} · ${esc(r.grade||'')}${esc(r.major?(' · '+r.major):'')}</div>
    <div class="rec-letter">${esc(letter)}</div>
    <div class="rec-kv">${kvTags(pill, s)}</div>
  </div>`;
}""",
"""function renderRecCard(pill, r, idx){
  const s = Object.assign({}, r, {answer:(r.qIndex!=null && pill.q) ? pill.q.o[r.qIndex] : ''});
  const letter = buildLetter(pill, s);
  const acts = (pill.actions||[]).map((a,i)=>{
    const d = r.done && r.done[i];
    return `<li data-i="${i}" class="${d?'done':''}"><span class="tick"></span><span>${a}</span></li>`;
  }).join('');
  return `<div class="rec-card" data-idx="${idx}">
    <div class="rec-head">${esc(r.time)} · ${r.version==='pro'?'进阶定制':'普通配方'} · ${esc(r.grade||'')}${esc(r.major?(' · '+r.major):'')}</div>
    <div class="rec-letter">${esc(letter)}</div>
    <div class="rec-kv">${kvTags(pill, s)}</div>
    <div class="rec-acts">
      <div class="ra-head">四年必做清单</div>
      <ul>${acts}</ul>
    </div>
  </div>`;
}""")

# ---------- 4) JS：历史列表渲染索引 + 清单可再次勾选并回存 ----------
rep("""  $('histList').innerHTML = recs.length
    ? recs.map(r=>renderRecCard(pill, r)).join('')
    : '<div class="hist-empty">这瓶药还没有留下药方记录。<br>去配一瓶并点「收进药盒」，就会出现在这里。</div>';
  $('historyModal').classList.add('show');""",
"""  $('histList').innerHTML = recs.length
    ? recs.map((r,idx)=>renderRecCard(pill, r, idx)).join('')
    : '<div class="hist-empty">这瓶药还没有留下药方记录。<br>去配一瓶并点「收进药盒」，就会出现在这里。</div>';
  $('histList').querySelectorAll('.rec-card').forEach(card=>{
    const idx = Number(card.dataset.idx);
    card.querySelectorAll('.rec-acts li').forEach(li=>{
      li.addEventListener('click', ()=>{
        li.classList.toggle('done');
        const done = Array.from(card.querySelectorAll('.rec-acts li')).map(x=>x.classList.contains('done'));
        updateRecordDone(pid, idx, done);
      });
    });
  });
  $('historyModal').classList.add('show');
}
function updateRecordDone(pid, idx, done){
  const recs = getRecords();
  let target = -1, seen = 0;
  for(let i=0;i<recs.length;i++){
    if(recs[i].pillId===pid){
      if(seen===idx){ target=i; break; }
      seen++;
    }
  }
  if(target>=0){
    recs[target].done = done;
    localStorage.setItem('pillRecords', JSON.stringify(recs));
  }
}""")

# 写回（保持 CRLF）
with io.open(path, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(html)
print('patched ok, bytes:', len(html.encode('utf-8')))

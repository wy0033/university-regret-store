# -*- coding: utf-8 -*-
import io

path = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(path, encoding='utf-8') as f:
    html = f.read()   # universal newlines -> \n

def rep(old, new, must=True):
    global html
    if old not in html:
        if must:
            raise AssertionError('NOT FOUND: ' + old[:80])
        return
    html = html.replace(old, new, 1)

# ---------- 1) CSS：版本选择 / 三列 seg / 进阶字段样式 ----------
rep(""".seg button:hover{border-color:var(--amber)}
.seg button.sel{background:var(--amber);border-color:var(--amber);color:#fff;font-weight:600}""",
""".seg button:hover{border-color:var(--amber)}
.seg button.sel{background:var(--amber);border-color:var(--amber);color:#fff;font-weight:600}
.seg-3{grid-template-columns:repeat(3,1fr)}
.ver-seg{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:26px}
.ver-btn{
  border:2px solid var(--line);border-radius:18px;background:var(--bg);padding:14px 16px;
  display:flex;flex-direction:column;gap:5px;align-items:flex-start;text-align:left;transition:all .2s;
}
.ver-btn .vt{font-size:16.5px;font-weight:700;color:var(--ink);letter-spacing:1px}
.ver-btn small{font-size:12px;color:var(--ink-soft);line-height:1.55}
.ver-btn:hover{border-color:var(--amber);transform:translateY(-2px);box-shadow:var(--shadow-sm)}
.ver-btn.sel{background:linear-gradient(145deg,var(--amber),var(--amber-deep));border-color:var(--amber);box-shadow:var(--shadow-sm)}
.ver-btn.sel .vt{color:#fff}
.ver-btn.sel small{color:rgba(255,255,255,.88)}
.pro-fields{
  border-top:1.5px dashed var(--line);padding-top:20px;margin-top:2px;
  animation:rise .35s ease both;
}
.ver-tip{
  font-size:12.5px;color:var(--amber-deep);background:rgba(245,201,123,.16);
  border:1px dashed var(--amber);border-radius:12px;padding:9px 14px;margin:14px 0 2px;line-height:1.6;
}""")

# ---------- 2) HTML：输入屏（版本选择 + 性别 + 期望目标 + 进阶字段） ----------
old_form = """    <div class="form-card">
      <h3 id="inputTitle">来，把方子告诉我</h3>
      <p class="form-sub" id="inputSub">配药前，我需要知道三件事</p>

      <div class="field">
        <label>你现在大几？</label>
        <div class="seg" id="gradeSeg">
          <button data-grade="大一">大一</button>
          <button data-grade="大二">大二</button>
          <button data-grade="大三">大三</button>
          <button data-grade="大四">大四</button>
        </div>
      </div>

      <div class="field">
        <label for="majorInput">你的专业 / 学院</label>
        <input class="text-input" id="majorInput" type="text" placeholder="比如：自动化学院" maxlength="30">
        <div class="hint">告诉我专业，四年后的信里会有专属于你的细节</div>
      </div>

      <div class="field">
        <label for="anxietyInput" id="anxietyLabel">最近最让你焦虑的一件事</label>
        <input class="text-input" id="anxietyInput" type="text" placeholder="比如：自动控制原理好难" maxlength="40">
        <div class="hint">一句话就够，越具体，信越扎心</div>
      </div>

      <div class="form-actions">
        <button class="btn btn-ghost" id="backToPick">返回货架</button>
        <button class="btn btn-primary" id="startMix">开始配药</button>
      </div>
    </div>"""
new_form = """    <div class="form-card">
      <h3 id="inputTitle">来，把方子告诉我</h3>
      <p class="form-sub" id="inputSub">配药前，选一个配方：速配，或深度定制</p>

      <div class="ver-seg" id="verSeg">
        <button class="ver-btn sel" data-ver="normal">
          <span class="vt">普通配方</span>
          <small>基础信息 · 一分钟速配</small>
        </button>
        <button class="ver-btn" data-ver="pro">
          <span class="vt">进阶定制</span>
          <small>加昵称与小故事 · 信更懂你</small>
        </button>
      </div>

      <div class="field">
        <label>你现在大几？</label>
        <div class="seg" id="gradeSeg">
          <button data-grade="大一">大一</button>
          <button data-grade="大二">大二</button>
          <button data-grade="大三">大三</button>
          <button data-grade="大四">大四</button>
        </div>
      </div>

      <div class="field">
        <label for="majorInput">你的专业 / 学院</label>
        <input class="text-input" id="majorInput" type="text" placeholder="比如：自动化学院" maxlength="30">
        <div class="hint">告诉我专业，四年后的信里会有专属于你的细节</div>
      </div>

      <div class="field">
        <label>你的性别</label>
        <div class="seg seg-3" id="genderSeg">
          <button data-gender="男生">男生</button>
          <button data-gender="女生">女生</button>
          <button data-gender="保密">保密</button>
        </div>
        <div class="hint">用于挑选朗读音色，也让信更贴合你</div>
      </div>

      <div class="field">
        <label for="goalInput">你的期望目标</label>
        <input class="text-input" id="goalInput" type="text" placeholder="比如：四年后能站在台上从容答辩" maxlength="30">
        <div class="hint">告诉四年后的你想成为什么样的人，信里会有回音</div>
      </div>

      <div class="field">
        <label for="anxietyInput" id="anxietyLabel">最近最让你焦虑的一件事</label>
        <input class="text-input" id="anxietyInput" type="text" placeholder="比如：自动控制原理好难" maxlength="40">
        <div class="hint">一句话就够，越具体，信越扎心</div>
      </div>

      <div id="proFields" style="display:none">
        <div class="ver-tip">进阶定制：再多告诉我两件小事，四年后的信会把它们写进去</div>
        <div class="field">
          <label for="nickInput">你的昵称 / 想被叫的名字</label>
          <input class="text-input" id="nickInput" type="text" placeholder="比如：阿澈" maxlength="12">
          <div class="hint">信的称呼会换成它，像老朋友来信</div>
        </div>
        <div class="field">
          <label for="detailInput">最近一件让你觉得可惜的小事</label>
          <input class="text-input" id="detailInput" type="text" placeholder="比如：错过了一次答疑，再没敢问" maxlength="40">
          <div class="hint">别小看它，四年后的你记得很清楚</div>
        </div>
      </div>

      <div class="form-actions">
        <button class="btn btn-ghost" id="backToPick">返回货架</button>
        <button class="btn btn-primary" id="startMix"><span id="mixBtnLabel">开始配药</span></button>
      </div>
    </div>"""
rep(old_form, new_form)

# 朗读说明文案
rep('温柔女声 · 深夜电台语速 · 自动朗读信件正文',
    '温柔女声 · 深夜电台语速 · 按你选的性别匹配音色')

# ---------- 3) JS：状态字段 ----------
rep("let state = {screen:'open', pill:null, grade:'大二', major:'', anxiety:'', collected:[]};",
    "let state = {screen:'open', pill:null, version:'normal', grade:'大二', major:'', gender:'保密', goal:'', nick:'', detail:'', anxiety:'', collected:[]};")

# ---------- 4) JS：信件合成（昵称 / 期望目标 / 小故事织入） ----------
rep("""function fill(text, d){
  return text.replace('{anxiety}', d.anxiety || '那件让你睡不着的事')
             .replace('{grade}', d.grade || '大二')
             .replace('{major}', d.major || '大学');
}""",
"""function fill(text, d){
  return text.replace('{anxiety}', d.anxiety || '那件让你睡不着的事')
             .replace('{grade}', d.grade || '大二')
             .replace('{major}', d.major || '大学');
}
function buildLetter(p, s){
  let t = fill(p.letter, s);
  t = t.replace('嘿，现在的你', '嘿，' + (s.nick || '现在的你'));
  if(s.version==='pro' && s.detail) t = t.replace('——', '对了，你还记得「' + s.detail + '」吗？当时你觉得好可惜。四年后的我可以告诉你：那件事后来有了个还不错的结果，你从中拿到了比结果更重要的东西。\\n\\n——');
  if(s.goal) t = t.replace('——', '还有，你写下的期望目标「' + s.goal + '」——四年后的我可以告诉你：你做到了。\\n\\n——');
  return t;
}""")

# ---------- 5) JS：choose 重置版本与性别 UI ----------
rep("""  $('anxietyInput').placeholder = state.pill.anxietyPh;
  $('gradeSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.grade===state.grade));
  showScreen('input');
}""",
"""  $('anxietyInput').placeholder = state.pill.anxietyPh;
  resetVersion();
  $('gradeSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.grade===state.grade));
  $('genderSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.gender===state.gender));
  showScreen('input');
}
function resetVersion(){
  state.version = 'normal';
  $('verSeg').querySelectorAll('.ver-btn').forEach(b=>b.classList.toggle('sel', b.dataset.ver==='normal'));
  $('proFields').style.display = 'none';
  $('mixBtnLabel').textContent = '开始配药';
}""")

# ---------- 6) JS：版本 / 性别切换监听 ----------
rep("""$('gradeSeg').addEventListener('click', e=>{
  const b = e.target.closest('button'); if(!b) return;
  state.grade = b.dataset.grade;
  $('gradeSeg').querySelectorAll('button').forEach(x=>x.classList.toggle('sel', x===b));
});""",
"""$('gradeSeg').addEventListener('click', e=>{
  const b = e.target.closest('button'); if(!b) return;
  state.grade = b.dataset.grade;
  $('gradeSeg').querySelectorAll('button').forEach(x=>x.classList.toggle('sel', x===b));
});
$('verSeg').addEventListener('click', e=>{
  const b = e.target.closest('.ver-btn'); if(!b) return;
  state.version = b.dataset.ver;
  $('verSeg').querySelectorAll('.ver-btn').forEach(x=>x.classList.toggle('sel', x===b));
  $('proFields').style.display = state.version==='pro' ? 'block' : 'none';
  $('mixBtnLabel').textContent = state.version==='pro' ? '开始深度配药' : '开始配药';
  if(state.version==='pro') toast('进阶定制：多填两项，信件会更懂你');
});
$('genderSeg').addEventListener('click', e=>{
  const b = e.target.closest('button'); if(!b) return;
  state.gender = b.dataset.gender;
  $('genderSeg').querySelectorAll('button').forEach(x=>x.classList.toggle('sel', x===b));
});""")

# ---------- 7) JS：startMix 读取新字段 ----------
rep("""$('startMix').addEventListener('click', ()=>{
  state.major = $('majorInput').value.trim();
  state.anxiety = $('anxietyInput').value.trim();
  if(!state.pill){ toast('请先选一瓶药'); showScreen('pick'); return; }""",
"""$('startMix').addEventListener('click', ()=>{
  state.major = $('majorInput').value.trim();
  state.anxiety = $('anxietyInput').value.trim();
  state.goal = $('goalInput').value.trim();
  state.nick = $('nickInput').value.trim();
  state.detail = $('detailInput').value.trim();
  if(!state.pill){ toast('请先选一瓶药'); showScreen('pick'); return; }""")

# ---------- 8) JS：成品屏（buildLetter + 关键词卡含性别/期望/昵称） ----------
rep("  const letter = fill(p.letter, state);",
    "  const letter = buildLetter(p, state);")
rep("""  $('kcardBody').innerHTML = [
    `<span class="kv"><b>${esc(state.major||'大学')}</b></span>`,
    `<span class="kv"><b>${esc(state.grade)}</b></span>`,
    `<span class="kv">正在：${esc(state.anxiety||'为一点小事烦恼')}</span>`,
    `<span class="kv">${p.keyword[0]}</span>`
  ].join('');""",
"""  const kv = [];
  kv.push(`<span class="kv"><b>${esc(state.major||'大学')}</b></span>`);
  kv.push(`<span class="kv"><b>${esc(state.grade)}</b></span>`);
  kv.push(`<span class="kv"><b>${esc(state.gender)}</b></span>`);
  if(state.goal) kv.push(`<span class="kv">期望：${esc(state.goal)}</span>`);
  if(state.version==='pro' && state.nick) kv.push(`<span class="kv">致：${esc(state.nick)}</span>`);
  kv.push(`<span class="kv">正在：${esc(state.anxiety||'为一点小事烦恼')}</span>`);
  kv.push(`<span class="kv">${p.keyword[0]}</span>`);
  $('kcardBody').innerHTML = kv.join('');""")

# ---------- 9) JS：语音按性别选音色 + 朗读完整定制信 ----------
rep("""function pickVoice(){
  if(!('speechSynthesis' in window)) return null;
  const voices = speechSynthesis.getVoices();
  const zh = voices.filter(v=>v.lang && v.lang.toLowerCase().startsWith('zh'));
  if(!zh.length) return null;
  return zh.find(v=>/女|female|xiaoxiao|huihui|meijia/i.test(v.name)) || zh[0];
}""",
"""function pickVoice(g){
  if(!('speechSynthesis' in window)) return null;
  const voices = speechSynthesis.getVoices();
  const zh = voices.filter(v=>v.lang && v.lang.toLowerCase().startsWith('zh'));
  if(!zh.length) return null;
  if(g==='男生') return zh.find(v=>/男|male|yunjian|tingting/i.test(v.name)) || zh[0];
  return zh.find(v=>/女|female|xiaoxiao|huihui|meijia/i.test(v.name)) || zh[0];
}""")
rep("  const text = fill(state.pill.letter, state);\n  const u = new SpeechSynthesisUtterance(text);\n  const v = pickVoice();",
    "  const text = buildLetter(state.pill, state);\n  const u = new SpeechSynthesisUtterance(text);\n  const v = pickVoice(state.gender);")

# 写回（保持 CRLF 与全文件一致）
with io.open(path, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(html)
print('patched ok, bytes:', len(html.encode('utf-8')))

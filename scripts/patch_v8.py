# -*- coding: utf-8 -*-
import io

path = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(path, encoding='utf-8') as f:
    html = f.read()

def rep(old, new, must=True):
    global html
    if old not in html:
        if must:
            raise AssertionError('NOT FOUND: ' + old[:80])
        return
    html = html.replace(old, new, 1)

# ---------- 1) CSS：分享弹窗 ----------
rep(""".night-remind{display:none;position:fixed;left:50%;bottom:20px;transform:translateX(-50%);z-index:70;""",
""".share-card{background:var(--bg);border:1.5px solid var(--line);border-radius:18px;padding:16px 18px;margin-bottom:16px}
.share-kv{display:flex;flex-wrap:wrap;gap:6px}
.share-kv .kv{background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:4px 12px;font-size:12.5px}
.share-kv .kv b{color:var(--amber-deep)}
.share-text{margin-top:14px;font-size:13.5px;line-height:2;color:var(--ink-soft);white-space:pre-line;border-top:1px dashed var(--line);padding-top:12px}
.share-copy{width:100%;margin-bottom:10px}
.night-remind{display:none;position:fixed;left:50%;bottom:20px;transform:translateX(-50%);z-index:70;""")

# ---------- 2) HTML：分享弹窗 ----------
rep("""<div class="night-remind" id="nightRemind">夜深了，配完这瓶药，早点休息</div>""",
"""<!-- ===== 分享弹窗 ===== -->
<div class="modal-mask" id="shareModal">
  <div class="modal">
    <h3 id="shareTitle">分享这瓶药</h3>
    <p class="modal-sub">把四年后的答案，递给朋友</p>
    <div class="share-card">
      <div class="share-kv" id="shareKv"></div>
      <div class="share-text" id="shareText"></div>
    </div>
    <button class="btn btn-primary share-copy" id="shareCopy">复制链接，去微信打开</button>
    <button class="modal-close" id="shareClose">收起</button>
  </div>
</div>

<div class="night-remind" id="nightRemind">夜深了，配完这瓶药，早点休息</div>""")

# ---------- 3) JS：分享逻辑改造 ----------
rep("""/* ===== 分享 ===== */
$('shareBtn').addEventListener('click', async ()=>{
  const p = state.pill;
  const text = `我在「大学后悔药便利店」配了一瓶「${p.name}」后悔药\\n${state.major||'大学'} | ${state.grade} | ${state.anxiety||'正在烦恼'} | ${p.keyword[0]}\\n—— 不是工具，是情绪出口。`;
  if(navigator.share){
    try{ await navigator.share({title:'大学后悔药便利店', text, url:location.href}); return; }catch(e){}
  }
  try{
    await navigator.clipboard.writeText(text + '\\n' + location.href);
    toast('关键词卡已复制，去分享给朋友吧');
  }catch(e){ toast('复制失败，可以截图关键词卡分享'); }
});""",
"""/* ===== 分享 ===== */
function legacyCopy(t){
  try{
    const ta = document.createElement('textarea');
    ta.value = t;
    ta.style.position='fixed'; ta.style.opacity='0';
    document.body.appendChild(ta);
    ta.select();
    const ok = document.execCommand('copy');
    document.body.removeChild(ta);
    return ok;
  }catch(e){ return false; }
}
function copyText(t){
  if(navigator.clipboard && navigator.clipboard.writeText){
    return navigator.clipboard.writeText(t).then(()=>true).catch(()=>legacyCopy(t));
  }
  return Promise.resolve(legacyCopy(t));
}
function buildShareText(p){
  return `我在「大学后悔药便利店」配了一瓶「${p.name}」后悔药\\n${state.grade||''} ${state.major||'大学'} | ${state.anxiety||'正在烦恼'} | ${p.keyword[0]}\\n—— 不是工具，是情绪出口。`;
}
$('shareBtn').addEventListener('click', ()=>{
  const p = state.pill;
  $('shareTitle').textContent = `「${p.name}」后悔药`;
  $('shareKv').innerHTML = kvTags(p, state);
  $('shareText').textContent = buildShareText(p);
  $('shareModal').classList.add('show');
});
$('shareCopy').addEventListener('click', async ()=>{
  const ok = await copyText(buildShareText(state.pill) + '\\n' + location.href);
  toast(ok ? '已复制，去微信粘贴就能打开' : '复制失败，可以长按链接手动复制');
});
$('shareClose').addEventListener('click', ()=>$('shareModal').classList.remove('show'));
$('shareModal').addEventListener('click', e=>{ if(e.target===$('shareModal')) $('shareModal').classList.remove('show'); });""")

# 写回（保持 CRLF）
with io.open(path, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(html)
print('patched ok, bytes:', len(html.encode('utf-8')))

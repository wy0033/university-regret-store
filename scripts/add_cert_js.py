# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) collect 第 8 瓶：openBox 后弹证书
old = """  if(state.collected.length===8){
    toast('8 瓶集齐！你的「大学结业证书」已解锁');
    openBox();
  }"""
new = """  if(state.collected.length===8){
    toast('8 瓶集齐！你的「大学结业证书」已解锁');
    openBox();
    showCert();
  }"""
assert s.count(old) == 1, 'collect 8'
s = s.replace(old, new)

# 2) openBox 药盒内证书加用户名
old = """    $('certName').innerHTML = `恭喜你，8 瓶后悔药全部集齐。<br>你把四年里每一个「如果当初」都收好了，<br>接下来的路，好好走。`;"""
new = """    $('certName').innerHTML = `兹证明 <b>${esc(state.user||'你')}</b> 同学，8 瓶后悔药全部集齐。<br>你把四年里每一个「如果当初」都收好了，<br>接下来的路，好好走。`;"""
assert s.count(old) == 1, 'certName'
s = s.replace(old, new)

# 3) 证书弹窗 JS（插在 /* ===== 公告 ===== */ 之前）
cert_js = """/* ===== 证书 ===== */
function copyText(txt){
  if(navigator.clipboard && window.isSecureContext){
    navigator.clipboard.writeText(txt).then(()=>toast('证书已复制，去粘贴给朋友吧')).catch(()=>fallbackCopy(txt));
  }else{
    fallbackCopy(txt);
  }
}
function fallbackCopy(txt){
  try{
    const ta = document.createElement('textarea');
    ta.value = txt;
    ta.style.position = 'fixed'; ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    toast('证书已复制，去粘贴给朋友吧');
  }catch(e){ toast('复制失败，请手动长按选择复制'); }
}
function showCert(){
  const name = state.user || '同学';
  $('certUserName').textContent = name + ' 同学';
  const d = new Date();
  $('certDate').textContent = d.getFullYear() + ' 年 ' + (d.getMonth()+1) + ' 月';
  $('certCard').classList.remove('zoom');
  $('certModal').classList.add('show');
}
$('certCard').addEventListener('click', ()=>$('certCard').classList.toggle('zoom'));
$('certCopy').addEventListener('click', ()=>{
  const name = state.user || '同学';
  const d = new Date();
  const txt = '大学结业证书\\n\\n兹证明 ' + name + ' 同学\\n已集齐「大学后悔药便利店」全部 8 瓶后悔药\\n把四年里每一个「如果当初」都收好了\\n特发此证，以资鼓励。\\n\\n大学后悔药便利店 · ' + d.getFullYear() + ' 年 ' + (d.getMonth()+1) + ' 月';
  copyText(txt);
});
$('certClose').addEventListener('click', ()=>$('certModal').classList.remove('show'));
$('certModal').addEventListener('click', e=>{ if(e.target===$('certModal')) $('certModal').classList.remove('show'); });

/* ===== 公告 ===== */"""
old = "/* ===== 公告 ===== */"
assert s.count(old) == 1, 'cert js anchor'
s = s.replace(old, cert_js)

io.open(p, 'w', encoding='utf-8').write(s)
print('cert js ok')

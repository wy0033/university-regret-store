# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) 按钮文案
old = '<button class="btn-soft" id="certCopy" type="button">复制证书</button>'
new = '<button class="btn-soft" id="certCopy" type="button">复制证书图片</button>'
assert s.count(old) == 1, 'copy btn'
s = s.replace(old, new)

# 2) 替换复制逻辑：canvas 绘制证书图片 → 剪贴板复制，失败则下载
old = """$('certCopy').addEventListener('click', ()=>{
  const name = state.user || '同学';
  const d = new Date();
  const txt = '大学结业证书\\n\\n兹证明 ' + name + ' 同学\\n已集齐「大学后悔药便利店」全部 8 瓶后悔药\\n把四年里每一个「如果当初」都收好了\\n特发此证，以资鼓励。\\n\\n大学后悔药便利店 · ' + d.getFullYear() + ' 年 ' + (d.getMonth()+1) + ' 月';
  copyText(txt);
});"""
new = """function roundRectPath(x,y,w,h,r){
  x.beginPath();
  x.moveTo(w,y+r); x.arcTo(w,y,w,h-r,r); x.arcTo(w,h,w-r,h,r);
  x.arcTo(0,h,r,h,r); x.arcTo(0,y,0,y+r,r);
  x.closePath();
}
function certImage(){
  return new Promise(async resolve=>{
    try{ await document.fonts.ready; }catch(e){}
    const W=900, H=620, c=document.createElement('canvas');
    c.width=W; c.height=H;
    const x=c.getContext('2d');
    const g=x.createLinearGradient(0,0,W,H);
    g.addColorStop(0,'#F5C97B'); g.addColorStop(1,'#E8A87C');
    x.fillStyle=g; roundRectPath(x,0,0,W,H,26); x.fill();
    x.strokeStyle='rgba(255,255,255,.6)'; x.lineWidth=3;
    roundRectPath(x,26,26,W-52,H-52,16); x.stroke();
    x.strokeStyle='rgba(255,255,255,.35)'; x.lineWidth=1.5;
    roundRectPath(x,40,40,W-80,H-80,12); x.stroke();
    const name = state.user || '同学';
    const d = new Date();
    x.textAlign='center';
    x.fillStyle='#fff';
    x.font='700 54px "Ma Shan Zheng","楷体",serif';
    x.fillText('大学结业证书', W/2, 132);
    x.font='16px "Noto Serif SC","宋体",serif';
    x.fillStyle='rgba(255,255,255,.88)';
    x.fillText('—— 大学后悔药便利店 ——', W/2, 172);
    let y=250;
    x.fillStyle='#fff';
    x.font='700 42px "Ma Shan Zheng","楷体",serif';
    x.fillText(name+' 同学', W/2, y);
    const nm = x.measureText(name+' 同学');
    x.strokeStyle='rgba(255,255,255,.7)'; x.lineWidth=2;
    x.beginPath(); x.moveTo(W/2-nm.width/2, y+10); x.lineTo(W/2+nm.width/2, y+10); x.stroke();
    y += 70;
    x.font='21px "Noto Serif SC","宋体",serif';
    x.fillStyle='rgba(255,255,255,.95)';
    x.fillText('已集齐「大学后悔药便利店」全部 8 瓶后悔药，', W/2, y); y+=38;
    x.fillText('把四年里每一个「如果当初」都收好了。', W/2, y); y+=38;
    x.fillText('特发此证，以资鼓励。', W/2, y);
    x.save(); x.translate(W-118, 128); x.rotate(-12*Math.PI/180);
    x.strokeStyle='rgba(255,255,255,.9)'; x.lineWidth=6;
    x.beginPath(); x.arc(0,0,46,0,Math.PI*2); x.stroke();
    x.font='700 21px "Noto Serif SC","宋体",serif';
    x.textBaseline='middle'; x.fillStyle='rgba(255,255,255,.9)';
    x.fillText('合格',0,2);
    x.restore();
    x.font='19px "Noto Serif SC","宋体",serif';
    x.fillStyle='rgba(255,255,255,.95)';
    x.textAlign='left';
    x.fillText('大学后悔药便利店', 70, H-88);
    x.textAlign='right';
    x.fillText(d.getFullYear()+' 年 '+(d.getMonth()+1)+' 月', W-70, H-88);
    resolve(c);
  });
}
function downloadCert(c){
  const a = document.createElement('a');
  a.download = '大学结业证书-' + (state.user||'同学') + '.png';
  a.href = c.toDataURL('image/png');
  document.body.appendChild(a); a.click(); document.body.removeChild(a);
  toast('已为你生成证书图片，请保存后发送给朋友');
}
$('certCopy').addEventListener('click', async ()=>{
  const c = await certImage();
  try{
    const blob = await new Promise(res=>c.toBlob(res,'image/png'));
    if(blob && navigator.clipboard && navigator.clipboard.write && window.isSecureContext){
      await navigator.clipboard.write([new ClipboardItem({'image/png': blob})]);
      toast('证书图片已复制，直接粘贴到微信就能发送');
      return;
    }
    throw new Error('clipboard unavailable');
  }catch(e){
    downloadCert(c);
  }
});"""
assert s.count(old) == 1, 'certCopy handler'
s = s.replace(old, new)

# 3) 移除不再使用的文字复制函数（copyText/fallbackCopy）
old = """function copyText(txt){
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
"""
assert s.count(old) == 1, 'copyText removal'
s = s.replace(old, '')

io.open(p, 'w', encoding='utf-8').write(s)
print('cert image ok')

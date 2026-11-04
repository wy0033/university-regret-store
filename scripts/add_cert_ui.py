# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) HTML：证书弹窗（插在 <!-- ===== 分享弹窗 ===== --> 之前）
cert_html = """<!-- ===== 证书弹窗 ===== -->
<div class="modal-mask" id="certModal">
  <div class="cert-pop">
    <div class="cert cert-card" id="certCard" title="点击放大 / 缩小">
      <div class="stamp">合格</div>
      <h4>大学结业证书</h4>
      <p class="cert-body">
        兹证明<br>
        <b class="cert-name" id="certUserName">○○ 同学</b><br>
        已集齐「大学后悔药便利店」全部 8 瓶后悔药，<br>
        把四年里每一个「如果当初」都收好了。<br>
        特发此证，以资鼓励。
      </p>
      <div class="cert-foot">
        <span>大学后悔药便利店</span>
        <span id="certDate">2026 年 9 月</span>
      </div>
    </div>
    <div class="cert-acts">
      <button class="btn-soft" id="certCopy" type="button">复制证书</button>
      <button class="btn-main" id="certClose" type="button">退出</button>
    </div>
  </div>
</div>

<!-- ===== 分享弹窗 ===== -->"""
old = "<!-- ===== 分享弹窗 ===== -->"
assert s.count(old) == 1, 'cert modal anchor'
s = s.replace(old, cert_html)

# 2) CSS：证书弹窗（插在 rankup 动画后）
old = """@keyframes rankpop{0%{transform:scale(.4);opacity:0}70%{transform:scale(1.15)}100%{transform:scale(1);opacity:1}}"""
new = """@keyframes rankpop{0%{transform:scale(.4);opacity:0}70%{transform:scale(1.15)}100%{transform:scale(1);opacity:1}}
#certModal{z-index:250}
.cert-pop{width:min(600px,94vw);text-align:center}
.cert-card{cursor:zoom-in;transition:transform .3s;margin:0}
.cert-card.zoom{cursor:zoom-out;transform:scale(1.22)}
.cert-body{font-size:14.5px;line-height:2.05}
.cert-name{font-family:var(--font-title);font-size:21px;letter-spacing:3px;text-decoration:underline;text-decoration-color:rgba(255,255,255,.6);text-underline-offset:4px}
.cert-foot{display:flex;justify-content:space-between;margin-top:18px;font-size:12.5px;opacity:.95;border-top:1px dashed rgba(255,255,255,.55);padding-top:12px}
.cert-acts{display:flex;gap:12px;justify-content:center;margin-top:18px}
.cert-acts .btn-soft,.cert-acts .btn-main{flex:1;max-width:210px}"""
assert s.count(old) == 1, 'cert css'
s = s.replace(old, new)

io.open(p, 'w', encoding='utf-8').write(s)
print('cert html/css ok')

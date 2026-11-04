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

# ---------- 1) CSS：货架 + 名言 + 夜间休息提醒 ----------
rep(""".pill-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}""",
""".pill-grid{display:flex;flex-direction:column;gap:22px}
.shelf-row{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.plank{height:16px;border-radius:10px;margin:-6px 3px 0;
  background:linear-gradient(180deg,#dda06a,#bb824e 55%,#9a6a3c);
  box-shadow:0 5px 12px rgba(130,85,40,.28),inset 0 2px 0 rgba(255,255,255,.38),inset 0 -2px 0 rgba(90,55,20,.25)}
.plank::after{content:'';display:block;height:3px;border-radius:2px;margin:0 12px;background:rgba(255,255,255,.25)}""")

rep(""".pill-card .ppromise{font-size:12.5px;color:var(--ink-soft);line-height:1.6}""",
""".pill-card .ppromise{font-size:12.5px;color:var(--ink-soft);line-height:1.6}
.mix-quote{margin-top:30px;font-size:15.5px;line-height:2;color:var(--ink);letter-spacing:.5px;font-weight:600}
.mix-quote b{display:block;margin-top:8px;font-size:12px;color:var(--amber-deep);font-weight:600;letter-spacing:2px}
.night-remind{display:none;position:fixed;left:50%;bottom:20px;transform:translateX(-50%);z-index:70;
  background:rgba(30,24,44,.94);color:#f6e7c9;border:1px solid rgba(245,201,123,.38);
  padding:11px 22px;border-radius:999px;font-size:13.5px;letter-spacing:1px;
  box-shadow:0 10px 26px rgba(0,0,0,.38);cursor:pointer;align-items:center;gap:9px}
body.night .night-remind{display:flex;animation:riseIn .7s ease .9s both}
.night-remind::before{content:'';width:8px;height:8px;border-radius:50%;background:#f5c97b;box-shadow:0 0 10px #f5c97b;flex:none}
@keyframes riseIn{from{opacity:0;transform:translateX(-50%) translateY(16px)}to{opacity:1;transform:translateX(-50%) translateY(0)}}""")

# ---------- 2) 响应式：货架行在窄屏 2 列 ----------
rep("""  .pill-grid{grid-template-columns:repeat(2,1fr);gap:13px}""",
"""  .shelf-row{grid-template-columns:repeat(2,1fr);gap:13px}
  .pill-grid{gap:16px}""")

# ---------- 3) HTML：货架分层（2 行 × 4 瓶 + 层板） ----------
rep("""    <div class="pill-grid" id="pillGrid">
    <div class="pill-card" data-id="p1" tabindex="0" role="button" aria-label="选择不挂科后悔药">""",
"""    <div class="pill-grid" id="pillGrid">
    <div class="shelf-row">
    <div class="pill-card" data-id="p1" tabindex="0" role="button" aria-label="选择不挂科后悔药">""")

rep("""      </div>
    <div class="pill-card" data-id="p5" tabindex="0" role="button" aria-label="选择和好如初后悔药">""",
"""      </div>
    </div>
    <div class="plank"></div>
    <div class="shelf-row">
    <div class="pill-card" data-id="p5" tabindex="0" role="button" aria-label="选择和好如初后悔药">""")

rep("""        <div class="body"><div class="pname"></div><div class="ptag"></div><div class="ppromise"></div></div>
      </div>
  </div>
  </section>""",
"""        <div class="body"><div class="pname"></div><div class="ptag"></div><div class="ppromise"></div></div>
      </div>
    </div>
    <div class="plank"></div>
  </div>
  </section>""")

# ---------- 4) HTML：配药屏加名言行 ----------
rep("""      <div class="mix-note" id="mixNote">配方师说：你的焦虑正在被研磨，请稍等三分钟。</div>""",
"""      <div class="mix-note" id="mixNote">配方师说：你的焦虑正在被研磨，请稍等三分钟。</div>
      <div class="mix-quote" id="mixQuote"></div>""")

# ---------- 5) HTML：夜间休息提醒（toast 前） ----------
rep("""<div id="toast" role="status"></div>""",
"""<div class="night-remind" id="nightRemind">夜深了，配完这瓶药，早点休息</div>
<div id="toast" role="status"></div>""")

# ---------- 6) JS：8 瓶药加名人名言 ----------
quotes = {
 "'不挂科'": "{t:'聪明在于勤奋，天才在于积累',a:'华罗庚'}",
 "'敢说话'": "{t:'一个人的成功，85% 靠的是勇气与表达',a:'戴尔·卡耐基'}",
 "'不内耗'": "{t:'人生如逆旅，我亦是行人',a:'苏轼《临江仙·送钱穆父》'}",
 "'去爱吧'": "{t:'于千万人之中遇见你所要遇见的人',a:'张爱玲《爱》'}",
 "'和好如初'": "{t:'径路窄处，留一步与人行',a:'洪应明《菜根谭》'}",
 "'向前走'": "{t:'其实地上本没有路，走的人多了，也便成了路',a:'鲁迅《故乡》'}",
 "'不将就'": "{t:'天生我材必有用',a:'李白《将进酒》'}",
 "'不熬夜'": "{t:'早睡早起，使人健康、富有、聪明',a:'本杰明·富兰克林'}",
}
for key, q in quotes.items():
    anchor = "name:{0}, tag:".format(key)
    assert anchor in html, 'quote anchor missing: ' + key
    html = html.replace(anchor, "name:{0}, quote:{1}, tag:".format(key, q), 1)

# ---------- 7) JS：配药动画显示名言 ----------
rep("""function runMix(){
  let i = 0;
  $('mixStep').textContent = MIX_STEPS[0];
  $('mixLine').textContent = state.pill.loading[0];""",
"""function runMix(){
  let i = 0;
  $('mixQuote').innerHTML = '“' + state.pill.quote.t + '”<b>—— ' + state.pill.quote.a + '</b>';
  $('mixStep').textContent = MIX_STEPS[0];
  $('mixLine').textContent = state.pill.loading[0];""")

# ---------- 8) JS：深夜场提醒 ----------
rep("""  toast(on ? '深夜场已开：夜风免费，心事打折' : '已切回日间场');
});""",
"""  toast(on ? '深夜场已开：夜风免费，心事打折。夜深了，早点休息' : '已切回日间场');
});
$('nightRemind').addEventListener('click', ()=>$('nightRemind').style.display='none');""")

# 写回（保持 CRLF）
with io.open(path, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(html)
print('patched ok, bytes:', len(html.encode('utf-8')))

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

# ---------- 1) CSS：flex 胶囊选项 ----------
rep(""".ver-tip{
  font-size:12.5px;color:var(--amber-deep);background:rgba(245,201,123,.16);
  border:1px dashed var(--amber);border-radius:12px;padding:9px 14px;margin:14px 0 2px;line-height:1.6;
}""",
""".ver-tip{
  font-size:12.5px;color:var(--amber-deep);background:rgba(245,201,123,.16);
  border:1px dashed var(--amber);border-radius:12px;padding:9px 14px;margin:14px 0 2px;line-height:1.6;
}
.seg-flex{display:flex;flex-wrap:wrap;gap:10px}
.seg-flex button{
  padding:9px 16px;border-radius:999px;border:1.5px solid var(--line);background:var(--bg);
  font-size:13.5px;color:var(--ink-soft);transition:all .18s;
}
.seg-flex button:hover{border-color:var(--amber)}
.seg-flex button.sel{background:var(--amber);border-color:var(--amber);color:#fff;font-weight:600}""")

# ---------- 2) HTML：进阶字段（昵称 / 状态 / 心理 / 专属问题 / 小故事） ----------
old_pro = """      <div id="proFields" style="display:none">
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
      </div>"""
new_pro = """      <div id="proFields" style="display:none">
        <div class="ver-tip">进阶定制：再多告诉我几件小事，四年后的信会把它们全部写进去</div>
        <div class="field">
          <label for="nickInput">你的昵称 / 想被叫的名字</label>
          <input class="text-input" id="nickInput" type="text" placeholder="比如：阿澈" maxlength="12">
          <div class="hint">信的称呼会换成它，像老朋友来信</div>
        </div>
        <div class="field">
          <label>你目前的状态</label>
          <div class="seg-flex" id="stateSeg">
            <button data-state="学业压力大">学业压力大</button>
            <button data-state="社团活动忙">社团活动忙</button>
            <button data-state="备考冲刺中">备考冲刺中</button>
            <button data-state="迷茫期">迷茫期</button>
            <button data-state="想躺平休息">想躺平休息</button>
          </div>
          <div class="hint">点一个最贴近的，四年后的信会记得</div>
        </div>
        <div class="field">
          <label>你的心理情况</label>
          <div class="seg-flex" id="moodSeg">
            <button data-mood="有点焦虑">有点焦虑</button>
            <button data-mood="有点迷茫">有点迷茫</button>
            <button data-mood="有点疲惫">有点疲惫</button>
            <button data-mood="比较平静">比较平静</button>
            <button data-mood="有点低落">有点低落</button>
          </div>
          <div class="hint">如实说就好，这里没有对错</div>
        </div>
        <div class="field">
          <label id="qLabel">专属问题</label>
          <div class="seg-flex" id="qSeg"></div>
          <div class="hint">选完这瓶药专属的一题，答案会被写进信里</div>
        </div>
        <div class="field">
          <label for="detailInput">最近一件让你觉得可惜的小事</label>
          <input class="text-input" id="detailInput" type="text" placeholder="比如：错过了一次答疑，再没敢问" maxlength="40">
          <div class="hint">别小看它，四年后的你记得很清楚</div>
        </div>
      </div>"""
rep(old_pro, new_pro)

# ---------- 3) JS：8 瓶药各加专属问题 q（t 题干 / o 选项 / e 每选项回应） ----------
qs = {
 'p1': ("你最近的复习状态是？",
   ['还没翻开书','学了一天，感觉没进脑子','在及格线边缘反复试探','其实准备得还行，就是慌'],
   ['但你后来用两周把整本书过了一遍，期末考了 89 分。','但那种"没进脑子"的感觉会在期末前突然消散——你后来靠一遍遍抄写把它过完了。','但你在及格线上试探到期末，最后稳稳上岸，还多考了 10 分。','但你考前一周的从容，是你这四年最好的状态之一。']),
 'p2': ("课堂上你有想法时，你通常会……？",
   ['等别人先说','心里演练十遍，最后放弃','说了，但声音发抖','其实常发言，只是怕被评价'],
   ['但后来你在一次小组讨论里忍不住开了口，那是你第一次觉得"原来我也可以"。','但你后来在社团面试里硬着头皮说完了一整段自我介绍，从那以后，开口变简单了。','但发抖的声音遮不住内容——后来有人专门来加你微信，说你讲得清楚。','但你后来把"怕被评价"换成了"我的风格"，舞台反而越来越大。']),
 'p3': ("你内耗最多的时候是？",
   ['刷到别人晒成绩和 offer','晚上躺床上复盘白天的话','忍不住对比别人的进度','计划太多，一个都没完成'],
   ['但你后来把刷朋友圈的时间固定到一天一次，世界安静了很多。','但你后来养成了"今天的事，写完就放下"，失眠少了，头发也回来了。','但你后来只和自己比：今天比昨天多学一小时，就赢了。','但你后来学会了"每天只列三件"，完成比列满更重要。']),
 'p4': ("你心里那个「如果当初」，是？",
   ['加了联系方式，没敢聊','约过一次，被婉拒了','明明互相喜欢，却错过','还没开始，就先放弃了'],
   ['但你后来在某天晚上发出了一句"今天图书馆开空调了吗"，故事就从那里开始了。','但被婉拒没有击垮你——你后来坦然地喜欢上了别人，还在一起了。','但你后来在毕业前把它说破了，对方说"我等这句话很久了"。','但放弃是最轻松的选项，你后来决定不再选它，就有了后来的人。']),
 'p5': ("和室友卡住的地方，通常是？",
   ['作息不同，互相迁就','一次误会，没当面说开','觉得对方不理解我','已经好久没好好聊天了'],
   ['但你们后来约法三章，还一起买了个小夜灯，矛盾变成了默契。','但你们后来在一次夜聊里把误会摊开，才发现双方都憋了很久。','但你们后来在深夜聊了一次，才知道对方其实很懂你。','但你们后来在毕业前夜聊到三点，把三年的话一次说完了。']),
 'p6': ("面对未来，你目前是？",
   ['完全没方向','有几个选项，拿不准','知道方向，但没底气','在按计划走，偶尔心慌'],
   ['但你后来从一件小事开始：写简历、约老师、列清单，方向是走出来的。','但你后来用排除法划掉了最不想去的那条路，剩下的路就亮了。','但你后来把"没底气"换成了"先试一次"，第一次就比想象中好。','但偶尔心慌很正常——你后来学会用"已完成"清单，把慌张一点点压实。']),
 'p7': ("关于现在的专业 / 方向，你的想法是？",
   ['不喜欢，但不敢换','想换，怕考不上 / 失败','在犹豫要不要坚持','确定要换，就差勇气'],
   ['但你后来真的换了，还为此偷偷看了一整年的书。','但你后来算过：最坏的结果也就是重来一次，而你有四年。','但坚持和将就的区别，你后来终于分清了，然后果断选了前者。','而勇气这件事，你后来在教务处排队交表的那一刻，就攒够了。']),
 'p8': ("你熬夜，最常因为？",
   ['作业 / 复习没做完','刷手机，停不下来','心里有事，睡不着','白天太忙，只有深夜属于自己'],
   ['但你后来学会了"先睡，明早起来再做"，效率反而更高了。','但你后来把充电器放到床外，用两本书代替了短视频。','但你后来把心事写进日记再上床，睡眠就慢慢回来了。','但你后来在 11:40 上床听播客，才发现深夜的另一种用法。']),
}
anchors = {
 'p1': "'把竞赛报名表交了——大四的你已经替你看过结果了']},",
 'p2': "'把你想说但没说的话，先写给一个朋友看']},",
 'p3': "'把「别人在干嘛」的刷新频率降到一天一次']},",
 'p4': "'如果被拒绝了——那也是你勇敢的证据，不是失败']},",
 'p5': "'主动发起一次宿舍夜聊，零食你出']},",
 'p6': "'列一份「想做的事」清单，允许自己划掉']},",
 'p7': "'把「万一选错了」换成「选错了我也能转回来」——你有四年']},",
 'p8': "'明天给自己安排 20 分钟的运动——不需要坚持，先试一次']},",
}
for pid, (t, o, e) in qs.items():
    qjs = ("q:{t:'%s',o:[%s],e:[%s]}},\n" % (
        t,
        ','.join("'%s'" % x for x in o),
        ','.join("'%s'" % x for x in e)))
    rep(anchors[pid], anchors[pid][:-1] + ',\n   ' + qjs.rstrip('\n'))

# ---------- 4) JS：state 增加字段 ----------
rep("let state = {screen:'open', pill:null, version:'normal', grade:'大二', major:'', gender:'保密', goal:'', nick:'', detail:'', anxiety:'', collected:[]};",
    "let state = {screen:'open', pill:null, version:'normal', grade:'大二', major:'', gender:'保密', goal:'', nick:'', detail:'', stateInfo:'', mood:'', qIndex:null, anxiety:'', collected:[]};")

# ---------- 5) JS：choose 渲染专属问题 ----------
rep("""  $('anxietyInput').placeholder = state.pill.anxietyPh;
  resetVersion();
  $('gradeSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.grade===state.grade));
  $('genderSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.gender===state.gender));
  showScreen('input');""",
"""  $('anxietyInput').placeholder = state.pill.anxietyPh;
  resetVersion();
  state.qIndex = null;
  renderQ();
  $('gradeSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.grade===state.grade));
  $('genderSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.gender===state.gender));
  $('stateSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.state===state.stateInfo));
  $('moodSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.mood===state.mood));
  showScreen('input');""")

# ---------- 6) JS：新增监听（状态 / 心理 / 专属问题）+ renderQ ----------
rep("""$('genderSeg').addEventListener('click', e=>{
  const b = e.target.closest('button'); if(!b) return;
  state.gender = b.dataset.gender;
  $('genderSeg').querySelectorAll('button').forEach(x=>x.classList.toggle('sel', x===b));
});""",
"""$('genderSeg').addEventListener('click', e=>{
  const b = e.target.closest('button'); if(!b) return;
  state.gender = b.dataset.gender;
  $('genderSeg').querySelectorAll('button').forEach(x=>x.classList.toggle('sel', x===b));
});
$('stateSeg').addEventListener('click', e=>{
  const b = e.target.closest('button'); if(!b) return;
  state.stateInfo = b.dataset.state;
  $('stateSeg').querySelectorAll('button').forEach(x=>x.classList.toggle('sel', x===b));
});
$('moodSeg').addEventListener('click', e=>{
  const b = e.target.closest('button'); if(!b) return;
  state.mood = b.dataset.mood;
  $('moodSeg').querySelectorAll('button').forEach(x=>x.classList.toggle('sel', x===b));
});
$('qSeg').addEventListener('click', e=>{
  const b = e.target.closest('button'); if(!b) return;
  state.qIndex = Number(b.dataset.q);
  $('qSeg').querySelectorAll('button').forEach(x=>x.classList.toggle('sel', x===b));
});
function renderQ(){
  const p = state.pill;
  if(!p || !p.q) return;
  $('qLabel').textContent = p.q.t;
  $('qSeg').innerHTML = p.q.o.map((o,i)=>`<button data-q="${i}">${o}</button>`).join('');
  $('qSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.q===String(state.qIndex)));
}""")

# ---------- 7) JS：startMix 读取新字段 ----------
rep("""  state.nick = $('nickInput').value.trim();
  state.detail = $('detailInput').value.trim();
  if(!state.pill){ toast('请先选一瓶药'); showScreen('pick'); return; }""",
"""  state.nick = $('nickInput').value.trim();
  state.detail = $('detailInput').value.trim();
  state.answer = (state.qIndex!=null && state.pill.q) ? state.pill.q.o[state.qIndex] : '';
  if(!state.pill){ toast('请先选一瓶药'); showScreen('pick'); return; }""")

# ---------- 8) JS：buildLetter 织入专属问题回应 ----------
rep("""  t = t.replace('嘿，现在的你', '嘿，' + (s.nick || '现在的你'));
  if(s.version==='pro' && s.detail) t = t.replace('——', '对了，你还记得「' + s.detail + '」吗？当时你觉得好可惜。四年后的我可以告诉你：那件事后来有了个还不错的结果，你从中拿到了比结果更重要的东西。\\n\\n——');""",
"""  t = t.replace('嘿，现在的你', '嘿，' + (s.nick || '现在的你'));
  if(s.version==='pro' && s.answer && p.q){
    const qi = p.q.o.indexOf(s.answer);
    const echo = qi>=0 ? p.q.e[qi] : '那件事，后来有了个不错的答案。';
    t = t.replace('——', '配药时你告诉我：「' + s.answer + '」。' + echo + '\\n\\n——');
  }
  if(s.version==='pro' && s.detail) t = t.replace('——', '对了，你还记得「' + s.detail + '」吗？当时你觉得好可惜。四年后的我可以告诉你：那件事后来有了个还不错的结果，你从中拿到了比结果更重要的东西。\\n\\n——');""")

# ---------- 9) JS：关键词卡增加状态 / 心情 ----------
rep("""  if(state.goal) kv.push(`<span class="kv">期望：${esc(state.goal)}</span>`);
  if(state.version==='pro' && state.nick) kv.push(`<span class="kv">致：${esc(state.nick)}</span>`);""",
"""  if(state.goal) kv.push(`<span class="kv">期望：${esc(state.goal)}</span>`);
  if(state.version==='pro'){
    if(state.stateInfo) kv.push(`<span class="kv">状态：${esc(state.stateInfo)}</span>`);
    if(state.mood) kv.push(`<span class="kv">心情：${esc(state.mood)}</span>`);
  }
  if(state.version==='pro' && state.nick) kv.push(`<span class="kv">致：${esc(state.nick)}</span>`);""")

# 写回（保持 CRLF）
with io.open(path, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(html)
print('patched ok, bytes:', len(html.encode('utf-8')))

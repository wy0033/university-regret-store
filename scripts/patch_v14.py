# -*- coding: utf-8 -*-
import io
p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(p, encoding='utf-8') as f:
    h = f.read()

def rep(old, new, cnt=1):
    global h
    assert old in h, 'ANCHOR MISS: ' + old[:60]
    h = h.replace(old, new, cnt)

# 1) 工具函数：插入到 fill 函数之后
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
const GRADE_YEARS = {大一:4, 大二:3, 大三:2, 大四:1};
const YEARS_CN = {4:'四', 3:'三', 2:'两', 1:'一'};
function gradeYears(g){ return GRADE_YEARS[g] || 4; }
function yearsText(g){ return (YEARS_CN[gradeYears(g)] || '四') + '年'; }
function voiceLabelText(){ return '听「' + yearsText(state.grade) + '后的你」读这封信'; }
function applyYears(text, g){
  const cn = YEARS_CN[gradeYears(g)] || '四';
  return text
    .split('四年后').join(cn + '年后')
    .split('你有四年').join('你有' + cn + '年')
    .split('你的四年，值得').join('剩下的' + cn + '年，值得')
    .split('三年').join('很久')
    .split('大三的秋天').join('后来的那个秋天')
    .split('大三体测').join('那学期的体测')
    .split('这四年').join('大学里')
    .split('四年前的我们').join(cn + '年前的我们');
}""")

# 2) buildLetter：署名动态 + 织入锚点用 sign + 结尾统一时限替换
rep("""function buildLetter(p, s){
  let t = fill(p.letter, s);
  t = t.replace('嘿，现在的你', '嘿，' + (s.nick || '现在的你'));
  if(s.version==='pro' && s.answer && p.q){
    const qi = p.q.o.indexOf(s.answer);
    const echo = qi>=0 ? p.q.e[qi] : '那件事，后来有了个不错的答案。';
    t = t.replace('—— 大四的你', '对了，配药的时候你告诉我：「' + s.answer + '」。你当时没多想，后来回头看，那正是故事的转折点。' + echo + '\\n\\n—— 大四的你');
  }
  if(s.version==='pro' && s.detail) t = t.replace('—— 大四的你', '还有件小事，你当时觉得可惜——「' + s.detail + '」。四年后的我可以告诉你：那件事后来有了个意外的结果，你从里面拿到了比结果更珍贵的东西。\\n\\n—— 大四的你');
  if(s.goal) t = t.replace('—— 大四的你', '还有你写在方子上的那个目标——「' + s.goal + '」。四年后的我可以告诉你：你真的做到了。\\n\\n—— 大四的你');""",
"""function buildLetter(p, s){
  let t = fill(p.letter, s);
  const sign = '—— ' + yearsText(s.grade) + '后的你';
  t = t.split('—— 大四的你').join(sign);
  t = t.replace('嘿，现在的你', '嘿，' + (s.nick || '现在的你'));
  if(s.version==='pro' && s.answer && p.q){
    const qi = p.q.o.indexOf(s.answer);
    const echo = qi>=0 ? p.q.e[qi] : '那件事，后来有了个不错的答案。';
    t = t.replace(sign, '对了，配药的时候你告诉我：「' + s.answer + '」。你当时没多想，后来回头看，那正是故事的转折点。' + echo + '\\n\\n' + sign);
  }
  if(s.version==='pro' && s.detail) t = t.replace(sign, '还有件小事，你当时觉得可惜——「' + s.detail + '」。四年后的我可以告诉你：那件事后来有了个意外的结果，你从里面拿到了比结果更珍贵的东西。\\n\\n' + sign);
  if(s.goal) t = t.replace(sign, '还有你写在方子上的那个目标——「' + s.goal + '」。四年后的我可以告诉你：你真的做到了。\\n\\n' + sign);""")

rep("""  return t;
}""",
"""  return applyYears(t, s.grade);
}""")

# 3) goalKw：返回前统一时限替换
rep("""  return p.keyword[0];
}""",
"""  return applyYears(p.keyword[0], s.grade);
}""")

# 4) showResult：清单 actions 时限替换 + 语音标签动态
rep("""  $('actList').innerHTML = p.actions.map((a,i)=>`
    <li data-i="${i}"><span class="tick"></span><span>${a}</span></li>`).join('');""",
"""  $('actList').innerHTML = p.actions.map((a,i)=>`
    <li data-i="${i}"><span class="tick"></span><span>${applyYears(a, state.grade)}</span></li>`).join('');""")

rep("""  $('voiceStop').style.display = 'none';
  stopVoice();
  showScreen('result');""",
"""  $('voiceStop').style.display = 'none';
  stopVoice();
  $('voiceLabel').textContent = voiceLabelText();
  showScreen('result');""")

# 5) 语音标签：HTML 初始 + onend/停止恢复
rep("""<span id="voiceLabel">听「大四的你」读这封信</span>""",
"""<span id="voiceLabel">听「四年后的你」读这封信</span>""")
rep("""$('voiceLabel').textContent='听「大四的你」读这封信'; $('voiceBtn').classList.remove('playing'); $('voiceStop').style.display='none';""",
"""$('voiceLabel').textContent=voiceLabelText(); $('voiceBtn').classList.remove('playing'); $('voiceStop').style.display='none';""")
rep("""  $('voiceLabel').textContent = '听「大四的你」读这封信';""",
"""  $('voiceLabel').textContent = voiceLabelText();""")

# 6) 分享弹窗：副标题动态
rep("""    <p class="modal-sub">把四年后的答案，递给朋友</p>""",
"""    <p class="modal-sub" id="shareSub">把四年后的答案，递给朋友</p>""")
rep("""  $('shareTitle').textContent = `「${p.name}」后悔药`;
  $('shareKv').innerHTML = kvTags(p, state);
  $('shareText').textContent = buildShareText(p);""",
"""  $('shareTitle').textContent = `「${p.name}」后悔药`;
  $('shareSub').textContent = '把' + yearsText(state.grade) + '后的答案，递给朋友';
  $('shareKv').innerHTML = kvTags(p, state);
  $('shareText').textContent = buildShareText(p);""")

# 7) 历史卡：清单 actions 也按记录时的年级动态
rep("""  const acts = (pill.actions||[]).map((a,i)=>{
    const d = r.done && r.done[i];
    return `<li data-i="${i}" class="${d?'done':''}"><span class="tick"></span><span>${a}</span></li>`;
  }).join('');""",
"""  const acts = (pill.actions||[]).map((a,i)=>{
    const d = r.done && r.done[i];
    return `<li data-i="${i}" class="${d?'done':''}"><span class="tick"></span><span>${applyYears(a, r.grade)}</span></li>`;
  }).join('');""")

with io.open(p, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(h)
print('patch_v14 ok')

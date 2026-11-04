# -*- coding: utf-8 -*-
import io
p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(p, encoding='utf-8') as f:
    h = f.read()

def rep(old, new, cnt=1):
    global h
    assert old in h, 'ANCHOR MISS: ' + old[:70]
    h = h.replace(old, new, cnt)

# 1) voiceNote 加 id
rep("""<div class="voice-note">温柔女声 · 深夜电台语速 · 按你选的性别匹配音色</div>""",
"""<div class="voice-note" id="voiceNote">温柔女声 · 深夜电台语速 · 按你选的性别匹配音色</div>""")

# 2) applyYears 移除被同学式时间点接管的两条规则（大三的秋天 / 大三体测）
rep("""  return text
    .split('三年').join('很久')
    .split('大三的秋天').join('后来的那个秋天')
    .split('大三体测').join('那学期的体测')
    .split('这四年').join('大学里')""",
"""  return text
    .split('三年').join('很久')
    .split('这四年').join('大学里')""")

# 3) buildLetter：applyYears 前加入 p3/p4/p8 按年级时间点动态化（参考同学版）
rep("""  t = applyYears(t, s.grade);
  return t.split('—— 大四的你').join('—— ' + yearsText(s.grade) + '后的你');
}""",
"""  // 按年级微调正文中的固定时间点（大一未来 / 大二当下 / 大三临近 / 大四回顾）
  if(p.id==='p3'){
    const p3map={大一:'到了大二下学期，你开始',大二:'就是从这学期开始，你',大三:'大二下学期你开始',大四:'大二下学期你开始'};
    t = t.replace('大二下学期你开始', p3map[s.grade]||'大二下学期你开始');
  }
  if(p.id==='p4'){
    const p4map={大一:'到了大三的秋天，',大二:'到了大三的秋天，',大三:'就是今年秋天，',大四:'大三的秋天，'};
    t = t.replace('就在大三的秋天，', p4map[s.grade]||'就在大三的秋天，');
  }
  if(p.id==='p8'){
    const p8a={大一:'因为到了大二，你也是这样',大二:'因为现在的你，就是这样',大三:'因为大二那年的我，也是这样',大四:'因为大二那年的我，也是这样'};
    t = t.replace('因为大二那年的我，也是这样', p8a[s.grade]||'因为大二那年的我，也是这样');
    const p8b={大一:'到了大三体测，你跑完八百米',大二:'到了大三体测，你跑完八百米',大三:'这次体测，你跑完八百米',大四:'大三体测你跑完八百米'};
    t = t.replace('大三体测你跑完八百米', p8b[s.grade]||'大三体测你跑完八百米');
  }
  t = applyYears(t, s.grade);
  return t.split('—— 大四的你').join('—— ' + yearsText(s.grade) + '后的你');
}""")

# 4) showResult：语音提示按性别动态（参考同学版）
rep("""  $('voiceLabel').textContent = voiceLabelText();
  showScreen('result');""",
"""  $('voiceLabel').textContent = voiceLabelText();
  $('voiceNote').textContent = (state.gender==='男生' ? '温柔男声' : '温柔女声') + ' · 深夜电台语速 · 按你选的性别匹配音色';
  showScreen('result');""")

with io.open(p, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(h)
print('patch_v15 ok')

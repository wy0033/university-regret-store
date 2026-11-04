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

# ---------- 1) p6 letter：去掉中间破折号（让织入段落在署名前自然成段） ----------
rep("""只是开始做小事——写一版很烂的第一稿简历，约老师聊了二十分钟""",
"""只是开始做小事，先写一版很烂的第一稿简历，约老师聊了二十分钟""")

# ---------- 2) buildLetter：织入过渡语升级 ----------
rep("""    t = t.replace('——', '配药时你告诉我：「' + s.answer + '」。' + echo + '\\n\\n——');""",
"""    t = t.replace('——', '对了，配药的时候你告诉我：「' + s.answer + '」。你当时没多想，后来回头看，那正是故事的转折点。' + echo + '\\n\\n——');""")

rep("""  if(s.version==='pro' && s.detail) t = t.replace('——', '对了，你还记得「' + s.detail + '」吗？当时你觉得好可惜。四年后的我可以告诉你：那件事后来有了个还不错的结果，你从中拿到了比结果更重要的东西。\\n\\n——');""",
"""  if(s.version==='pro' && s.detail) t = t.replace('——', '还有件小事，你当时觉得可惜——「' + s.detail + '」。四年后的我可以告诉你：那件事后来有了个意外的结果，你从里面拿到了比结果更珍贵的东西。\\n\\n——');""")

rep("""  if(s.goal) t = t.replace('——', '还有，你写下的期望目标「' + s.goal + '」——四年后的我可以告诉你：你做到了。\\n\\n——');""",
"""  if(s.goal) t = t.replace('——', '还有你写在方子上的那个目标——「' + s.goal + '」。四年后的我可以告诉你：你真的做到了。\\n\\n——');""")

# ---------- 3) buildLetter：p6 结局按目标动态化（考研 / 考公 / 默认就业） ----------
rep("""  if(s.goal) t = t.replace('——', '还有你写在方子上的那个目标——「' + s.goal + '」。四年后的我可以告诉你：你真的做到了。\\n\\n——');
  return t;
}""",
"""  if(s.goal) t = t.replace('——', '还有你写在方子上的那个目标——「' + s.goal + '」。四年后的我可以告诉你：你真的做到了。\\n\\n——');
  if(p.id==='p6' && s.goal){
    if(/考研|读研|研究生|上岸|保研/.test(s.goal)){
      t = t.replace('但你拿到了 offer，心里有底', '但你收到了那所学校的录取通知，心里有底');
      t = t.replace('签完三方协议的那个下午', '在收到拟录取通知的那个下午');
    } else if(/考公|公务员|编制/.test(s.goal)){
      t = t.replace('但你拿到了 offer，心里有底', '但你通过了笔试和面试，心里有底');
      t = t.replace('签完三方协议的那个下午', '在公示名单上看到自己名字的那个下午');
    }
  }
  return t;
}""")

# ---------- 4) 关键词卡：p6 动态关键词 + goalKw 函数 ----------
rep("""function kvTags(p, s){""",
"""function goalKw(p, s){
  if(p.id==='p6' && s.goal){
    if(/考研|读研|研究生|上岸|保研/.test(s.goal)) return '四年后：收到录取通知，心里有底';
    if(/考公|公务员|编制/.test(s.goal)) return '四年后：通过考试，心里有底';
  }
  return p.keyword[0];
}
function kvTags(p, s){""")

rep("""  kv.push(`<span class="kv">${p.keyword[0]}</span>`);
  return kv.join('');""",
"""  kv.push(`<span class="kv">${goalKw(p, s)}</span>`);
  return kv.join('');""")

# ---------- 5) 分享文案：同步动态关键词 ----------
rep("""  return `我在「大学后悔药便利店」配了一瓶「${p.name}」后悔药\\n${state.grade||''} ${state.major||'大学'} | ${state.anxiety||'正在烦恼'} | ${p.keyword[0]}\\n—— 不是工具，是情绪出口。`;""",
"""  return `我在「大学后悔药便利店」配了一瓶「${p.name}」后悔药\\n${state.grade||''} ${state.major||'大学'} | ${state.anxiety||'正在烦恼'} | ${goalKw(p, state)}\\n—— 不是工具，是情绪出口。`;""")

# 写回（保持 CRLF）
with io.open(path, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(html)
print('patched ok, bytes:', len(html.encode('utf-8')))

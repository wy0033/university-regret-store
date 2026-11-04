# -*- coding: utf-8 -*-
import io

path = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(path, encoding='utf-8') as f:
    h = f.read()

def rep(old, new, must=True):
    global h
    if old not in h:
        if must:
            raise AssertionError('NOT FOUND: ' + old[:80])
        return
    h = h.replace(old, new, 1)

# ---------- 1) buildLetter：p6 特判 → 通用结局自洽（覆盖 p1/p6 及同类意象） ----------
rep("""  if(p.id==='p6' && s.goal){
    if(/考研|读研|研究生|上岸|保研/.test(s.goal)){
      t = t.replace('但你拿到了 offer，心里有底', '但你收到了那所学校的录取通知，心里有底');
      t = t.replace('签完三方协议的那个下午', '在收到拟录取通知的那个下午');
    } else if(/考公|公务员|编制/.test(s.goal)){
      t = t.replace('但你拿到了 offer，心里有底', '但你通过了笔试和面试，心里有底');
      t = t.replace('签完三方协议的那个下午', '在公示名单上看到自己名字的那个下午');
    }
  }""",
"""  if(s.goal && /考研|读研|研究生|上岸|保研/.test(s.goal)){
    t = t.replace('刚拿到 offer 的那个晚上', '收到录取通知的那个晚上');
    t = t.replace('进了心仪的公司', '考上了心仪的学校');
    t = t.replace('都在变成你简历上的一行字', '都在变成你成绩单上的一行字');
    t = t.replace('但你拿到了 offer，心里有底', '但你收到了那所学校的录取通知，心里有底');
    t = t.replace('签完三方协议的那个下午', '在收到拟录取通知的那个下午');
  } else if(s.goal && /考公|公务员|编制/.test(s.goal)){
    t = t.replace('刚拿到 offer 的那个晚上', '收到录用通知的那个晚上');
    t = t.replace('进了心仪的公司', '考上了心仪的岗位');
    t = t.replace('都在变成你简历上的一行字', '都在变成你成绩单上的一行字');
    t = t.replace('但你拿到了 offer，心里有底', '但你通过了笔试和面试，心里有底');
    t = t.replace('签完三方协议的那个下午', '在公示名单上看到自己名字的那个下午');
  }""")

# ---------- 2) goalKw：p6 特判 → 按 keyword 内容联动（p1/p6 通用） ----------
rep("""function goalKw(p, s){
  if(p.id==='p6' && s.goal){
    if(/考研|读研|研究生|上岸|保研/.test(s.goal)) return '四年后：收到录取通知，心里有底';
    if(/考公|公务员|编制/.test(s.goal)) return '四年后：通过考试，心里有底';
  }
  return p.keyword[0];
}""",
"""function goalKw(p, s){
  if(s.goal && /考研|读研|研究生|上岸|保研/.test(s.goal)){
    if(p.keyword[0].includes('进了心仪的公司')) return '四年后：考上了心仪的学校';
    if(p.keyword[0].includes('签了三方')) return '四年后：收到录取通知，心里有底';
  }
  if(s.goal && /考公|公务员|编制/.test(s.goal)){
    if(p.keyword[0].includes('进了心仪的公司')) return '四年后：考上了心仪的岗位';
    if(p.keyword[0].includes('签了三方')) return '四年后：通过考试，心里有底';
  }
  return p.keyword[0];
}""")

with io.open(path, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(h)
print('patched ok, bytes:', len(h.encode('utf-8')))

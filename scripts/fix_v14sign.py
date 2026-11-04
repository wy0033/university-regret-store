# -*- coding: utf-8 -*-
import io
p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(p, encoding='utf-8') as f:
    h = f.read()

old = """function buildLetter(p, s){
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
  if(s.goal) t = t.replace(sign, '还有你写在方子上的那个目标——「' + s.goal + '」。四年后的我可以告诉你：你真的做到了。\\n\\n' + sign);"""
new = """function buildLetter(p, s){
  let t = fill(p.letter, s);
  t = t.replace('嘿，现在的你', '嘿，' + (s.nick || '现在的你'));
  if(s.version==='pro' && s.answer && p.q){
    const qi = p.q.o.indexOf(s.answer);
    const echo = qi>=0 ? p.q.e[qi] : '那件事，后来有了个不错的答案。';
    t = t.replace('—— 大四的你', '对了，配药的时候你告诉我：「' + s.answer + '」。你当时没多想，后来回头看，那正是故事的转折点。' + echo + '\\n\\n—— 大四的你');
  }
  if(s.version==='pro' && s.detail) t = t.replace('—— 大四的你', '还有件小事，你当时觉得可惜——「' + s.detail + '」。四年后的我可以告诉你：那件事后来有了个意外的结果，你从里面拿到了比结果更珍贵的东西。\\n\\n—— 大四的你');
  if(s.goal) t = t.replace('—— 大四的你', '还有你写在方子上的那个目标——「' + s.goal + '」。四年后的我可以告诉你：你真的做到了。\\n\\n—— 大四的你');"""
assert old in h, 'buildLetter head anchor not found'
h = h.replace(old, new, 1)

old2 = """  return applyYears(t, s.grade);
}"""
new2 = """  t = applyYears(t, s.grade);
  return t.split('—— 大四的你').join('—— ' + yearsText(s.grade) + '后的你');
}"""
assert old2 in h, 'buildLetter tail anchor not found'
h = h.replace(old2, new2, 1)

with io.open(p, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(h)
print('buildLetter sign fixed')

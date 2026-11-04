# -*- coding: utf-8 -*-
import io, re, ast

path = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
h = io.open(path, encoding='utf-8').read()

m = re.search(r"\{id:'p6'.*?letter:'(.*?)',\n   keyword", h, re.S)
letter = m.group(1).replace('\\n', '\n')
mq = re.search(r"\{id:'p6'.*?q:\{t:'(.*?)',o:(\[.*?\]),e:(\[.*?\])\}", h, re.S)
q = {'t': mq.group(1), 'o': ast.literal_eval(mq.group(2)), 'e': ast.literal_eval(mq.group(3))}
p6 = {'id':'p6', 'letter': letter, 'q': q}

def buildLetter(p, s):
    t = p['letter']
    for k, v in [('anxiety', s['anxiety'])]:
        t = t.replace('{' + k + '}', v or '那件让你烦恼的小事')
    t = t.replace('嘿，现在的你', '嘿，' + (s.get('nick') or '现在的你'))
    if s.get('version')=='pro' and s.get('answer') and p.get('q'):
        qi = p['q']['o'].index(s['answer']) if s['answer'] in p['q']['o'] else -1
        echo = p['q']['e'][qi] if qi>=0 else '那件事，后来有了个不错的答案。'
        t = t.replace('—— 大四的你', '对了，配药的时候你告诉我：「' + s['answer'] + '」。你当时没多想，后来回头看，那正是故事的转折点。' + echo + '\n\n—— 大四的你')
    if s.get('version')=='pro' and s.get('detail'):
        t = t.replace('—— 大四的你', '还有件小事，你当时觉得可惜——「' + s['detail'] + '」。四年后的我可以告诉你：那件事后来有了个意外的结果，你从里面拿到了比结果更珍贵的东西。\n\n—— 大四的你')
    if s.get('goal'):
        t = t.replace('—— 大四的你', '还有你写在方子上的那个目标——「' + s['goal'] + '」。四年后的我可以告诉你：你真的做到了。\n\n—— 大四的你')
    if p['id']=='p6' and s.get('goal'):
        if re.search(r'考研|读研|研究生|上岸|保研', s['goal']):
            t = t.replace('但你拿到了 offer，心里有底', '但你收到了那所学校的录取通知，心里有底')
            t = t.replace('签完三方协议的那个下午', '在收到拟录取通知的那个下午')
        elif re.search(r'考公|公务员|编制', s['goal']):
            t = t.replace('但你拿到了 offer，心里有底', '但你通过了笔试和面试，心里有底')
            t = t.replace('签完三方协议的那个下午', '在公示名单上看到自己名字的那个下午')
    return t

pro = {'nick':'张浩杉','version':'pro','goal':'考研杭电','answer':'知道方向，但没底气','detail':'大一上浪费很多时间，高数没熟练掌握','anxiety':'不知道毕业后要干嘛'}
print('=== 考研 + 进阶定制 ===')
print(buildLetter(p6, pro))
print()

normal = {'nick':'李四','version':'normal','goal':'进互联网大厂','anxiety':'不知道毕业后要干嘛'}
print('=== 就业目标 + 普通配方 ===')
print(buildLetter(p6, normal))
print()

assert '签完三方' not in buildLetter(p6, pro)
assert '录取通知' in buildLetter(p6, pro)
assert '签完三方' in buildLetter(p6, normal) or '拿到了 offer' in buildLetter(p6, normal)
print('ALL OK')

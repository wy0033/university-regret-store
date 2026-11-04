# -*- coding: utf-8 -*-
import io, re, ast

path = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
h = io.open(path, encoding='utf-8').read()

m = re.search(r"\{id:'p6'.*?letter:'(.*?)',\n   keyword:\[(.*?)\],", h, re.S)
letter = m.group(1).replace('\\n', '\n')
p6 = {'id':'p6', 'letter': letter}

def buildLetter(p, s):
    t = p['letter']
    t = t.replace('{anxiety}', s['anxiety'] or '那件让你烦恼的小事')
    t = t.replace('嘿，现在的你', '嘿，' + (s.get('nick') or '现在的你'))
    if s.get('goal'):
        t = t.replace('—— 大四的你', '还有你写在方子上的那个目标——「' + s['goal'] + '」。四年后的我可以告诉你：你真的做到了。\n\n—— 大四的你')
    if s.get('goal') and p['id'] == 'p6':
        t = t.replace('你连「想做什么」都说不出来', '你心里其实有个方向——「' + s['goal'] + '」，只是还不敢说出口')
    if s.get('goal') and re.search(r'考研|读研|研究生|上岸|保研', s['goal']):
        t = t.replace('但你拿到了 offer，心里有底', '但你收到了那所学校的录取通知，心里有底')
        t = t.replace('签完三方协议的那个下午', '在收到拟录取通知的那个下午')
    return t

# 有目标：开头呼应目标，结尾呼应结局
r1 = buildLetter(p6, {'goal':'考研上岸杭电', 'anxiety':'x'})
print('=== 有目标（考研上岸杭电）===')
print(r1[:120])
print('...')
print(r1[-60:])
assert '你心里其实有个方向——「考研上岸杭电」' in r1, '开头未呼应目标'
assert '你连「想做什么」都说不出来' not in r1, '旧句仍在'
assert '在收到拟录取通知的那个下午' in r1

# 无目标：保持原句
r2 = buildLetter(p6, {'goal':'', 'anxiety':'x'})
assert '你连「想做什么」都说不出来' in r2 and '你心里其实有个方向' not in r2
print('\n无目标 OK：保持「你连想做什么都说不出来」')
print('ALL OK')

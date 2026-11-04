# -*- coding: utf-8 -*-
import io, re, ast

path = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
h = io.open(path, encoding='utf-8').read()

# 提取全部 8 瓶的 letter 与 keyword
ms = re.findall(r"\{id:'(p\d)'.*?letter:'(.*?)',\n   keyword:\[(.*?)\],", h, re.S)
PILLS = {}
for pid, letter, kw in ms:
    kwv = ast.literal_eval(kw) if kw.strip().startswith('[') else [ast.literal_eval(kw)]
    PILLS[pid] = {'id': pid, 'letter': letter.replace('\\n', '\n'), 'keyword': kwv}

def buildLetter(p, s):
    t = p['letter']
    t = t.replace('{anxiety}', s['anxiety'] or '那件让你烦恼的小事')
    t = t.replace('嘿，现在的你', '嘿，' + (s.get('nick') or '现在的你'))
    if s.get('version')=='pro' and s.get('answer') and p.get('q'):
        qi = p['q']['o'].index(s['answer']) if s['answer'] in p['q']['o'] else -1
        echo = p['q']['e'][qi] if qi>=0 else '那件事，后来有了个不错的答案。'
        t = t.replace('—— 大四的你', '对了，配药的时候你告诉我：「' + s['answer'] + '」。你当时没多想，后来回头看，那正是故事的转折点。' + echo + '\n\n—— 大四的你')
    if s.get('version')=='pro' and s.get('detail'):
        t = t.replace('—— 大四的你', '还有件小事，你当时觉得可惜——「' + s['detail'] + '」。四年后的我可以告诉你：那件事后来有了个意外的结果，你从里面拿到了比结果更珍贵的东西。\n\n—— 大四的你')
    if s.get('goal'):
        t = t.replace('—— 大四的你', '还有你写在方子上的那个目标——「' + s['goal'] + '」。四年后的我可以告诉你：你真的做到了。\n\n—— 大四的你')
    if s.get('goal') and re.search(r'考研|读研|研究生|上岸|保研', s['goal']):
        t = t.replace('刚拿到 offer 的那个晚上', '收到录取通知的那个晚上')
        t = t.replace('进了心仪的公司', '考上了心仪的学校')
        t = t.replace('都在变成你简历上的一行字', '都在变成你成绩单上的一行字')
        t = t.replace('但你拿到了 offer，心里有底', '但你收到了那所学校的录取通知，心里有底')
        t = t.replace('签完三方协议的那个下午', '在收到拟录取通知的那个下午')
    elif s.get('goal') and re.search(r'考公|公务员|编制', s['goal']):
        t = t.replace('刚拿到 offer 的那个晚上', '收到录用通知的那个晚上')
        t = t.replace('进了心仪的公司', '考上了心仪的岗位')
        t = t.replace('都在变成你简历上的一行字', '都在变成你成绩单上的一行字')
        t = t.replace('但你拿到了 offer，心里有底', '但你通过了笔试和面试，心里有底')
        t = t.replace('签完三方协议的那个下午', '在公示名单上看到自己名字的那个下午')
    return t

def goalKw(p, s):
    if s.get('goal') and re.search(r'考研|读研|研究生|上岸|保研', s['goal']):
        if '进了心仪的公司' in p['keyword'][0]: return '四年后：考上了心仪的学校'
        if '签了三方' in p['keyword'][0]: return '四年后：收到录取通知，心里有底'
    if s.get('goal') and re.search(r'考公|公务员|编制', s['goal']):
        if '进了心仪的公司' in p['keyword'][0]: return '四年后：考上了心仪的岗位'
        if '签了三方' in p['keyword'][0]: return '四年后：通过考试，心里有底'
    return p['keyword'][0]

# --- p1 考研 ---
r = buildLetter(PILLS['p1'], {'nick':'张三','version':'normal','goal':'考研杭电','anxiety':'自动控制原理好难'})
print('DEBUG p1 考研 >>>', r[-160:])
assert '刚拿到 offer' not in r and '进了心仪的公司' not in r, 'p1 考研未联动'
assert '收到录取通知的那个晚上' in r and '成绩单上的一行字' in r, 'p1 考研结局缺失'
print('p1 考研 OK →', r[-45:])

# --- p1 考公 ---
r = buildLetter(PILLS['p1'], {'nick':'张三','version':'normal','goal':'考公务员','anxiety':'x'})
assert '刚拿到 offer' not in r and '收到录用通知的那个晚上' in r
print('p1 考公 OK →', r[-45:])

# --- p1 默认（无目标）---
r = buildLetter(PILLS['p1'], {'nick':'张三','version':'normal','goal':'','anxiety':'x'})
assert '刚拿到 offer 的那个晚上' in r, 'p1 默认应保留 offer'
print('p1 默认 OK')

# --- p6 考研 ---
r = buildLetter(PILLS['p6'], {'nick':'李四','version':'pro','goal':'考研杭电','answer':'完全没方向','detail':'简历空白','anxiety':'x'})
assert '签完三方' not in r and '录取通知' in r
print('p6 考研 OK →', r[-45:])

# --- p8 默认（无目标）---
r = buildLetter(PILLS['p8'], {'nick':'王五','version':'normal','goal':'','anxiety':'x'})
assert '七点半自然醒' in r
print('p8 默认 OK')

print('DEBUG kw p1 =', repr(PILLS['p1']['keyword']))
print('DEBUG goalKw =', repr(goalKw(PILLS['p1'], {'goal':'考研'})))
# --- goalKw 联动 ---
assert goalKw(PILLS['p1'], {'goal':'考研'}) == '四年后：考上了心仪的学校'
assert goalKw(PILLS['p1'], {'goal':'考公'}) == '四年后：考上了心仪的岗位'
assert goalKw(PILLS['p6'], {'goal':'考研'}) == '四年后：收到录取通知，心里有底'
assert goalKw(PILLS['p6'], {'goal':'考公'}) == '四年后：通过考试，心里有底'
assert goalKw(PILLS['p2'], {'goal':'考研'}) == PILLS['p2']['keyword'][0]
assert goalKw(PILLS['p8'], {'goal':'考研'}) == PILLS['p8']['keyword'][0]
print('goalKw OK')

print('\nALL OK')

# -*- coding: utf-8 -*-
import io
p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(p, encoding='utf-8') as f:
    h = f.read()

old = "我知道你今晚又在想他/她，那条消息打了又删，删了又打。"
new = "我知道你今晚又在想心里那个人，那条消息打了又删，删了又打。"
assert old in h, 'p4 anchor not found'
h = h.replace(old, new, 1)

with io.open(p, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(h)
print('p4 neutral ok')

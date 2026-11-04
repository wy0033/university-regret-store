# -*- coding: utf-8 -*-
import io
p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(p, encoding='utf-8') as f:
    h = f.read()
old = "']},\n   q:{t:"
new = "'],\n   q:{t:"
n = h.count(old)
h = h.replace(old, new)
with io.open(p, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(h)
print('fixed', n)

# -*- coding: utf-8 -*-
import os
base = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store'
with open(os.path.join(base, 'part1.html'), encoding='utf-8') as f:
    p1 = f.read()
with open(os.path.join(base, 'part2.html'), encoding='utf-8') as f:
    p2 = f.read()
with open(os.path.join(base, 'part3.html'), encoding='utf-8') as f:
    p3 = f.read()
full = p1 + p2 + p3
out = os.path.join(base, 'index.html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(full)
for part in ('part1.html', 'part2.html', 'part3.html'):
    os.remove(os.path.join(base, part))
print('index.html bytes:', os.path.getsize(out))

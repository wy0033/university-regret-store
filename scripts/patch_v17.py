# -*- coding: utf-8 -*-
import io
p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(p, encoding='utf-8') as f:
    h = f.read()

old = ".pill-card .ptag{font-size:12px;color:var(--amber-deep);font-weight:600}"
new = """.pill-card .ptag{font-size:12px;color:var(--amber-deep);font-weight:600}
body.night .pill-card .ptag{color:#5B8DD0;font-weight:700;text-shadow:0 1px 2px rgba(0,0,0,.25)}"""
assert old in h, 'ptag anchor not found'
h = h.replace(old, new, 1)

with io.open(p, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(h)
print('patch_v17 ok')

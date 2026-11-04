# -*- coding: utf-8 -*-
import io
p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(p, encoding='utf-8') as f:
    h = f.read()
h = h.replace('aria-label="选择不后悔后悔药"', 'aria-label="选择向前走后悔药"')
h = h.replace('alt="不后悔后悔药场景插画"', 'alt="向前走后悔药场景插画"')
with io.open(p, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(h)
print('ok')

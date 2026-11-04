# -*- coding: utf-8 -*-
import io
p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(p, encoding='utf-8') as f:
    h = f.read()
old = """.night-remind{display:none;position:fixed;left:50%;bottom:20px;transform:translateX(-50%);z-index:70;
  background:rgba(30,24,44,.94);color:#f6e7c9;border:1px solid rgba(245,201,123,.38);
  padding:11px 22px;border-radius:999px;font-size:13.5px;letter-spacing:1px;
  box-shadow:0 10px 26px rgba(0,0,0,.38);cursor:pointer;align-items:center;gap:9px}"""
new = """.night-remind{display:none;position:fixed;left:50%;bottom:24px;transform:translateX(-50%);z-index:70;
  background:rgba(30,24,44,.94);color:#f6e7c9;border:1px solid rgba(245,201,123,.38);
  padding:10px 20px;border-radius:999px;font-size:13.5px;letter-spacing:1px;white-space:nowrap;max-width:calc(100vw - 32px);
  box-shadow:0 10px 26px rgba(0,0,0,.38);cursor:pointer;align-items:center;gap:9px}"""
assert old in h
h = h.replace(old, new)
with io.open(p, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(h)
print('css tweak ok')

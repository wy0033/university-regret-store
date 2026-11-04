# -*- coding: utf-8 -*-
import io
p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(p, encoding='utf-8') as f:
    h = f.read()

old = """.night-remind{display:none;position:fixed;left:50%;bottom:24px;transform:translateX(-50%);z-index:70;
  background:rgba(30,24,44,.94);color:#f6e7c9;border:1px solid rgba(245,201,123,.38);
  padding:10px 20px;border-radius:999px;font-size:13.5px;letter-spacing:1px;white-space:nowrap;max-width:calc(100vw - 32px);
  box-shadow:0 10px 26px rgba(0,0,0,.38);cursor:pointer;align-items:center;gap:9px}
body.night .night-remind{display:flex;animation:riseIn .7s ease .9s both}
.night-remind::before{content:'';width:8px;height:8px;border-radius:50%;background:#f5c97b;box-shadow:0 0 10px #f5c97b;flex:none}
@keyframes riseIn{from{opacity:0;transform:translateX(-50%) translateY(16px)}to{opacity:1;transform:translateX(-50%) translateY(0)}}"""
new = """.night-remind{display:none;position:fixed;right:26px;bottom:24px;z-index:70;
  background:rgba(30,24,44,.94);color:#f6e7c9;border:1px solid rgba(245,201,123,.38);
  padding:10px 20px;border-radius:999px;font-size:13.5px;letter-spacing:1px;white-space:nowrap;max-width:calc(100vw - 32px);
  box-shadow:0 10px 26px rgba(0,0,0,.38);cursor:pointer;align-items:center;gap:9px}
body.night .night-remind{display:flex;animation:riseIn .7s ease .9s both}
.night-remind::before{content:'';width:8px;height:8px;border-radius:50%;background:#f5c97b;box-shadow:0 0 10px #f5c97b;flex:none}
@keyframes riseIn{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}
@media (max-width:460px){.night-remind{right:12px;bottom:14px;font-size:12.5px;padding:9px 16px}}"""
assert old in h
h = h.replace(old, new)
with io.open(p, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(h)
print('remind corner ok')

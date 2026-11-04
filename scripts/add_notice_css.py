# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) CSS：公告/升级弹窗样式（插在 .rank-rule 后）
old = """.rank-rule{margin-top:10px;font-size:11px;color:var(--ink-soft);opacity:.8;line-height:1.8;border-top:1px dashed var(--line);padding-top:9px}"""
new = """.rank-rule{margin-top:10px;font-size:11px;color:var(--ink-soft);opacity:.8;line-height:1.8;border-top:1px dashed var(--line);padding-top:9px}
#noticeModal{z-index:230}
#rankupModal{z-index:240}
.notice-body{text-align:left;margin-top:6px}
.notice-sec{margin:12px 0;padding:12px 14px;border-radius:12px;background:var(--bg);border:1px solid var(--line)}
.notice-sec b{display:block;color:var(--amber-deep);font-size:14px;letter-spacing:1px;margin-bottom:6px}
.notice-sec p{font-size:13px;color:var(--ink-soft);line-height:1.85;margin:0}
.notice-sec p u{text-decoration-color:var(--amber-deep)}
.notice-sec.warn{border-color:var(--amber);background:linear-gradient(180deg,rgba(245,201,123,.14),rgba(245,201,123,.05))}
.rankup-modal{text-align:center}
.rankup-star{color:var(--amber);width:46px;height:46px;margin:2px auto 10px;animation:rankpop .5s ease}
.rankup-star svg{width:100%;height:100%}
.rank-chip.big{font-size:20px;padding:10px 28px;display:inline-flex;box-shadow:0 8px 22px rgba(0,0,0,.14)}
.rankup-note{margin-top:14px;font-size:13px;color:var(--ink-soft);line-height:1.8}
@keyframes rankpop{0%{transform:scale(.4);opacity:0}70%{transform:scale(1.15)}100%{transform:scale(1);opacity:1}}"""
assert s.count(old) == 1, 'rank css'
s = s.replace(old, new)

io.open(p, 'w', encoding='utf-8').write(s)
print('notice css ok')

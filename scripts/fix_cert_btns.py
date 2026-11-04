# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) HTML：按钮 class 改为 cert-btn
old = """    <div class="cert-acts">
      <button class="btn-soft" id="certCopy" type="button">复制证书图片</button>
      <button class="btn-main" id="certClose" type="button">退出</button>
    </div>"""
new = """    <div class="cert-acts">
      <button class="cert-btn" id="certCopy" type="button">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
        复制证书图片
      </button>
      <button class="cert-btn solid" id="certClose" type="button">退出</button>
    </div>"""
assert s.count(old) == 1, 'cert acts html'
s = s.replace(old, new)

# 2) CSS：重做按钮样式（白面板 + 高对比按钮）
old = """.cert-acts{display:flex;gap:12px;justify-content:center;margin-top:18px}
.cert-acts .btn-soft,.cert-acts .btn-main{flex:1;max-width:210px}"""
new = """.cert-acts{display:flex;gap:12px;justify-content:center;margin-top:18px;background:var(--panel);border:1.5px solid var(--line);border-radius:16px;padding:14px}
.cert-btn{flex:1;display:inline-flex;align-items:center;justify-content:center;gap:7px;padding:12px 0;border-radius:999px;font-size:15px;font-weight:600;letter-spacing:1px;cursor:pointer;background:var(--bg);border:1.5px solid var(--line);color:var(--ink);transition:all .2s;max-width:240px}
.cert-btn svg{width:16px;height:16px;flex:none}
.cert-btn:hover{border-color:var(--amber);color:var(--amber-deep);transform:translateY(-1px)}
.cert-btn.solid{background:var(--amber);border-color:var(--amber);color:#fff}
.cert-btn.solid:hover{background:var(--amber-deep);border-color:var(--amber-deep);color:#fff}"""
assert s.count(old) == 1, 'cert acts css'
s = s.replace(old, new)

io.open(p, 'w', encoding='utf-8').write(s)
print('cert buttons re-rendered')

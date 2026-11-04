# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) CSS：等级徽章 + 账户弹窗等级面板（插在 .top-actions 规则后）
old = """.top-actions{display:flex;gap:8px}"""
new = """.top-actions{display:flex;gap:8px}
.rank-badge{
  display:inline-flex;align-items:center;gap:6px;padding:7px 13px;border-radius:999px;
  color:#fff;font-size:12px;font-weight:700;letter-spacing:1px;border:1.5px solid rgba(255,255,255,.6);
  box-shadow:var(--shadow-sm);cursor:pointer;transition:transform .2s;white-space:nowrap;
}
.rank-badge:hover{transform:translateY(-2px)}
.rank-badge svg{width:13px;height:13px;flex:none}
.rank-panel{margin-top:14px;padding:13px 15px;border-radius:14px;background:var(--panel);border:1.5px dashed var(--line)}
.rank-row{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.rank-chip{display:inline-flex;padding:4px 13px;border-radius:999px;color:#fff;font-weight:700;font-size:13px;letter-spacing:1px}
.rank-sub{font-size:12.5px;color:var(--ink-soft)}
.rank-note{margin-top:9px;font-size:12px;color:var(--ink-soft);line-height:1.75}
.rank-rule{margin-top:10px;font-size:11px;color:var(--ink-soft);opacity:.8;line-height:1.8;border-top:1px dashed var(--line);padding-top:9px}"""
assert s.count(old) == 1, 'top-actions css'
s = s.replace(old, new)

# 2) HTML：顶栏等级徽章（插在深夜场按钮前）
old = """  <div class="top-actions">
    <button class="top-btn" id="nightToggle" title="深夜模式">"""
new = """  <div class="top-actions">
    <button class="rank-badge" id="rankBadge" title="我的等级" style="display:none">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l2.9 5.9 6.6.9-4.8 4.6 1.2 6.5L12 17.3 6.1 19.9l1.2-6.5L2.5 8.8l6.6-.9z"/></svg>
      <span id="rankBadgeTxt">黑铁 1 级</span>
    </button>
    <button class="top-btn" id="nightToggle" title="深夜模式">"""
assert s.count(old) == 1, 'top actions html'
s = s.replace(old, new)

# 3) HTML：账户弹窗等级面板（插在 acct-row 之后）
old = """    <div class="acct-acts">
      <button class="btn-soft" id="logoutBtn" type="button">退出登录</button>
      <button class="btn-danger" id="delAcctBtn" type="button">删除账户</button>
    </div>"""
new = """    <div class="rank-panel" id="rankPanel" style="display:none">
      <div class="rank-row"><span class="rank-chip" id="rankChip">黑铁 1 级</span><span class="rank-sub" id="rankSub"></span></div>
      <p class="rank-note" id="rankNote"></p>
      <p class="rank-rule">等级规则：黑铁→青铜→白银→黄金各 3 级，完成普通药盒升 1 级、进阶药盒升 2 级；集齐 8 瓶直升钻石 1 级，全部进阶定制则直升荣耀 1 级，之后每瓶每多完成 1 次升 1 级，无上限。</p>
    </div>
    <div class="acct-acts">
      <button class="btn-soft" id="logoutBtn" type="button">退出登录</button>
      <button class="btn-danger" id="delAcctBtn" type="button">删除账户</button>
    </div>"""
assert s.count(old) == 1, 'acct acts'
s = s.replace(old, new)

io.open(p, 'w', encoding='utf-8').write(s)
print('rank html/css ok')

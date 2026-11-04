# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) CSS：浮动导航按钮（插在 /* ===== 提示 ===== */ 之前）
css = '''/* ===== 浮动导航 ===== */
.nav-float{
  position:fixed;right:22px;bottom:26px;z-index:80;display:flex;gap:10px;
}
.nav-fbtn{
  display:flex;align-items:center;gap:6px;padding:9px 16px;border-radius:999px;
  background:var(--panel);border:1.5px solid var(--line);color:var(--ink-soft);
  font-size:13px;box-shadow:var(--shadow-sm);transition:all .2s;font-weight:600;letter-spacing:1px;
}
.nav-fbtn:hover{border-color:var(--amber);color:var(--ink);transform:translateY(-2px)}
.nav-fbtn svg{width:14px;height:14px;flex:none}
.nav-fbtn.end{background:var(--amber);border-color:var(--amber);color:#fff}

/* ===== 提示 ===== */'''
old = '/* ===== 提示 ===== */'
assert s.count(old) == 1, 'toast css anchor'
s = s.replace(old, css)

# 2) HTML：浮动按钮组（插在 <!-- ===== 登录/注册屏 ===== --> 之前）
nav_html = '''<!-- ===== 浮动导航 ===== -->
<div class="nav-float" id="navFloat" style="display:none">
  <button class="nav-fbtn" id="backBtn" title="返回上一页">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5"/><path d="M12 19l-7-7 7-7"/></svg>
    <span>返回</span>
  </button>
  <button class="nav-fbtn end" id="endBtn" title="结束，回到首页">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/></svg>
    <span>结束</span>
  </button>
</div>

<!-- ===== 登录/注册屏 ===== -->'''
old = '<!-- ===== 登录/注册屏 ===== -->'
assert s.count(old) == 1, 'login html anchor'
s = s.replace(old, nav_html)

io.open(p, 'w', encoding='utf-8').write(s)
print('nav html/css ok')

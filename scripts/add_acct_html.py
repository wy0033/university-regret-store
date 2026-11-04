# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) body 后插入登录屏
login_html = '''<!-- ===== 登录/注册屏 ===== -->
<div id="loginScreen">
  <div class="login-card">
    <div class="login-brand"><span class="logo">药</span><span>大学后悔药便利店</span></div>
    <p class="login-sub">先登录，再进店。药盒和药方只属于你自己的账户。</p>
    <div class="login-tabs">
      <button class="login-tab on" id="tabLogin" type="button">登录</button>
      <button class="login-tab" id="tabReg" type="button">注册</button>
    </div>
    <form class="lf on" id="formLogin" autocomplete="off">
      <div class="fld"><label>昵称</label><input id="liName" type="text" placeholder="你的昵称" maxlength="12"></div>
      <div class="fld"><label>密码</label><input id="liPwd" type="password" placeholder="登录密码" maxlength="20"></div>
      <p class="login-err" id="liErr"></p>
      <button class="btn-main" type="submit">进入便利店</button>
    </form>
    <form class="lf" id="formReg" autocomplete="off">
      <div class="fld"><label>昵称</label><input id="rgName" type="text" placeholder="取一个昵称（不可重名）" maxlength="12"></div>
      <div class="fld"><label>密码</label><input id="rgPwd" type="password" placeholder="设置密码（4 位以上）" maxlength="20"></div>
      <div class="fld"><label>确认密码</label><input id="rgPwd2" type="password" placeholder="再输一次密码" maxlength="20"></div>
      <p class="login-err" id="rgErr"></p>
      <button class="btn-main" type="submit">创建账户，进店</button>
    </form>
    <p class="login-tip">账户可以无限创建，也可以随时删除。<br>所有数据只保存在你这台浏览器的本地。</p>
  </div>
</div>

'''
old_body = '<div id="app">\n'
assert s.count(old_body) == 1, 'app div not found'
s = s.replace(old_body, login_html + old_body, 1)

# 2) 顶部账户按钮（boxBtn 之后）
old_btn = '''    <button class="top-btn" id="boxBtn" title="我的药盒">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 8l-9-5-9 5v8l9 5 9-5V8z"/><path d="M3 8l9 5 9-5"/><path d="M12 13v8"/></svg>
      <span id="boxCount">药盒 0/8</span>
    </button>
  </div>'''
new_btn = '''    <button class="top-btn" id="boxBtn" title="我的药盒">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 8l-9-5-9 5v8l9 5 9-5V8z"/><path d="M3 8l9 5 9-5"/><path d="M12 13v8"/></svg>
      <span id="boxCount">药盒 0/8</span>
    </button>
    <button class="top-btn" id="acctBtn" title="我的账户">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
      <span id="acctName">账户</span>
    </button>
  </div>'''
assert s.count(old_btn) == 1, 'boxBtn block not found'
s = s.replace(old_btn, new_btn)

# 3) acctModal（boxModal 之前）
acct_modal = '''<!-- ===== 账户弹窗 ===== -->
<div class="modal-mask" id="acctModal">
  <div class="modal">
    <h3>我的账户</h3>
    <p class="modal-sub">账户数据彼此独立，互不影响</p>
    <div class="acct-row">
      <div class="acct-ava" id="acctAva">?</div>
      <div class="acct-info"><b id="acctName2"></b><span id="acctMeta"></span></div>
    </div>
    <div class="acct-acts">
      <button class="btn-soft" id="logoutBtn" type="button">退出登录</button>
      <button class="btn-danger" id="delAcctBtn" type="button">删除账户</button>
    </div>
    <button class="modal-close" id="acctClose">收起</button>
  </div>
</div>

<!-- ===== 药盒弹窗 ===== -->'''
old_modal = '<!-- ===== 药盒弹窗 ===== -->'
assert s.count(old_modal) == 1, 'boxModal comment not found'
s = s.replace(old_modal, acct_modal)

io.open(p, 'w', encoding='utf-8').write(s)
print('html ok')

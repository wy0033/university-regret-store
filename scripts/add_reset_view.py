# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) HTML：formReset（插在 formReg 结束之后、login-tip 之前）
old = """    <p class=\"login-tip\">账户可以无限创建，也可以随时删除。<br>所有数据只保存在你这台浏览器的本地。</p>"""
new = """    <form class=\"lf\" id=\"formReset\" autocomplete=\"off\">
      <div class=\"fld\"><label>昵称</label><input id=\"rsName\" type=\"text\" placeholder=\"要重置的账户昵称\" maxlength=\"12\"></div>
      <div class=\"fld\"><label>新密码</label><input id=\"rsPwd\" type=\"password\" placeholder=\"设置新密码（4 位以上）\" maxlength=\"20\"></div>
      <div class=\"fld\"><label>确认新密码</label><input id=\"rsPwd2\" type=\"password\" placeholder=\"再输一次新密码\" maxlength=\"20\"></div>
      <p class=\"login-err\" id=\"rsErr\"></p>
      <button class=\"btn-main\" type=\"submit\">重置密码</button>
      <p class=\"login-back\" id=\"resetBack\">返回登录</p>
    </form>
    <p class=\"login-tip\">账户可以无限创建，也可以随时删除。<br>所有数据只保存在你这台浏览器的本地。</p>"""
assert s.count(old) == 1, 'login tip'
s = s.replace(old, new)

# 2) CSS：.login-back（插在 .login-tip 样式之后）
old = ".login-tip{text-align:center;color:var(--ink-soft);font-size:11.5px;margin-top:18px;line-height:1.8;opacity:.85}"
new = """.login-tip{text-align:center;color:var(--ink-soft);font-size:11.5px;margin-top:18px;line-height:1.8;opacity:.85}
.login-back{text-align:center;color:var(--ink-soft);font-size:13px;margin-top:14px;cursor:pointer;letter-spacing:1px;transition:color .2s}
.login-back:hover{color:var(--amber-deep)}"""
assert s.count(old) == 1, 'login-tip css'
s = s.replace(old, new)

io.open(p, 'w', encoding='utf-8').write(s)
print('reset html/css ok')

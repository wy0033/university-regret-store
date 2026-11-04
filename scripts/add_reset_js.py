# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) tab 切换隐藏重置视图
old = """document.getElementById('tabLogin').addEventListener('click', ()=>{
  document.getElementById('tabLogin').classList.add('on');
  document.getElementById('tabReg').classList.remove('on');
  document.getElementById('formLogin').classList.add('on');
  document.getElementById('formReg').classList.remove('on');
  loginErr(''); regErr('');
});"""
new = """document.getElementById('tabLogin').addEventListener('click', ()=>{
  document.getElementById('tabLogin').classList.add('on');
  document.getElementById('tabReg').classList.remove('on');
  document.getElementById('formLogin').classList.add('on');
  document.getElementById('formReg').classList.remove('on');
  document.getElementById('formReset').classList.remove('on');
  loginErr(''); regErr(''); rsErr('');
});"""
assert s.count(old) == 1, 'tabLogin'
s = s.replace(old, new)

old = """document.getElementById('tabReg').addEventListener('click', ()=>{
  document.getElementById('tabReg').classList.add('on');
  document.getElementById('tabLogin').classList.remove('on');
  document.getElementById('formReg').classList.add('on');
  document.getElementById('formLogin').classList.remove('on');
  loginErr(''); regErr('');
});"""
new = """document.getElementById('tabReg').addEventListener('click', ()=>{
  document.getElementById('tabReg').classList.add('on');
  document.getElementById('tabLogin').classList.remove('on');
  document.getElementById('formReg').classList.add('on');
  document.getElementById('formLogin').classList.remove('on');
  document.getElementById('formReset').classList.remove('on');
  loginErr(''); regErr(''); rsErr('');
});"""
assert s.count(old) == 1, 'tabReg'
s = s.replace(old, new)

# 2) rsErr 函数（放在 loginErr/regErr 定义后）
old = """function loginErr(msg){ document.getElementById('liErr').textContent = msg; }
function regErr(msg){ document.getElementById('rgErr').textContent = msg; }"""
new = """function loginErr(msg){ document.getElementById('liErr').textContent = msg; }
function regErr(msg){ document.getElementById('rgErr').textContent = msg; }
function rsErr(msg){ document.getElementById('rsErr').textContent = msg; }"""
assert s.count(old) == 1, 'err fns'
s = s.replace(old, new)

# 3) 登录密码错误 → 跳重置视图
old = """  if(acc.pwd !== pwd){ loginErr('密码不对，再想想'); return; }"""
new = """  if(acc.pwd !== pwd){
    document.getElementById('formLogin').classList.remove('on');
    document.getElementById('formReg').classList.remove('on');
    document.getElementById('formReset').classList.add('on');
    document.getElementById('rsName').value = name;
    loginErr(''); regErr('');
    rsErr('密码不对，先重置一个新密码吧');
    return;
  }"""
assert s.count(old) == 1, 'login pwd wrong'
s = s.replace(old, new)

# 4) 重置表单提交 + 返回登录
old = "/* ===== 退出 / 删除账户 ===== */"
new = """/* ===== 重置密码 ===== */
document.getElementById('formReset').addEventListener('submit', e=>{
  e.preventDefault();
  const name = document.getElementById('rsName').value.trim();
  const pwd = document.getElementById('rsPwd').value;
  const pwd2 = document.getElementById('rsPwd2').value;
  if(!name){ rsErr('先填要重置的账户昵称'); return; }
  const list = loadAccounts();
  const acc = list.find(a=>a.name===name);
  if(!acc){ rsErr('没有这个账户，去「注册」一个吧'); return; }
  if(!pwd || pwd.length<4){ rsErr('新密码至少 4 位'); return; }
  if(pwd !== pwd2){ rsErr('两次输入的新密码不一致'); return; }
  acc.pwd = pwd;
  saveAccounts(list);
  state.user = name;
  try{ sessionStorage.setItem('pillCurUser', name); }catch(e){}
  toast('密码已重置，欢迎回来，' + name);
  loadNight();
  enterApp();
  runPending();
});
document.getElementById('resetBack').addEventListener('click', ()=>{
  document.getElementById('formReset').classList.remove('on');
  document.getElementById('formLogin').classList.add('on');
  loginErr(''); regErr(''); rsErr('');
});

/* ===== 退出 / 删除账户 ===== */"""
assert s.count(old) == 1, 'reset js anchor'
s = s.replace(old, new)

io.open(p, 'w', encoding='utf-8').write(s)
print('reset js ok')

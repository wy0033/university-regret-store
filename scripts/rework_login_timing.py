# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) pendingAction 变量（挂在 showLogin 定义之前）
old = "function showLogin(){"
new = "let pendingAction = null; /* collect | openBox */\nfunction showLogin(){"
assert s.count(old) == 1, 'showLogin'
s = s.replace(old, new, 1)

# 2) enterApp 适配游客
old = """function enterApp(){
  const u = currentAccount();
  if(!u){ showLogin(); return; }
  document.getElementById('acctName').textContent = u.name;
  document.getElementById('acctAva').textContent = u.name.charAt(0).toUpperCase();
  document.getElementById('acctName2').textContent = u.name;
  document.getElementById('acctMeta').textContent = '注册于 ' + u.createdAt;
  document.getElementById('loginScreen').classList.add('hide');
  document.getElementById('app').style.display = '';
  loadBox();
  bindPills();
  try{ if('speechSynthesis' in window){ speechSynthesis.getVoices(); } }catch(e){}
}"""
new = """function enterApp(){
  const u = currentAccount();
  if(u){
    document.getElementById('acctName').textContent = u.name;
    document.getElementById('acctAva').textContent = u.name.charAt(0).toUpperCase();
    document.getElementById('acctName2').textContent = u.name;
    document.getElementById('acctMeta').textContent = '注册于 ' + u.createdAt;
  }else{
    document.getElementById('acctName').textContent = '未登录';
    document.getElementById('acctAva').textContent = '?';
    document.getElementById('acctName2').textContent = '游客';
    document.getElementById('acctMeta').textContent = '登录后，药盒和药方记录才会属于你';
  }
  document.getElementById('loginScreen').classList.add('hide');
  document.getElementById('app').style.display = '';
  loadBox();
  bindPills();
  try{ if('speechSynthesis' in window){ speechSynthesis.getVoices(); } }catch(e){}
}
function runPending(){
  const act = pendingAction; pendingAction = null;
  if(act==='collect'){ document.getElementById('collectBtn').click(); }
  else if(act==='openBox'){ document.getElementById('boxBtn').click(); }
}"""
assert s.count(old) == 1, 'enterApp'
s = s.replace(old, new)

# 3) initLogin：游客直接进入
old = """function initLogin(){
  let cur = '';
  try{ cur = sessionStorage.getItem('pillCurUser')||''; }catch(e){}
  if(cur){
    if(loadAccounts().some(a=>a.name===cur)){
      state.user = cur;
      loadNight();
      enterApp();
      return;
    }
  }
  showLogin();
}"""
new = """function initLogin(){
  let cur = '';
  try{ cur = sessionStorage.getItem('pillCurUser')||''; }catch(e){}
  if(cur && loadAccounts().some(a=>a.name===cur)){
    state.user = cur;
  }
  loadNight();
  enterApp();
}"""
assert s.count(old) == 1, 'initLogin'
s = s.replace(old, new)

# 4) 登录成功执行 pendingAction
old = """  state.user = name;
  try{ sessionStorage.setItem('pillCurUser', name); }catch(e){}
  toast('欢迎回来，' + name);
  loadNight();
  enterApp();
});"""
new = """  state.user = name;
  try{ sessionStorage.setItem('pillCurUser', name); }catch(e){}
  toast('欢迎回来，' + name);
  loadNight();
  enterApp();
  runPending();
});"""
assert s.count(old) == 1, 'login submit'
s = s.replace(old, new)

old = """  state.user = name;
  try{ sessionStorage.setItem('pillCurUser', name); }catch(e){}
  toast('账户创建成功，欢迎进店，' + name);
  loadNight();
  enterApp();
});"""
new = """  state.user = name;
  try{ sessionStorage.setItem('pillCurUser', name); }catch(e){}
  toast('账户创建成功，欢迎进店，' + name);
  loadNight();
  enterApp();
  runPending();
});"""
assert s.count(old) == 1, 'reg submit'
s = s.replace(old, new)

# 5) acctBtn：未登录打开登录屏
old = "document.getElementById('acctBtn').addEventListener('click', ()=>document.getElementById('acctModal').classList.add('show'));"
new = """document.getElementById('acctBtn').addEventListener('click', ()=>{
  if(!state.user){ showLogin(); toast('先登录，才能管理账户'); return; }
  document.getElementById('acctModal').classList.add('show');
});"""
assert s.count(old) == 1, 'acctBtn'
s = s.replace(old, new)

# 6) 退出登录：回游客模式
old = """  state.user = null;
  try{ sessionStorage.removeItem('pillCurUser'); }catch(e){}
  toast('已退出登录，下次进店记得登录');
  showLogin();
});"""
new = """  state.user = null;
  try{ sessionStorage.removeItem('pillCurUser'); }catch(e){}
  toast('已退出登录，药盒和药方记录已隐藏');
  loadNight();
  enterApp();
});"""
assert s.count(old) == 1, 'logout'
s = s.replace(old, new)

# 7) 删除账户：回游客模式
old = """  state.user = null;
  document.getElementById('acctModal').classList.remove('show');
  toast('账户已删除');
  showLogin();
});"""
new = """  state.user = null;
  document.getElementById('acctModal').classList.remove('show');
  toast('账户已删除');
  loadNight();
  enterApp();
});"""
assert s.count(old) == 1, 'delAcct'
s = s.replace(old, new)

# 8) collectBtn 登录检查
old = """$('collectBtn').addEventListener('click', ()=>{
  const id = state.pill.id;"""
new = """$('collectBtn').addEventListener('click', ()=>{
  if(!state.user){ pendingAction='collect'; showLogin(); toast('先登录，才能把药收进药盒'); return; }
  const id = state.pill.id;"""
assert s.count(old) == 1, 'collectBtn'
s = s.replace(old, new)

# 9) boxBtn 登录检查
old = "$('boxBtn').addEventListener('click', openBox);"
new = """$('boxBtn').addEventListener('click', ()=>{
  if(!state.user){ pendingAction='openBox'; showLogin(); toast('先登录，才能查看药盒'); return; }
  openBox();
});"""
assert s.count(old) == 1, 'boxBtn'
s = s.replace(old, new)

# 10) 登录屏副标题文案
old = "    <p class=\"login-sub\">先登录，再进店。药盒和药方只属于你自己的账户。</p>"
new = "    <p class=\"login-sub\">药盒和药方只属于你自己的账户，使用时先登录即可。</p>"
assert s.count(old) == 1, 'login sub'
s = s.replace(old, new)

io.open(p, 'w', encoding='utf-8').write(s)
print('login timing rework ok')

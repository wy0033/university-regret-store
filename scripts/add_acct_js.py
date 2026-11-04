# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) state 加 user
old = "let state = {screen:'open', pill:null,"
new = "let state = {user:null, screen:'open', pill:null,"
assert s.count(old) == 1, 'state def not found'
s = s.replace(old, new)

# 2) 账户模块：插到 "/* ===== 工具 ===== */" 之前
acct_js = '''/* ===== 账户系统 ===== */
function loadAccounts(){
  try{ return JSON.parse(localStorage.getItem('pillAccounts')||'[]'); }catch(e){ return []; }
}
function saveAccounts(list){
  try{ localStorage.setItem('pillAccounts', JSON.stringify(list)); }catch(e){}
}
function acctKey(k){ return 'acct_' + (state.user||'guest') + '_' + k; }
function currentAccount(){
  return loadAccounts().find(a=>a.name===state.user) || null;
}
function showLogin(){
  document.getElementById('app').style.display = 'none';
  document.getElementById('loginScreen').classList.remove('hide');
}
function enterApp(){
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
}
function initLogin(){
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
}
/* ===== 登录 / 注册 ===== */
function loginErr(msg){ document.getElementById('liErr').textContent = msg; }
function regErr(msg){ document.getElementById('rgErr').textContent = msg; }
document.getElementById('tabLogin').addEventListener('click', ()=>{
  document.getElementById('tabLogin').classList.add('on');
  document.getElementById('tabReg').classList.remove('on');
  document.getElementById('formLogin').classList.add('on');
  document.getElementById('formReg').classList.remove('on');
  loginErr(''); regErr('');
});
document.getElementById('tabReg').addEventListener('click', ()=>{
  document.getElementById('tabReg').classList.add('on');
  document.getElementById('tabLogin').classList.remove('on');
  document.getElementById('formReg').classList.add('on');
  document.getElementById('formLogin').classList.remove('on');
  loginErr(''); regErr('');
});
document.getElementById('formLogin').addEventListener('submit', e=>{
  e.preventDefault();
  const name = document.getElementById('liName').value.trim();
  const pwd = document.getElementById('liPwd').value;
  if(!name || !pwd){ loginErr('昵称和密码都要填哦'); return; }
  const acc = loadAccounts().find(a=>a.name===name);
  if(!acc){ loginErr('还没有这个账户，先去「注册」一个吧'); return; }
  if(acc.pwd !== pwd){ loginErr('密码不对，再想想'); return; }
  state.user = name;
  try{ sessionStorage.setItem('pillCurUser', name); }catch(e){}
  toast('欢迎回来，' + name);
  loadNight();
  enterApp();
});
document.getElementById('formReg').addEventListener('submit', e=>{
  e.preventDefault();
  const name = document.getElementById('rgName').value.trim();
  const pwd = document.getElementById('rgPwd').value;
  const pwd2 = document.getElementById('rgPwd2').value;
  if(!name){ regErr('先取一个昵称吧'); return; }
  if(name.length<2){ regErr('昵称至少 2 个字'); return; }
  if(!pwd){ regErr('设置一个密码吧'); return; }
  if(pwd.length<4){ regErr('密码至少 4 位'); return; }
  if(pwd !== pwd2){ regErr('两次输入的密码不一致'); return; }
  const list = loadAccounts();
  if(list.some(a=>a.name===name)){ regErr('这个昵称已经有人用啦，换一个试试（不能重名）'); return; }
  const d = new Date();
  const p2 = n => String(n).padStart(2,'0');
  list.push({name, pwd, createdAt: d.getFullYear()+'-'+p2(d.getMonth()+1)+'-'+p2(d.getDate())});
  saveAccounts(list);
  state.user = name;
  try{ sessionStorage.setItem('pillCurUser', name); }catch(e){}
  toast('账户创建成功，欢迎进店，' + name);
  loadNight();
  enterApp();
});
/* ===== 退出 / 删除账户 ===== */
document.getElementById('acctBtn').addEventListener('click', ()=>document.getElementById('acctModal').classList.add('show'));
document.getElementById('acctClose').addEventListener('click', ()=>document.getElementById('acctModal').classList.remove('show'));
document.getElementById('acctModal').addEventListener('click', e=>{ if(e.target===document.getElementById('acctModal')) document.getElementById('acctModal').classList.remove('show'); });
document.getElementById('logoutBtn').addEventListener('click', ()=>{
  document.getElementById('acctModal').classList.remove('show');
  state.user = null;
  try{ sessionStorage.removeItem('pillCurUser'); }catch(e){}
  toast('已退出登录，下次进店记得登录');
  showLogin();
});
document.getElementById('delAcctBtn').addEventListener('click', ()=>{
  const u = currentAccount();
  if(!u) return;
  if(!confirm('确定删除账户「' + u.name + '」吗？')) return;
  if(!confirm('删除后，这个账户的药盒和所有药方记录都会被清空，且无法恢复。真的要删除吗？')) return;
  let list = loadAccounts();
  list = list.filter(a=>a.name!==u.name);
  saveAccounts(list);
  try{
    Object.keys(localStorage).forEach(k=>{ if(k.indexOf('acct_'+u.name+'_')===0) localStorage.removeItem(k); });
  }catch(e){}
  try{ sessionStorage.removeItem('pillCurUser'); }catch(e){}
  state.user = null;
  document.getElementById('acctModal').classList.remove('show');
  toast('账户已删除');
  showLogin();
});

/* ===== 工具 ===== */'''
old_tool = '/* ===== 工具 ===== */'
assert s.count(old_tool) == 1, 'tool comment not found'
s = s.replace(old_tool, acct_js)

io.open(p, 'w', encoding='utf-8').write(s)
print('acct module ok')

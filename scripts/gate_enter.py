# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) enterBtn：未登录先登录，登录后自动进选药屏
old = """$('enterBtn').addEventListener('click', ()=>{
  showScreen('pick');
  toast('店长：' + CLERK.open);
});"""
new = """$('enterBtn').addEventListener('click', ()=>{
  if(!state.user){ pendingAction='enter'; showLogin(); toast('先登录，才能推门进店选药'); return; }
  showScreen('pick');
  toast('店长：' + CLERK.open);
});"""
assert s.count(old) == 1, 'enterBtn'
s = s.replace(old, new)

# 2) runPending 增加 enter 分支
old = """function runPending(){
  const act = pendingAction; pendingAction = null;
  if(act==='collect'){ document.getElementById('collectBtn').click(); }
  else if(act==='openBox'){ document.getElementById('boxBtn').click(); }
}"""
new = """function runPending(){
  const act = pendingAction; pendingAction = null;
  if(act==='enter'){ showScreen('pick'); toast('店长：' + CLERK.open); }
  else if(act==='collect'){ document.getElementById('collectBtn').click(); }
  else if(act==='openBox'){ document.getElementById('boxBtn').click(); }
}"""
assert s.count(old) == 1, 'runPending'
s = s.replace(old, new)

# 3) 登录屏副标题文案同步（进店即登录）
old = "    <p class=\"login-sub\">药盒和药方只属于你自己的账户，使用时先登录即可。</p>"
new = "    <p class=\"login-sub\">先登录，再推门进店。药盒和药方只属于你自己的账户。</p>"
assert s.count(old) == 1, 'login sub'
s = s.replace(old, new)

io.open(p, 'w', encoding='utf-8').write(s)
print('enter gate ok')

# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) loadBox key
old = "try{ state.collected = JSON.parse(localStorage.getItem('pillBox')||'[]'); }catch(e){ state.collected = []; }"
new = "try{ state.collected = JSON.parse(localStorage.getItem(acctKey('pillBox'))||'[]'); }catch(e){ state.collected = []; }"
assert s.count(old) == 1, 'loadBox'
s = s.replace(old, new)

# 2) saveBox key
old = "localStorage.setItem('pillBox', JSON.stringify(state.collected));"
new = "localStorage.setItem(acctKey('pillBox'), JSON.stringify(state.collected));"
assert s.count(old) == 1, 'saveBox'
s = s.replace(old, new)

# 3) getRecords key
old = "try{ return JSON.parse(localStorage.getItem('pillRecords')||'[]'); }catch(e){ return []; }"
new = "try{ return JSON.parse(localStorage.getItem(acctKey('pillRecords'))||'[]'); }catch(e){ return []; }"
assert s.count(old) == 1, 'getRecords'
s = s.replace(old, new)

# 4) saveRecord / updateRecordDone / deleteRecord key（3 处相同）
old = "localStorage.setItem('pillRecords', JSON.stringify(recs));"
new = "localStorage.setItem(acctKey('pillRecords'), JSON.stringify(recs));"
cnt = s.count(old)
assert cnt == 3, f'pillRecords setItem count = {cnt}'
s = s.replace(old, new)

# 5) 夜间初始化重构
old = """let nightManual = null;
try{ nightManual = localStorage.getItem('nightManual'); }catch(e){}
applyNight(nightManual ? nightManual==='1' : nightNow());"""
new = """let nightManual = null;
function loadNight(){
  try{ nightManual = state.user ? localStorage.getItem(acctKey('nightManual')) : null; }catch(e){ nightManual = null; }
  applyNight(nightManual ? nightManual==='1' : nightNow());
}"""
assert s.count(old) == 1, 'night init'
s = s.replace(old, new)

# 6) nightToggle 保存 key
old = """  nightManual = on?'1':'0';
  try{ localStorage.setItem('nightManual', nightManual); }catch(e){}"""
new = """  nightManual = on?'1':'0';
  if(state.user){ try{ localStorage.setItem(acctKey('nightManual'), nightManual); }catch(e){} }"""
assert s.count(old) == 1, 'night save'
s = s.replace(old, new)

# 7) 初始化流程
old = """/* ===== 初始化 ===== */
loadBox();
bindPills();
if('speechSynthesis' in window){ speechSynthesis.getVoices(); }"""
new = """/* ===== 初始化 ===== */
initLogin();"""
assert s.count(old) == 1, 'init flow'
s = s.replace(old, new)

io.open(p, 'w', encoding='utf-8').write(s)
print('keys + night + init ok')

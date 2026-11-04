# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) rankAfterChange：toast 改弹窗
old = """function rankAfterChange(){
  const before = rankCache ? (rankCache.tier.key + rankCache.level) : '';
  const r = renderRank();
  const after = r.tier.key + r.level;
  if(before && before!==after){
    toast('恭喜升级：' + r.tier.name + ' ' + r.level + ' 级');
  }
  return r;
}"""
new = """function rankAfterChange(){
  const before = rankCache ? (rankCache.tier.key + rankCache.level) : '';
  const r = renderRank();
  const after = r.tier.key + r.level;
  if(before && before!==after){
    const chip = $('rankupChip');
    chip.style.background = r.tier.color;
    chip.textContent = r.tier.name + ' ' + r.level + ' 级';
    $('rankupNote').textContent = r.note || '继续配药，解锁更多等级';
    $('rankupModal').classList.add('show');
  }
  return r;
}"""
assert s.count(old) == 1, 'rankAfterChange'
s = s.replace(old, new)

# 2) 登录成功弹公告（三处 enterApp(); runPending(); 后追加 showNotice();）
old = """  toast('欢迎回来，' + name);
  loadNight();
  enterApp();
  runPending();
});"""
new = """  toast('欢迎回来，' + name);
  loadNight();
  enterApp();
  runPending();
  showNotice();
});"""
assert s.count(old) == 1, 'login submit'
s = s.replace(old, new)

old = """  toast('账户创建成功，欢迎进店，' + name);
  loadNight();
  enterApp();
  runPending();
});"""
new = """  toast('账户创建成功，欢迎进店，' + name);
  loadNight();
  enterApp();
  runPending();
  showNotice();
});"""
assert s.count(old) == 1, 'reg submit'
s = s.replace(old, new)

old = """  toast('密码已重置，欢迎回来，' + name);
  loadNight();
  enterApp();
  runPending();
});"""
new = """  toast('密码已重置，欢迎回来，' + name);
  loadNight();
  enterApp();
  runPending();
  showNotice();
});"""
assert s.count(old) == 1, 'reset submit'
s = s.replace(old, new)

# 3) 公告逻辑（插在 /* ===== 等级系统 ===== */ 之前）
notice_js = """/* ===== 公告 ===== */
function showNotice(){
  if(state.user){
    const r = renderRank();
    $('noticeUser').textContent = state.user;
    $('noticeRankLine').textContent = '你目前是：' + r.tier.name + ' ' + r.level + ' 级，继续配药升级吧';
  }else{
    $('noticeUser').textContent = '同学';
    $('noticeRankLine').textContent = '登录后开启等级成长';
  }
  $('noticeModal').classList.add('show');
}
$('noticeBtn').addEventListener('click', showNotice);
$('noticeClose').addEventListener('click', ()=>$('noticeModal').classList.remove('show'));
$('noticeModal').addEventListener('click', e=>{ if(e.target===$('noticeModal')) $('noticeModal').classList.remove('show'); });
$('rankupClose').addEventListener('click', ()=>$('rankupModal').classList.remove('show'));
$('rankupModal').addEventListener('click', e=>{ if(e.target===$('rankupModal')) $('rankupModal').classList.remove('show'); });

/* ===== 等级系统 ===== */"""
old = "/* ===== 等级系统 ===== */"
assert s.count(old) == 1, 'notice js anchor'
s = s.replace(old, notice_js)

io.open(p, 'w', encoding='utf-8').write(s)
print('notice js ok')

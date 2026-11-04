# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) 等级系统 JS（插在 /* ===== 药盒 ===== */ 之前）
rank_js = """/* ===== 等级系统 ===== */
const RANK_TIERS = [
  {key:'iron',    name:'黑铁', color:'#8D7B68'},
  {key:'bronze',  name:'青铜', color:'#B08D57'},
  {key:'silver',  name:'白银', color:'#9AA3AD'},
  {key:'gold',    name:'黄金', color:'#D4A017'},
  {key:'diamond', name:'钻石', color:'#4A90D9'},
  {key:'glory',   name:'荣耀', color:'#9B59B6'}
];
let rankCache = null;
function calcRank(){
  const recs = getRecords();
  const per = {}, adv = {};
  PILLS.forEach(p=>{ per[p.id]=0; adv[p.id]=0; });
  recs.forEach(r=>{ if(per[r.pillId]!=null){ per[r.pillId]++; if(r.version==='pro') adv[r.pillId]++; } });
  const ids = PILLS.map(p=>p.id);
  const total = ids.reduce((s,id)=>s+per[id],0);
  const doneCount = ids.filter(id=>per[id]>0).length;
  const allDone = ids.every(id=>per[id]>=1);
  const allAdv = allDone && ids.every(id=>adv[id]===per[id]) && total>0;
  let tier, level, sub, note;
  if(allAdv){
    tier = RANK_TIERS[5];
    level = Math.min.apply(null, ids.map(id=>adv[id]));
    sub = '8 瓶全部进阶定制完成';
    note = '每瓶药再完成 1 次进阶，即可升 ' + tier.name + ' ' + (level+1) + ' 级（无上限）';
  }else if(allDone){
    tier = RANK_TIERS[4];
    level = Math.min.apply(null, ids.map(id=>per[id]));
    sub = '8 瓶全部集齐' + (total>8 ? '，含重复完成' : '');
    note = '每瓶药再完成 1 次，即可升 ' + tier.name + ' ' + (level+1) + ' 级（无上限）';
  }else{
    let pts = ids.reduce((s,id)=>s + per[id] + adv[id], 0);
    const rawPts = pts;
    pts = Math.min(pts, 11);
    const ti = Math.min(Math.floor(pts/3), 3);
    const lv = pts%3+1;
    tier = RANK_TIERS[ti]; level = lv;
    sub = '已解锁 ' + total + ' 次药方 · 已集齐 ' + doneCount + '/8 瓶';
    if(ti===3 && lv===3){
      note = '已到黄金 3 级满级，集齐 8 瓶直升钻石 1 级';
    }else{
      const nextName = lv===3
        ? RANK_TIERS[ti+1].name + ' 1 级'
        : tier.name + ' ' + (lv+1) + ' 级';
      note = '再完成 1 次（普通 +1 级 / 进阶 +2 级）即可升 ' + nextName;
    }
    if(doneCount<8){
      note += '；还差 ' + (8-doneCount) + ' 瓶集齐，集齐 8 瓶直升钻石 1 级';
    }
  }
  return {tier, level, sub, note, total, doneCount, allDone, allAdv};
}
function renderRank(){
  const r = calcRank();
  const badge = $('rankBadge');
  if(!state.user){
    badge.style.display = 'none';
    $('rankPanel').style.display = 'none';
    rankCache = r;
    return r;
  }
  badge.style.display = 'inline-flex';
  badge.style.background = r.tier.color;
  $('rankBadgeTxt').textContent = r.tier.name + ' ' + r.level + ' 级';
  const panel = $('rankPanel');
  panel.style.display = '';
  const chip = $('rankChip');
  chip.style.background = r.tier.color;
  chip.textContent = r.tier.name + ' ' + r.level + ' 级';
  $('rankSub').textContent = r.sub;
  $('rankNote').textContent = r.note;
  rankCache = r;
  return r;
}
function rankAfterChange(){
  const before = rankCache ? (rankCache.tier.key + rankCache.level) : '';
  const r = renderRank();
  const after = r.tier.key + r.level;
  if(before && before!==after){
    toast('恭喜升级：' + r.tier.name + ' ' + r.level + ' 级');
  }
  return r;
}

/* ===== 药盒 ===== */"""
old = "/* ===== 药盒 ===== */"
assert s.count(old) == 1, 'rank js anchor'
s = s.replace(old, rank_js)

# 2) saveRecord 末尾触发升级检测
old = """  localStorage.setItem(acctKey('pillRecords'), JSON.stringify(recs));
}
function renderRecCard(pill, r, idx){"""
new = """  localStorage.setItem(acctKey('pillRecords'), JSON.stringify(recs));
  if(state.user) rankAfterChange();
}
function renderRecCard(pill, r, idx){"""
assert s.count(old) == 1, 'saveRecord'
s = s.replace(old, new)

# 3) enterApp 登录/游客后刷新等级
old = """  document.getElementById('loginScreen').classList.add('hide');
  document.getElementById('app').style.display = '';
  loadBox();
  bindPills();"""
new = """  document.getElementById('loginScreen').classList.add('hide');
  document.getElementById('app').style.display = '';
  loadBox();
  bindPills();
  renderRank();"""
assert s.count(old) == 1, 'enterApp'
s = s.replace(old, new)

# 4) acctBtn 打开弹窗时刷新等级
old = """document.getElementById('acctBtn').addEventListener('click', ()=>{
  if(!state.user){ showLogin(); toast('先登录，才能管理账户'); return; }
  document.getElementById('acctModal').classList.add('show');
});"""
new = """document.getElementById('acctBtn').addEventListener('click', ()=>{
  if(!state.user){ showLogin(); toast('先登录，才能管理账户'); return; }
  renderRank();
  document.getElementById('acctModal').classList.add('show');
});"""
assert s.count(old) == 1, 'acctBtn'
s = s.replace(old, new)

io.open(p, 'w', encoding='utf-8').write(s)
print('rank js ok')

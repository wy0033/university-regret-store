// 验证 v15：p3/p4/p8 时间点按年级动态 + 4/3/2/1 年级映射（大一四年后…大四一年后）
const fs = require('fs');
const h = fs.readFileSync('C:/Users/37800/Doubao/chats/2026-09-12/new-chat/regret-store/index.html', 'utf8');
const pillsMatch = h.match(/const PILLS = \[[\s\S]*?\n\];/);
const funcMatch = h.match(/function fill\(text, d\)\{[\s\S]*?\n\/\* ===== 开场 ===== \*\//);
if (!pillsMatch || !funcMatch) throw new Error('extract fail');
const script = pillsMatch[0] + '\n' + funcMatch[0] + '\n' + `
const grades = ['大一','大二','大三','大四'];
const yearOf = {大一:4, 大二:3, 大三:2, 大四:1};
const cnOf = {4:'四', 3:'三', 2:'两', 1:'一'};
const signOf = {大一:'四年后的你', 大二:'三年后的你', 大三:'两年后的你', 大四:'一年后的你'};
const p3expect = {大一:'到了大二下学期，你开始', 大二:'就是从这学期开始，你', 大三:'大二下学期你开始', 大四:'大二下学期你开始'};
const p4expect = {大一:'到了大三的秋天，', 大二:'到了大三的秋天，', 大三:'就是今年秋天，', 大四:'大三的秋天，'};
const p8aExpect = {大一:'因为到了大二，你也是这样', 大二:'因为现在的你，就是这样', 大三:'因为大二那年的我，也是这样', 大四:'因为大二那年的我，也是这样'};
const p8bExpect = {大一:'到了大三体测，你跑完八百米', 大二:'到了大三体测，你跑完八百米', 大三:'这次体测，你跑完八百米', 大四:'大三体测你跑完八百米'};
let fail = 0;
for(const g of grades){
  const s = {version:'pro', grade:g, major:'计算机', gender:'男生', goal:'考研上岸杭电', nick:'小张', detail:'错过一次竞赛报名', stateInfo:'有点焦虑', mood:'平静', answer:'还没翻开书', anxiety:'自动控制原理好难'};
  const y = yearOf[g], cn = cnOf[y];
  for(const pid of ['p1','p3','p4','p5','p7','p8']){
    const pill = PILLS.find(x=>x.id===pid);
    const letter = buildLetter(pill, s);
    const kw = applyYears(pill.keyword[0], g);
    let errs = [];
    if(!letter.includes('—— ' + signOf[g])) errs.push('署名应为['+signOf[g]+']');
    for(const other of grades.filter(x=>x!==g)){
      const ocn = cnOf[yearOf[other]];
      if(letter.includes(ocn + '年后')) errs.push('不应含[' + ocn + '年后]');
    }
    if(pid==='p3' && !letter.includes(p3expect[g])) errs.push('p3时间点应为['+p3expect[g]+']');
    if(pid==='p4'){
      if(!letter.includes(p4expect[g])) errs.push('p4时间点应为['+p4expect[g]+']');
      if(!letter.includes(cn+'年前的我们')) errs.push('p4 X年前的我们不匹配');
    }
    if(pid==='p8'){
      if(!letter.includes(p8aExpect[g])) errs.push('p8a应为['+p8aExpect[g]+']');
      if(!letter.includes(p8bExpect[g])) errs.push('p8b应为['+p8bExpect[g]+']');
      if(!letter.includes('剩下的'+cn+'年，值得')) errs.push('p8 剩下的X年不匹配');
    }
    if(pid==='p5' && letter.includes('三年没说的话')) errs.push('p5三年未中性化');
    if(kw.startsWith(cn+'年后')===false) errs.push('keyword前缀应为['+cn+'年后:]实际['+kw.slice(0,8)+']');
    if(!letter.includes(cn+'年后的我可以告诉你')) errs.push('goal段年限不匹配');
    if(errs.length){ fail++; console.log('FAIL', pid, g, errs.join(' | ')); }
    else console.log('OK ', pid, g, '|', letter.slice(-24).replace(/\\n/g,' '));
  }
}
// actions 动态（p7 你有X年）
for(const g of grades){
  const cn = cnOf[yearOf[g]];
  const pill = PILLS.find(x=>x.id==='p7');
  const act = pill.actions.find(a=>a.includes('你有四年'));
  if(!applyYears(act, g).includes('你有'+cn+'年')){ fail++; console.log('FAIL actions p7', g); }
}
console.log(fail ? ('FAILS='+fail) : 'ALL PASS');
`;
fs.writeFileSync(__dirname + '/verify_v15_run.js', script, 'utf8');
console.log('verify_v15 generated');

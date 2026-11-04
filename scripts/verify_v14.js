// 从 index.html 提取真实 PILLS 数据与 buildLetter 相关纯函数，验证年级动态化
const fs = require('fs');
const h = fs.readFileSync('C:/Users/37800/Doubao/chats/2026-09-12/new-chat/regret-store/index.html', 'utf8');

const pillsMatch = h.match(/const PILLS = \[[\s\S]*?\n\];/);
if (!pillsMatch) throw new Error('PILLS not found');
const funcMatch = h.match(/function fill\(text, d\)\{[\s\S]*?\n\/\* ===== 开场 ===== \*\//);
if (!funcMatch) throw new Error('funcs not found');

const script = pillsMatch[0] + '\n' + funcMatch[0] + '\n' + `
const grades = ['大一','大二','大三','大四'];
const yearOf = {大一:4, 大二:3, 大三:2, 大四:1};
const cnOf = {4:'四', 3:'三', 2:'两', 1:'一'};
const signOf = {大一:'四年后的你', 大二:'三年后的你', 大三:'两年后的你', 大四:'一年后的你'};
let fail = 0;
for(const g of grades){
  const s = {version:'pro', grade:g, major:'计算机', gender:'保密', goal:'考研上岸杭电', nick:'小张', detail:'错过一次竞赛报名', stateInfo:'有点焦虑', mood:'平静', answer:'还没翻开书', anxiety:'自动控制原理好难'};
  const y = yearOf[g], cn = cnOf[y];
  for(const pid of ['p1','p4','p5','p7','p8']){
    const pill = PILLS.find(x=>x.id===pid);
    const letter = buildLetter(pill, s);
    const kw = applyYears(pill.keyword[0], g);
    let errs = [];
    if(!letter.includes('—— ' + signOf[g])) errs.push('署名应为['+signOf[g]+']');
    for(const other of grades.filter(x=>x!==g)){
      const oy = yearOf[other], ocn = cnOf[oy];
      if(letter.includes(ocn + '年后')) errs.push('不应含[' + ocn + '年后]');
    }
    if(letter.includes('你有' + cn + '年')===false && letter.includes('你有四年')) errs.push('你有X年未动态');
    if(letter.includes(cn+'年前的我们')===false && letter.includes('年前的我们') && !letter.includes(cn+'年前的我们')) errs.push('X年前的我们不匹配');
    const act0 = applyYears(pill.actions[0], g);
    if(pill.actions.some(a=>a.includes('你有四年')) && !applyYears(pill.actions.find(a=>a.includes('你有四年')), g).includes('你有'+cn+'年')) errs.push('actions你有X年未动态');
    if(kw.startsWith(cn+'年后')===false) errs.push('keyword前缀应为['+cn+'年后:]实际['+kw.slice(0,8)+']');
    if(letter.includes('三年没说的话') || letter.includes('三年的话')) errs.push('p5三年未中性化');
    if(letter.includes('大三的秋天') || letter.includes('大三体测')) errs.push('大三表述未中性化');
    if(letter.includes('这四年')) errs.push('这四年未中性化');
    if(letter.includes('剩下的'+cn+'年')===false && letter.includes('剩下的')) errs.push('剩下的X年不匹配');
    if(letter.includes(cn+'年后的我可以告诉你')===false) errs.push('goal段年限不匹配');
    if(errs.length){ fail++; console.log('FAIL', pid, g, errs.join(' | '), '>>>', letter.slice(-80).replace(/\\n/g,' ')); }
    else console.log('OK ', pid, g, '|', letter.slice(-24).replace(/\\n/g,' '));
  }
}
// p4 中性锚点检查
{
  const s = {version:'normal', grade:'大四', major:'', gender:'保密', goal:'', nick:'', detail:'', stateInfo:'', mood:'', answer:'', anxiety:'喜欢一个人不敢开口'};
  const letter = buildLetter(PILLS.find(x=>x.id==='p4'), s);
  if(!letter.includes('后来的那个秋天')) { fail++; console.log('FAIL p4 秋天锚点'); }
  if(letter.includes('一年后的你')===false){ fail++; console.log('FAIL p4 大四署名'); }
  console.log('OK  p4 大四·normal |', letter.slice(-30).replace(/\\n/g,' '));
}
console.log(fail ? ('FAILS='+fail) : 'ALL PASS');
`;
fs.writeFileSync(__dirname + '/verify_v14_run.js', script, 'utf8');
console.log('verify_v14 generated');

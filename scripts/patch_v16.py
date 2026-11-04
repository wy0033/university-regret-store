# -*- coding: utf-8 -*-
import io
p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(p, encoding='utf-8') as f:
    h = f.read()

def rep(old, new, cnt=1):
    global h
    assert old in h, 'ANCHOR MISS: ' + old[:70]
    h = h.replace(old, new, cnt)

# 1) 工具函数块：数字映射 -> 同学版文本映射（三年后/两年后/一年后/毕业后）
rep("""const GRADE_YEARS = {大一:4, 大二:3, 大三:2, 大四:1};
const YEARS_CN = {4:'四', 3:'三', 2:'两', 1:'一'};
function gradeYears(g){ return GRADE_YEARS[g] || 4; }
function yearsText(g){ return (YEARS_CN[gradeYears(g)] || '四') + '年'; }
function voiceLabelText(){ return '听「' + yearsText(state.grade) + '后的你」读这封信'; }
function applyYears(text, g){
  const cn = YEARS_CN[gradeYears(g)] || '四';
  return text
    .split('三年').join('很久')
    .split('这四年').join('大学里')
    .split('四年前的我们').join(cn + '年前的我们')
    .split('你有四年').join('你有' + cn + '年')
    .split('你的四年，值得').join('剩下的' + cn + '年，值得')
    .split('四年后').join(cn + '年后');
}""",
"""function gradeSign(grade){
  return {'大一':'三年后的你','大二':'两年后的你','大三':'一年后的你','大四':'刚毕业的你'}[grade] || '大四的你';
}
function laterLabel(grade){
  return {'大一':'三年后','大二':'两年后','大三':'一年后','大四':'毕业后'}[grade] || '四年后';
}
function agoLabel(grade){
  return {'大一':'三年前','大二':'两年前','大三':'一年前','大四':'四年前'}[grade] || '四年前';
}
function remLabel(grade){
  return {'大一':'三年','大二':'两年','大三':'一年','大四':'大半年'}[grade] || '几年';
}
function voiceLabelText(){ return '听「' + gradeSign(state.grade) + '」读这封信'; }
function applyYears(text, g){
  return text
    .split('三年').join('很久')
    .split('这四年').join('大学里')
    .split('四年前的我们').join(agoLabel(g) + '的我们')
    .split('你有四年').join('你有' + remLabel(g))
    .split('你的四年，值得').join('剩下的' + remLabel(g) + '，值得')
    .split('四年后').join(laterLabel(g));
}""")

# 2) buildLetter 署名位
rep("""  t = applyYears(t, s.grade);
  return t.split('—— 大四的你').join('—— ' + yearsText(s.grade) + '后的你');
}""",
"""  t = applyYears(t, s.grade);
  return t.split('—— 大四的你').join('—— ' + gradeSign(s.grade));
}""")

# 3) 分享弹窗副标题
rep("""  $('shareSub').textContent = '把' + yearsText(state.grade) + '后的答案，递给朋友';""",
"""  $('shareSub').textContent = '把' + laterLabel(state.grade) + '的答案，递给朋友';""")

with io.open(p, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(h)
print('patch_v16 ok')

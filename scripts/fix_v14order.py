# -*- coding: utf-8 -*-
import io
p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(p, encoding='utf-8') as f:
    h = f.read()

old = """function applyYears(text, g){
  const cn = YEARS_CN[gradeYears(g)] || '四';
  return text
    .split('四年后').join(cn + '年后')
    .split('你有四年').join('你有' + cn + '年')
    .split('你的四年，值得').join('剩下的' + cn + '年，值得')
    .split('三年').join('很久')
    .split('大三的秋天').join('后来的那个秋天')
    .split('大三体测').join('那学期的体测')
    .split('这四年').join('大学里')
    .split('四年前的我们').join(cn + '年前的我们');
}"""
new = """function applyYears(text, g){
  const cn = YEARS_CN[gradeYears(g)] || '四';
  return text
    .split('三年').join('很久')
    .split('大三的秋天').join('后来的那个秋天')
    .split('大三体测').join('那学期的体测')
    .split('这四年').join('大学里')
    .split('四年前的我们').join(cn + '年前的我们')
    .split('你有四年').join('你有' + cn + '年')
    .split('你的四年，值得').join('剩下的' + cn + '年，值得')
    .split('四年后').join(cn + '年后');
}"""
assert old in h, 'applyYears anchor not found'
h = h.replace(old, new, 1)
with io.open(p, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(h)
print('applyYears order fixed')

# -*- coding: utf-8 -*-
import io

path = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(path, encoding='utf-8') as f:
    h = f.read()

old = """  if(s.goal) t = t.replace('—— 大四的你', '还有你写在方子上的那个目标——「' + s.goal + '」。四年后的我可以告诉你：你真的做到了。\\n\\n—— 大四的你');
  if(s.goal && /考研|读研|研究生|上岸|保研/.test(s.goal)){"""
new = """  if(s.goal) t = t.replace('—— 大四的你', '还有你写在方子上的那个目标——「' + s.goal + '」。四年后的我可以告诉你：你真的做到了。\\n\\n—— 大四的你');
  if(s.goal && p.id==='p6'){
    t = t.replace('你连「想做什么」都说不出来', '你心里其实有个方向——「' + s.goal + '」，只是还不敢说出口');
  }
  if(s.goal && /考研|读研|研究生|上岸|保研/.test(s.goal)){"""
assert old in h, 'anchor not found'
h = h.replace(old, new)
with io.open(path, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(h)
print('patched ok')

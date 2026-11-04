# -*- coding: utf-8 -*-
import io

path = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(path, encoding='utf-8') as f:
    h = f.read()

def rep(old, new, must=True):
    global h
    if old not in h:
        if must:
            raise AssertionError('NOT FOUND: ' + old[:80])
        return
    h = h.replace(old, new, 1)

# 三段织入改为锚定署名「—— 大四的你」，避免文案内破折号造成错位
rep("""    t = t.replace('——', '对了，配药的时候你告诉我：「' + s.answer + '」。你当时没多想，后来回头看，那正是故事的转折点。' + echo + '\\n\\n——');""",
"""    t = t.replace('—— 大四的你', '对了，配药的时候你告诉我：「' + s.answer + '」。你当时没多想，后来回头看，那正是故事的转折点。' + echo + '\\n\\n—— 大四的你');""")

rep("""  if(s.version==='pro' && s.detail) t = t.replace('——', '还有件小事，你当时觉得可惜——「' + s.detail + '」。四年后的我可以告诉你：那件事后来有了个意外的结果，你从里面拿到了比结果更珍贵的东西。\\n\\n——');""",
"""  if(s.version==='pro' && s.detail) t = t.replace('—— 大四的你', '还有件小事，你当时觉得可惜——「' + s.detail + '」。四年后的我可以告诉你：那件事后来有了个意外的结果，你从里面拿到了比结果更珍贵的东西。\\n\\n—— 大四的你');""")

rep("""  if(s.goal) t = t.replace('——', '还有你写在方子上的那个目标——「' + s.goal + '」。四年后的我可以告诉你：你真的做到了。\\n\\n——');""",
"""  if(s.goal) t = t.replace('—— 大四的你', '还有你写在方子上的那个目标——「' + s.goal + '」。四年后的我可以告诉你：你真的做到了。\\n\\n—— 大四的你');""")

with io.open(path, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(h)
print('anchor fix ok')

# -*- coding: utf-8 -*-
import io
p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
with io.open(p, encoding='utf-8') as f:
    h = f.read()
old = """    localStorage.setItem('pillRecords', JSON.stringify(recs));
  }
}
}
$('histClose')"""
new = """    localStorage.setItem('pillRecords', JSON.stringify(recs));
  }
}
$('histClose')"""
assert old in h, 'dup brace block not found'
h = h.replace(old, new)
with io.open(p, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(h)
print('fixed ok')

# -*- coding: utf-8 -*-
import os, urllib.request

base = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\assets'
os.makedirs(base, exist_ok=True)

imgs = {
    'hero.jpg': 'https://aka.doubaocdn.com/s/VpqROeUWKt',
    'p1.jpg': 'https://aka.doubaocdn.com/s/ppjVtIGrBH',
    'p2.jpg': 'https://aka.doubaocdn.com/s/b39ebZpbWJ',
    'p3.jpg': 'https://aka.doubaocdn.com/s/p93aLVX0nU',
    'p4.jpg': 'https://aka.doubaocdn.com/s/BvpZEB8fIc',
    'p5.jpg': 'https://aka.doubaocdn.com/s/agoTXe5qYU',
    'p6.jpg': 'https://aka.doubaocdn.com/s/xDSFvUNmkq',
    'p7.jpg': 'https://aka.doubaocdn.com/s/vF7Vceprtj',
    'p8.jpg': 'https://aka.doubaocdn.com/s/6juRwtVu97',
}

for name, url in imgs.items():
    path = os.path.join(base, name)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=60) as r, open(path, 'wb') as f:
        f.write(r.read())
    print(name, os.path.getsize(path), 'bytes')

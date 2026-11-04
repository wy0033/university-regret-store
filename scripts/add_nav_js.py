# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) showScreen：历史栈 + 导航按钮显隐
old = """function showScreen(name){
  screens.forEach(s => $(`screen-${s}`).classList.toggle('active', s===name));
  state.screen = name;
  window.scrollTo({top:0, behavior:'smooth'});
}"""
new = """let histStack = [];
function showScreen(name, noHist){
  if(!noHist && histStack[histStack.length-1] !== state.screen){
    histStack.push(state.screen);
  }
  screens.forEach(s => $(`screen-${s}`).classList.toggle('active', s===name));
  state.screen = name;
  const nav = $('navFloat');
  if(nav) nav.style.display = (name==='open') ? 'none' : 'flex';
  window.scrollTo({top:0, behavior:'smooth'});
}
function stopFlowTimers(){
  if(mixTimer) clearInterval(mixTimer);
  if(twTimer) clearInterval(twTimer);
}
$('backBtn').addEventListener('click', ()=>{
  let prev = null;
  while(histStack.length){
    prev = histStack.pop();
    if(prev !== state.screen) break;
    prev = null;
  }
  if(prev){
    stopFlowTimers();
    showScreen(prev, true);
    toast('已返回上一页');
  }else{
    toast('已经在第一页啦');
  }
});
$('endBtn').addEventListener('click', ()=>{
  histStack = [];
  stopFlowTimers();
  stopVoice();
  showScreen('open', true);
  toast('欢迎下次光临，记得照顾好自己');
});"""
assert s.count(old) == 1, 'showScreen'
s = s.replace(old, new)

io.open(p, 'w', encoding='utf-8').write(s)
print('nav js ok')

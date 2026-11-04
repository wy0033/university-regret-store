
/* ===== 数据：8 瓶后悔药 ===== */
const PILLS = [
  {id:'p1', no:'①', name:'不挂科', quote:{t:'聪明在于勤奋，天才在于积累',a:'华罗庚'}, tag:'考试周专用', promise:'期末不挂科，毕业不后悔',
   anxietyPh:'比如：自动控制原理好难',
   loading:['正在统计你这周刷过的学习通视频数……','正在计算你在图书馆占座的胜率……','正在备份你熬夜掉的头发……'],
   letter:'嘿，现在的你：我知道你最近在为「{anxiety}」发愁，书上的方框图像迷宫，你觉得自己什么都没学会。但我想告诉你：这门课我最后考了 89 分。不是因为突然变聪明了，是因为你后来把课后题一道一道啃完了。你现在觉得跨不过去的坎，只是因为你还在山脚下。对了，你现在担心的那个竞赛，后来拿了省二。你在图书馆熬的每一个夜，都在变成你简历上的一行字。别害怕。你走的每一步都作数。—— 大四的你，刚拿到 offer 的那个晚上',
   keyword:['四年后：考了 89 分，进了心仪的公司'],
   actions:['今晚 11 点前睡，把「再刷一小时」改成「再睡一小时」','明天把课后题第 1 章重做一遍，只做 5 道','把竞赛报名表交了——大四的你已经替你看过结果了'],
   q:{t:'你最近的复习状态是？',o:['还没翻开书','学了一天，感觉没进脑子','在及格线边缘反复试探','其实准备得还行，就是慌'],e:['但你后来用两周把整本书过了一遍，期末考了 89 分。','但那种"没进脑子"的感觉会在期末前突然消散——你后来靠一遍遍抄写把它过完了。','但你在及格线上试探到期末，最后稳稳上岸，还多考了 10 分。','但你考前一周的从容，是你这四年最好的状态之一。']}},
  {id:'p2', no:'②', name:'敢说话', quote:{t:'一个人的成功，85% 靠的是勇气与表达',a:'戴尔·卡耐基'}, tag:'社恐专用', promise:'开口的那一刻，世界开始回应',
   anxietyPh:'比如：不敢在社团面试里说话',
   loading:['正在把你想说的话从喉咙里拽出来……','正在演练你开口后冷场三秒的场景……','正在清空你脑子里「万一说错了」的弹幕……'],
   letter:'嘿，现在的你：我知道你最近又在「{anxiety}」这件事上退了一步——就像在社团面试门外站了十分钟，最后还是转身走了。但你猜怎么着？后来你鼓起勇气又试了一次，进了宣讲团，现在站在一百多人的台上讲专业原理，手都不抖。没有人会记住你说话时的紧张，大家只会记住你说的内容。社恐不是病，是你还没找到那个让你愿意开口的话题。下次举手的时候，别想太多。你比你以为的更有意思。—— 大四的你，刚结束一场宣讲',
   keyword:['四年后：站在百人讲台上不抖'],
   actions:['下次课堂提问，抢在倒数第三个举一次手','加一个你真正感兴趣的社团，只面试一次','把你想说但没说的话，先写给一个朋友看'],
   q:{t:'课堂上你有想法时，你通常会……？',o:['等别人先说','心里演练十遍，最后放弃','说了，但声音发抖','其实常发言，只是怕被评价'],e:['但后来你在一次小组讨论里忍不住开了口，那是你第一次觉得"原来我也可以"。','但你后来在社团面试里硬着头皮说完了一整段自我介绍，从那以后，开口变简单了。','但发抖的声音遮不住内容——后来有人专门来加你微信，说你讲得清楚。','但你后来把"怕被评价"换成了"我的风格"，舞台反而越来越大。']}},
  {id:'p3', no:'③', name:'不内耗', quote:{t:'人生如逆旅，我亦是行人',a:'苏轼《临江仙·送钱穆父》'}, tag:'卷躺纠结专用', promise:'卷要卷得清醒，躺要躺得心安',
   anxietyPh:'比如：卷不动又躺不平',
   loading:['正在清点你收藏的 47 个「别人好厉害」……','正在把你和昨天的自己重新连线……','正在把「卷不动」调成「先走两圈」……'],
   letter:'嘿，现在的你：我知道你这阵子又累又不甘心，卷不动，躺不平，连「休息」都要先找个借口。我想告诉你：后来你没有变成别人眼里的那种「厉害的人」，但你把日子过明白了——大二下学期你开始每天只列三件最重要的事，做完就收工，剩下的时间去操场走了很多圈。绩点没有暴涨，但你的睡眠回来了，头发也回来了。你不是懒，你是把力气用错了地方：用来和「别人在干嘛」比较。别比了，你只需要和昨晚的自己比。—— 大四的你，刚结束一次傍晚散步',
   keyword:['四年后：睡眠回来了，头发也回来了'],
   actions:['今天只列三件最重要的事，做完就收工','晚上去操场走 20 分钟，不带手机','把「别人在干嘛」的刷新频率降到一天一次'],
   q:{t:'你内耗最多的时候是？',o:['刷到别人晒成绩和 offer','晚上躺床上复盘白天的话','忍不住对比别人的进度','计划太多，一个都没完成'],e:['但你后来把刷朋友圈的时间固定到一天一次，世界安静了很多。','但你后来养成了"今天的事，写完就放下"，失眠少了，头发也回来了。','但你后来只和自己比：今天比昨天多学一小时，就赢了。','但你后来学会了"每天只列三件"，完成比列满更重要。']}},
  {id:'p4', no:'④', name:'去爱吧', quote:{t:'于千万人之中遇见你所要遇见的人',a:'张爱玲《爱》'}, tag:'心动 / 失恋专用', promise:'有些话现在不说，四年后会后悔',
   anxietyPh:'比如：喜欢一个人不敢开口',
   loading:['正在翻看你偷偷保存的那条朋友圈……','正在计算你们在图书馆偶遇的次数……','正在把「如果当初」调成静音……'],
   letter:'嘿，现在的你：我知道你最近在为「{anxiety}」反复纠结，那条消息打了又删，删了又打。听我说——后来你们真的在一起过。就在大三的秋天，你鼓起勇气约了一次晚自习。没有小说里那么浪漫，你们只是坐在图书馆二楼，把高数题讲了三遍。后来分开了，但分开后你也没后悔过开口。因为比「在一起过」更难受的，是「我从来没说过」。你怕的不是被拒绝，是被拒绝后还要假装没发生过。可真正的遗憾只有一个：四年后你连开口的资格都没有了。去说吧，就当替四年前的我们补一枪。—— 大四的你，在毕业照里笑得最真的那个',
   keyword:['四年后：说了，不后悔'],
   actions:['这周找一个「顺路」的借口，约一次晚自习','把想说的话写在备忘录里，先念给自己听一遍','如果被拒绝了——那也是你勇敢的证据，不是失败'],
   q:{t:'你心里那个「如果当初」，是？',o:['加了联系方式，没敢聊','约过一次，被婉拒了','明明互相喜欢，却错过','还没开始，就先放弃了'],e:['但你后来在某天晚上发出了一句"今天图书馆开空调了吗"，故事就从那里开始了。','但被婉拒没有击垮你——你后来坦然地喜欢上了别人，还在一起了。','但你后来在毕业前把它说破了，对方说"我等这句话很久了"。','但放弃是最轻松的选项，你后来决定不再选它，就有了后来的人。']}},
  {id:'p5', no:'⑤', name:'和好如初', quote:{t:'径路窄处，留一步与人行',a:'洪应明《菜根谭》'}, tag:'宿舍 / 人际专用', promise:'夜聊比熬夜更治愈',
   anxietyPh:'比如：和室友关系有点僵',
   loading:['正在统计你们上一次好好聊天的时间……','正在把床帘后的心事一盏盏点亮……','正在调制「先开口」的勇气配方……'],
   letter:'嘿，现在的你：我知道你和室友的关系最近让你有点累，同一间屋子，却像隔着海峡。后来你们在毕业前夜聊到凌晨三点，把三年没说的话一次性说完了——原来那次你没去聚餐，大家以为你在生气；你深夜没睡，大家以为你不想理人。误会都是猜出来的，真相都是聊出来的。那天之后，你们成了毕业照里最舍不得的一群人。别怕先开口，宿舍这间小屋，值得一次「我先说」。—— 大四的你，刚和室友吃完散伙饭',
   keyword:['四年后：和室友成了最舍不得的人'],
   actions:['这周找一位室友，从一句「最近怎么样」开始','把一次误会当面说开，发消息不如面对面','主动发起一次宿舍夜聊，零食你出'],
   q:{t:'和室友卡住的地方，通常是？',o:['作息不同，互相迁就','一次误会，没当面说开','觉得对方不理解我','已经好久没好好聊天了'],e:['但你们后来约法三章，还一起买了个小夜灯，矛盾变成了默契。','但你们后来在一次夜聊里把误会摊开，才发现双方都憋了很久。','但你们后来在深夜聊了一次，才知道对方其实很懂你。','但你们后来在毕业前夜聊到三点，把三年的话一次说完了。']}},
  {id:'p6', no:'⑥', name:'向前走', quote:{t:'其实地上本没有路，走的人多了，也便成了路',a:'鲁迅《故乡》'}, tag:'毕业迷茫专用', promise:'毕业那天，你不慌',
   anxietyPh:'比如：不知道毕业后要干嘛',
   loading:['正在扫描你简历上的空白处……','正在把「不知道干嘛」翻译成「还没开始」……','正在为你预约一次毕业前的从容……'],
   letter:'嘿，现在的你：我知道你最近很慌，身边的人都在投简历、定方向，你连「想做什么」都说不出来。我现在可以告诉你结局：你后来没有想明白什么大道理，只是开始做小事，先写一版很烂的第一稿简历，约老师聊了二十分钟，把「想做的事」列了十七件又划掉十二件。然后你慢慢发现，路不是想出来的，是走出来的。毕业那天你没有变成人生赢家，但你拿到了 offer，心里有底。你现在不知道方向，不是你的错，是时候还没到。—— 大四的你，签完三方协议的那个下午',
   keyword:['四年后：签了三方，心里有底'],
   actions:['今天写一版很烂的第一稿简历（烂没关系）','约一位老师聊 20 分钟，只问方向','列一份「想做的事」清单，允许自己划掉'],
   q:{t:'面对未来，你目前是？',o:['完全没方向','有几个选项，拿不准','知道方向，但没底气','在按计划走，偶尔心慌'],e:['但你后来从一件小事开始：写简历、约老师、列清单，方向是走出来的。','但你后来用排除法划掉了最不想去的那条路，剩下的路就亮了。','但你后来把"没底气"换成了"先试一次"，第一次就比想象中好。','但偶尔心慌很正常——你后来学会用"已完成"清单，把慌张一点点压实。']}},
  {id:'p7', no:'⑦', name:'不将就', quote:{t:'天生我材必有用',a:'李白《将进酒》'}, tag:'方向选择专用', promise:'转专业不犹豫，选路不后悔',
   anxietyPh:'比如：想转专业又不敢',
   loading:['正在把你列了三次的转专业申请表从草稿箱里翻出来……','正在对比你偷偷看过的 37 个专业就业帖……','正在把「万一选错了呢」调成单曲循环……'],
   letter:'嘿，现在的你：我知道你最近又在翻培养方案，把「转专业申请表」存进草稿箱三次又删掉。你怕的不是麻烦，是怕选错。但我要告诉你：后来你真的转了。所有人都说你疯了，只有我知道你偷偷看了一整年的书。转专业那天你在教务处排了四十分钟队，手心的汗把表都浸湿了。可四年后你的毕业设计拿了全校优秀。你现在纠结的不是「选哪条路」，是「我有没有资格选」。你有。—— 大四的你，毕业展上被围观的作者',
   keyword:['四年后：转成功了，毕业设计全校优秀'],
   actions:['这周去学院教务处，问清楚转专业的时间线和门槛（只问，不决定）','找一位已经转成功的学长学姐，聊 20 分钟','把「万一选错了」换成「选错了我也能转回来」——你有四年'],
   q:{t:'关于现在的专业 / 方向，你的想法是？',o:['不喜欢，但不敢换','想换，怕考不上 / 失败','在犹豫要不要坚持','确定要换，就差勇气'],e:['但你后来真的换了，还为此偷偷看了一整年的书。','但你后来算过：最坏的结果也就是重来一次，而你有四年。','但坚持和将就的区别，你后来终于分清了，然后果断选了前者。','而勇气这件事，你后来在教务处排队交表的那一刻，就攒够了。']}},
  {id:'p8', no:'⑧', name:'不熬夜', quote:{t:'早睡早起，使人健康、富有、聪明',a:'本杰明·富兰克林'}, tag:'健康自律专用', promise:'早睡早起，四年不掉队',
   anxietyPh:'比如：天天熬夜戒不掉',
   loading:['正在统计你这周的第 14 次凌晨两点……','正在检测你的发际线海拔……','正在把明天的「一定早睡」提前到今天……'],
   letter:'嘿，现在的你：我知道你又熬夜了。不是不想睡，是只有深夜那两小时，才感觉时间是自己的。我太懂了，因为大二那年的我，也是这样。后来你猜怎么着？大三体测你跑完八百米在操场边上坐了十分钟，才第一次认真看夕阳。那学期你开始 11:40 上床，一开始睡不着，就听播客，慢慢就睡着了。四年后你最大的成就不是绩点，是每天七点半自然醒，赶在食堂豆浆卖完前到。别把身体当电池，你的四年，值得被清醒地过完。—— 大四的你，晨跑回来的路上',
   keyword:['四年后：七点半自然醒，从不脱发'],
   actions:['今晚比昨天早睡 20 分钟（就 20 分钟）','把手机充电器放到床以外的地方','明天给自己安排 20 分钟的运动——不需要坚持，先试一次'],
   q:{t:'你熬夜，最常因为？',o:['作业 / 复习没做完','刷手机，停不下来','心里有事，睡不着','白天太忙，只有深夜属于自己'],e:['但你后来学会了"先睡，明早起来再做"，效率反而更高了。','但你后来把充电器放到床外，用两本书代替了短视频。','但你后来把心事写进日记再上床，睡眠就慢慢回来了。','但你后来在 11:40 上床听播客，才发现深夜的另一种用法。']}},
];

const MIX_STEPS = ['武火熬煮','萃取焦虑','封装未来'];
const CLERK = {
  open:'欢迎光临后悔药便利店，今天想治哪一种不甘心？',
  paper:'配方师说：你的心事正在药釜里慢慢熬煮，请稍等三分钟。',
  night:'深夜场营业中，夜风免费，心事打折。',
  bye:'药不能停，但你可以先好好睡一觉。明天再来，我等你。'
};

/* ===== 状态 ===== */
let state = {screen:'open', pill:null, version:'normal', grade:'大二', major:'', gender:'保密', goal:'', nick:'', detail:'', stateInfo:'', mood:'', qIndex:null, anxiety:'', collected:[]};
let twTimer = null, mixTimer = null;
const $ = id => document.getElementById(id);
const screens = ['open','pick','input','mix','result'];

/* ===== 工具 ===== */
function showScreen(name){
  screens.forEach(s => $(`screen-${s}`).classList.toggle('active', s===name));
  state.screen = name;
  window.scrollTo({top:0, behavior:'smooth'});
}
function toast(msg){
  const t = $('toast'); t.textContent = msg; t.classList.add('show');
  clearTimeout(t._t); t._t = setTimeout(()=>t.classList.remove('show'), 2600);
}
function esc(s){ return (s||'').replace(/[&<>"]/g, c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }
function fill(text, d){
  return text.replace('{anxiety}', d.anxiety || '那件让你睡不着的事')
             .replace('{grade}', d.grade || '大二')
             .replace('{major}', d.major || '大学');
}
function buildLetter(p, s){
  let t = fill(p.letter, s);
  t = t.replace('嘿，现在的你', '嘿，' + (s.nick || '现在的你'));
  if(s.version==='pro' && s.answer && p.q){
    const qi = p.q.o.indexOf(s.answer);
    const echo = qi>=0 ? p.q.e[qi] : '那件事，后来有了个不错的答案。';
    t = t.replace('—— 大四的你', '对了，配药的时候你告诉我：「' + s.answer + '」。你当时没多想，后来回头看，那正是故事的转折点。' + echo + '\n\n—— 大四的你');
  }
  if(s.version==='pro' && s.detail) t = t.replace('—— 大四的你', '还有件小事，你当时觉得可惜——「' + s.detail + '」。四年后的我可以告诉你：那件事后来有了个意外的结果，你从里面拿到了比结果更珍贵的东西。\n\n—— 大四的你');
  if(s.goal) t = t.replace('—— 大四的你', '还有你写在方子上的那个目标——「' + s.goal + '」。四年后的我可以告诉你：你真的做到了。\n\n—— 大四的你');
  if(s.goal && p.id==='p6'){
    t = t.replace('你连「想做什么」都说不出来', '你心里其实有个方向——「' + s.goal + '」，只是还不敢说出口');
  }
  if(s.goal && /考研|读研|研究生|上岸|保研/.test(s.goal)){
    t = t.replace('刚拿到 offer 的那个晚上', '收到录取通知的那个晚上');
    t = t.replace('进了心仪的公司', '考上了心仪的学校');
    t = t.replace('都在变成你简历上的一行字', '都在变成你成绩单上的一行字');
    t = t.replace('但你拿到了 offer，心里有底', '但你收到了那所学校的录取通知，心里有底');
    t = t.replace('签完三方协议的那个下午', '在收到拟录取通知的那个下午');
  } else if(s.goal && /考公|公务员|编制/.test(s.goal)){
    t = t.replace('刚拿到 offer 的那个晚上', '收到录用通知的那个晚上');
    t = t.replace('进了心仪的公司', '考上了心仪的岗位');
    t = t.replace('都在变成你简历上的一行字', '都在变成你成绩单上的一行字');
    t = t.replace('但你拿到了 offer，心里有底', '但你通过了笔试和面试，心里有底');
    t = t.replace('签完三方协议的那个下午', '在公示名单上看到自己名字的那个下午');
  }
  return t;
}

/* ===== 开场 ===== */
$('enterBtn').addEventListener('click', ()=>{
  showScreen('pick');
  toast('店长：' + CLERK.open);
});

/* ===== 选药 ===== */
const imgMap = {};
function bindPills(){
  $('pillGrid').querySelectorAll('.pill-card').forEach(card=>{
    const p = PILLS.find(x=>x.id===card.dataset.id);
    if(!p) return;
    imgMap[p.id] = card.querySelector('img').src;
    card.querySelector('.pname').textContent = '「' + p.name + '」后悔药';
    card.querySelector('.ptag').textContent = p.tag;
    card.querySelector('.ppromise').textContent = p.promise;
    const act = ()=>choose(p.id);
    card.addEventListener('click', act);
    card.addEventListener('keydown', e=>{ if(e.key==='Enter'||e.key===' '){e.preventDefault();act();} });
  });
}
function choose(id){
  state.pill = PILLS.find(p=>p.id===id);
  $('inputTitle').textContent = `「${state.pill.name}」· 来，把方子告诉我`;
  $('inputSub').textContent = `配药前，选一个配方：速配，或深度定制`;
  $('anxietyLabel').textContent = `最近最让你焦虑的一件事（${state.pill.name}相关）`;
  $('anxietyInput').placeholder = state.pill.anxietyPh;
  resetVersion();
  resetForm();
  renderQ();
  $('gradeSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.grade===state.grade));
  $('genderSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.gender===state.gender));
  showScreen('input');
}
function resetForm(){
  state.qIndex = null;
  state.stateInfo = '';
  state.mood = '';
  state.answer = '';
  ['majorInput','anxietyInput','goalInput','nickInput','detailInput'].forEach(id=>{ $(id).value=''; });
  $('stateSeg').querySelectorAll('button').forEach(b=>b.classList.remove('sel'));
  $('moodSeg').querySelectorAll('button').forEach(b=>b.classList.remove('sel'));
}
function resetVersion(){
  state.version = 'normal';
  $('verSeg').querySelectorAll('.ver-btn').forEach(b=>b.classList.toggle('sel', b.dataset.ver==='normal'));
  $('proFields').style.display = 'none';
  $('mixBtnLabel').textContent = '开始配药';
}

/* ===== 输入 ===== */
$('gradeSeg').addEventListener('click', e=>{
  const b = e.target.closest('button'); if(!b) return;
  state.grade = b.dataset.grade;
  $('gradeSeg').querySelectorAll('button').forEach(x=>x.classList.toggle('sel', x===b));
});
$('verSeg').addEventListener('click', e=>{
  const b = e.target.closest('.ver-btn'); if(!b) return;
  state.version = b.dataset.ver;
  $('verSeg').querySelectorAll('.ver-btn').forEach(x=>x.classList.toggle('sel', x===b));
  $('proFields').style.display = state.version==='pro' ? 'block' : 'none';
  $('mixBtnLabel').textContent = state.version==='pro' ? '开始深度配药' : '开始配药';
  if(state.version==='pro') toast('进阶定制：多填两项，信件会更懂你');
});
$('genderSeg').addEventListener('click', e=>{
  const b = e.target.closest('button'); if(!b) return;
  state.gender = b.dataset.gender;
  $('genderSeg').querySelectorAll('button').forEach(x=>x.classList.toggle('sel', x===b));
});
$('stateSeg').addEventListener('click', e=>{
  const b = e.target.closest('button'); if(!b) return;
  state.stateInfo = b.dataset.state;
  $('stateSeg').querySelectorAll('button').forEach(x=>x.classList.toggle('sel', x===b));
});
$('moodSeg').addEventListener('click', e=>{
  const b = e.target.closest('button'); if(!b) return;
  state.mood = b.dataset.mood;
  $('moodSeg').querySelectorAll('button').forEach(x=>x.classList.toggle('sel', x===b));
});
$('qSeg').addEventListener('click', e=>{
  const b = e.target.closest('button'); if(!b) return;
  state.qIndex = Number(b.dataset.q);
  $('qSeg').querySelectorAll('button').forEach(x=>x.classList.toggle('sel', x===b));
});
function renderQ(){
  const p = state.pill;
  if(!p || !p.q) return;
  $('qLabel').textContent = p.q.t;
  $('qSeg').innerHTML = p.q.o.map((o,i)=>`<button data-q="${i}">${o}</button>`).join('');
  $('qSeg').querySelectorAll('button').forEach(b=>b.classList.toggle('sel', b.dataset.q===String(state.qIndex)));
}
$('backToPick').addEventListener('click', ()=>showScreen('pick'));
$('startMix').addEventListener('click', ()=>{
  state.major = $('majorInput').value.trim();
  state.anxiety = $('anxietyInput').value.trim();
  state.goal = $('goalInput').value.trim();
  state.nick = $('nickInput').value.trim();
  state.detail = $('detailInput').value.trim();
  state.answer = (state.qIndex!=null && state.pill.q) ? state.pill.q.o[state.qIndex] : '';
  if(!state.pill){ toast('请先选一瓶药'); showScreen('pick'); return; }
  if(state.version==='pro' && state.qIndex==null){ toast('进阶定制：请先回答这瓶药的专属问题'); return; }
  $('mixNote').textContent = state.pill.id==='p8' ? CLERK.night + ' ' + CLERK.paper : CLERK.paper;
  showScreen('mix');
  runMix();
});

/* ===== 配药动画 ===== */
function runMix(){
  let i = 0;
  $('mixQuote').innerHTML = '“' + state.pill.quote.t + '”<b>—— ' + state.pill.quote.a + '</b>';
  $('mixStep').textContent = MIX_STEPS[0];
  $('mixLine').textContent = state.pill.loading[0];
  clearInterval(mixTimer);
  mixTimer = setInterval(()=>{
    i++;
    if(i < 3){
      $('mixStep').textContent = MIX_STEPS[i];
      $('mixLine').textContent = state.pill.loading[i];
    } else {
      clearInterval(mixTimer);
      setTimeout(showResult, 650);
    }
  }, 1600);
}

function goalKw(p, s){
  if(s.goal && /考研|读研|研究生|上岸|保研/.test(s.goal)){
    if(p.keyword[0].includes('进了心仪的公司')) return '四年后：考上了心仪的学校';
    if(p.keyword[0].includes('签了三方')) return '四年后：收到录取通知，心里有底';
  }
  if(s.goal && /考公|公务员|编制/.test(s.goal)){
    if(p.keyword[0].includes('进了心仪的公司')) return '四年后：考上了心仪的岗位';
    if(p.keyword[0].includes('签了三方')) return '四年后：通过考试，心里有底';
  }
  return p.keyword[0];
}
function kvTags(p, s){
  const kv = [];
  kv.push(`<span class="kv"><b>${esc(s.major||'大学')}</b></span>`);
  kv.push(`<span class="kv"><b>${esc(s.grade||'大二')}</b></span>`);
  kv.push(`<span class="kv"><b>${esc(s.gender||'保密')}</b></span>`);
  if(s.goal) kv.push(`<span class="kv">期望：${esc(s.goal)}</span>`);
  if(s.version==='pro'){
    if(s.stateInfo) kv.push(`<span class="kv">状态：${esc(s.stateInfo)}</span>`);
    if(s.mood) kv.push(`<span class="kv">心情：${esc(s.mood)}</span>`);
  }
  if(s.version==='pro' && s.nick) kv.push(`<span class="kv">致：${esc(s.nick)}</span>`);
  kv.push(`<span class="kv">正在：${esc(s.anxiety||'为一点小事烦恼')}</span>`);
  kv.push(`<span class="kv">${goalKw(p, s)}</span>`);
  return kv.join('');
}

/* ===== 成品 ===== */
function showResult(){
  const p = state.pill;
  $('resultImg').src = imgMap[p.id];
  $('resultTag').textContent = '后悔药已配好 · ' + p.no;
  $('resultTitle').textContent = `「${p.name}」后悔药`;
  const letter = buildLetter(p, state);
  $('letterText').textContent = '';
  typeLetter(letter);
  $('kcardBody').innerHTML = kvTags(p, state);
  $('actList').innerHTML = p.actions.map((a,i)=>`
    <li data-i="${i}"><span class="tick"></span><span>${a}</span></li>`).join('');
  $('actList').querySelectorAll('li').forEach(li=>{
    li.addEventListener('click', ()=>li.classList.toggle('done'));
  });
  $('collectBtn').textContent = state.collected.includes(p.id) ? '再记一次' : '收进药盒';
  $('voiceStop').style.display = 'none';
  stopVoice();
  showScreen('result');
  toast('店长：' + CLERK.bye);
}
function typeLetter(text){
  clearInterval(twTimer);
  let i = 0;
  twTimer = setInterval(()=>{
    i += 2;
    $('letterText').textContent = text.slice(0, i);
    if(i >= text.length){ clearInterval(twTimer); $('caret').style.display='none'; }
  }, 16);
}

/* ===== 语音朗读 ===== */
let voiceOn = false;
function pickVoice(g){
  if(!('speechSynthesis' in window)) return null;
  const voices = speechSynthesis.getVoices();
  const zh = voices.filter(v=>v.lang && v.lang.toLowerCase().startsWith('zh'));
  if(!zh.length) return null;
  if(g==='男生') return zh.find(v=>/男|male|yunjian|tingting/i.test(v.name)) || zh[0];
  return zh.find(v=>/女|female|xiaoxiao|huihui|meijia/i.test(v.name)) || zh[0];
}
function speakLetter(){
  if(!('speechSynthesis' in window)){ toast('当前浏览器不支持语音朗读'); return; }
  const text = buildLetter(state.pill, state);
  const u = new SpeechSynthesisUtterance(text);
  const v = pickVoice(state.gender);
  if(v) u.voice = v;
  u.lang = 'zh-CN'; u.rate = 0.92; u.pitch = 1.02;
  speechSynthesis.cancel();
  speechSynthesis.speak(u);
  voiceOn = true;
  $('voiceLabel').textContent = '朗读中……';
  $('voiceBtn').classList.add('playing');
  $('voiceStop').style.display = '';
  u.onend = ()=>{ voiceOn=false; $('voiceLabel').textContent='听「大四的你」读这封信'; $('voiceBtn').classList.remove('playing'); $('voiceStop').style.display='none'; };
}
function stopVoice(){
  if('speechSynthesis' in window) speechSynthesis.cancel();
  voiceOn = false;
  $('voiceLabel').textContent = '听「大四的你」读这封信';
  $('voiceBtn').classList.remove('playing');
  $('voiceStop').style.display = 'none';
}
$('voiceBtn').addEventListener('click', speakLetter);
$('voiceStop').addEventListener('click', stopVoice);
if('speechSynthesis' in window) speechSynthesis.onvoiceschanged = ()=>pickVoice();

/* ===== 药盒 ===== */
function loadBox(){
  try{ state.collected = JSON.parse(localStorage.getItem('pillBox')||'[]'); }catch(e){ state.collected = []; }
  $('boxCount').textContent = `药盒 ${state.collected.length}/8`;
}
function saveBox(){
  localStorage.setItem('pillBox', JSON.stringify(state.collected));
  $('boxCount').textContent = `药盒 ${state.collected.length}/8`;
}
$('collectBtn').addEventListener('click', ()=>{
  const id = state.pill.id;
  if(state.collected.includes(id)){
    saveRecord();
    toast(`已追加「${state.pill.name}」的药方记录`);
    return;
  }
  state.collected.push(id); saveBox();
  saveRecord();
  toast(`「${state.pill.name}」已收进药盒（${state.collected.length}/8）`);
  $('collectBtn').textContent = '再记一次';
  if(state.collected.length===8){
    toast('8 瓶集齐！你的「大学结业证书」已解锁');
    openBox();
  }
});
function nowStr(){
  const d = new Date();
  const p = n => String(n).padStart(2,'0');
  return `${d.getMonth()+1}-${p(d.getDate())} ${p(d.getHours())}:${p(d.getMinutes())}`;
}
function getRecords(){
  try{ return JSON.parse(localStorage.getItem('pillRecords')||'[]'); }catch(e){ return []; }
}
function saveRecord(){
  const rec = {
    pillId: state.pill.id, version: state.version, grade: state.grade,
    major: state.major, gender: state.gender, goal: state.goal,
    nick: state.nick, detail: state.detail, stateInfo: state.stateInfo,
    mood: state.mood, qIndex: state.qIndex, anxiety: state.anxiety,
    time: nowStr(),
    done: Array.from(document.querySelectorAll('#actList li')).map(li=>li.classList.contains('done'))
  };
  let recs = getRecords();
  recs.unshift(rec);
  const per = {};
  recs = recs.filter(r=>{ per[r.pillId]=(per[r.pillId]||0)+1; return per[r.pillId]<=5; });
  localStorage.setItem('pillRecords', JSON.stringify(recs));
}
function renderRecCard(pill, r, idx){
  const s = Object.assign({}, r, {answer:(r.qIndex!=null && pill.q) ? pill.q.o[r.qIndex] : ''});
  const letter = buildLetter(pill, s);
  const acts = (pill.actions||[]).map((a,i)=>{
    const d = r.done && r.done[i];
    return `<li data-i="${i}" class="${d?'done':''}"><span class="tick"></span><span>${a}</span></li>`;
  }).join('');
  return `<div class="rec-card" data-idx="${idx}">
    <div class="rec-head">${esc(r.time)} · ${r.version==='pro'?'进阶定制':'普通配方'} · ${esc(r.grade||'')}${esc(r.major?(' · '+r.major):'')}</div>
    <div class="rec-letter">${esc(letter)}</div>
    <div class="rec-kv">${kvTags(pill, s)}</div>
    <div class="rec-acts">
      <div class="ra-head">四年必做清单</div>
      <ul>${acts}</ul>
    </div>
  </div>`;
}
function openHistory(pid){
  const pill = PILLS.find(p=>p.id===pid);
  if(!pill) return;
  const recs = getRecords().filter(r=>r.pillId===pid);
  $('histTitle').textContent = `「${pill.name}」药方历史`;
  $('histSub').textContent = recs.length ? `共 ${recs.length} 次记录 · 按时间倒序` : '还没有药方记录';
  $('histList').innerHTML = recs.length
    ? recs.map((r,idx)=>renderRecCard(pill, r, idx)).join('')
    : '<div class="hist-empty">这瓶药还没有留下药方记录。<br>去配一瓶并点「收进药盒」，就会出现在这里。</div>';
  $('histList').querySelectorAll('.rec-card').forEach(card=>{
    const idx = Number(card.dataset.idx);
    card.querySelectorAll('.rec-acts li').forEach(li=>{
      li.addEventListener('click', ()=>{
        li.classList.toggle('done');
        const done = Array.from(card.querySelectorAll('.rec-acts li')).map(x=>x.classList.contains('done'));
        updateRecordDone(pid, idx, done);
      });
    });
  });
  $('historyModal').classList.add('show');
}
function updateRecordDone(pid, idx, done){
  const recs = getRecords();
  let target = -1, seen = 0;
  for(let i=0;i<recs.length;i++){
    if(recs[i].pillId===pid){
      if(seen===idx){ target=i; break; }
      seen++;
    }
  }
  if(target>=0){
    recs[target].done = done;
    localStorage.setItem('pillRecords', JSON.stringify(recs));
  }
}
$('histClose').addEventListener('click', ()=>$('historyModal').classList.remove('show'));
$('historyModal').addEventListener('click', e=>{ if(e.target===$('historyModal')) $('historyModal').classList.remove('show'); });
function openBox(){
  $('boxGrid').innerHTML = PILLS.map(p=>{
    const got = state.collected.includes(p.id);
    if(got){
      return `<button class="box-slot got" data-id="${p.id}" aria-label="查看${p.name}药方历史"><span class="bn">${p.no}</span><span>${p.name}</span><span class="bsub">点按看记录</span></button>`;
    }
    return `<div class="box-slot"><span class="bn">?</span><span>未集齐</span></div>`;
  }).join('');
  $('boxGrid').querySelectorAll('.box-slot.got').forEach(btn=>{
    btn.addEventListener('click', ()=>openHistory(btn.dataset.id));
  });
  const done = state.collected.length===8;
  $('certBox').style.display = done ? 'block' : 'none';
  if(done){
    $('certName').innerHTML = `恭喜你，8 瓶后悔药全部集齐。<br>你把四年里每一个「如果当初」都收好了，<br>接下来的路，好好走。`;
  }
  $('boxModal').classList.add('show');
}
$('boxBtn').addEventListener('click', openBox);
$('boxClose').addEventListener('click', ()=>$('boxModal').classList.remove('show'));
$('boxModal').addEventListener('click', e=>{ if(e.target===$('boxModal')) $('boxModal').classList.remove('show'); });

/* ===== 分享 ===== */
function legacyCopy(t){
  try{
    const ta = document.createElement('textarea');
    ta.value = t;
    ta.style.position='fixed'; ta.style.opacity='0';
    document.body.appendChild(ta);
    ta.select();
    const ok = document.execCommand('copy');
    document.body.removeChild(ta);
    return ok;
  }catch(e){ return false; }
}
function copyText(t){
  if(navigator.clipboard && navigator.clipboard.writeText){
    return navigator.clipboard.writeText(t).then(()=>true).catch(()=>legacyCopy(t));
  }
  return Promise.resolve(legacyCopy(t));
}
function buildShareText(p){
  return `我在「大学后悔药便利店」配了一瓶「${p.name}」后悔药\n${state.grade||''} ${state.major||'大学'} | ${state.anxiety||'正在烦恼'} | ${goalKw(p, state)}\n—— 不是工具，是情绪出口。`;
}
$('shareBtn').addEventListener('click', ()=>{
  const p = state.pill;
  $('shareTitle').textContent = `「${p.name}」后悔药`;
  $('shareKv').innerHTML = kvTags(p, state);
  $('shareText').textContent = buildShareText(p);
  $('shareModal').classList.add('show');
});
$('shareCopy').addEventListener('click', async ()=>{
  const ok = await copyText(buildShareText(state.pill) + '\n' + location.href);
  toast(ok ? '已复制，去微信粘贴就能打开' : '复制失败，可以长按链接手动复制');
});
$('shareClose').addEventListener('click', ()=>$('shareModal').classList.remove('show'));
$('shareModal').addEventListener('click', e=>{ if(e.target===$('shareModal')) $('shareModal').classList.remove('show'); });

/* ===== 再来一瓶 / 重开 ===== */
$('againBtn').addEventListener('click', ()=>{ stopVoice(); showScreen('pick'); });

/* ===== 深夜模式 ===== */
function nightNow(){
  const h = new Date().getHours();
  return h>=22 || h<6;
}
function applyNight(on){
  document.body.classList.toggle('night', on);
  $('nightToggle').classList.toggle('on', on);
  $('nightLabel').textContent = on ? '深夜场·已开' : '深夜场';
}
let nightManual = null;
try{ nightManual = localStorage.getItem('nightManual'); }catch(e){}
applyNight(nightManual ? nightManual==='1' : nightNow());
$('nightToggle').addEventListener('click', ()=>{
  const on = !document.body.classList.contains('night');
  applyNight(on);
  nightManual = on?'1':'0';
  try{ localStorage.setItem('nightManual', nightManual); }catch(e){}
  toast(on ? '深夜场已开：夜风免费，心事打折。夜深了，早点休息' : '已切回日间场');
});
$('nightRemind').addEventListener('click', ()=>$('nightRemind').style.display='none');

/* ===== 初始化 ===== */
loadBox();
bindPills();
if('speechSynthesis' in window){ speechSynthesis.getVoices(); }

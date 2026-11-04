# -*- coding: utf-8 -*-
import io

p = r'C:\Users\37800\Doubao\chats\2026-09-12\new-chat\regret-store\index.html'
s = io.open(p, encoding='utf-8').read()

# 1) HTML：顶栏公告按钮（插在 top-actions 起始处）
old = """  <div class="top-actions">
    <button class="rank-badge" id="rankBadge" title="我的等级" style="display:none">"""
new = """  <div class="top-actions">
    <button class="top-btn" id="noticeBtn" title="进店公告">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11v2a1 1 0 0 0 1 1h2l4 5V5L6 10H4a1 1 0 0 0-1 1z"/><path d="M15 8a5 5 0 0 1 0 8"/><path d="M18 5a9 9 0 0 1 0 14"/></svg>
      <span>公告</span>
    </button>
    <button class="rank-badge" id="rankBadge" title="我的等级" style="display:none">"""
assert s.count(old) == 1, 'top actions'
s = s.replace(old, new)

# 2) HTML：公告弹窗 + 升级弹窗（插在 <!-- ===== 分享弹窗 ===== --> 之前）
modals = """<!-- ===== 公告弹窗 ===== -->
<div class="modal-mask" id="noticeModal">
  <div class="modal notice-modal">
    <h3>进店公告</h3>
    <div class="notice-body">
      <div class="notice-sec">
        <b>欢迎光临，<span id="noticeUser">同学</span></b>
        <p id="noticeRankLine">你目前是：黑铁 1 级</p>
      </div>
      <div class="notice-sec">
        <b>等级规则</b>
        <p>黑铁 → 青铜 → 白银 → 黄金，各 3 级。完成一次普通药盒升 1 级，完成一次进阶药盒升 2 级。</p>
      </div>
      <div class="notice-sec">
        <b>集齐奖励</b>
        <p>集齐 8 瓶后悔药，直升「钻石 1 级」，并解锁你的「大学结业证书」；若 8 瓶全部以进阶定制完成，直升「荣耀 1 级」。之后每瓶药每多完成 1 次，再升 1 级，没有上限。</p>
      </div>
      <div class="notice-sec warn">
        <b>重要提示</b>
        <p>配完药后，<u>只有点击「收进药盒」按钮</u>，这瓶药才会被收入药盒、计入完成记录并升级哦。</p>
      </div>
    </div>
    <button class="btn-main" id="noticeClose">知道了，进店</button>
  </div>
</div>

<!-- ===== 升级弹窗 ===== -->
<div class="modal-mask" id="rankupModal">
  <div class="modal rankup-modal">
    <div class="rankup-star">
      <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l2.9 5.9 6.6.9-4.8 4.6 1.2 6.5L12 17.3 6.1 19.9l1.2-6.5L2.5 8.8l6.6-.9z"/></svg>
    </div>
    <h3>恭喜升级</h3>
    <div class="rank-chip big" id="rankupChip">黑铁 2 级</div>
    <p class="rankup-note" id="rankupNote"></p>
    <button class="btn-main" id="rankupClose">继续进店</button>
  </div>
</div>

<!-- ===== 分享弹窗 ===== -->"""
old = "<!-- ===== 分享弹窗 ===== -->"
assert s.count(old) == 1, 'share modal anchor'
s = s.replace(old, modals)

io.open(p, 'w', encoding='utf-8').write(s)
print('notice html ok')

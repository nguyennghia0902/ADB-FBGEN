"""
styles_feedback.py
──────────────────
Tất cả CSS và các đoạn HTML tĩnh dùng trong 2_sinh_feedback.py.
Import và gọi từng hàm tương ứng trong file logic chính.
"""
import streamlit as st


# ─────────────────────────────────────────────────────────────────────────────
# BASE CSS
# ─────────────────────────────────────────────────────────────────────────────
def inject_base_css() -> None:
    """Inject toàn bộ CSS giao diện dark-theme cho trang Sinh Feedback."""
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Inter', sans-serif;
    background: #0f1117;
    color: #e2e8f0;
}
/* ── Hero ── */
.hero-wrap {
    background: linear-gradient(135deg, #0f1117 0%, #1a1510 50%, #0d1a1f 100%);
    border: 1px solid #2d3748; border-radius: 16px;
    padding: 36px 40px 32px; margin-bottom: 28px;
    position: relative; overflow: hidden;
}
.hero-wrap::before {
    content:""; position:absolute; inset:0;
    background: radial-gradient(ellipse at 70% 35%, rgba(184,115,51,.10) 0%, transparent 60%);
    pointer-events:none;
}
.hero-badge {
    display:inline-block;
    background:rgba(184,115,51,.13); border:1px solid rgba(184,115,51,.38);
    color:#b87333; font-size:0.72rem; font-weight:600;
    letter-spacing:.08em; text-transform:uppercase;
    padding:4px 12px; border-radius:99px; margin-bottom:16px;
}
.hero-title {
    font-size:clamp(1.4rem,2.5vw,1.9rem);
    font-weight:700; color:#f1f5f9; line-height:1.25; margin-bottom:10px;
}
.hero-title span { color:#b87333; }
.hero-sub { font-size:0.9rem; color:#64748b; line-height:1.65; max-width:620px; }
.hero-meta-row { display:flex; flex-wrap:wrap; gap:10px; margin-top:20px; }
.hero-meta {
    background:rgba(255,255,255,.04); border:1px solid #2d3748;
    border-radius:8px; padding:6px 13px;
    font-size:0.79rem; color:#94a3b8;
    display:flex; align-items:center; gap:6px;
}
/* ── Section heading ── */
.sec-heading {
    font-size:0.72rem; font-weight:600;
    text-transform:uppercase; letter-spacing:.1em;
    color:#b87333; margin-bottom:14px; margin-top:6px;
    display:flex; align-items:center; gap:8px;
}
.sec-heading::after { content:""; flex:1; height:1px; background:#1e2535; }
/* ── Textarea override ── */
[data-testid="stTextArea"] textarea {
    background:#0f1117 !important; border:1px solid #2d3748 !important;
    border-radius:8px !important; color:#e2e8f0 !important;
    font-family:'Inter', sans-serif !important; font-size:0.87rem !important;
    resize:vertical;
}
[data-testid="stTextArea"] textarea:focus {
    border-color:#8b4513 !important;
    box-shadow:0 0 0 2px rgba(139,69,19,.20) !important;
}
[data-testid="stTextArea"] label {
    font-size:0.82rem !important; font-weight:600 !important; color:#94a3b8 !important;
}
/* ── Primary button ── */
[data-testid="stButton"] > button[kind="primary"] {
    background: linear-gradient(135deg, #8b4513 0%, #5c2e0e 100%) !important;
    border: none !important; border-radius: 8px !important;
    color: #fff !important; font-weight: 600 !important;
    font-size: 0.88rem !important; padding: 10px 20px !important;
    transition: opacity .18s ease, transform .15s ease !important;
}
[data-testid="stButton"] > button[kind="primary"]:hover {
    opacity: .88 !important; transform: translateY(-1px) !important;
}
/* ── Router badge ── */
.router-wrap {
    background:#0f1117; border:1px solid #1e2535;
    border-left:3px solid #b87333; border-radius:8px;
    padding:12px 16px; margin-bottom:16px;
    font-size:0.82rem; color:#94a3b8;
    display:flex; align-items:center; gap:10px;
}
.router-wrap .r-icon { font-size:1.1rem; }
.router-tag {
    display:inline-block;
    background:rgba(184,115,51,.12); border:1px solid rgba(184,115,51,.3);
    color:#b87333; font-size:0.68rem; font-weight:600;
    padding:2px 9px; border-radius:99px;
}
/* ── Label badge ── */
.label-badge {
    border-radius:10px; padding:14px 18px; margin-bottom:16px;
    display:flex; align-items:center; justify-content:space-between;
}
.label-name { font-size:1.45rem; font-weight:700; display:flex; align-items:center; gap:10px; }
.label-conf { font-size:0.83rem; font-weight:500; opacity:.85; }
/* ── Prob bar ── */
.prob-row { display:flex; align-items:center; gap:10px; margin-bottom:6px; }
.prob-lbl { width:86px; font-size:0.78rem; font-weight:600; flex-shrink:0; }
.prob-track { flex:1; background:#1e2535; border-radius:6px; height:12px; overflow:hidden; }
.prob-fill { height:100%; border-radius:6px; }
.prob-val {
    width:44px; text-align:right;
    font-size:0.78rem; color:#64748b;
    font-family:'JetBrains Mono', monospace;
}
/* ── Feedback box ── */
.feedback-box {
    background:#0a0d14; border:1px solid #1e2535;
    border-left:3px solid #b87333; border-radius:8px;
    padding:16px 18px; font-size:0.87rem; color:#cbd5e1;
    line-height:1.7; margin-top:4px;
}
/* ── PRA box ── */
.pra-box {
    background:#0f1117; border:1px solid #2d3748;
    border-left:3px solid #6ee7b7; border-radius:8px;
    padding:12px 16px; font-size:0.83rem; color:#94a3b8;
    line-height:1.65; margin-bottom:14px;
}
.pra-label {
    font-size:0.70rem; font-weight:600;
    text-transform:uppercase; letter-spacing:.07em;
    color:#6ee7b7; margin-bottom:6px;
}
/* ── JSON block ── */
.json-block {
    background:#0a0d14; border:1px solid #1e2535; border-radius:8px;
    padding:14px 16px; font-family:'JetBrains Mono', monospace;
    font-size:0.76rem; color:#64748b;
    line-height:1.65; white-space:pre-wrap; overflow-x:auto;
}
/* ── Pipeline info row ── */
.pipe-row { display:flex; flex-wrap:wrap; gap:8px; margin-bottom:20px; }
.pipe-step {
    background:#161b27; border:1px solid #2d3748;
    border-radius:8px; padding:8px 14px;
    font-size:0.78rem; color:#94a3b8;
    display:flex; align-items:center; gap:7px;
}
.pipe-step .dot { width:7px; height:7px; border-radius:50%; flex-shrink:0; }
.dot-brown  { background:#b87333; box-shadow:0 0 5px #b87333; }
.dot-green  { background:#6ee7b7; box-shadow:0 0 5px #6ee7b7; }
.dot-blue   { background:#60a5fa; box-shadow:0 0 5px #60a5fa; }
/* ── Empty state ── */
.empty-state { text-align:center; padding:48px 20px; color:#4b5563; }
.empty-state .es-icon { font-size:2.5rem; margin-bottom:12px; }
.empty-state p { font-size:0.85rem; color:#374151; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# COMPONENT RENDERERS
# ─────────────────────────────────────────────────────────────────────────────
def render_hero() -> None:
    st.markdown("""
<div class="hero-wrap">
  <div class="hero-badge">🎯 Auto Grading &amp; Feedback Generation</div>
  <div class="hero-title">
    CHẤM ĐIỂM VÀ SINH PHẢN HỒI<br>
    CÂU TRẢ LỜI <span>TỰ LUẬN</span> TỰ ĐỘNG
  </div>
  <div class="hero-sub">
    Nhập câu hỏi và câu trả lời của sinh viên. Hệ thống phân loại độ chính xác
    bằng <strong style="color:#a78bfa">DeBERTa-v3</strong> và sinh nhận xét
    bằng <strong style="color:#a78bfa">Flan-T5</strong>. Nếu không có đáp án tham chiếu,
    <strong style="color:#6ee7b7">Groq LLM</strong> sẽ tự động sinh đáp án gợi ý.
  </div>
  <div class="hero-meta-row">
    <div class="hero-meta"><span>🎯</span> DeBERTa-v3-base · F1=78.98%</div>
    <div class="hero-meta"><span>💬</span> Flan-T5-base · ROUGE-L=52.64</div>
    <div class="hero-meta"><span>🤖</span> Groq LLM · Zero-shot PRA</div>
    <div class="hero-meta"><span>🤗</span> HuggingFace Hub</div>
  </div>
</div>
""", unsafe_allow_html=True)


def render_pipeline_steps() -> None:
    st.markdown("""
<style>
.pipeline-wrapper {
    display: flex;
    align-items: flex-start;
    justify-content: center;
    gap: 0;
    margin: 1.5rem 0 2rem 0;
    padding: 1.2rem 2rem;
    min-width: 900px; 
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    overflow-x: auto;
}

.pipe-node {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    flex: 1;
    min-width: 160px;
    max-width: 200px;
    position: relative;
    z-index: 1;
}

/* Đường kết nối ngang giữa các node */
.pipe-node:not(:last-child)::after {
    content: '';
    position: absolute;
    top: 22px;
    left: calc(50% + 22px);
    width: calc(100% - 22px);
    height: 2px;
    background: linear-gradient(90deg, rgba(99,102,241,0.5), rgba(99,102,241,0.1));
    z-index: 0;
}

.pipe-icon-wrap {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    flex-shrink: 0;
    position: relative;
    z-index: 2;
    box-shadow: 0 0 0 4px rgba(0,0,0,0.2);
}

/* Màu riêng cho từng bước */
.pipe-icon-wrap.c-blue   { background: linear-gradient(135deg,#3b82f6,#6366f1); }
.pipe-icon-wrap.c-violet { background: linear-gradient(135deg,#8b5cf6,#a78bfa); }
.pipe-icon-wrap.c-orange { background: linear-gradient(135deg,#f59e0b,#f97316); }
.pipe-icon-wrap.c-teal   { background: linear-gradient(135deg,#14b8a6,#06b6d4); }
.pipe-icon-wrap.c-green  { background: linear-gradient(135deg,#10b981,#22c55e); }

.pipe-label {
    font-size: 0.70rem;
    font-weight: 600;
    color: rgba(255,255,255,0.55);
    text-align: center;
    line-height: 1.4;
    letter-spacing: 0.01em;
}

.pipe-label strong {
    display: block;
    font-size: 0.75rem;
    color: rgba(255,255,255,0.85);
    margin-bottom: 2px;
}

/* Responsive: xếp dọc trên màn hình nhỏ */
@media (max-width: 640px) {
    .pipeline-wrapper { flex-direction: column; align-items: center; gap: 12px; }
    .pipe-node:not(:last-child)::after { display: none; }
}
</style>

<div class="pipeline-wrapper">

  <div class="pipe-node">
    <div class="pipe-icon-wrap c-blue">📝</div>
    <div class="pipe-label">
      <strong>Nhập liệu</strong>
      Question · Student · Reference
    </div>
  </div>

  <div class="pipe-node">
    <div class="pipe-icon-wrap c-violet">🤖</div>
    <div class="pipe-label">
      <strong>Groq LLM</strong>
      Sinh Pseudo Reference nếu thiếu
    </div>
  </div>

  <div class="pipe-node">
    <div class="pipe-icon-wrap c-orange">⚖️</div>
    <div class="pipe-label">
      <strong>DeBERTa-v3</strong>
      CORRECT · PARTIAL · INCORRECT
    </div>
  </div>

  <div class="pipe-node">
    <div class="pipe-icon-wrap c-teal">💬</div>
    <div class="pipe-label">
      <strong>Flan-T5</strong>
      Sinh nhận xét chi tiết
    </div>
  </div>

  <div class="pipe-node">
    <div class="pipe-icon-wrap c-green">📊</div>
    <div class="pipe-label">
      <strong>Kết quả</strong>
      Hiển thị &amp; xuất JSON
    </div>
  </div>

</div>
""", unsafe_allow_html=True)


def render_router_badge(has_reference: bool) -> None:
    if not has_reference:
        st.markdown("""
<div class="router-wrap">
  <span class="r-icon">🔀</span>
  <span>
    <strong style="color:#e2e8f0">Router:</strong>
    Không có Reference Answer →
    <span class="router-tag">Groq LLM</span>
    sẽ sinh Pseudo Reference Answer (PRA) tự động
  </span>
</div>
""", unsafe_allow_html=True)
    else:
        st.markdown("""
<div class="router-wrap" style="border-left-color:#10b981">
  <span class="r-icon">✅</span>
  <span>
    <strong style="color:#e2e8f0">Router:</strong>
    Reference Answer đã được cung cấp →
    <span class="router-tag" style="color:#6ee7b7;background:rgba(16,185,129,.12);border-color:rgba(16,185,129,.3)">Bỏ qua LLM</span>,
    sử dụng trực tiếp
  </span>
</div>
""", unsafe_allow_html=True)


def render_label_badge(label: str, confidence: float, cfg: dict) -> None:
    st.markdown(f"""
<div class="label-badge" style="background:{cfg['bg']};border:1.5px solid {cfg['border']};">
  <div class="label-name" style="color:{cfg['color']};">{cfg['emoji']} {label}</div>
  <div class="label-conf" style="color:{cfg['color']};">Confidence: {confidence:.1%}</div>
</div>
""", unsafe_allow_html=True)


def render_prob_bars(probs: dict, prob_color: dict) -> None:
    st.markdown('<div class="sec-heading">📈 Phân phối xác suất</div>', unsafe_allow_html=True)
    for lbl in ["CORRECT", "PARTIAL", "INCORRECT"]:
        p = probs[lbl]
        c = prob_color[lbl]
        st.markdown(f"""
<div class="prob-row">
  <div class="prob-lbl" style="color:{c};">{lbl}</div>
  <div class="prob-track"><div class="prob-fill" style="width:{p*100:.1f}%;background:{c};"></div></div>
  <div class="prob-val">{p:.1%}</div>
</div>
""", unsafe_allow_html=True)


def render_pra_box(reference_text: str) -> None:
    st.markdown('<div class="sec-heading">🤖 Pseudo Reference Answer</div>', unsafe_allow_html=True)
    st.markdown(f"""
<div class="pra-box">
  <div class="pra-label">Sinh bởi Groq LLM (zero-shot)</div>
  {reference_text}
</div>
""", unsafe_allow_html=True)


def render_feedback_box(feedback_text: str) -> None:
    st.markdown('<div class="sec-heading">💬 Nhận xét chi tiết</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="feedback-box">{feedback_text}</div>', unsafe_allow_html=True)


def render_empty_state() -> None:
    st.markdown("""
<div class="empty-state">
  <div class="es-icon">🎯</div>
  <p>Kết quả sẽ hiển thị ở đây<br>sau khi bạn nhấn <strong>Chấm điểm</strong>.</p>
</div>
""", unsafe_allow_html=True)


def render_json_block(json_str: str) -> None:
    st.markdown(f'<div class="json-block">{json_str}</div>', unsafe_allow_html=True)

"""
styles_homepage.py
──────────────────
Toàn bộ CSS và HTML component tĩnh cho 1_homepage.py.
"""
import streamlit as st


def inject_base_css() -> None:
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Inter', sans-serif;
    background: #0f1117;
    color: #e2e8f0;
}
/* ── Hero ── */
.hero-wrap {
    background: linear-gradient(135deg, #0f1117 0%, #1a1f2e 50%, #0d1b2a 100%);
    border: 1px solid #2d3748; border-radius: 16px;
    padding: 48px 40px 40px; margin-bottom: 28px;
    position: relative; overflow: hidden;
}
.hero-wrap::before {
    content: ""; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(ellipse at 70% 40%, rgba(99,102,241,.12) 0%, transparent 65%);
    pointer-events: none;
}
.hero-badge {
    display: inline-block;
    background: rgba(99,102,241,.15); border: 1px solid rgba(99,102,241,.4);
    color: #818cf8; font-size: 0.72rem; font-weight: 600;
    letter-spacing: .08em; text-transform: uppercase;
    padding: 4px 12px; border-radius: 99px; margin-bottom: 20px;
}
.hero-title { font-size: clamp(1.55rem, 3vw, 2.15rem); font-weight: 700; line-height: 1.25; color: #f1f5f9; margin-bottom: 10px; }
.hero-title span { color: #818cf8; }
.hero-sub { font-size: 0.95rem; color: #94a3b8; line-height: 1.65; max-width: 560px; margin-bottom: 28px; }
.hero-meta-row { display: flex; flex-wrap: wrap; gap: 10px; }
.hero-meta {
    background: rgba(255,255,255,.05); border: 1px solid #2d3748;
    border-radius: 8px; padding: 8px 14px;
    font-size: 0.80rem; color: #cbd5e1;
    display: flex; align-items: center; gap: 7px;
}
.hero-meta .icon { font-size: 1rem; }
/* ── Info card ── */
.info-card { background: #161b27; border: 1px solid #2d3748; border-radius: 12px; padding: 22px 24px; height: 100%; }
.info-card h4 {
    font-size: 0.78rem; font-weight: 600; text-transform: uppercase; letter-spacing: .07em;
    color: #818cf8; margin-bottom: 16px;
}
.info-row {
    display: flex; align-items: flex-start; gap: 10px;
    padding: 9px 0; border-bottom: 1px solid #1e2535; font-size: 0.87rem;
}
.info-row:last-child { border-bottom: none; }
.info-label { color: #64748b; min-width: 100px; flex-shrink: 0; }
.info-value { color: #e2e8f0; font-weight: 500; }
.info-value a { color: #818cf8; text-decoration: none; }
/* ── Tech pill ── */
.tech-grid { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 4px; }
.tech-pill {
    background: rgba(99,102,241,.12); border: 1px solid rgba(99,102,241,.3);
    color: #a5b4fc; font-size: 0.78rem; font-weight: 500;
    padding: 5px 12px; border-radius: 99px;
}
.tech-pill.green { background: rgba(16,185,129,.1); border-color: rgba(16,185,129,.3); color: #6ee7b7; }
.tech-pill.blue  { background: rgba(59,130,246,.1);  border-color: rgba(59,130,246,.3);  color: #93c5fd; }
.tech-pill.orange{ background: rgba(245,158,11,.1);  border-color: rgba(245,158,11,.3);  color: #fcd34d; }
/* ── Phase timeline ── */
.phase-wrap { background: #161b27; border: 1px solid #2d3748; border-radius: 12px; padding: 24px 26px; margin-bottom: 20px; }
.phase-wrap h4 { font-size: 0.78rem; font-weight: 600; text-transform: uppercase; letter-spacing: .07em; color: #818cf8; margin-bottom: 20px; }
.phase-item { display: flex; gap: 16px; padding: 12px 0; border-bottom: 1px solid #1e2535; }
.phase-item:last-child { border-bottom: none; }
.phase-num {
    width: 32px; height: 32px; border-radius: 8px; flex-shrink: 0;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.75rem; font-weight: 700;
    background: rgba(99,102,241,.15); border: 1px solid rgba(99,102,241,.35); color: #818cf8;
}
.phase-done .phase-num { background: rgba(16,185,129,.15); border-color: rgba(16,185,129,.4); color: #6ee7b7; }
.phase-content { flex: 1; }
.phase-title { font-size: 0.88rem; font-weight: 600; color: #e2e8f0; margin-bottom: 3px; }
.phase-desc  { font-size: 0.80rem; color: #64748b; line-height: 1.5; }
.phase-tag {
    display: inline-block; font-size: 0.65rem; font-weight: 600;
    padding: 2px 8px; border-radius: 99px; margin-top: 5px;
    background: rgba(16,185,129,.12); border: 1px solid rgba(16,185,129,.3); color: #6ee7b7;
}
/* ── Stat card ── */
.stat-row { display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 20px; }
.stat-card {
    flex: 1; min-width: 120px;
    background: #161b27; border: 1px solid #2d3748; border-radius: 12px;
    padding: 18px 20px; text-align: center;
}
.stat-number { font-size: 1.6rem; font-weight: 700; color: #818cf8; }
.stat-label  { font-size: 0.75rem; color: #64748b; margin-top: 4px; }
/* ── Architecture flow ── */
.arch-wrap { background: #161b27; border: 1px solid #2d3748; border-radius: 12px; padding: 24px 26px; margin-bottom: 20px; }
.arch-wrap h4 { font-size: 0.78rem; font-weight: 600; text-transform: uppercase; letter-spacing: .07em; color: #818cf8; margin-bottom: 18px; }
.arch-step { display: flex; align-items: flex-start; gap: 14px; padding: 10px 0; border-bottom: 1px solid #1e2535; }
.arch-step:last-child { border-bottom: none; }
.arch-icon {
    width: 36px; height: 36px; border-radius: 8px; flex-shrink: 0;
    display: flex; align-items: center; justify-content: center; font-size: 1.1rem;
    background: rgba(99,102,241,.12); border: 1px solid rgba(99,102,241,.25);
}
.arch-body  { flex: 1; }
.arch-title { font-size: 0.87rem; font-weight: 600; color: #e2e8f0; }
.arch-desc  { font-size: 0.78rem; color: #64748b; margin-top: 2px; line-height: 1.5; }
.arch-model {
    display: inline-block; font-size: 0.68rem; font-weight: 600;
    padding: 2px 9px; border-radius: 99px; margin-top: 4px;
    background: rgba(99,102,241,.12); border: 1px solid rgba(99,102,241,.3); color: #a5b4fc;
}
</style>
""", unsafe_allow_html=True)


def render_hero() -> None:
    st.markdown("""
<div class="hero-wrap">
  <div class="hero-badge">📚 Cơ sở dữ liệu nâng cao</div>
  <div class="hero-title">
    PHÁT TRIỂN CƠ SỞ DỮ LIỆU<br>
    HỖ TRỢ <span>KIỂM TRA VÀ ĐÁNH GIÁ</span><br> DẠNG CÂU HỎI TỰ LUẬN
  </div>
  <div class="hero-sub">
    Hệ thống tự động chấm điểm và sinh phản hồi câu trả lời tự luận
    sử dụng mô hình ngôn ngữ lớn (DeBERTa + Flan-T5), dữ liệu lưu trữ
    trên HuggingFace Hub, minh họa CSDL quan hệ (PostgreSQL) và đồ thị (Neo4j).
  </div>
  <div class="hero-meta-row">
    <div class="hero-meta"><span class="icon">🗄️</span> PostgreSQL · Neo4j</div>
    <div class="hero-meta"><span class="icon">🤗</span> HuggingFace Hub</div>
    <div class="hero-meta"><span class="icon">🐳</span> Docker</div>
    <div class="hero-meta"><span class="icon">🎯</span> DeBERTa-v3 · Flan-T5</div>
  </div>
</div>
""", unsafe_allow_html=True)


def render_info_student() -> None:
    st.markdown("""
<div class="info-card">
  <h4>👤 Thông tin học viên</h4>
  <div class="info-row"><span class="info-label">Họ và tên</span><span class="info-value">Bùi Nguyên Nghĩa</span></div>
  <div class="info-row"><span class="info-label">MSHV</span><span class="info-value">KHMT836021</span></div>
  <div class="info-row"><span class="info-label">Môn học</span><span class="info-value">Cơ sở dữ liệu nâng cao</span></div>
  <div class="info-row"><span class="info-label">GVHD</span><span class="info-value">TS. Trần Sơn Hải</span></div>
  <div class="info-row">
    <span class="info-label">HuggingFace</span>
    <span class="info-value"><a href="https://huggingface.co/nguyennghia0902" target="_blank">🤗 nguyennghia0902</a></span>
  </div>
  <div class="info-row">
    <span class="info-label">Dataset</span>
    <span class="info-value">
      <a href="https://huggingface.co/datasets/nguyennghia0902/unified-feedback-grading-adb" target="_blank">
        unified-feedback-grading-adb
      </a>
    </span>
  </div>
</div>
""", unsafe_allow_html=True)


def render_info_stack() -> None:
    st.markdown("""
<div class="info-card">
  <h4>🛠️ Stack công nghệ</h4>
  <div class="info-row">
    <span class="info-label">AI Models</span>
    <span class="info-value">
      <div class="tech-grid">
        <span class="tech-pill">DeBERTa-v3-base</span>
        <span class="tech-pill">Flan-T5-base</span>
        <span class="tech-pill">Llama 3.1-8b</span>
      </div>
    </span>
  </div>
  <div class="info-row">
    <span class="info-label">Databases</span>
    <span class="info-value">
      <div class="tech-grid">
        <span class="tech-pill blue">PostgreSQL 16</span>
        <span class="tech-pill green">Neo4j 5.18</span>
      </div>
    </span>
  </div>
  <div class="info-row">
    <span class="info-label">Platform</span>
    <span class="info-value">
      <div class="tech-grid">
        <span class="tech-pill orange">HuggingFace Hub</span>
        <span class="tech-pill blue">Kaggle GPU</span>
        <span class="tech-pill">Docker</span>
      </div>
    </span>
  </div>
  <div class="info-row">
    <span class="info-label">Frontend</span>
    <span class="info-value">
      <div class="tech-grid">
        <span class="tech-pill green">Streamlit</span>
        <span class="tech-pill">Python 3.11</span>
      </div>
    </span>
  </div>
</div>
""", unsafe_allow_html=True)


def render_stat_row() -> None:
    st.markdown("""
<div class="stat-row">
  <div class="stat-card"><div class="stat-number">28,130</div><div class="stat-label">Tổng mẫu dữ liệu</div></div>
  <div class="stat-card"><div class="stat-number">3</div><div class="stat-label">Nguồn dữ liệu</div></div>
  <div class="stat-card"><div class="stat-number">78.98%</div><div class="stat-label">F1-Macro (Grading)</div></div>
  <div class="stat-card"><div class="stat-number">52.64</div><div class="stat-label">ROUGE-L (Feedback)</div></div>
  <div class="stat-card"><div class="stat-number">3</div><div class="stat-label">Nhãn phân loại</div></div>
</div>
""", unsafe_allow_html=True)


def render_arch_pipeline() -> None:
    st.markdown("""
<div class="arch-wrap">
  <h4>⚙️ Kiến trúc Pipeline</h4>
  <div class="arch-step">
    <div class="arch-icon">📥</div>
    <div class="arch-body">
      <div class="arch-title">Nhận đầu vào</div>
      <div class="arch-desc">Question (Q) · Student Answer (SA) · Reference Answer (RA, tùy chọn)</div>
    </div>
  </div>
  <div class="arch-step">
    <div class="arch-icon">🔀</div>
    <div class="arch-body">
      <div class="arch-title">Router kiểm tra Reference Answer</div>
      <div class="arch-desc">Nếu RA trống → Llama 3.1-8b sinh Pseudo Reference Answer (PRA) zero-shot</div>
      <span class="arch-model">Llama 3.1-8b-instruct</span>
    </div>
  </div>
  <div class="arch-step">
    <div class="arch-icon">🎯</div>
    <div class="arch-body">
      <div class="arch-title">Stage 1 — Auto Grading</div>
      <div class="arch-desc">Phân loại Q + RA/PRA + SA → CORRECT / PARTIAL / INCORRECT</div>
      <span class="arch-model">DeBERTa-v3-base · F1=78.98%</span>
    </div>
  </div>
  <div class="arch-step">
    <div class="arch-icon">💬</div>
    <div class="arch-body">
      <div class="arch-title">Stage 2 — Feedback Generation</div>
      <div class="arch-desc">Sinh nhận xét chi tiết dựa trên nhãn phân loại và so sánh đáp án</div>
      <span class="arch-model">Flan-T5-base · ROUGE-L=52.64</span>
    </div>
  </div>
  <div class="arch-step">
    <div class="arch-icon">📤</div>
    <div class="arch-body">
      <div class="arch-title">JSON Output</div>
      <div class="arch-desc">label · confidence · probs · feedback — tải về hoặc xem trực tiếp</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


def render_phase_timeline() -> None:
    st.markdown("""
<div class="phase-wrap">
  <h4>🗓️ Kế hoạch thực hiện (4 Phases)</h4>
  <div class="phase-item phase-done">
    <div class="phase-num">✓</div>
    <div class="phase-content">
      <div class="phase-title">Phase 1 — Exploratory Data Analysis</div>
      <div class="phase-desc">EDA từng bộ dữ liệu: SciEntsBank, Mohler, LLM_Generated. Phân tích phân phối điểm, từ ngữ, phản hồi.</div>
      <span class="phase-tag">✅ Hoàn thành</span>
    </div>
  </div>
  <div class="phase-item phase-done">
    <div class="phase-num">✓</div>
    <div class="phase-content">
      <div class="phase-title">Phase 2 — Data Merging and Database Setup</div>
      <div class="phase-desc">Hợp nhất 3 bộ dữ liệu (28,130 mẫu), embedding, đẩy lên HuggingFace. Khởi tạo PostgreSQL &amp; Neo4j minh họa.</div>
      <span class="phase-tag">✅ Hoàn thành</span>
    </div>
  </div>
  <div class="phase-item phase-done">
    <div class="phase-num">✓</div>
    <div class="phase-content">
      <div class="phase-title">Phase 3 — Model Training</div>
      <div class="phase-desc">Huấn luyện DeBERTa-v3-base (Grading, 7 epochs) và Flan-T5-base (Feedback) trên Kaggle GPU T4. Push lên HuggingFace Hub.</div>
      <span class="phase-tag">✅ Hoàn thành</span>
    </div>
  </div>
  <div class="phase-item phase-done">
    <div class="phase-num">4</div>
    <div class="phase-content">
      <div class="phase-title">Phase 4 — Streamlit App and Docker</div>
      <div class="phase-desc">Xây dựng ứng dụng Streamlit demo pipeline đầu cuối. Đóng gói toàn bộ trong Docker Compose.</div>
      <span class="phase-tag">✅ Hoàn thành</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


def render_dataset_table_header() -> None:
    st.markdown("""
<div class="info-card">
  <h4>📊 Thống kê bộ dữ liệu tổng hợp</h4>
</div>
""", unsafe_allow_html=True)

import streamlit as st

st.set_page_config(
    page_title="Feedback System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background: #0d1117;
        border-right: 1px solid #1e2535;
    }
    .sb-logo-wrap {
        display: flex; align-items: center; gap: 10px;
        padding: 4px 0 20px 0;
        border-bottom: 1px solid #1e2535;
        margin-bottom: 20px;
    }
    .sb-logo-icon {
        width: 38px; height: 38px; border-radius: 10px; flex-shrink: 0;
        background: linear-gradient(135deg, #7c3aed, #4f46e5);
        display: flex; align-items: center; justify-content: center;
        font-size: 1.2rem;
    }
    .sb-logo-text { line-height: 1.25; }
    .sb-logo-title { font-size: 0.92rem; font-weight: 700; color: #f1f5f9; }
    .sb-logo-sub   { font-size: 0.70rem; color: #64748b; letter-spacing: .03em; }
    .sb-section-label {
        font-size: 0.65rem; font-weight: 600;
        text-transform: uppercase; letter-spacing: .1em;
        color: #374151; margin: 20px 0 10px 0;
    }
    .sb-model-card {
        background: #161b27; border: 1px solid #1e2535;
        border-radius: 9px; padding: 10px 13px; margin-bottom: 8px;
    }
    .sb-model-row {
        display: flex; align-items: center;
        justify-content: space-between; gap: 6px;
    }
    .sb-model-name { font-size: 0.78rem; font-weight: 600; color: #e2e8f0; }
    .sb-model-base {
        font-size: 0.68rem; color: #64748b;
        font-family: 'JetBrains Mono', monospace; margin-top: 2px;
    }
    .sb-badge {
        font-size: 0.62rem; font-weight: 600;
        padding: 2px 7px; border-radius: 99px; flex-shrink: 0;
    }
    .sb-badge-violet {
        background: rgba(139,92,246,.15); border: 1px solid rgba(139,92,246,.35); color: #a78bfa;
    }
    .sb-badge-green {
        background: rgba(16,185,129,.12);  border: 1px solid rgba(16,185,129,.30);  color: #6ee7b7;
    }
    .sb-badge-blue {
        background: rgba(96,165,250,.12);  border: 1px solid rgba(96,165,250,.30);  color: #93c5fd;
    }
    .sb-metric-row { display: flex; gap: 7px; margin-bottom: 16px; }
    .sb-metric {
        flex: 1; background: #161b27; border: 1px solid #1e2535;
        border-radius: 8px; padding: 9px 10px; text-align: center;
    }
    .sb-metric-val { font-size: 0.92rem; font-weight: 700; color: #a78bfa; }
    .sb-metric-lbl { font-size: 0.60rem; color: #4b5563; margin-top: 2px; }
    .sb-stack-row  { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 4px; }
    .sb-stack-pill {
        background: #1e2535; border: 1px solid #2d3748;
        border-radius: 99px; padding: 3px 10px;
        font-size: 0.70rem; color: #94a3b8;
    }
    .sb-footer {
        border-top: 1px solid #1e2535; padding-top: 14px; margin-top: 20px;
        font-size: 0.68rem; color: #374151; line-height: 1.65; text-align: center;
    }
    .sb-footer a { color: #6366f1; text-decoration: none; }
    </style>

    <div class="sb-logo-wrap">
      <div class="sb-logo-icon">🎯</div>
      <div class="sb-logo-text">
        <div class="sb-logo-title">Auto Grading <br> Feedback Generation</div>
        <div class="sb-logo-sub">ASAG · Hybrid DB · NLP</div>
      </div>
    </div>

    <div class="sb-section-label">🤖 Models</div>
    <div class="sb-model-card">
      <div class="sb-model-row">
        <div class="sb-model-name">Auto Grading</div>
        <span class="sb-badge sb-badge-violet">F1 78.98%</span>
      </div>
      <div class="sb-model-base">deberta-v3-base</div>
    </div>
    <div class="sb-model-card">
      <div class="sb-model-row">
        <div class="sb-model-name">Feedback Gen</div>
        <span class="sb-badge sb-badge-green">ROUGE 52.64</span>
      </div>
      <div class="sb-model-base">flan-t5-base</div>
    </div>
    <div class="sb-model-card">
      <div class="sb-model-row">
        <div class="sb-model-name">Pseudo Ref</div>
        <span class="sb-badge sb-badge-blue">Zero-shot</span>
      </div>
      <div class="sb-model-base">Llama 3.1-8b</div>
    </div>

    <div class="sb-section-label">📊 Dataset</div>
    <div class="sb-metric-row">
      <div class="sb-metric">
        <div class="sb-metric-val">28K</div>
        <div class="sb-metric-lbl">Mẫu</div>
      </div>
      <div class="sb-metric">
        <div class="sb-metric-val">3</div>
        <div class="sb-metric-lbl">Nguồn</div>
      </div>
      <div class="sb-metric">
        <div class="sb-metric-val">3</div>
        <div class="sb-metric-lbl">Nhãn</div>
      </div>
    </div>

    <div class="sb-section-label">🛠️ Stack</div>
    <div class="sb-stack-row">
      <span class="sb-stack-pill">PostgreSQL</span>
      <span class="sb-stack-pill">Neo4j</span>
      <span class="sb-stack-pill">HuggingFace</span>
      <span class="sb-stack-pill">Streamlit</span>
      <span class="sb-stack-pill">Docker</span>
    </div>

    <div class="sb-footer">
      Môn: Cơ sở dữ liệu nâng cao<br>
      <a href="https://huggingface.co/nguyennghia0902" target="_blank">
        🤗 nguyennghia0902
      </a>
    </div>
    """, unsafe_allow_html=True)

home_page = st.Page("pages/1_homepage.py", title="Trang chủ",   icon="🏠")
sinh_fb = st.Page("pages/2_sinh_feedback.py", title="Sinh phản hồi", icon="🚀")
database = st.Page("pages/3_he_thong_database.py", title="Hệ thống CSDL",   icon="🗄️")
# --- Định nghĩa các page ---
pg = st.navigation([home_page, sinh_fb, database])


pg.run()
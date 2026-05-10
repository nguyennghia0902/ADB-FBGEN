"""
1_homepage.py
─────────────
Trang chủ — giới thiệu dự án, thông tin học viên,
kiến trúc pipeline và thống kê bộ dữ liệu.
"""
import pandas as pd
import streamlit as st

from utils.styles_homepage import (
    inject_base_css,
    render_hero,
    render_info_student,
    render_info_stack,
    render_stat_row,
    render_arch_pipeline,
    render_phase_timeline,
    render_dataset_table_header,
)

# ──────────────────────────────────────────────────────────────────────────────
inject_base_css()
render_hero()

# ── ROW 1 — Thông tin sinh viên + Stack công nghệ ────────────────────────────
col_a, col_b = st.columns([1.1, 1], gap="large")
with col_a:
    render_info_student()
with col_b:
    render_info_stack()

# ── STATS ─────────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
render_stat_row()

# ── ROW 2 — Kiến trúc pipeline + Timeline Phase ───────────────────────────────
col_c, col_d = st.columns([1, 1], gap="large")
with col_c:
    render_arch_pipeline()
with col_d:
    render_phase_timeline()

# ── DATASET TABLE ─────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
render_dataset_table_header()

df_stats = pd.DataFrame([
    {"Nguồn": "SciEntsBank",   "Tổng mẫu": 10_804, "Điểm TB": 0.581, "ĐLC Điểm": 0.399, "Số từ TB (SA)": 12.03, "Có Feedback": "—"},
    {"Nguồn": "Mohler",        "Tổng mẫu":  7_326, "Điểm TB": 0.930, "ĐLC Điểm": 0.187, "Số từ TB (SA)": 19.54, "Có Feedback": "—"},
    {"Nguồn": "LLM_Generated", "Tổng mẫu": 10_000, "Điểm TB": 0.712, "ĐLC Điểm": 0.322, "Số từ TB (SA)": 31.14, "Có Feedback": "10,000"},
    {"Nguồn": "TỔNG / TB",     "Tổng mẫu": 28_130, "Điểm TB": 0.718, "ĐLC Điểm": 0.355, "Số từ TB (SA)": 20.78, "Có Feedback": "10,000"},
])
st.dataframe(df_stats, width='stretch', hide_index=True)

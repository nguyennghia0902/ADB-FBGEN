"""
3_he_thong_database.py
──────────────────────
Trang minh họa hệ thống cơ sở dữ liệu:
PostgreSQL (schema quan hệ) và Neo4j (đồ thị).
"""
import pandas as pd
import streamlit as st

from utils.styles_database import (
    inject_base_css,
    render_hero,
    render_pg_connection,
    render_pg_schemas,
    render_pg_erd,
    render_pg_sql_queries,
    render_neo4j_connection,
    render_neo4j_nodes,
    render_neo4j_relationships,
    render_neo4j_cypher_queries,
)

# ──────────────────────────────────────────────────────────────────────────────
inject_base_css()
render_hero()

tab_pg, tab_neo = st.tabs(["🐘 PostgreSQL", "🔵 Neo4j"])

# ── TAB 1 — PostgreSQL ────────────────────────────────────────────────────────
with tab_pg:
    render_pg_connection()

    st.markdown('<div class="sec-heading">📐 Schema — 5 Bảng quan hệ</div>', unsafe_allow_html=True)
    col_s1, col_s2 = st.columns(2, gap="medium")
    schema_left, schema_right = render_pg_schemas()
    with col_s1:
        st.markdown(schema_left, unsafe_allow_html=True)
    with col_s2:
        st.markdown(schema_right, unsafe_allow_html=True)

    st.markdown('<div class="sec-heading">🔗 Sơ đồ quan hệ (ERD tóm tắt)</div>', unsafe_allow_html=True)
    render_pg_erd()

    st.markdown('<div class="sec-heading">🔍 Câu truy vấn SQL mẫu</div>', unsafe_allow_html=True)
    render_pg_sql_queries()

    st.markdown('<div class="sec-heading">📋 Dữ liệu mẫu — grading_results</div>', unsafe_allow_html=True)
    df_sample = pd.DataFrame([
        {"answer_id": 1, "predicted_label": "PARTIAL",   "true_label": "PARTIAL",   "confidence": 0.7812, "pra_used": False, "model": "deberta-auto-grading-newfinal"},
        {"answer_id": 2, "predicted_label": "CORRECT",   "true_label": "CORRECT",   "confidence": 0.9201, "pra_used": False, "model": "deberta-auto-grading-newfinal"},
        {"answer_id": 3, "predicted_label": "PARTIAL",   "true_label": "PARTIAL",   "confidence": 0.6534, "pra_used": False, "model": "deberta-auto-grading-newfinal"},
        {"answer_id": 4, "predicted_label": "CORRECT",   "true_label": "CORRECT",   "confidence": 0.9580, "pra_used": False, "model": "deberta-auto-grading-newfinal"},
        {"answer_id": 5, "predicted_label": "INCORRECT", "true_label": "INCORRECT", "confidence": 0.8344, "pra_used": False, "model": "deberta-auto-grading-newfinal"},
    ])
    st.dataframe(df_sample, use_container_width=True, hide_index=True)


# ── TAB 2 — Neo4j ─────────────────────────────────────────────────────────────
with tab_neo:
    render_neo4j_connection()

    col_n1, col_n2 = st.columns([1, 1], gap="medium")
    with col_n1:
        render_neo4j_nodes()
        render_neo4j_relationships()
    with col_n2:
        render_neo4j_cypher_queries()

    st.markdown('<div class="sec-heading">📊 Thống kê Graph</div>', unsafe_allow_html=True)
    df_graph = pd.DataFrame([
        {"Node / Rel": ":Dataset",       "Số lượng": 3, "Mô tả": "SciEntsBank, Mohler, LLM_Generated"},
        {"Node / Rel": ":Question",      "Số lượng": 5, "Mô tả": "Câu hỏi mẫu minh họa"},
        {"Node / Rel": ":Answer",        "Số lượng": 5, "Mô tả": "Câu trả lời sinh viên"},
        {"Node / Rel": ":GradingResult", "Số lượng": 5, "Mô tả": "Kết quả chấm từ DeBERTa"},
        {"Node / Rel": ":Model",         "Số lượng": 2, "Mô tả": "DeBERTa grading + Flan-T5 feedback"},
        {"Node / Rel": "BELONGS_TO",     "Số lượng": 5, "Mô tả": "Question → Dataset"},
        {"Node / Rel": "ANSWERS",        "Số lượng": 5, "Mô tả": "Answer → Question"},
        {"Node / Rel": "GRADES",         "Số lượng": 5, "Mô tả": "GradingResult → Answer"},
        {"Node / Rel": "PRODUCED_BY",    "Số lượng": 5, "Mô tả": "GradingResult → Model"},
    ])
    st.dataframe(df_graph, use_container_width=True, hide_index=True)

"""
styles_database.py
──────────────────
Toàn bộ CSS và HTML component tĩnh cho 3_he_thong_database.py.
"""
import streamlit as st


def inject_base_css() -> None:
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Inter', sans-serif; background: #0f1117; color: #e2e8f0;
}
/* ── Hero ── */
.hero-wrap {
    background: linear-gradient(135deg, #0f1117 0%, #0d1b2a 60%, #0f1117 100%);
    border: 1px solid #2d3748; border-radius: 16px;
    padding: 36px 40px 32px; margin-bottom: 28px;
    position: relative; overflow: hidden;
}
.hero-wrap::before {
    content:""; position:absolute; inset:0;
    background: radial-gradient(ellipse at 75% 30%, rgba(16,185,129,.09) 0%, transparent 60%);
    pointer-events:none;
}
.hero-badge {
    display:inline-block; background:rgba(16,185,129,.12); border:1px solid rgba(16,185,129,.35);
    color:#6ee7b7; font-size:0.72rem; font-weight:600;
    letter-spacing:.08em; text-transform:uppercase;
    padding:4px 12px; border-radius:99px; margin-bottom:16px;
}
.hero-title { font-size:clamp(1.4rem,2.5vw,1.9rem); font-weight:700; color:#f1f5f9; line-height:1.25; margin-bottom:10px; }
.hero-title span { color:#6ee7b7; }
.hero-sub { font-size:0.9rem; color:#64748b; line-height:1.65; max-width:580px; }
/* ── Section heading ── */
.sec-heading {
    font-size:0.72rem; font-weight:600; text-transform:uppercase; letter-spacing:.1em;
    color:#6ee7b7; margin-bottom:16px; margin-top:8px;
    display:flex; align-items:center; gap:8px;
}
.sec-heading::after { content:""; flex:1; height:1px; background:#1e2535; }
/* ── DB card ── */
.db-card { background:#161b27; border:1px solid #2d3748; border-radius:12px; padding:22px 24px; margin-bottom:16px; }
.db-card h4 { font-size:0.78rem; font-weight:600; text-transform:uppercase; letter-spacing:.07em; margin-bottom:14px; }
.db-card h4.pg  { color:#60a5fa; }
.db-card h4.neo { color:#6ee7b7; }
/* ── Connection badge ── */
.conn-badge {
    display:inline-flex; align-items:center; gap:8px;
    background:#0f1117; border:1px solid #2d3748; border-radius:8px; padding:8px 14px;
    font-family:'JetBrains Mono', monospace; font-size:0.78rem; color:#94a3b8; margin-bottom:8px;
}
.conn-badge .dot { width:8px; height:8px; border-radius:50%; flex-shrink:0; }
.dot-pg  { background:#60a5fa; box-shadow:0 0 6px #60a5fa; }
.dot-neo { background:#6ee7b7; box-shadow:0 0 6px #6ee7b7; }
/* ── Code block ── */
.code-block {
    background:#0a0d14; border:1px solid #1e2535; border-left:3px solid #6ee7b7;
    border-radius:8px; padding:16px 18px;
    font-family:'JetBrains Mono', monospace; font-size:0.78rem; color:#94a3b8;
    line-height:1.7; white-space:pre-wrap; margin-bottom:12px; overflow-x:auto;
}
.code-block.pg { border-left-color:#60a5fa; }
.kw  { color:#818cf8; font-weight:600; }
.ty  { color:#f472b6; }
.cm  { color:#4b5563; font-style:italic; }
.str { color:#6ee7b7; }
.num { color:#fb923c; }
/* ── Schema table ── */
.schema-wrap { background:#0a0d14; border:1px solid #1e2535; border-radius:8px; overflow:hidden; margin-bottom:12px; }
.schema-wrap table { width:100%; border-collapse:collapse; font-size:0.80rem; }
.schema-wrap th {
    background:#161b27; color:#64748b; font-weight:600; font-size:0.70rem;
    text-transform:uppercase; letter-spacing:.06em; padding:8px 12px; text-align:left;
    border-bottom:1px solid #1e2535;
}
.schema-wrap td { padding:7px 12px; border-bottom:1px solid #0f1117; vertical-align:top; }
.schema-wrap tr:last-child td { border-bottom:none; }
.col-name { color:#e2e8f0; font-weight:500; font-family:'JetBrains Mono',monospace; }
.col-type { color:#f472b6; font-family:'JetBrains Mono',monospace; }
.col-pk   { color:#fcd34d; font-size:0.68rem; font-weight:600; }
.col-fk   { color:#6ee7b7; font-size:0.68rem; font-weight:600; }
.col-desc { color:#64748b; }
/* ── Relationship card (Neo4j) ── */
.rel-item { display:flex; align-items:center; gap:12px; padding:10px 0; border-bottom:1px solid #1e2535; font-size:0.83rem; }
.rel-item:last-child { border-bottom:none; }
.rel-node {
    background:rgba(16,185,129,.12); border:1px solid rgba(16,185,129,.3);
    color:#6ee7b7; font-family:'JetBrains Mono',monospace;
    font-size:0.75rem; font-weight:600; padding:4px 10px; border-radius:6px;
}
.rel-arrow { color:#4b5563; font-size:1.1rem; }
.rel-label {
    background:#1e2535; color:#94a3b8; font-family:'JetBrains Mono',monospace;
    font-size:0.70rem; font-weight:500; padding:2px 9px; border-radius:4px;
}
</style>
""", unsafe_allow_html=True)


def render_hero() -> None:
    st.markdown("""
<div class="hero-wrap">
  <div class="hero-badge">🗄️ Hệ thống Cơ sở Dữ liệu</div>
  <div class="hero-title">MINH HỌA <span>DATABASE</span> BẰNG PostgreSQL &amp; Neo4j</div>
  <div class="hero-sub">
    Schema quan hệ (PostgreSQL) và đồ thị (Neo4j) lưu trữ dữ liệu câu hỏi,
    câu trả lời sinh viên và kết quả chấm điểm. Phần này chỉ minh họa —
    không tích hợp trực tiếp vào pipeline ứng dụng Streamlit.
  </div>
</div>
""", unsafe_allow_html=True)


# ── PostgreSQL ────────────────────────────────────────────────────────────────
def render_pg_connection() -> None:
    st.markdown("""
<div class="db-card">
  <h4 class="pg">🐘 Kết nối PostgreSQL (DBeaver)</h4>
  <div class="conn-badge"><span class="dot dot-pg"></span>Host: localhost · Port: 5432</div><br>
  <div class="conn-badge"><span class="dot dot-pg"></span>Database: adb · User: adb · Password: adb</div>
</div>
""", unsafe_allow_html=True)


def render_pg_schemas() -> None:
    """Render 5 schema tables cho PostgreSQL (trả về 2 cột HTML cho col_s1 / col_s2)."""
    # col_s1
    col_s1_html = """
<div class="db-card">
  <h4 class="pg">datasets</h4>
  <div class="schema-wrap"><table>
    <tr><th>Cột</th><th>Kiểu</th><th>Ghi chú</th></tr>
    <tr><td class="col-name">id</td><td class="col-type">SERIAL</td><td><span class="col-pk">PK</span></td></tr>
    <tr><td class="col-name">source_name</td><td class="col-type">VARCHAR(50)</td><td class="col-desc">SciEntsBank / Mohler / LLM_Generated</td></tr>
    <tr><td class="col-name">description</td><td class="col-type">TEXT</td><td class="col-desc"></td></tr>
    <tr><td class="col-name">total_rows</td><td class="col-type">INT</td><td class="col-desc">Tổng mẫu</td></tr>
    <tr><td class="col-name">created_at</td><td class="col-type">TIMESTAMP</td><td class="col-desc">DEFAULT NOW()</td></tr>
  </table></div>
</div>
<div class="db-card">
  <h4 class="pg">answers</h4>
  <div class="schema-wrap"><table>
    <tr><th>Cột</th><th>Kiểu</th><th>Ghi chú</th></tr>
    <tr><td class="col-name">id</td><td class="col-type">SERIAL</td><td><span class="col-pk">PK</span></td></tr>
    <tr><td class="col-name">question_id</td><td class="col-type">INT</td><td><span class="col-fk">FK → questions</span></td></tr>
    <tr><td class="col-name">student_answer</td><td class="col-type">TEXT</td><td class="col-desc">Câu trả lời sinh viên</td></tr>
    <tr><td class="col-name">reference_answer</td><td class="col-type">TEXT</td><td class="col-desc">Đáp án tham chiếu</td></tr>
    <tr><td class="col-name">raw_score</td><td class="col-type">NUMERIC(4,2)</td><td class="col-desc">0.0 / 0.5 / 1.0</td></tr>
    <tr><td class="col-name">label</td><td class="col-type">VARCHAR(20)</td><td class="col-desc">INCORRECT/PARTIAL/CORRECT</td></tr>
    <tr><td class="col-name">feedback</td><td class="col-type">TEXT</td><td class="col-desc">Nhận xét gốc</td></tr>
    <tr><td class="col-name">source</td><td class="col-type">VARCHAR(50)</td><td class="col-desc">Tên nguồn dữ liệu</td></tr>
  </table></div>
</div>
<div class="db-card">
  <h4 class="pg">model_info</h4>
  <div class="schema-wrap"><table>
    <tr><th>Cột</th><th>Kiểu</th><th>Ghi chú</th></tr>
    <tr><td class="col-name">id</td><td class="col-type">SERIAL</td><td><span class="col-pk">PK</span></td></tr>
    <tr><td class="col-name">model_key</td><td class="col-type">VARCHAR(50)</td><td class="col-desc">grading / feedback</td></tr>
    <tr><td class="col-name">hf_repo_id</td><td class="col-type">VARCHAR(200)</td><td class="col-desc">HuggingFace repo</td></tr>
    <tr><td class="col-name">base_model</td><td class="col-type">VARCHAR(100)</td><td class="col-desc">Model gốc</td></tr>
    <tr><td class="col-name">best_epoch</td><td class="col-type">INT</td><td class="col-desc"></td></tr>
    <tr><td class="col-name">best_f1_macro</td><td class="col-type">NUMERIC(5,4)</td><td class="col-desc">DeBERTa</td></tr>
    <tr><td class="col-name">best_rouge_l</td><td class="col-type">NUMERIC(6,4)</td><td class="col-desc">Flan-T5</td></tr>
  </table></div>
</div>
"""
    # col_s2
    col_s2_html = """
<div class="db-card">
  <h4 class="pg">questions</h4>
  <div class="schema-wrap"><table>
    <tr><th>Cột</th><th>Kiểu</th><th>Ghi chú</th></tr>
    <tr><td class="col-name">id</td><td class="col-type">SERIAL</td><td><span class="col-pk">PK</span></td></tr>
    <tr><td class="col-name">dataset_id</td><td class="col-type">INT</td><td><span class="col-fk">FK → datasets</span></td></tr>
    <tr><td class="col-name">question_id</td><td class="col-type">VARCHAR(100)</td><td class="col-desc">ID gốc từ dataset</td></tr>
    <tr><td class="col-name">question</td><td class="col-type">TEXT</td><td class="col-desc">Nội dung câu hỏi</td></tr>
    <tr><td class="col-name">domain</td><td class="col-type">VARCHAR(100)</td><td class="col-desc">Chủ đề / môn học</td></tr>
  </table></div>
</div>
<div class="db-card">
  <h4 class="pg">grading_results</h4>
  <div class="schema-wrap"><table>
    <tr><th>Cột</th><th>Kiểu</th><th>Ghi chú</th></tr>
    <tr><td class="col-name">id</td><td class="col-type">SERIAL</td><td><span class="col-pk">PK</span></td></tr>
    <tr><td class="col-name">answer_id</td><td class="col-type">INT</td><td><span class="col-fk">FK → answers</span></td></tr>
    <tr><td class="col-name">model_name</td><td class="col-type">VARCHAR(100)</td><td class="col-desc">HF repo ID</td></tr>
    <tr><td class="col-name">predicted_label</td><td class="col-type">VARCHAR(20)</td><td class="col-desc">Nhãn dự đoán</td></tr>
    <tr><td class="col-name">confidence</td><td class="col-type">NUMERIC(5,4)</td><td class="col-desc">Độ tin cậy</td></tr>
    <tr><td class="col-name">prob_incorrect</td><td class="col-type">NUMERIC(5,4)</td><td class="col-desc"></td></tr>
    <tr><td class="col-name">prob_partial</td><td class="col-type">NUMERIC(5,4)</td><td class="col-desc"></td></tr>
    <tr><td class="col-name">prob_correct</td><td class="col-type">NUMERIC(5,4)</td><td class="col-desc"></td></tr>
    <tr><td class="col-name">pra_used</td><td class="col-type">BOOLEAN</td><td class="col-desc">Llama 3.1 sinh PRA</td></tr>
    <tr><td class="col-name">feedback_output</td><td class="col-type">TEXT</td><td class="col-desc">Nhận xét do T5 sinh</td></tr>
    <tr><td class="col-name">graded_at</td><td class="col-type">TIMESTAMP</td><td class="col-desc">DEFAULT NOW()</td></tr>
  </table></div>
</div>
"""
    return col_s1_html, col_s2_html


def render_pg_erd() -> None:
    st.markdown("""<div class="code-block pg">datasets (1) ──────&lt; (N) questions
questions (1) ──────&lt; (N) answers
answers   (1) ──────&lt; (N) grading_results
model_info (1) ────&lt; (N) grading_results   [qua model_name]</div>""", unsafe_allow_html=True)


def render_pg_sql_queries() -> None:
    st.markdown("**Thống kê nhãn theo nguồn dữ liệu**")
    st.markdown("""<div class="code-block pg"><span class="kw">SELECT</span>
    a.source,
    a.label                    <span class="kw">AS</span> true_label,
    gr.predicted_label,
    <span class="kw">COUNT</span>(*)                  <span class="kw">AS</span> num_samples,
    <span class="kw">ROUND</span>(<span class="kw">AVG</span>(gr.confidence), 3) <span class="kw">AS</span> avg_confidence
<span class="kw">FROM</span> grading_results gr
<span class="kw">JOIN</span> answers a  <span class="kw">ON</span> gr.answer_id  = a.id
<span class="kw">GROUP BY</span> a.source, a.label, gr.predicted_label
<span class="kw">ORDER BY</span> a.source, a.label;</div>""", unsafe_allow_html=True)

    st.markdown("**Câu hỏi khó — sinh viên hay trả lời sai**")
    st.markdown("""<div class="code-block pg"><span class="kw">SELECT</span>
    q.question_id,
    <span class="kw">LEFT</span>(q.question, 70) || <span class="str">'...'</span> <span class="kw">AS</span> question_preview,
    <span class="kw">COUNT</span>(*)            <span class="kw">AS</span> total_answers,
    <span class="kw">SUM</span>(<span class="kw">CASE WHEN</span> a.label = <span class="str">'INCORRECT'</span> <span class="kw">THEN</span> 1 <span class="kw">ELSE</span> 0 <span class="kw">END</span>) <span class="kw">AS</span> incorrect_count,
    <span class="kw">ROUND</span>(100.0 * <span class="kw">SUM</span>(<span class="kw">CASE WHEN</span> a.label = <span class="str">'INCORRECT'</span>
                          <span class="kw">THEN</span> 1 <span class="kw">ELSE</span> 0 <span class="kw">END</span>) / <span class="kw">COUNT</span>(*), 1) <span class="kw">AS</span> pct_incorrect
<span class="kw">FROM</span> questions q
<span class="kw">JOIN</span> answers a <span class="kw">ON</span> a.question_id = q.id
<span class="kw">GROUP BY</span> q.id, q.question_id, q.question
<span class="kw">HAVING COUNT</span>(*) >= 2
<span class="kw">ORDER BY</span> pct_incorrect <span class="kw">DESC</span>
<span class="kw">LIMIT</span> 10;</div>""", unsafe_allow_html=True)

    st.markdown("**So sánh nhãn thật vs nhãn dự đoán (Confusion view)**")
    st.markdown("""<div class="code-block pg"><span class="kw">SELECT</span>
    a.label            <span class="kw">AS</span> true_label,
    gr.predicted_label,
    <span class="kw">COUNT</span>(*)          <span class="kw">AS</span> count
<span class="kw">FROM</span> grading_results gr
<span class="kw">JOIN</span> answers a <span class="kw">ON</span> gr.answer_id = a.id
<span class="kw">GROUP BY</span> a.label, gr.predicted_label
<span class="kw">ORDER BY</span> a.label, gr.predicted_label;</div>""", unsafe_allow_html=True)


# ── Neo4j ─────────────────────────────────────────────────────────────────────
def render_neo4j_connection() -> None:
    st.markdown("""
<div class="db-card">
  <h4 class="neo">🔵 Kết nối Neo4j (DBeaver / Neo4j Browser)</h4>
  <div class="conn-badge"><span class="dot dot-neo"></span>Bolt: bolt://localhost:7687</div><br>
  <div class="conn-badge"><span class="dot dot-neo"></span>User: adb · Password: adb</div><br>
  <div class="conn-badge"><span class="dot dot-neo"></span>Browser: http://localhost:7474</div>
</div>
""", unsafe_allow_html=True)


def render_neo4j_nodes() -> None:
    st.markdown('<div class="sec-heading">🔷 Node Labels</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="db-card">
  <div class="schema-wrap"><table>
    <tr><th>Node</th><th>Thuộc tính chính</th></tr>
    <tr><td class="col-name">:Dataset</td><td class="col-desc">name, description, total_rows, domain</td></tr>
    <tr><td class="col-name">:Question</td><td class="col-desc">question_id, text, domain</td></tr>
    <tr><td class="col-name">:Answer</td><td class="col-desc">answer_id, student_answer, reference_answer, raw_score, true_label</td></tr>
    <tr><td class="col-name">:GradingResult</td><td class="col-desc">result_id, predicted_label, confidence, prob_*, pra_used, feedback</td></tr>
    <tr><td class="col-name">:Model</td><td class="col-desc">repo_id, base_model, task, best_f1_macro / best_rougeL</td></tr>
  </table></div>
</div>
""", unsafe_allow_html=True)


def render_neo4j_relationships() -> None:
    st.markdown('<div class="sec-heading">🔗 Relationships</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="db-card">
  <div class="rel-item">
    <span class="rel-node">:Question</span><span class="rel-arrow">──</span>
    <span class="rel-label">BELONGS_TO</span><span class="rel-arrow">──►</span>
    <span class="rel-node">:Dataset</span>
  </div>
  <div class="rel-item">
    <span class="rel-node">:Answer</span><span class="rel-arrow">──</span>
    <span class="rel-label">ANSWERS</span><span class="rel-arrow">──►</span>
    <span class="rel-node">:Question</span>
  </div>
  <div class="rel-item">
    <span class="rel-node">:GradingResult</span><span class="rel-arrow">──</span>
    <span class="rel-label">GRADES</span><span class="rel-arrow">──►</span>
    <span class="rel-node">:Answer</span>
  </div>
  <div class="rel-item">
    <span class="rel-node">:GradingResult</span><span class="rel-arrow">──</span>
    <span class="rel-label">PRODUCED_BY</span><span class="rel-arrow">──►</span>
    <span class="rel-node">:Model</span>
  </div>
</div>
""", unsafe_allow_html=True)


def render_neo4j_cypher_queries() -> None:
    st.markdown('<div class="sec-heading">🔍 Cypher Queries mẫu</div>', unsafe_allow_html=True)

    st.markdown("**Xem toàn bộ graph**")
    st.markdown("""<div class="code-block"><span class="kw">MATCH</span> (n)
<span class="kw">RETURN</span> n <span class="kw">LIMIT</span> <span class="num">25</span>;</div>""", unsafe_allow_html=True)

    st.markdown("**Câu trả lời + kết quả chấm điểm + model**")
    st.markdown("""<div class="code-block"><span class="kw">MATCH</span> (gr:GradingResult)-[:GRADES]->(a:Answer)
      -[:ANSWERS]->(q:Question),
      (gr)-[:PRODUCED_BY]->(m:Model)
<span class="kw">RETURN</span>
  q.question_id,
  <span class="kw">LEFT</span>(q.text, <span class="num">60</span>) <span class="kw">AS</span> question,
  a.true_label,
  gr.predicted_label,
  gr.confidence,
  m.base_model
<span class="kw">ORDER BY</span> gr.confidence <span class="kw">DESC</span>;</div>""", unsafe_allow_html=True)

    st.markdown("**Phát hiện câu trả lời bị chấm sai**")
    st.markdown("""<div class="code-block"><span class="kw">MATCH</span> (gr:GradingResult)-[:GRADES]->(a:Answer)
<span class="kw">WHERE</span> gr.predicted_label &lt;&gt; a.true_label
<span class="kw">RETURN</span>
  a.answer_id,
  a.true_label       <span class="kw">AS</span> gold,
  gr.predicted_label <span class="kw">AS</span> predicted,
  gr.confidence;</div>""", unsafe_allow_html=True)

    st.markdown("**Câu hỏi theo dataset**")
    st.markdown("""<div class="code-block"><span class="kw">MATCH</span> (q:Question)-[:BELONGS_TO]->(d:Dataset)
<span class="kw">RETURN</span>
  d.name         <span class="kw">AS</span> dataset,
  d.total_rows,
  <span class="kw">count</span>(q)       <span class="kw">AS</span> num_questions,
  <span class="kw">collect</span>(q.question_id) <span class="kw">AS</span> ids
<span class="kw">ORDER BY</span> d.total_rows <span class="kw">DESC</span>;</div>""", unsafe_allow_html=True)

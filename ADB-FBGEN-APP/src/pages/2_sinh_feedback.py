"""
2_sinh_feedback.py
──────────────────
Trang chấm điểm & sinh phản hồi tự luận — HuggingFace Space (Streamlit).
Pipeline:
  1. Nhận Question + Student Answer + (tùy chọn) Reference Answer
  2. Nếu thiếu Reference → Groq LLM sinh Pseudo Reference Answer (PRA)
  3. DeBERTa-v3 phân loại: CORRECT / PARTIAL / INCORRECT + xác suất
  4. Keyword-overlap hiệu chỉnh nhãn (post-processing)
  5. Flan-T5 sinh nhận xét giáo dục ngắn gọn
  6. Hiển thị kết quả + xuất JSON
"""

import os
import json
import re

import torch
import streamlit as st
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    T5ForConditionalGeneration,
)
from groq import Groq

from utils.styles_feedback import (
    inject_base_css,
    render_hero,
    render_pipeline_steps,
    render_router_badge,
    render_label_badge,
    render_prob_bars,
    render_pra_box,
    render_feedback_box,
    render_empty_state,
    render_json_block,
)

# ──────────────────────────────────────────────────────────────────────────────
# CONFIG
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Auto Grading & Feedback",
    page_icon="🎯",
    layout="wide",
)

GROQ_API_KEY     = os.environ.get("GROQ_API_KEY")
GRADING_MODEL_ID = "nguyennghia0902/deberta-auto-grading-newfinal"
FEEDBACK_MODEL_ID = "nguyennghia0902/t5-feedback-generator-newfinal"

LABEL_CONFIG = {
    "CORRECT":   {"color": "#10b981", "bg": "rgba(16,185,129,.10)",  "border": "rgba(16,185,129,.35)",  "emoji": "✅"},
    "PARTIAL":   {"color": "#f59e0b", "bg": "rgba(245,158,11,.10)",  "border": "rgba(245,158,11,.35)",  "emoji": "⚠️"},
    "INCORRECT": {"color": "#ef4444", "bg": "rgba(239,68,68,.10)",   "border": "rgba(239,68,68,.35)",   "emoji": "❌"},
}
PROB_COLOR = {"CORRECT": "#10b981", "PARTIAL": "#f59e0b", "INCORRECT": "#ef4444"}

# ──────────────────────────────────────────────────────────────────────────────
# MODEL LOADING  (cache — chỉ load 1 lần khi khởi động Space)
# ──────────────────────────────────────────────────────────────────────────────
@st.cache_resource(show_spinner="⏳ Đang khởi tạo hệ thống AI (lần đầu mất ~1-2 phút)...")
def load_models():
    try:
        g_tok   = AutoTokenizer.from_pretrained(GRADING_MODEL_ID)
        g_model = AutoModelForSequenceClassification.from_pretrained(
            GRADING_MODEL_ID, torch_dtype=torch.float32
        )
        g_model.eval()

        f_tok   = AutoTokenizer.from_pretrained(FEEDBACK_MODEL_ID)
        f_model = T5ForConditionalGeneration.from_pretrained(FEEDBACK_MODEL_ID)
        f_model.eval()

        return g_tok, g_model, f_tok, f_model
    except Exception as exc:
        st.error(f"🚨 Không thể load mô hình: {exc}")
        st.stop()


grading_tokenizer, grading_model, feedback_tokenizer, feedback_model = load_models()

# ──────────────────────────────────────────────────────────────────────────────
# INFERENCE FUNCTIONS
# ──────────────────────────────────────────────────────────────────────────────
_STOP_WORDS = {"the", "a", "an", "is", "are", "was", "were", "to", "of", "and", "in", "it", "that"}

def clean_reference(reference: str) -> str:
    """Loại bỏ ký hiệu hóa học/toán học khỏi Reference trước khi truyền vào model."""
    # oxygen (O2) → oxygen
    reference = re.sub(r'\s*\([A-Z][a-z]?\d*\)', '', reference)
    # Công thức đứng độc lập: O2, CO2, H2O, ATP
    reference = re.sub(r'\b[A-Z][a-z]?\d+\b', '', reference)
    # Công thức toán: F = ma, E = mc²
    reference = re.sub(r'\b[A-Z]\s*=\s*[A-Za-z0-9\s\*\+\-\/\^²³]+', '', reference)
    # Dấu mũi tên hóa học
    reference = re.sub(r'→|->|⟶', '', reference)
    # Dọn khoảng trắng
    return re.sub(r'\s+', ' ', reference).strip()

def _keywords(text: str) -> set:
    return set(re.findall(r'\b\w+\b', text.lower())) - _STOP_WORDS


def keyword_overlap_boost(student: str, reference: str, result: dict) -> dict:
    """Hiệu chỉnh nhãn DeBERTa dựa trên tỉ lệ keyword trùng khớp."""
    ref_kw = _keywords(reference)
    if not ref_kw:
        return result

    ratio = len(_keywords(student) & ref_kw) / len(ref_kw)
    if ratio >= 0.75:
        result["label"] = "CORRECT"
        result["note"]  = f"✅ Keyword overlap {ratio:.0%}"
    elif ratio >= 0.40:
        result["label"] = "PARTIAL"
        result["note"]  = f"⚠️ Keyword overlap {ratio:.0%}"
    else:
        result["label"] = "INCORRECT"
        result["note"]  = f"❌ Keyword overlap {ratio:.0%}"
    return result


def predict_grade(question: str, reference: str, student: str) -> dict:
    """Chấm điểm bằng DeBERTa-v3."""
    context = f"Question: {question} [SEP] Reference: {reference}"
    
    try:
        enc = grading_tokenizer(
            context,
            student,                  # ← sentence B riêng biệt
            return_tensors="pt",
            truncation=True,
            max_length=512,
            padding="max_length"
        )
        with torch.no_grad():
            logits = grading_model(**enc).logits
            probs = torch.nn.functional.softmax(logits, dim=-1)[0]
            idx = torch.argmax(probs).item()

        id2label = {0: "INCORRECT", 1: "PARTIAL", 2: "CORRECT"}
        return {
            "label": id2label[idx],
            "confidence": probs[idx].item(),
            "probs": {
                "INCORRECT": round(probs[0].item(), 4),
                "PARTIAL":   round(probs[1].item(), 4),
                "CORRECT":   round(probs[2].item(), 4),
            },
        }
    except Exception as exc:
        st.error(f"🚨 Lỗi Grading: {exc}")
        st.stop()


def generate_feedback(question: str, reference: str, student: str, label: str) -> str:
    """Sinh nhận xét giáo dục bằng Flan-T5."""
    # Map nhãn sang score và text
    label_map = {"CORRECT": (1.0, "correct"), "PARTIAL": (0.5, "partially correct"), "INCORRECT": (0.0, "incorrect")}
    score_val, score_text = label_map.get(label, (0.0, "unknown"))
    
    # ✅ Format đúng với lúc train
    prompt = (
        f"Generate educational feedback based on the following information: "
        f"Question: {question} "
        f"Ideal Answer: {reference} "
        f"Student Response: {student} "
        f"Assigned Score: {score_val:.1f}/1.0 {score_text} "
        f"Feedback:"
    )
    
    try:
        enc = feedback_tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            ids = feedback_model.generate(
                **enc,
                max_new_tokens=120,
                num_beams=4,
                early_stopping=True
            )
        return feedback_tokenizer.decode(ids[0], skip_special_tokens=True).strip()
    except Exception as exc:
        st.error(f"🚨 Lỗi Feedback: {exc}")
        st.stop()


@st.cache_data(show_spinner=False, ttl=3600)
def generate_pseudo_reference(question: str) -> str:
    """Gọi Groq (Llama 3.1-8b) để sinh Pseudo Reference Answer — cache theo câu hỏi."""
    client = Groq(api_key=GROQ_API_KEY)
    resp = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a science teacher. Write a concise reference answer (1-2 sentences). "
                    "Include only key concepts and core mechanism. "
                    "No equations, no filler, no explanation — answer only."
                ),
            },
            {"role": "user", "content": question},
        ],
        model="llama-3.1-8b-instant",
        temperature=0.1,
        max_tokens=80,
    )
    return resp.choices[0].message.content.strip()

# ──────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ──────────────────────────────────────────────────────────────────────────────
if "result" not in st.session_state:
    st.session_state.result = None

# ──────────────────────────────────────────────────────────────────────────────
# PAGE RENDER
# ──────────────────────────────────────────────────────────────────────────────
inject_base_css()
render_hero()
render_pipeline_steps()

col_left, col_right = st.columns([1, 1], gap="large")

# ── CỘT TRÁI — INPUT ──────────────────────────────────────────────────────────
with col_left:
    st.markdown('<div class="sec-heading">📥 Nhập liệu</div>', unsafe_allow_html=True)

    question         = st.text_area("❓ Câu hỏi (Question) *",
                                    placeholder="Nhập câu hỏi cần chấm điểm...", height=100)
    student_answer   = st.text_area("🎓 Câu trả lời của sinh viên (Student Answer) *",
                                    placeholder="Nhập câu trả lời của sinh viên...", height=130)
    reference_answer = st.text_area("📖 Đáp án tham chiếu (Reference Answer)",
                                    placeholder="Tùy chọn — để trống để LLM tự sinh Pseudo Reference Answer.",
                                    height=100)

    run_btn = st.button("🚀  Chấm điểm và tạo nhận xét", type="primary", use_container_width=True)
    render_router_badge(has_reference=bool(reference_answer.strip()))

# ── RUN LOGIC ─────────────────────────────────────────────────────────────────
if run_btn:
    if not question.strip() or not student_answer.strip():
        st.warning("⚠️ Vui lòng nhập đầy đủ Câu hỏi và Câu trả lời của sinh viên.")
        st.stop()

    ref      = reference_answer.strip()
    pra_used = False

    # Bước 1: Sinh Pseudo Reference nếu thiếu
    if not ref:
        with st.spinner("🤖 Groq LLM đang sinh Pseudo Reference Answer..."):
            ref = clean_reference(generate_pseudo_reference(question.strip()))
        pra_used = True

    # Bước 2: Chấm điểm (DeBERTa + keyword boost)
    with st.spinner("🔍 DeBERTa đang chấm điểm..."):
        grading = predict_grade(question, ref, student_answer)
        grading = keyword_overlap_boost(student_answer, ref, grading)

    # Bước 3: Sinh Feedback (Flan-T5)
    with st.spinner("💬 Flan-T5 đang sinh nhận xét..."):
        feedback = generate_feedback(question, ref, student_answer, grading["label"])

    # Lưu vào session state
    st.session_state.result = {
        "question":       question,
        "student_answer": student_answer,
        "reference":      ref,
        "pra_used":       pra_used,
        "grading":        grading,
        "feedback":       feedback,
    }

# ── CỘT PHẢI — OUTPUT ─────────────────────────────────────────────────────────
with col_right:
    st.markdown('<div class="sec-heading">📊 Kết quả</div>', unsafe_allow_html=True)

    res = st.session_state.result
    if res is None:
        render_empty_state()
    else:
        label = res["grading"]["label"]
        conf  = res["grading"]["confidence"]
        probs = res["grading"]["probs"]
        cfg   = LABEL_CONFIG[label]

        render_label_badge(label, conf, cfg)
        render_prob_bars(probs, PROB_COLOR)

        st.markdown("<br>", unsafe_allow_html=True)

        if res["pra_used"]:
            render_pra_box(res["reference"])

        render_feedback_box(res["feedback"])

        st.markdown("<br>", unsafe_allow_html=True)

        # JSON output
        json_output = {
            "input": {
                "question":              res["question"],
                "student_answer":        res["student_answer"],
                "reference_answer_used": res["reference"],
                "pra_generated":         res["pra_used"],
            },
            "output": {
                "label":      label,
                "confidence": round(conf, 4),
                "probs":      probs,
                "feedback":   res["feedback"],
                "note":       res["grading"].get("note", ""),
            },
        }
        json_str = json.dumps(json_output, ensure_ascii=False, indent=2)

        with st.expander("📄 JSON Output", expanded=False):
            render_json_block(json_str)

        st.download_button(
            label="⬇️  Tải kết quả JSON",
            data=json_str,
            file_name="grading_result.json",
            mime="application/json",
            use_container_width=True,
        )

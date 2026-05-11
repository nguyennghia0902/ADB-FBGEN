<div align="center">

# 🎓 MÔ HÌNH HÓA VÀ TÍCH HỢP CƠ SỞ DỮ LIỆU ĐA NGUỒN
## Cải tiến Bài toán Tự động  TạO Sinh Phản hồi 

[![HuggingFace Demo](https://img.shields.io/badge/🤗%20Demo-ADB--FBGEN-blue?style=for-the-badge)](https://huggingface.co/spaces/nguyennghia0902/ADB-FBGEN)
[![GitHub](https://img.shields.io/badge/GitHub-ADB--FBGEN-181717?style=for-the-badge&logo=github)](https://github.com/nguyennghia0902/ADB-FBGEN)
[![Google Drive](https://img.shields.io/badge/Google%20Drive-Tài%20nguyên-34A853?style=for-the-badge&logo=google-drive&logoColor=white)](https://drive.google.com/drive/folders/14w8zY61wFhFt1ByGE_C2Sv8nM1zO-Amp?usp=sharing)

> **Dự án cá nhân** · Học phần: Cơ sở Dữ liệu Nâng cao · Trường ĐH Sư phạm TP. Hồ Chí Minh

</div>

---

## 📌 Tổng quan

Dự án xây dựng ứng dụng **ADB-FBGEN-APP** — hệ thống hỗ trợ **chấm điểm tự động** và **sinh phản hồi giáo dục** cho câu trả lời tự luận ngắn.

Hệ thống kết hợp:
- 🗄️ **PostgreSQL** — lưu trữ dữ liệu có cấu trúc, tối ưu cho huấn luyện mô hình
- 🔗 **Neo4j** — cơ sở dữ liệu đồ thị, khai thác quan hệ ngữ nghĩa đa chiều
- 🤖 **DeBERTa-v3** — phân loại 3 lớp: `CORRECT` / `PARTIAL` / `INCORRECT`
- 💬 **Flan-T5** — sinh phản hồi giáo dục tự nhiên, có căn cứ
- 🧠 **Pseudo Reference Answer (PRA)** — tự động sinh đáp án chuẩn khi giáo viên không cung cấp
- 🐳 **Docker Compose** — đóng gói toàn bộ hệ thống, triển khai một lệnh

---

## 🏗️ Kiến trúc hệ thống

```
┌─────────────────────────────────────────────────────┐
│          Tầng 4 · Giao diện Streamlit                │
│     (Trang chủ · Sinh phản hồi · Quản trị CSDL)    │
└───────────────────┬─────────────────────────────────┘
                    ▼
┌─────────────────────────────────────────────────────┐
│     Tầng 3 · Inference Pipeline                     │
│  DeBERTa → Keyword Boost → Flan-T5                  │
└───────────────────┬─────────────────────────────────┘
                    ▼
┌─────────────────────────────────────────────────────┐
│     Tầng 2 · Model Hub (HuggingFace)                │
│  deberta-auto-grading · t5-feedback-generator       │
└───────────────────┬─────────────────────────────────┘
                    ▼
┌─────────────────────────────────────────────────────┐
│     Tầng 1 · Dữ liệu                               │
│  HF Dataset · PostgreSQL · Neo4j                    │
└─────────────────────────────────────────────────────┘
```

---

## 📂 Tài nguyên dự án

Toàn bộ tài nguyên được lưu trữ tập trung tại **Google Drive**:

[![Google Drive](https://img.shields.io/badge/📁%20Truy%20cập%20Google%20Drive-34A853?style=flat-square&logo=google-drive&logoColor=white)](https://drive.google.com/drive/folders/14w8zY61wFhFt1ByGE_C2Sv8nM1zO-Amp?usp=sharing)

| Thư mục / Tệp | Nội dung |
|---|---|
| 📄 **Báo cáo & Slide** | Tiểu luận và slide thuyết trình (định dạng PDF) |
| 📓 **Notebook** | Các notebook chi tiết từng giai đoạn: thu thập dữ liệu, EDA, huấn luyện, đánh giá |
| 📊 **Dataset** | Các bộ dữ liệu đã xử lý và tập hợp nhất 28.130 mẫu |
| 🐳 **Mã nguồn (Dockerized)** | Dự án `ADB-FINAL` gồm Docker-compose (PostgreSQL + Neo4j) và toàn bộ mã nguồn Streamlit (file `.zip`) |

---

## 🔗 Liên kết nhanh

| Tài nguyên | Đường dẫn |
|---|---|
| 🤗 Ứng dụng Demo | [huggingface.co/spaces/nguyennghia0902/ADB-FBGEN](https://huggingface.co/spaces/nguyennghia0902/ADB-FBGEN) |
| 💻 GitHub Repo | [github.com/nguyennghia0902/ADB-FBGEN](https://github.com/nguyennghia0902/ADB-FBGEN) |
| 📁 Google Drive | [Truy cập tại đây](https://drive.google.com/drive/folders/14w8zY61wFhFt1ByGE_C2Sv8nM1zO-Amp?usp=sharing) |
| 🧠 Mô hình DeBERTa | [nguyennghia0902/deberta-auto-grading-newfinal](https://huggingface.co/nguyennghia0902/deberta-auto-grading-newfinal) |
| 💬 Mô hình Flan-T5 | [nguyennghia0902/t5-feedback-generator-newfinal](https://huggingface.co/nguyennghia0902/t5-feedback-generator-newfinal) |
| 📊 Dataset | [nguyennghia0902/unified-feedback-grading-adb](https://huggingface.co/datasets/nguyennghia0902/unified-feedback-grading-adb) |

---

## 📊 Kết quả nổi bật

| Mô hình | Metric | Kết quả | Mục tiêu |
|---|---|---|---|
| DeBERTa-v3 (AutoGrading) | F1-Macro | **0.7898** | ≥ 0.75 ✅ |
| Flan-T5-base (Feedback) | ROUGE-L | **52.64** | ≥ 50.0 ✅ |
| Tập dữ liệu hợp nhất | Số mẫu | **28.130** | ≥ 20.000 ✅ |

> GPU: Tesla T4 · DeBERTa: 4.56 giờ · Flan-T5: 3.87 giờ · Optimizer: AdamW / Adafactor

---

## 👤 Thông tin thực hiện

<table>
  <tr>
    <td><strong>Họ và tên</strong></td>
    <td>Bùi Nguyên Nghĩa</td>
  </tr>
  <tr>
    <td><strong>Mã học viên</strong></td>
    <td>KHMT836021</td>
  </tr>
  <tr>
    <td><strong>Chương trình</strong></td>
    <td>Cao học Khóa 36 · Ngành Khoa học Máy tính</td>
  </tr>
  <tr>
    <td><strong>Trường</strong></td>
    <td>Đại học Sư phạm Thành phố Hồ Chí Minh</td>
  </tr>
  <tr>
    <td><strong>Học phần</strong></td>
    <td>Cơ sở Dữ liệu Nâng cao</td>
  </tr>
  <tr>
    <td><strong>Giảng viên</strong></td>
    <td>TS. Trần Sơn Hải</td>
  </tr>
</table>

---

<div align="center">

*Trường Đại học Sư phạm Thành phố Hồ Chí Minh · Khoa Công nghệ Thông tin · 2025–2027*

</div>

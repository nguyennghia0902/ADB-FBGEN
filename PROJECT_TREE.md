# adb-final
## Cấu trúc thư mục dự án Docker

ADB-FINAL/
├── docker-compose.yml               # Khởi chạy PostgreSQL + Neo4j
├── mydb/                            # Dữ liệu minh họa (không tích hợp app)
│   ├── postgres/
│   │   └── init.sql                 # Schema + seed data PostgreSQL
│   └── neo4j/
│       └── seed.cypher              # Nodes + relationships Neo4j
└── ADB-FBGEN-APP/                   # Ứng dụng chính
    ├── requirements.txt             # Thư viện Python
    ├── streamlit_app.py             # File điều hướng chính
    ├── pages/                       # Các trang con của Streamlit
    │   ├── 1_homepage.py            # Giới thiệu dự án
    │   ├── 2_sinh_feedback.py       # Trang chính: grading + feedback
    │   └── 3_he_thong_database.py   # Trang hệ thống database
    └── utils/                       # Các file hỗ trợ (styles, helpers)
        ├── styles_homepage.py
        ├── styles_feedback.py
        └── styles_database.py





## Ghi chú
- Thư mục `db/` chỉ phục vụ minh họa cơ sở dữ liệu, KHÔNG kết nối vào app Streamlit.
- Models DeBERTa và Flan-T5 được load trực tiếp từ HuggingFace Hub khi app khởi động.
- HuggingFace cache mount vào volume `hf_cache` để tránh download lại mỗi lần restart.
- Kết nối DBeaver:
    PostgreSQL: host=localhost port=5432 db=adb user=adb pass=adb
    Neo4j:      bolt://localhost:7687  user=neo4j pass=adb_password

## Chạy dự án
    docker compose up --build

## Truy cập
    Streamlit App  : http://localhost:8501
    Neo4j Browser  : http://localhost:7474

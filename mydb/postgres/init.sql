-- =============================================================================
-- ADB-FINAL: PostgreSQL Schema + Seed Data (Minh họa, KHÔNG tích hợp App)
-- Kết nối qua DBeaver: host=localhost port=5432 db=adb_grading user=adb_user
-- =============================================================================

-- 0. Tạo database (chạy với user postgres)
-- CREATE DATABASE adb_grading;
-- \c adb_grading

-- =============================================================================
-- 1. SCHEMA
-- =============================================================================

CREATE TABLE IF NOT EXISTS datasets (
    id          SERIAL PRIMARY KEY,
    source_name VARCHAR(50)  NOT NULL,          -- 'SciEntsBank' | 'Mohler' | 'LLM_Generated'
    description TEXT,
    total_rows  INT,
    created_at  TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS questions (
    id          SERIAL PRIMARY KEY,
    dataset_id  INT REFERENCES datasets(id) ON DELETE CASCADE,
    question_id VARCHAR(100),                   -- id gốc từ dataset
    question    TEXT NOT NULL,
    domain      VARCHAR(100),                   -- môn học / chủ đề
    created_at  TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS answers (
    id               SERIAL PRIMARY KEY,
    question_id      INT REFERENCES questions(id) ON DELETE CASCADE,
    student_answer   TEXT NOT NULL,
    reference_answer TEXT,
    raw_score        NUMERIC(4,2),              -- 0.0 | 0.5 | 1.0
    label            VARCHAR(20),               -- INCORRECT | PARTIAL | CORRECT
    feedback         TEXT,
    embedding_vector TEXT,                      -- JSON array (768-dim), rút gọn để minh họa
    source           VARCHAR(50),
    created_at       TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS grading_results (
    id               SERIAL PRIMARY KEY,
    answer_id        INT REFERENCES answers(id) ON DELETE CASCADE,
    model_name       VARCHAR(100) NOT NULL,     -- 'deberta-auto-grading-newfinal'
    predicted_label  VARCHAR(20)  NOT NULL,
    confidence       NUMERIC(5,4),
    prob_incorrect   NUMERIC(5,4),
    prob_partial     NUMERIC(5,4),
    prob_correct     NUMERIC(5,4),
    feedback_output  TEXT,
    pra_used         BOOLEAN DEFAULT FALSE,     -- TRUE nếu Phi-3 sinh PRA
    graded_at        TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS model_info (
    id              SERIAL PRIMARY KEY,
    model_key       VARCHAR(50)  UNIQUE NOT NULL, -- 'grading' | 'feedback'
    hf_repo_id      VARCHAR(200) NOT NULL,
    base_model      VARCHAR(100),
    best_epoch      INT,
    best_f1_macro   NUMERIC(5,4),
    best_rouge_l    NUMERIC(6,4),
    description     TEXT,
    trained_at      TIMESTAMP
);

-- =============================================================================
-- 2. SEED DATA
-- =============================================================================

-- 2.1 Datasets
INSERT INTO datasets (source_name, description, total_rows) VALUES
  ('SciEntsBank',    'Tập dữ liệu khoa học đất/môi trường (SEMEVAL-2013)', 10804),
  ('Mohler',         'Tập dữ liệu khoa học máy tính (Mohler et al.)',      7326),
  ('LLM_Generated',  'Tập dữ liệu sinh bởi LLM, có feedback sẵn',         10000);

-- 2.2 Câu hỏi mẫu
INSERT INTO questions (dataset_id, question_id, question, domain) VALUES
  (1, 'SEB-Q001', 'What is the process by which plants make food using sunlight?',       'Biology'),
  (1, 'SEB-Q002', 'Describe the water cycle.',                                           'Earth Science'),
  (2, 'MOH-Q001', 'What is a primary key in a relational database?',                     'Database'),
  (2, 'MOH-Q002', 'Explain the difference between a stack and a queue.',                 'Data Structures'),
  (3, 'LLM-Q001', 'What is the difference between supervised and unsupervised learning?','Machine Learning');

-- 2.3 Câu trả lời mẫu (minh họa)
INSERT INTO answers (question_id, student_answer, reference_answer, raw_score, label, feedback, source) VALUES
  (1,
   'Plants use sunlight and CO2 to produce glucose.',
   'Photosynthesis is the process by which plants use sunlight, water, and CO2 to produce glucose and oxygen.',
   0.5, 'PARTIAL',
   'Good partial answer. You mentioned sunlight and CO2 but omitted water and the production of oxygen.',
   'SciEntsBank'),

  (2,
   'The water cycle involves evaporation, condensation, and precipitation.',
   'The water cycle describes how water evaporates, condenses into clouds, and falls as precipitation, returning to bodies of water.',
   1.0, 'CORRECT',
   'Excellent! You correctly described all three main stages of the water cycle.',
   'SciEntsBank'),

  (3,
   'A primary key uniquely identifies each row in a table.',
   'A primary key is a column or set of columns that uniquely identifies each row in a relational database table. It must be unique and not null.',
   0.5, 'PARTIAL',
   'Correct concept but missing the constraints: NOT NULL and uniqueness must both be stated.',
   'Mohler'),

  (4,
   'A stack is LIFO and a queue is FIFO.',
   'A stack follows Last-In-First-Out (LIFO) order, while a queue follows First-In-First-Out (FIFO) order.',
   1.0, 'CORRECT',
   'Perfect. You correctly identified the ordering principle for both data structures.',
   'Mohler'),

  (5,
   'Supervised learning uses labeled data.',
   'Supervised learning uses labeled training data to learn a mapping from inputs to outputs. Unsupervised learning finds patterns in unlabeled data.',
   0.0, 'INCORRECT',
   'Incomplete. You only described supervised learning and did not address unsupervised learning at all.',
   'LLM_Generated');

-- 2.4 Kết quả chấm điểm mô hình
INSERT INTO grading_results
  (answer_id, model_name, predicted_label, confidence, prob_incorrect, prob_partial, prob_correct, feedback_output, pra_used)
VALUES
  (1, 'nguyennghia0902/deberta-auto-grading-newfinal', 'PARTIAL',    0.7812, 0.0854, 0.7812, 0.1334,
   'Partial answer. Mentions sunlight and CO2 but misses water and oxygen.',          FALSE),
  (2, 'nguyennghia0902/deberta-auto-grading-newfinal', 'CORRECT',    0.9201, 0.0321, 0.0478, 0.9201,
   'Complete and accurate description of the water cycle.',                           FALSE),
  (3, 'nguyennghia0902/deberta-auto-grading-newfinal', 'PARTIAL',    0.6534, 0.1203, 0.6534, 0.2263,
   'Core concept correct but NOT NULL constraint not mentioned.',                     FALSE),
  (4, 'nguyennghia0902/deberta-auto-grading-newfinal', 'CORRECT',    0.9580, 0.0201, 0.0219, 0.9580,
   'Correct identification of LIFO and FIFO.',                                        FALSE),
  (5, 'nguyennghia0902/deberta-auto-grading-newfinal', 'INCORRECT',  0.8344, 0.8344, 0.1101, 0.0555,
   'Only supervised learning described. Unsupervised learning not addressed.',        FALSE);

-- 2.5 Thông tin model
INSERT INTO model_info
  (model_key, hf_repo_id, base_model, best_epoch, best_f1_macro, best_rouge_l, description, trained_at)
VALUES
  ('grading',
   'nguyennghia0902/deberta-auto-grading-newfinal',
   'microsoft/deberta-v3-base',
   6, 0.7898, NULL,
   'DeBERTa-v3-base fine-tuned for 3-class grading (INCORRECT/PARTIAL/CORRECT) on unified dataset 28k samples.',
   '2026-05-04 09:53:00'),
  ('feedback',
   'nguyennghia0902/flan-t5-feedback-newfinal',
   'google/flan-t5-base',
   7, NULL, 0.5264,
   'Flan-T5-base fine-tuned for detailed feedback generation. Best ROUGE-L=52.64.',
   '2026-05-04 14:00:00');

-- =============================================================================
-- 3. VIEWS HỮU ÍCH
-- =============================================================================

CREATE OR REPLACE VIEW v_grading_summary AS
SELECT
    q.question_id,
    LEFT(q.question, 60) || '...'       AS question_preview,
    LEFT(a.student_answer, 50) || '...' AS student_preview,
    a.label                             AS true_label,
    gr.predicted_label,
    gr.confidence,
    (a.label = gr.predicted_label)      AS is_correct_prediction,
    gr.graded_at
FROM grading_results gr
JOIN answers  a ON gr.answer_id  = a.id
JOIN questions q ON a.question_id = q.id;

-- SELECT * FROM v_grading_summary;

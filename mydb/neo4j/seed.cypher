CREATE CONSTRAINT IF NOT EXISTS FOR (d:Dataset)  REQUIRE d.name       IS UNIQUE;
CREATE CONSTRAINT IF NOT EXISTS FOR (q:Question) REQUIRE q.question_id IS UNIQUE;
CREATE CONSTRAINT IF NOT EXISTS FOR (m:Model)    REQUIRE m.repo_id     IS UNIQUE;

MERGE (d1:Dataset {name: "SciEntsBank"})
  SET d1.description = "SEMEVAL-2013 science domain",
      d1.total_rows  = 10804,
      d1.domain      = "Earth Science / Biology";

MERGE (d2:Dataset {name: "Mohler"})
  SET d2.description = "Computer Science short answers",
      d2.total_rows  = 7326,
      d2.domain      = "Computer Science";

MERGE (d3:Dataset {name: "LLM_Generated"})
  SET d3.description = "LLM-synthesised QA pairs with feedback",
      d3.total_rows  = 10000,
      d3.domain      = "Mixed";

MERGE (q1:Question {question_id: "SEB-Q001"})
  SET q1.text   = "What is the process by which plants make food using sunlight?",
      q1.domain = "Biology";

MERGE (q2:Question {question_id: "SEB-Q002"})
  SET q2.text   = "Describe the water cycle.",
      q2.domain = "Earth Science";

MERGE (q3:Question {question_id: "MOH-Q001"})
  SET q3.text   = "What is a primary key in a relational database?",
      q3.domain = "Database";

MERGE (q4:Question {question_id: "MOH-Q002"})
  SET q4.text   = "Explain the difference between a stack and a queue.",
      q4.domain = "Data Structures";

MERGE (q5:Question {question_id: "LLM-Q001"})
  SET q5.text   = "What is the difference between supervised and unsupervised learning?",
      q5.domain = "Machine Learning";

MERGE (a1:Answer {answer_id: "A001"})
  SET a1.student_answer   = "Plants use sunlight and CO2 to produce glucose.",
      a1.reference_answer = "Photosynthesis uses sunlight, water, CO2 to produce glucose and oxygen.",
      a1.raw_score        = 0.5,
      a1.true_label       = "PARTIAL";

MERGE (a2:Answer {answer_id: "A002"})
  SET a2.student_answer   = "The water cycle involves evaporation, condensation, and precipitation.",
      a2.reference_answer = "Water evaporates, condenses into clouds, and falls as precipitation.",
      a2.raw_score        = 1.0,
      a2.true_label       = "CORRECT";

MERGE (a3:Answer {answer_id: "A003"})
  SET a3.student_answer   = "A primary key uniquely identifies each row in a table.",
      a3.reference_answer = "A primary key uniquely identifies rows; must be UNIQUE and NOT NULL.",
      a3.raw_score        = 0.5,
      a3.true_label       = "PARTIAL";

MERGE (a4:Answer {answer_id: "A004"})
  SET a4.student_answer   = "A stack is LIFO and a queue is FIFO.",
      a4.reference_answer = "Stack follows LIFO; Queue follows FIFO ordering.",
      a4.raw_score        = 1.0,
      a4.true_label       = "CORRECT";

MERGE (a5:Answer {answer_id: "A005"})
  SET a5.student_answer   = "Supervised learning uses labeled data.",
      a5.reference_answer = "Supervised uses labeled data; unsupervised finds patterns in unlabeled data.",
      a5.raw_score        = 0.0,
      a5.true_label       = "INCORRECT";

MERGE (gr1:GradingResult {result_id: "GR001"})
  SET gr1.predicted_label = "PARTIAL",
      gr1.confidence      = 0.7812,
      gr1.prob_incorrect  = 0.0854,
      gr1.prob_partial    = 0.7812,
      gr1.prob_correct    = 0.1334,
      gr1.pra_used        = false,
      gr1.feedback        = "Partial: mentions sunlight/CO2 but misses water and oxygen.";

MERGE (gr2:GradingResult {result_id: "GR002"})
  SET gr2.predicted_label = "CORRECT",
      gr2.confidence      = 0.9201,
      gr2.prob_incorrect  = 0.0321,
      gr2.prob_partial    = 0.0478,
      gr2.prob_correct    = 0.9201,
      gr2.pra_used        = false,
      gr2.feedback        = "Complete and accurate description of the water cycle.";

MERGE (gr3:GradingResult {result_id: "GR003"})
  SET gr3.predicted_label = "PARTIAL",
      gr3.confidence      = 0.6534,
      gr3.prob_incorrect  = 0.1203,
      gr3.prob_partial    = 0.6534,
      gr3.prob_correct    = 0.2263,
      gr3.pra_used        = false,
      gr3.feedback        = "Core concept correct but NOT NULL constraint not mentioned.";

MERGE (gr4:GradingResult {result_id: "GR004"})
  SET gr4.predicted_label = "CORRECT",
      gr4.confidence      = 0.9580,
      gr4.prob_incorrect  = 0.0201,
      gr4.prob_partial    = 0.0219,
      gr4.prob_correct    = 0.9580,
      gr4.pra_used        = false,
      gr4.feedback        = "Correct identification of LIFO and FIFO.";

MERGE (gr5:GradingResult {result_id: "GR005"})
  SET gr5.predicted_label = "INCORRECT",
      gr5.confidence      = 0.8344,
      gr5.prob_incorrect  = 0.8344,
      gr5.prob_partial    = 0.1101,
      gr5.prob_correct    = 0.0555,
      gr5.pra_used        = false,
      gr5.feedback        = "Only supervised described; unsupervised learning not addressed.";

MERGE (m1:Model {repo_id: "nguyennghia0902/deberta-auto-grading-newfinal"})
  SET m1.base_model    = "microsoft/deberta-v3-base",
      m1.task          = "sequence-classification",
      m1.best_f1_macro = 0.7898,
      m1.best_epoch    = 6,
      m1.num_labels    = 3;

MERGE (m2:Model {repo_id: "nguyennghia0902/flan-t5-feedback-newfinal"})
  SET m2.base_model  = "google/flan-t5-base",
      m2.task        = "text2text-generation",
      m2.best_rougeL = 0.5264,
      m2.best_epoch  = 7;

MATCH (q:Question {question_id:"SEB-Q001"}), (d:Dataset {name:"SciEntsBank"})
  MERGE (q)-[:BELONGS_TO]->(d);
MATCH (q:Question {question_id:"SEB-Q002"}), (d:Dataset {name:"SciEntsBank"})
  MERGE (q)-[:BELONGS_TO]->(d);
MATCH (q:Question {question_id:"MOH-Q001"}), (d:Dataset {name:"Mohler"})
  MERGE (q)-[:BELONGS_TO]->(d);
MATCH (q:Question {question_id:"MOH-Q002"}), (d:Dataset {name:"Mohler"})
  MERGE (q)-[:BELONGS_TO]->(d);
MATCH (q:Question {question_id:"LLM-Q001"}), (d:Dataset {name:"LLM_Generated"})
  MERGE (q)-[:BELONGS_TO]->(d);

MATCH (a:Answer {answer_id:"A001"}), (q:Question {question_id:"SEB-Q001"})
  MERGE (a)-[:ANSWERS]->(q);
MATCH (a:Answer {answer_id:"A002"}), (q:Question {question_id:"SEB-Q002"})
  MERGE (a)-[:ANSWERS]->(q);
MATCH (a:Answer {answer_id:"A003"}), (q:Question {question_id:"MOH-Q001"})
  MERGE (a)-[:ANSWERS]->(q);
MATCH (a:Answer {answer_id:"A004"}), (q:Question {question_id:"MOH-Q002"})
  MERGE (a)-[:ANSWERS]->(q);
MATCH (a:Answer {answer_id:"A005"}), (q:Question {question_id:"LLM-Q001"})
  MERGE (a)-[:ANSWERS]->(q);

MATCH (gr:GradingResult {result_id:"GR001"}), (a:Answer {answer_id:"A001"}), (m:Model {repo_id:"nguyennghia0902/deberta-auto-grading-newfinal"})
  MERGE (gr)-[:GRADES]->(a)
  MERGE (gr)-[:PRODUCED_BY]->(m);
MATCH (gr:GradingResult {result_id:"GR002"}), (a:Answer {answer_id:"A002"}), (m:Model {repo_id:"nguyennghia0902/deberta-auto-grading-newfinal"})
  MERGE (gr)-[:GRADES]->(a)
  MERGE (gr)-[:PRODUCED_BY]->(m);
MATCH (gr:GradingResult {result_id:"GR003"}), (a:Answer {answer_id:"A003"}), (m:Model {repo_id:"nguyennghia0902/deberta-auto-grading-newfinal"})
  MERGE (gr)-[:GRADES]->(a)
  MERGE (gr)-[:PRODUCED_BY]->(m);
MATCH (gr:GradingResult {result_id:"GR004"}), (a:Answer {answer_id:"A004"}), (m:Model {repo_id:"nguyennghia0902/deberta-auto-grading-newfinal"})
  MERGE (gr)-[:GRADES]->(a)
  MERGE (gr)-[:PRODUCED_BY]->(m);
MATCH (gr:GradingResult {result_id:"GR005"}), (a:Answer {answer_id:"A005"}), (m:Model {repo_id:"nguyennghia0902/deberta-auto-grading-newfinal"})
  MERGE (gr)-[:GRADES]->(a)
  MERGE (gr)-[:PRODUCED_BY]->(m);

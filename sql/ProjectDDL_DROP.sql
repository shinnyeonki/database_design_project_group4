DROP TABLE seminar_participation CASCADE CONSTRAINTS;
DROP TABLE seminar CASCADE CONSTRAINTS;
DROP TABLE incentive CASCADE CONSTRAINTS;
-- DROP TABLE customer_evaluation_type CASCADE CONSTRAINTS;
DROP TABLE customer_evaluation CASCADE CONSTRAINTS;
-- DROP TABLE pm_evaluation_type CASCADE CONSTRAINTS;
DROP TABLE pm_evaluation CASCADE CONSTRAINTS;
-- DROP TABLE peer_evaluation_type CASCADE CONSTRAINTS;
DROP TABLE peer_evaluation CASCADE CONSTRAINTS;
DROP TABLE contract CASCADE CONSTRAINTS;
DROP TABLE salary CASCADE CONSTRAINTS;
DROP TABLE department CASCADE CONSTRAINTS;
DROP TABLE participation_project CASCADE CONSTRAINTS;
DROP TABLE project CASCADE CONSTRAINTS;
DROP TABLE customer CASCADE CONSTRAINTS;
DROP TABLE employee CASCADE CONSTRAINTS;

-- CREATE SEQUENCE employee_id_seq START WITH 10000 INCREMENT BY 1;
-- CREATE SEQUENCE customer_id_seq START WITH 10000 INCREMENT BY 1;
-- CREATE SEQUENCE project_id_seq START WITH 10000 INCREMENT BY 1;
-- CREATE SEQUENCE contract_id_seq START WITH 10000 INCREMENT BY 1;
-- CREATE SEQUENCE salary_id_seq START WITH 10000 INCREMENT BY 1;
-- CREATE SEQUENCE peer_evaluation.evaluation_id_seq START WITH 10000 INCREMENT BY 1;
-- CREATE SEQUENCE pm_evaluation.evaluation_id_seq START WITH 10000 INCREMENT BY 1;
-- CREATE SEQUENCE customer_evaluation.evaluation_id_seq START WITH 10000 INCREMENT BY 1;
-- CREATE SEQUENCE seminar_id_seq START WITH 10000 INCREMENT BY 1;
DROP SEQUENCE seminar_id_seq;
DROP SEQUENCE customer_evaluation_id_seq;
DROP SEQUENCE pm_evaluation_id_seq;
DROP SEQUENCE peer_evaluation_id_seq;
DROP SEQUENCE salary_id_seq;
DROP SEQUENCE contract_id_seq;
DROP SEQUENCE project_id_seq;
DROP SEQUENCE customer_id_seq;
DROP SEQUENCE employee_id_seq;

DROP MATERIALIZED VIEW employee_search_mv;
DROP INDEX idx_department_name;
DROP INDEX idx_employee_name;


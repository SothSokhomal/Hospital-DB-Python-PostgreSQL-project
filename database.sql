-- Drop tables in reverse order if they exist (to avoid FK errors during re-run)
DROP TABLE IF EXISTS admission_tbl CASCADE;
DROP TABLE IF EXISTS patient_tbl CASCADE;
DROP TABLE IF EXISTS testResult_tbl CASCADE;
DROP TABLE IF EXISTS medication_tbl CASCADE;
DROP TABLE IF EXISTS medicalCondition_tbl CASCADE;
DROP TABLE IF EXISTS insurance_tbl CASCADE;
DROP TABLE IF EXISTS hospital_tbl CASCADE;
DROP TABLE IF EXISTS doctor_tbl CASCADE;

-- 1. Doctor Table
CREATE TABLE doctor_tbl (
    doctor_id   SERIAL PRIMARY KEY,
    doctor_name VARCHAR(255)
);

-- 2. Hospital Table
CREATE TABLE hospital_tbl (
    hospital_id   SERIAL PRIMARY KEY,
    hospital_name VARCHAR(255)
);

-- 3. Insurance Table
CREATE TABLE insurance_tbl (
    insurance_id   SERIAL PRIMARY KEY,
    provider_name  VARCHAR(255)
);

-- 4. Medical Condition Table
CREATE TABLE medicalCondition_tbl (
    condition_id   SERIAL PRIMARY KEY,
    condition_name VARCHAR(255)
);

-- 5. Medication Table
CREATE TABLE medication_tbl (
    medication_id   SERIAL PRIMARY KEY,
    medication_name VARCHAR(255)
);

-- 6. Test Result Table
CREATE TABLE testResult_tbl (
    test_id   SERIAL PRIMARY KEY,
    test_name VARCHAR(255)
);

-- 7. Patient Table
CREATE TABLE patient_tbl (
    patient_id     SERIAL PRIMARY KEY,
    patient_name   VARCHAR(255),

    condition_id   INTEGER REFERENCES medicalCondition_tbl(condition_id),
    medication_id  INTEGER REFERENCES medication_tbl(medication_id),
    insurance_id   INTEGER REFERENCES insurance_tbl(insurance_id)
);

-- 8. Admission Table
CREATE TABLE admission_tbl (
    admission_id   SERIAL PRIMARY KEY,
    admission_name VARCHAR(255),

    patient_id     INTEGER REFERENCES patient_tbl(patient_id),
    doctor_id      INTEGER REFERENCES doctor_tbl(doctor_id),
    hospital_id    INTEGER REFERENCES hospital_tbl(hospital_id),
    test_id        INTEGER REFERENCES testResult_tbl(test_id)
);

-- SAMPLE DATA (same as yours)
INSERT INTO medicalCondition_tbl (condition_name) VALUES
('Diabetes'), ('Hypertension'), ('Asthma'), ('Heart Disease'), ('Migraine'),
('Arthritis'), ('COVID-19'), ('Pneumonia'), ('Kidney Disease'), ('Flu');

INSERT INTO medication_tbl (medication_name) VALUES
('Metformin'), ('Lisinopril'), ('Albuterol'), ('Aspirin'), ('Ibuprofen'),
('Paracetamol'), ('Remdesivir'), ('Azithromycin'), ('Insulin'), ('Amoxicillin');

INSERT INTO insurance_tbl (provider_name) VALUES
('AIA Insurance'), ('Prudential'), ('Manulife'), ('Allianz'), ('MetLife'),
('Cigna'), ('AXA'), ('Sun Life'), ('Ping An'), ('Tokio Marine');

INSERT INTO doctor_tbl (doctor_name) VALUES
('Dr. Smith'), ('Dr. Johnson'), ('Dr. Lee'), ('Dr. Brown'), ('Dr. Davis'),
('Dr. Wilson'), ('Dr. Taylor'), ('Dr. Clark'), ('Dr. Lewis'), ('Dr. Walker');

INSERT INTO hospital_tbl (hospital_name) VALUES
('Central Hospital'), ('City Medical Center'), ('Sunrise Hospital'),
('Green Valley Clinic'), ('Royal Care Hospital'), ('Hope Medical Center'),
('LifeCare Hospital'), ('Community Health Center'), ('Global Medical Hospital'),
('Saint Mary Hospital');

INSERT INTO testResult_tbl (test_name) VALUES
('Blood Test'), ('X-Ray'), ('MRI Scan'), ('CT Scan'), ('Ultrasound'),
('ECG'), ('Urine Test'), ('COVID Test'), ('Allergy Test'), ('Cholesterol Test');

INSERT INTO patient_tbl (patient_name, condition_id, medication_id, insurance_id) VALUES
('John Doe',    1,1,1), ('Jane Smith',   2,2,2), ('Michael Brown', 3,3,3),
('Emily Davis', 4,4,4), ('David Wilson', 5,5,5), ('Sarah Taylor',  6,6,6),
('Daniel Lee',  7,7,7), ('Olivia Clark', 8,8,8), ('James Lewis',   9,9,9),
('Sophia Walker',10,10,10);

INSERT INTO admission_tbl (admission_name, patient_id, doctor_id, hospital_id, test_id) VALUES
('Emergency Admission',1,1,1,1), ('Routine Checkup',   2,2,2,2),
('Asthma Treatment',   3,3,3,3), ('Heart Surgery',     4,4,4,4),
('Migraine Treatment', 5,5,5,5), ('Joint Pain Therapy',6,6,6,6),
('COVID Treatment',    7,7,7,7), ('Pneumonia Care',    8,8,8,8),
('Kidney Dialysis',    9,9,9,9), ('Flu Treatment',    10,10,10,10);

-- Optional: verify
SELECT count(*) FROM admission_tbl;
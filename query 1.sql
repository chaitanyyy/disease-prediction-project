CREATE DATABASE IF NOT EXISTS disease_prediction;
USE disease_prediction;

-- Heart Disease table
CREATE TABLE heart_disease (
    age INT, sex INT, cp INT,
    trestbps INT, chol INT, fbs INT,
    restecg INT, thalach INT, exang INT,
    oldpeak DECIMAL(4,2), slope INT,
    ca INT, thal INT, target INT
);

-- Diabetes table
CREATE TABLE diabetes (    
    pregnancies INT, glucose INT,
    blood_pressure INT, skin_thickness INT,
    insulin INT, bmi DECIMAL(5,2),
    diabetes_pedigree DECIMAL(5,3),
    age INT, outcome INT
);

-- Kidney Disease table
CREATE TABLE kidney_disease (
    age DECIMAL(5,1), bp DECIMAL(5,1),
    sg DECIMAL(5,3), al DECIMAL(5,1),
    su DECIMAL(5,1), rbc VARCHAR(10),
    pc VARCHAR(10), pcc VARCHAR(10),
    ba VARCHAR(10), bgr DECIMAL(6,1),
    bu DECIMAL(6,1), sc DECIMAL(5,2),
    sod DECIMAL(6,1), pot DECIMAL(5,2),
    hemo DECIMAL(5,1), pcv VARCHAR(10),
    wbcc VARCHAR(10), rbcc VARCHAR(10),
    htn VARCHAR(10), dm VARCHAR(10),
    cad VARCHAR(10), appet VARCHAR(10),
    pe VARCHAR(10), ane VARCHAR(10),
    classification VARCHAR(10)
);

-- Liver Disease table
CREATE TABLE liver_disease (
    age INT, gender VARCHAR(10),
    total_bilirubin DECIMAL(6,2),
    direct_bilirubin DECIMAL(6,2),
    alkaline_phosphotase INT,
    alamine_aminotransferase INT,
    aspartate_aminotransferase INT,
    total_proteins DECIMAL(5,2),
    albumin DECIMAL(5,2),
    albumin_globulin_ratio DECIMAL(5,2),
    dataset INT
);

-- Parkinsons table
CREATE TABLE parkinsons (
    mdvp_fo DECIMAL(8,3),
    mdvp_fhi DECIMAL(8,3),
    mdvp_flo DECIMAL(8,3),
    mdvp_jitter DECIMAL(8,5),
    mdvp_shimmer DECIMAL(8,5),
    nhr DECIMAL(8,5),
    hnr DECIMAL(8,3),
    rpde DECIMAL(8,6),
    dfa DECIMAL(8,6),
    spread1 DECIMAL(10,6),
    spread2 DECIMAL(8,6),
    d2 DECIMAL(8,6),
    ppe DECIMAL(8,6),
    status INT
);

-- Model Results table
CREATE TABLE model_results (
    disease_name VARCHAR(50),
    model_name VARCHAR(50),
    accuracy DECIMAL(5,2),
    precision_score DECIMAL(5,2),
    recall_score DECIMAL(5,2),
    f1_score DECIMAL(5,2),
    roc_auc DECIMAL(5,2)
);
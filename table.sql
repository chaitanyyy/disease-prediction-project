USE disease_prediction;

SELECT 'heart_disease'    AS table_name, COUNT(*) AS total FROM heart_disease
UNION ALL SELECT 'diabetes',             COUNT(*) FROM diabetes
UNION ALL SELECT 'kidney_disease',       COUNT(*) FROM kidney_disease
UNION ALL SELECT 'liver_disease',        COUNT(*) FROM liver_disease
UNION ALL SELECT 'parkinsons',           COUNT(*) FROM parkinsons;
-- Query 3: Diabetes Risk by Glucose
SELECT
    CASE
        WHEN glucose < 100 THEN 'Normal'
        WHEN glucose < 126 THEN 'Pre-diabetic'
        ELSE 'Diabetic Range'
    END AS glucose_category,
    COUNT(*) AS total,
    SUM(outcome) AS diabetic_count,
    ROUND(100.0*SUM(outcome)/COUNT(*),1) AS diabetic_pct,
    ROUND(AVG(bmi),1) AS avg_bmi,
    ROUND(AVG(age),1) AS avg_age
FROM diabetes
GROUP BY glucose_category;
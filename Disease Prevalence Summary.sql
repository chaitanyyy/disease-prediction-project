-- Query 4: Disease Prevalence Summary
SELECT 'Heart Disease' AS disease,
    COUNT(*) AS total,
    SUM(target) AS positive_cases,
    ROUND(100.0*SUM(target)/COUNT(*),1) AS prevalence_pct
FROM heart_disease
UNION ALL
SELECT 'Diabetes', COUNT(*), SUM(outcome),
    ROUND(100.0*SUM(outcome)/COUNT(*),1)
FROM diabetes
UNION ALL
SELECT "Parkinson's", COUNT(*), SUM(status),
    ROUND(100.0*SUM(status)/COUNT(*),1)
FROM parkinsons
UNION ALL
SELECT 'Liver Disease', COUNT(*),
    SUM(CASE WHEN dataset=1 THEN 1 ELSE 0 END),
    ROUND(100.0*SUM(CASE WHEN dataset=1
    THEN 1 ELSE 0 END)/COUNT(*),1)
FROM liver_disease;
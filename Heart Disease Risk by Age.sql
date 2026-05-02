-- Query 2: Heart Disease Risk by Age
SELECT
    CASE
        WHEN age < 40 THEN 'Under 40'
        WHEN age < 50 THEN '40-50'
        WHEN age < 60 THEN '50-60'
        ELSE 'Over 60'
    END AS age_group,
    COUNT(*) AS total,
    SUM(target) AS disease_count,
    ROUND(100.0 * SUM(target)/COUNT(*),1) AS risk_pct
FROM heart_disease
GROUP BY age_group
ORDER BY risk_pct DESC;
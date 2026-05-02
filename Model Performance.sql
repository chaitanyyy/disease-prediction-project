USE disease_prediction;

-- Query 1: Model Performance
SELECT disease_name, model_name,
       accuracy, f1_score, roc_auc
FROM model_results
ORDER BY disease_name, accuracy DESC;
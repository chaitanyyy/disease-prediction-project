# 🏥 Multi-Disease Prediction System
> Machine Learning models predicting 5 diseases 
> with up to 100% accuracy using real patient data.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.8-green)
![Tableau](https://img.shields.io/badge/Tableau-Public-yellow)

---

## 📌 Business Problem
Healthcare providers need fast, accurate tools to 
predict disease risk from patient data — reducing 
misdiagnosis and enabling early intervention.

---

## 💡 Solution
Built an end-to-end ML pipeline covering:
- Data cleaning & EDA for 5 disease datasets
- 10 ML models trained & evaluated
- SQL analysis for risk factor identification
- Interactive Tableau dashboard for insights

---

## 🎯 Diseases Covered

| Disease | Dataset Size | Best Model | Accuracy | F1 Score |
|---|---|---|---|---|
| Heart Disease | 303 | Random Forest | 98.54% | 98.52% |
| Diabetes | 768 | Random Forest | 75.32% | 66.07% |
| Kidney Disease | 400 | Random Forest | 100.0% | 100.0% |
| Liver Disease | 583 | Random Forest | 74.36% | 83.33% |
| Parkinson's | 195 | Random Forest | 94.87% | 96.97% |

---

## 🔍 Key Findings

### Heart Disease
- Under-40 age group has HIGHEST risk (73.7%)!
- Over-60 group has lower risk (39.2%) than expected
- Random Forest achieved 98.54% accuracy

### Diabetes
- Diabetic-range glucose → 59.3% diabetes probability
- Pre-diabetic group → 28% already diabetic
- Normal glucose → only 7.3% diabetic

### Disease Prevalence
- Parkinson's → 75.4% positive in dataset
- Liver Disease → 71% positive
- Heart Disease → 51.3% positive
- Diabetes → 34.9% positive

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.13 | Data processing & ML |
| Pandas | Data cleaning (2,249 records) |
| NumPy | Numerical operations |
| Scikit-learn | ML models (RF, GB, LR, SVM) |
| Matplotlib | EDA visualizations |
| Seaborn | Statistical plots |
| SQLAlchemy | Python ↔ MySQL connection |
| MySQL | Store & query patient data |
| Tableau Public | Interactive dashboard |

---

## 📁 Project Structure

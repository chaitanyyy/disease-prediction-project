# python/train_models.py
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score, roc_auc_score)
from sklearn.preprocessing import LabelEncoder, StandardScaler
import warnings
warnings.filterwarnings('ignore')

MYSQL_PASSWORD = "chaitany41"
BASE = r'C:\Users\Mane Chaitanya\Desktop\disease-prediction-project\data\processed'

engine = create_engine(
    f'mysql+pymysql://root:{MYSQL_PASSWORD}@localhost:3306/disease_prediction'
)

results = []

def evaluate_model(name, disease, y_test, y_pred, y_prob=None):
    acc  = round(accuracy_score(y_test, y_pred) * 100, 2)
    prec = round(precision_score(y_test, y_pred,
                 zero_division=0) * 100, 2)
    rec  = round(recall_score(y_test, y_pred,
                 zero_division=0) * 100, 2)
    f1   = round(f1_score(y_test, y_pred,
                 zero_division=0) * 100, 2)
    auc  = round(roc_auc_score(y_test, y_prob
                 if y_prob is not None else y_pred) * 100, 2)

    print(f"   {name:30} Acc:{acc}% | F1:{f1}% | AUC:{auc}%")
    results.append({
        'disease_name': disease,
        'model_name': name,
        'accuracy': acc,
        'precision_score': prec,
        'recall_score': rec,
        'f1_score': f1,
        'roc_auc': auc
    })
    return acc

print("="*60)
print("TRAINING ML MODELS FOR ALL 5 DISEASES")
print("="*60)

# ── 1. HEART DISEASE ──
print("\n1️⃣  Heart Disease Models...")
heart = pd.read_csv(f'{BASE}\\heart_clean.csv')
X = heart.drop('target', axis=1)
y = heart['target']
X_train,X_test,y_train,y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

for model, name in [
    (RandomForestClassifier(n_estimators=100, random_state=42),
     'Random Forest'),
    (GradientBoostingClassifier(random_state=42),
     'Gradient Boosting'),
    (LogisticRegression(max_iter=1000), 'Logistic Regression')
]:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:,1]
    evaluate_model(name, 'Heart Disease', y_test, y_pred, y_prob)

# ── 2. DIABETES ──
print("\n2️⃣  Diabetes Models...")
diab = pd.read_csv(f'{BASE}\\diabetes_clean.csv')
X = diab.drop('outcome', axis=1)
y = diab['outcome']
X_train,X_test,y_train,y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc  = scaler.transform(X_test)

for model, name, Xtr, Xte in [
    (RandomForestClassifier(n_estimators=100, random_state=42),
     'Random Forest', X_train, X_test),
    (GradientBoostingClassifier(random_state=42),
     'Gradient Boosting', X_train, X_test),
    (SVC(probability=True, random_state=42),
     'SVM', X_train_sc, X_test_sc)
]:
    model.fit(Xtr, y_train)
    y_pred = model.predict(Xte)
    y_prob = model.predict_proba(Xte)[:,1]
    evaluate_model(name, 'Diabetes', y_test, y_pred, y_prob)

# ── 3. KIDNEY DISEASE ──
print("\n3️⃣  Kidney Disease Models...")
kidney = pd.read_csv(f'{BASE}\\kidney_clean.csv')

# Encode categoricals
le = LabelEncoder()
for col in kidney.select_dtypes(include='object').columns:
    kidney[col] = le.fit_transform(
        kidney[col].astype(str)
    )

X = kidney.drop('classification', axis=1)
y = kidney['classification']
X_train,X_test,y_train,y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

for model, name in [
    (RandomForestClassifier(n_estimators=100, random_state=42),
     'Random Forest'),
    (GradientBoostingClassifier(random_state=42),
     'Gradient Boosting')
]:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    evaluate_model(name, 'Kidney Disease',
                   y_test, y_pred)

# ── 4. LIVER DISEASE ──
print("\n4️⃣  Liver Disease Models...")
liver = pd.read_csv(f'{BASE}\\liver_clean.csv')
liver['gender'] = le.fit_transform(liver['gender'])
liver['target'] = (liver['dataset'] == 1).astype(int)
liver = liver.drop('dataset', axis=1)

X = liver.drop('target', axis=1)
y = liver['target']
X_train,X_test,y_train,y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

for model, name in [
    (RandomForestClassifier(n_estimators=100, random_state=42),
     'Random Forest'),
    (GradientBoostingClassifier(random_state=42),
     'Gradient Boosting')
]:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:,1]
    evaluate_model(name, 'Liver Disease',
                   y_test, y_pred, y_prob)

# ── 5. PARKINSONS ──
print("\n5️⃣  Parkinson's Disease Models...")
park = pd.read_csv(f'{BASE}\\parkinsons_clean.csv')

X = park.drop('status', axis=1)
y = park['status']
X_train,X_test,y_train,y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

for model, name in [
    (RandomForestClassifier(n_estimators=100, random_state=42),
     'Random Forest'),
    (GradientBoostingClassifier(random_state=42),
     'Gradient Boosting')
]:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:,1]
    evaluate_model(name, "Parkinson's",
                   y_test, y_pred, y_prob)

# ── SAVE RESULTS ──
print("\n📊 Saving model results...")
results_df = pd.DataFrame(results)
results_df.to_sql('model_results', engine,
                  if_exists='replace', index=False)
results_df.to_csv(f'{BASE}\\model_results.csv', index=False)

print("\n" + "="*60)
print("🎉 ALL MODELS TRAINED!")
print("="*60)
print("\nBest Models per Disease:")
best = results_df.loc[
    results_df.groupby('disease_name')['accuracy'].idxmax()
][['disease_name','model_name','accuracy','f1_score']]
print(best.to_string(index=False))
# python/eda_load.py
# EDA Analysis + Load all 5 datasets into MySQL

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import warnings
warnings.filterwarnings('ignore')

MYSQL_PASSWORD = "chaitany41"
BASE_RAW  = r'C:\Users\Mane Chaitanya\Desktop\disease-prediction-project\data\raw'
BASE_PROC = r'C:\Users\Mane Chaitanya\Desktop\disease-prediction-project\data\processed'

engine = create_engine(
    f'mysql+pymysql://root:{MYSQL_PASSWORD}@localhost:3306/disease_prediction'
)

print("="*60)
print("LOADING & EDA FOR ALL 5 DISEASES")
print("="*60)

# ════════════════════════════════
# 1. HEART DISEASE
# ════════════════════════════════
print("\n1️⃣  Heart Disease Dataset...")
heart = pd.read_csv(f'{BASE_RAW}\\heart.csv')
print(f"   Shape: {heart.shape}")
print(f"   Missing: {heart.isnull().sum().sum()}")
print(f"   Disease %: {heart['target'].value_counts(normalize=True).round(2).to_dict()}")

# Clean
heart = heart.dropna()
heart.to_sql('heart_disease', engine,
             if_exists='replace', index=False)
heart.to_csv(f'{BASE_PROC}\\heart_clean.csv', index=False)
print(f"   ✅ Loaded {len(heart)} rows")

# ════════════════════════════════
# 2. DIABETES
# ════════════════════════════════
print("\n2️⃣  Diabetes Dataset...")
diabetes = pd.read_csv(f'{BASE_RAW}\\diabetes.csv')
print(f"   Shape: {diabetes.shape}")
print(f"   Missing: {diabetes.isnull().sum().sum()}")
print(f"   Diabetic %: {diabetes['Outcome'].value_counts(normalize=True).round(2).to_dict()}")

# Replace 0s with median (0 glucose/BP is impossible)
cols_to_fix = ['Glucose','BloodPressure','SkinThickness',
               'Insulin','BMI']
for col in cols_to_fix:
    diabetes[col] = diabetes[col].replace(
        0, diabetes[col].median()
    )

diabetes.columns = [
    'pregnancies','glucose','blood_pressure',
    'skin_thickness','insulin','bmi',
    'diabetes_pedigree','age','outcome'
]
diabetes.to_sql('diabetes', engine,
                if_exists='replace', index=False)
diabetes.to_csv(f'{BASE_PROC}\\diabetes_clean.csv', index=False)
print(f"   ✅ Loaded {len(diabetes)} rows")

# ════════════════════════════════
# 3. KIDNEY DISEASE
# ════════════════════════════════
print("\n3️⃣  Kidney Disease Dataset...")
kidney = pd.read_csv(f'{BASE_RAW}\\kidney.csv')
print(f"   Shape: {kidney.shape}")

# Clean
kidney.columns = [col.strip() for col in kidney.columns]
kidney = kidney.replace('?', np.nan)
kidney = kidney.replace('\t', '', regex=True)

# Fill numeric nulls with median
num_cols = kidney.select_dtypes(include=[np.number]).columns
kidney[num_cols] = kidney[num_cols].fillna(
    kidney[num_cols].median()
)
# Fill categorical nulls with mode
cat_cols = kidney.select_dtypes(include=['object']).columns
for col in cat_cols:
    kidney[col] = kidney[col].fillna(
        kidney[col].mode()[0]
    )

# Encode target
kidney['classification'] = kidney['classification'].str.strip()
kidney.to_sql('kidney_disease', engine,
              if_exists='replace', index=False)
kidney.to_csv(f'{BASE_PROC}\\kidney_clean.csv', index=False)
print(f"   ✅ Loaded {len(kidney)} rows")

# ════════════════════════════════
# 4. LIVER DISEASE
# ════════════════════════════════
print("\n4️⃣  Liver Disease Dataset...")
liver = pd.read_csv(f'{BASE_RAW}\\liver.csv')
print(f"   Shape: {liver.shape}")

liver.columns = [
    'age','gender','total_bilirubin','direct_bilirubin',
    'alkaline_phosphotase','alamine_aminotransferase',
    'aspartate_aminotransferase','total_proteins',
    'albumin','albumin_globulin_ratio','dataset'
]
liver['albumin_globulin_ratio'] = liver[
    'albumin_globulin_ratio'
].fillna(liver['albumin_globulin_ratio'].median())

liver.to_sql('liver_disease', engine,
             if_exists='replace', index=False)
liver.to_csv(f'{BASE_PROC}\\liver_clean.csv', index=False)
print(f"   ✅ Loaded {len(liver)} rows")

# ════════════════════════════════
# 5. PARKINSONS
# ════════════════════════════════
print("\n5️⃣  Parkinson's Dataset...")
park = pd.read_csv(f'{BASE_RAW}\\parkinsons.csv')
print(f"   Shape: {park.shape}")

# Drop name column if exists
if 'name' in park.columns:
    park = park.drop('name', axis=1)

park.to_sql('parkinsons', engine,
            if_exists='replace', index=False)
park.to_csv(f'{BASE_PROC}\\parkinsons_clean.csv', index=False)
print(f"   ✅ Loaded {len(park)} rows")

# ════════════════════════════════
# EDA VISUALIZATIONS
# ════════════════════════════════
print("\n📊 Generating EDA charts...")

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Disease Distribution Across All Datasets',
             fontsize=16, fontweight='bold')

# Heart
axes[0,0].bar(['No Disease','Disease'],
    heart['target'].value_counts().values,
    color=['#2ecc71','#e74c3c'])
axes[0,0].set_title('Heart Disease')
axes[0,0].set_ylabel('Count')

# Diabetes
axes[0,1].bar(['No Diabetes','Diabetes'],
    diabetes['outcome'].value_counts().values,
    color=['#2ecc71','#e74c3c'])
axes[0,1].set_title('Diabetes')

# Kidney
kidney_counts = kidney['classification'].value_counts()
axes[0,2].bar(kidney_counts.index,
    kidney_counts.values,
    color=['#2ecc71','#e74c3c'])
axes[0,2].set_title('Kidney Disease')

# Liver
axes[1,0].bar(['Liver Disease','No Disease'],
    liver['dataset'].value_counts().values,
    color=['#e74c3c','#2ecc71'])
axes[1,0].set_title('Liver Disease')

# Parkinsons
axes[1,1].bar(['Parkinson\'s','Healthy'],
    park['status'].value_counts().values,
    color=['#e74c3c','#2ecc71'])
axes[1,1].set_title("Parkinson's Disease")

# Summary
diseases    = ['Heart','Diabetes','Kidney','Liver',"Parkinson's"]
total_rows  = [len(heart), len(diabetes),
               len(kidney), len(liver), len(park)]
axes[1,2].bar(diseases, total_rows, color='#3498db')
axes[1,2].set_title('Dataset Sizes')
axes[1,2].set_ylabel('Records')

plt.tight_layout()
plt.savefig(f'{BASE_PROC}\\eda_overview.png',
            dpi=150, bbox_inches='tight')
plt.show()
print("✅ EDA chart saved!")

print("\n" + "="*60)
print("🎉 ALL 5 DATASETS LOADED & EDA COMPLETE!")
print("="*60)
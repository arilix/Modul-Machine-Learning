# Bab 5 — Contoh Alur Workflow Machine Learning

Mari kita lihat workflow lengkap dari data mentah sampai prediksi!

## Studi Kasus: Prediksi Harga Rumah

**Problem**: Memprediksi harga rumah berdasarkan luas, lokasi, dan jumlah kamar.

## Step-by-Step Workflow

### Step 1: Import Libraries

```python
# Data manipulation
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Models
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
import xgboost as xgb

# Evaluation
from sklearn.metrics import mean_squared_error, r2_score
```

### Step 2: Load dan Explore Data

```python
# Load data
df = pd.read_csv('house_data.csv')

# Lihat struktur data
print(df.head())
print(df.info())
print(df.describe())

# Lihat missing values
print(df.isnull().sum())

# Visualisasi
df['harga'].hist(bins=50)
plt.xlabel('Harga (juta)')
plt.ylabel('Frekuensi')
plt.title('Distribusi Harga Rumah')
plt.show()
```

### Step 3: Data Cleaning

```python
# Hapus duplikasi
df = df.drop_duplicates()

# Hapus outlier (harga terlalu ekstrem)
Q1 = df['harga'].quantile(0.25)
Q3 = df['harga'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['harga'] >= Q1 - 1.5*IQR) & (df['harga'] <= Q3 + 1.5*IQR)]

# Perbaiki inkonsistensi
df['lokasi'] = df['lokasi'].str.lower().str.strip()
```

### Step 4: Handle Missing Values

```python
# Strategi per kolom
df['luas'].fillna(df['luas'].median(), inplace=True)
df['kamar'].fillna(df['kamar'].mode()[0], inplace=True)
df['lokasi'].fillna('unknown', inplace=True)

# Atau hapus jika terlalu banyak missing
# df = df.dropna()
```

### Step 5: Feature Engineering

```python
# Buat fitur baru
df['luas_per_kamar'] = df['luas'] / df['kamar']
df['is_jakarta'] = (df['lokasi'] == 'jakarta').astype(int)

# Encoding kategorikal
df_encoded = pd.get_dummies(df, columns=['lokasi'], drop_first=True)
```

### Step 6: Split Data

```python
# Pisahkan fitur dan target
X = df_encoded.drop(['id', 'harga'], axis=1)
y = df_encoded['harga']

# Split 80-20
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training: {len(X_train)} samples")
print(f"Testing: {len(X_test)} samples")
```

### Step 7: Scaling (jika perlu)

```python
# Untuk model yang butuh scaling (SVM, Neural Net, KNN)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Untuk tree-based models (Random Forest, XGBoost) → SKIP scaling
```

### Step 8: Training Models

```python
# Model 1: Linear Regression (Baseline)
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)

# Model 2: Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

# Model 3: XGBoost
xgb_model = xgb.XGBRegressor(n_estimators=100, random_state=42)
xgb_model.fit(X_train, y_train)
xgb_pred = xgb_model.predict(X_test)
```

### Step 9: Evaluation

```python
# Fungsi evaluasi
def evaluate_model(y_true, y_pred, model_name):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    print(f"{model_name}:")
    print(f"  RMSE: {rmse:.2f}")
    print(f"  R²: {r2:.4f}")
    print()

# Evaluasi semua model
evaluate_model(y_test, lr_pred, "Linear Regression")
evaluate_model(y_test, rf_pred, "Random Forest")
evaluate_model(y_test, xgb_pred, "XGBoost")
```

**Output Example**:
```
Linear Regression:
  RMSE: 250.45
  R²: 0.7823

Random Forest:
  RMSE: 180.32
  R²: 0.8756

XGBoost:
  RMSE: 165.78
  R²: 0.8912
```

### Step 10: Hyperparameter Tuning

Setelah tahu model mana yang terbaik (XGBoost di contoh ini), kita tuning hyperparameternya untuk hasil optimal.

#### **Metode 1: Manual Tuning**

```python
# Coba berbagai kombinasi manual
params_to_try = [
    {'n_estimators': 50, 'max_depth': 3, 'learning_rate': 0.1},
    {'n_estimators': 100, 'max_depth': 5, 'learning_rate': 0.1},
    {'n_estimators': 200, 'max_depth': 7, 'learning_rate': 0.05},
]

best_score = 0
best_params = None

for params in params_to_try:
    model = xgb.XGBRegressor(**params, random_state=42)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    r2 = r2_score(y_test, pred)
    
    print(f"Params: {params} → R²: {r2:.4f}")
    
    if r2 > best_score:
        best_score = r2
        best_params = params

print(f"\nBest params: {best_params}")
print(f"Best R²: {best_score:.4f}")
```

#### **Metode 2: Grid Search (Recommended)**

```python
from sklearn.model_selection import GridSearchCV

# Define parameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.05, 0.1],
    'subsample': [0.8, 1.0]
}

# GridSearchCV
grid_search = GridSearchCV(
    estimator=xgb.XGBRegressor(random_state=42),
    param_grid=param_grid,
    cv=5,  # 5-fold cross-validation
    scoring='r2',  # Metric to optimize
    n_jobs=-1,  # Use all CPU cores
    verbose=1  # Show progress
)

# Fit (akan coba 3×3×3×2×5 = 270 kombinasi!)
print("Starting Grid Search...")
grid_search.fit(X_train, y_train)

print("\n" + "="*60)
print("BEST PARAMETERS FOUND:")
print("="*60)
print(grid_search.best_params_)
print(f"\nBest Cross-Validation R²: {grid_search.best_score_:.4f}")

# Get best model
best_model = grid_search.best_estimator_

# Evaluate on test set
best_pred = best_model.predict(X_test)
test_r2 = r2_score(y_test, best_pred)
test_rmse = np.sqrt(mean_squared_error(y_test, best_pred))

print(f"\nTest Set Performance:")
print(f"  R²: {test_r2:.4f}")
print(f"  RMSE: {test_rmse:.2f}")
```

**Output Example:**
```
Fitting 5 folds for each of 54 candidates, totalling 270 fits
========================================================
BEST PARAMETERS FOUND:
========================================================
{'learning_rate': 0.05, 'max_depth': 5, 'n_estimators': 200, 'subsample': 1.0}

Best Cross-Validation R²: 0.8945

Test Set Performance:
  R²: 0.9012
  RMSE: 152.34
```

#### **Metode 3: Random Search (Alternatif Lebih Cepat)**

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

# Define parameter distribution
param_dist = {
    'n_estimators': randint(50, 500),  # Random integer dari 50-500
    'max_depth': randint(3, 15),
    'learning_rate': uniform(0.01, 0.2),  # Random float dari 0.01-0.21
    'subsample': uniform(0.6, 0.4),  # Random float dari 0.6-1.0
    'colsample_bytree': uniform(0.6, 0.4)
}

# RandomizedSearchCV
random_search = RandomizedSearchCV(
    estimator=xgb.XGBRegressor(random_state=42),
    param_distributions=param_dist,
    n_iter=50,  # Coba 50 kombinasi random (jauh lebih cepat!)
    cv=5,
    scoring='r2',
    n_jobs=-1,
    random_state=42,
    verbose=1
)

print("Starting Random Search...")
random_search.fit(X_train, y_train)

print(f"\nBest params: {random_search.best_params_}")
print(f"Best CV R²: {random_search.best_score_:.4f}")
```

#### **Interpretasi Hasil Tuning**

```python
# Lihat top 5 kombinasi terbaik
results_df = pd.DataFrame(grid_search.cv_results_)
top_5 = results_df.nsmallest(5, 'rank_test_score')[
    ['params', 'mean_test_score', 'std_test_score']
]

print("\nTop 5 Best Parameter Combinations:")
print(top_5)
```

**Output:**
```
Top 5 Best Parameter Combinations:
                                           params  mean_test_score  std_test_score
42  {'learning_rate': 0.05, 'max_depth': 5,...        0.8945          0.0123
15  {'learning_rate': 0.1, 'max_depth': 5, ...        0.8932          0.0145
38  {'learning_rate': 0.05, 'max_depth': 7,...        0.8921          0.0156
...
```

**💡 Insight:**
- Jika mean_test_score mirip (±0.01), pilih yang **lebih simple** (n_estimators kecil)
- Jika std_test_score tinggi (>0.05), model **kurang stabil** → coba parameter lain
- Jika CV score >> test score → **overfitting** → regularisasi lebih kuat

#### **Comparison: Before vs After Tuning**

```python
# Summary comparison
comparison = pd.DataFrame({
    'Stage': ['Baseline (default)', 'After Tuning'],
    'R²': [0.8912, 0.9012],
    'RMSE': [165.78, 152.34],
    'Parameters': [
        "n_estimators=100, max_depth=None, lr=0.3",
        "n_estimators=200, max_depth=5, lr=0.05"
    ]
})

print("\n" + "="*80)
print("IMPACT OF HYPERPARAMETER TUNING")
print("="*80)
print(comparison.to_string(index=False))

improvement = ((0.9012 - 0.8912) / 0.8912) * 100
print(f"\nR² Improvement: +{improvement:.2f}%")
```

### Step 11: Cross-Validation untuk Cek Stabilitas

```python
from sklearn.model_selection import cross_val_score

# Cross-validation dengan best model
cv_scores = cross_val_score(
    best_model, 
    X_train, 
    y_train, 
    cv=5,  # 5-fold
    scoring='r2'
)

print("\nCross-Validation Scores:")
print(f"Scores: {cv_scores}")
print(f"Mean: {cv_scores.mean():.4f}")
print(f"Std: {cv_scores.std():.4f}")

# Interpretasi
if cv_scores.std() < 0.05:
    print("✅ Model STABIL (std < 0.05)")
elif cv_scores.std() < 0.1:
    print("⚠️ Model CUKUP STABIL (std < 0.1)")
else:
    print("❌ Model KURANG STABIL (std > 0.1) - perlu lebih banyak data")
```

### Step 12: Prediksi Data Baru

```python
# Data rumah baru
new_house = pd.DataFrame({
    'luas': [150],
    'kamar': [3],
    'lokasi_bandung': [0],
    'lokasi_jakarta': [1],
    'lokasi_surabaya': [0],
    'luas_per_kamar': [50],
    'is_jakarta': [1]
})

# Prediksi dengan best model (setelah tuning)
predicted_price = best_model.predict(new_house)
print(f"Prediksi harga: Rp {predicted_price[0]:.2f} juta")

# Prediksi beberapa rumah sekaligus
multiple_houses = pd.DataFrame({
    'luas': [150, 200, 100],
    'kamar': [3, 4, 2],
    'lokasi_bandung': [0, 1, 0],
    'lokasi_jakarta': [1, 0, 1],
    'lokasi_surabaya': [0, 0, 0],
    'luas_per_kamar': [50, 50, 50],
    'is_jakarta': [1, 0, 1]
})

predictions = best_model.predict(multiple_houses)
for i, price in enumerate(predictions):
    print(f"Rumah {i+1}: Rp {price:.2f} juta")
```

### Step 13: Save Model untuk Production

```python
import joblib

# Save best model (hasil tuning)
joblib.dump(best_model, 'house_price_model_tuned.pkl')

# Save scaler juga (jika pakai scaling)
joblib.dump(scaler, 'scaler.pkl')

print("✅ Model saved successfully!")

# Load model (untuk dipakai lain waktu)
loaded_model = joblib.load('house_price_model_tuned.pkl')
loaded_scaler = joblib.load('scaler.pkl')

# Test loaded model
test_pred = loaded_model.predict(new_house)
print(f"Loaded model prediction: Rp {test_pred[0]:.2f} juta")
```

**💡 Production Tips:**

1. **Save metadata bersama model:**
```python
import json

metadata = {
    'model_type': 'XGBoost',
    'best_params': grid_search.best_params_,
    'train_r2': train_r2,
    'test_r2': test_r2,
    'features': list(X.columns),
    'trained_date': '2026-02-26',
    'version': '1.0'
}

with open('model_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)
```

2. **Validate sebelum deploy:**
```python
# Check model performance sama dengan saat training
assert abs(loaded_model.predict(X_test).mean() - best_pred.mean()) < 0.01
print("✅ Model validation passed!")
```

3. **Monitor in production:**
```python
# Log setiap prediksi
def predict_and_log(model, data):
    prediction = model.predict(data)
    
    # Log ke database/file
    log = {
        'timestamp': datetime.now(),
        'input': data.to_dict(),
        'prediction': prediction[0],
        'model_version': '1.0'
    }
    
    # Save log...
    return prediction
```

---

## 📊 Updated Visual Workflow

```
Data Mentah (CSV)
    ↓
[1. Load & Explore] → info(), describe(), visualisasi
    ↓
[2. Data Cleaning] → Hapus duplikat, fix outlier, perbaiki inkonsistensi
    ↓
[3. Handle Missing] → fillna(), dropna(), imputasi
    ↓
[4. Feature Engineering] → Buat fitur baru, encoding, binning
    ↓
[5. Split Data] → Train (80%) | Test (20%)
    ↓
[6. Scaling] → StandardScaler/MinMaxScaler (jika perlu)
    ↓
[7. Training Baseline] → Try 2-3 model dengan default params
    ↓
[8. Evaluation Baseline] → Compare metric (RMSE, R², Accuracy)
    ↓
[9. Pick Best Model] → Pilih model terbaik dari baseline
    ↓
[10. Hyperparameter Tuning] → GridSearchCV/RandomizedSearchCV
    ├─ Define parameter grid
    ├─ Cross-validation (5-fold)
    ├─ Find best parameters
    └─ Get best estimator
    ↓
[11. Cross-Validation] → Cek stabilitas model (5-fold CV)
    ↓
[12. Final Evaluation] → Evaluate best model pada test set (ONLY ONCE!)
    ├─ Calculate metrics
    ├─ Confusion matrix / Residual plot
    └─ Feature importance
    ↓
[13. Prediction] → Prediksi data baru
    ↓
[14. Save Model] → joblib.dump() + metadata
    ↓
[PRODUCTION] → Deploy, monitor, maintain
```

---

## 🎯 Checklist Lengkap Workflow ML

Sebelum deploy model, pastikan sudah:

### Data Quality ✅
- [ ] No missing values (atau sudah di-handle)
- [ ] No duplicates
- [ ] Outliers checked & handled
- [ ] Data types correct
- [ ] Consistent formatting

### Feature Engineering ✅
- [ ] Kategorikal di-encode
- [ ] Fitur numerik di-scale (jika perlu)
- [ ] Fitur baru yang relevan sudah dibuat
- [ ] Feature importance checked

### Model Development ✅
- [ ] Minimal 2-3 model dicoba sebagai baseline
- [ ] Best model dipilih berdasarkan metric yang relevan
- [ ] Hyperparameter tuning dilakukan
- [ ] Cross-validation score stabil (std < 0.1)
- [ ] No overfitting (train score ≈ test score)

### Evaluation ✅
- [ ] Test set evaluation dilakukan (hanya 1x!)
- [ ] Metric sesuai use case (regression: RMSE/R², classification: F1/Recall)
- [ ] Confusion matrix / Residual plot checked
- [ ] Edge cases tested

### Production Ready ✅
- [ ] Model saved dengan joblib/pickle
- [ ] Scaler/encoder saved (jika ada)
- [ ] Metadata saved (params, version, date)
- [ ] Model validated after loading
- [ ] Documentation lengkap
- [ ] Monitoring plan ready

---

## 💡 Common Pitfalls & Solutions

### ❌ **Pitfall 1: Data Leakage**
**Problem**: Informasi dari test set bocor ke training.

**Contoh Salah:**
```python
# SALAH! Scaling dilakukan sebelum split
X_scaled = scaler.fit_transform(X)  # Fit pakai ALL data!
X_train, X_test = train_test_split(X_scaled, ...)
```

**Solusi:**
```python
# BENAR! Fit scaler hanya di training set
X_train, X_test = train_test_split(X, ...)
scaler.fit(X_train)  # Fit hanya training
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Transform pakai parameter dari training
```

### ❌ **Pitfall 2: Overfitting di Hyperparameter Tuning**
**Problem**: Model too good to be true di validation, jelek di test.

**Solusi:**
```python
# Gunakan cross-validation, bukan single validation set
# Train-Val-Test split: 60-20-20

# 1. Tune di Train+Val dengan CV
# 2. Final evaluate di Test (ONLY ONCE!)
# 3. Jika Test score jauh < CV score → over-tuned!
```

### ❌ **Pitfall 3: Memilih Model Berdasarkan Test Set**
**Problem**: Coba banyak model, pilih yang terbaik di test set = overfitting test set!

**Solusi:**
```python
# BENAR: Pilih model berdasarkan CV score
# Test set HANYA untuk final evaluation (1x saja!)

# 1. Baseline models → evaluate dengan CV
# 2. Pick best model
# 3. Tune hyperparameter → evaluate dengan CV
# 4. Final test → evaluate di test set (1x)
```

### ❌ **Pitfall 4: Tidak Cek Feature Importance**
**Problem**: Model pakai fitur yang tidak masuk akal atau bocor info.

**Solusi:**
```python
# Selalu cek feature importance
importances = best_model.feature_importances_
feature_imp = pd.DataFrame({
    'feature': X.columns,
    'importance': importances
}).sort_values('importance', ascending=False)

print(feature_imp)

# Jika ada fitur aneh dengan importance tinggi → investigate!
```

---

---

## 🔄 Pipeline Sederhana (Otomatis)

Sklearn punya fitur Pipeline yang mempermudah workflow dan **mencegah data leakage**:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

# Buat pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # Step 1: Scaling
    ('model', RandomForestRegressor())  # Step 2: Model
])

# Training (scaling otomatis!)
pipeline.fit(X_train, y_train)

# Prediksi (scaling otomatis!)
predictions = pipeline.predict(X_test)

# Save pipeline (include scaling!)
joblib.dump(pipeline, 'pipeline_model.pkl')

# Hyperparameter tuning dengan Pipeline
param_grid = {
    'model__n_estimators': [50, 100, 200],
    'model__max_depth': [5, 10, 15]
}

grid = GridSearchCV(pipeline, param_grid, cv=5)
grid.fit(X_train, y_train)
best_pipeline = grid.best_estimator_
```

**Keuntungan Pipeline:**
- ✅ Scaling otomatis (tidak perlu manual)
- ✅ Mencegah data leakage (fit hanya di training)
- ✅ Code lebih clean
- ✅ Easy to deploy (save 1 file aja!)

---

*Modul 2 — Cara Mengolah Data Tabel dengan Machine Learning*

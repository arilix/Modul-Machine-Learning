# Bab 4 — Korelasi Antar Metric

Metric-metric tidak berdiri sendiri! Mari kita pahami hubungan antar metric agar bisa memilih dan menginterpretasi dengan tepat.

---

## 1. Hubungan MAE, MSE, dan RMSE

### Formula Connection

$$MSE = \frac{1}{n}\sum(error)^2$$
$$RMSE = \sqrt{MSE}$$
$$MAE = \frac{1}{n}\sum|error|$$

### Properti Matematika

**Selalu berlaku**: $MAE \leq RMSE$

**Kenapa?**
Karena MSE/RMSE memberikan "penalty lebih besar" untuk error besar (dikuadratkan).

### Contoh Perhitungan

**Data**: Errors = [10, 10, 10, 100]

```
MAE = (10+10+10+100)/4 = 32.5

MSE = (10²+10²+10²+100²)/4 
    = (100+100+100+10000)/4
    = 2575

RMSE = √2575 = 50.7
```

**Observasi**:
- MAE = 32.5 → "Typical error"
- RMSE = 50.7 → Lebih besar karena error 100 sangat di-"hukum"

### Ratio RMSE/MAE

Ratio ini memberitahu **seberapa banyak variasi dalam error**:

| RMSE/MAE | Interpretasi |
|----------|--------------|
| **≈ 1** | Error konsisten (sedikit outlier) |
| **1-1.5** | Normal distribution error |
| **> 1.5** | Banyak outlier / error bervariasi |

**Contoh**:

**Case 1 - Konsisten**:
```
Errors: [10, 11, 9, 10]
MAE = 10
RMSE = 10.05
Ratio = 1.005 ← Sangat konsisten!
```

**Case 2 - Banyak Outlier**:
```
Errors: [10, 10, 10, 100]
MAE = 32.5
RMSE = 50.7
Ratio = 1.56 ← Ada outlier besar!
```

### Kapan Pakai Mana?

**Gunakan MAE jika**:
- ✅ Interpretasi mudah penting (rupiah, meter, kg)
- ✅ Semua error sama pentingnya
- ✅ Outlier ingin di-ignore

**Gunakan RMSE jika**:
- ✅ Error besar harus lebih di-penalty
- ✅ Standard metric (banyak paper/kompetisi)
- ✅ Distribusi error normal

**Gunakan keduanya!**:
```python
print(f"MAE: {mae:.2f} → Typical error")
print(f"RMSE: {rmse:.2f} → With penalty for large errors")
print(f"Ratio: {rmse/mae:.2f} → Error consistency")
```

---

## 2. Hubungan Precision dan Recall

### Trade-off Fundamental

**Precision dan Recall punya trade-off yang tidak bisa dihindari!**

### Analogi: Metal Detector di Airport

**Setting 1: Sensitif Tinggi (High Recall)**
- Alarm bunyi untuk anything metalic
- Recall = 100% (semua senjata terdeteksi) ✅
- Precision = 10% (banyak false alarm: koin, kunci, jam) ❌

**Setting 2: Sensitif Rendah (High Precision)**
- Alarm hanya bunyi untuk objek besar
- Precision = 90% (alarm benar-benar senjata) ✅
- Recall = 30% (banyak senjata kecil lolos) ❌

### Threshold Effect

Model biasanya output **probabilitas** (0-1), lalu kita set threshold:

**Contoh**: Prediksi Spam

| Email | Spam Probability | Threshold 0.5 | Threshold 0.8 |
|-------|------------------|---------------|---------------|
| 1 | 0.95 | Spam | Spam |
| 2 | 0.75 | Spam | Normal |
| 3 | 0.60 | Spam | Normal |
| 4 | 0.30 | Normal | Normal |

**Threshold 0.5 (Default)**:
- Prediksi 3 spam, aktual 2 spam
- Precision = 2/3 = 67%
- Recall = 2/2 = 100%

**Threshold 0.8 (Konservatif)**:
- Prediksi 1 spam, aktual 2 spam
- Precision = 1/1 = 100%
- Recall = 1/2 = 50%

### Precision-Recall Curve

**Visual tool** untuk melihat trade-off di berbagai threshold.

```python
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

precisions, recalls, thresholds = precision_recall_curve(y_true, y_proba)

plt.plot(recalls, precisions)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.show()
```

**Kurva ideal**: Precision dan Recall tinggi bersamaan (pojok kanan atas).

### F1-Score: Harmonic Mean

$$F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$

**Kenapa Harmonic Mean, bukan Arithmetic Mean?**

**Contoh**:
- Precision = 100%, Recall = 10%

**Arithmetic Mean**:
```
Mean = (100 + 10) / 2 = 55%
```

**Harmonic Mean (F1)**:
```
F1 = 2 × (100 × 10) / (100 + 10) = 18%
```

F1 "hukum berat" metric yang rendah! Lebih realistis.

### Kapan Prioritaskan Mana?

| Situasi | Prioritas | Alasan |
|---------|-----------|--------|
| **Email Spam Filter** | Precision | Email penting ke spam = buruk |
| **Cancer Detection** | Recall | Miss cancer = sangat buruk |
| **Fraud Detection** | Recall | Miss fraud = kerugian besar |
| **Search Engine** | Precision | Hasil tidak relevan = user kecewa |
| **Recommendation** | Precision | Rekomendasi jelek = user kecewa |
| **COVID Test** | Recall | Miss positive = spread disease |

**Balanced case**: Gunakan **F1-Score**!

---

## 3. Kenapa Accuracy Tidak Selalu Bagus

### Problem: Imbalanced Data

**Skenario**: Deteksi Fraud di 10,000 transaksi
- Fraud: 10 transaksi (0.1%)
- Normal: 9,990 transaksi (99.9%)

### Model Naif

**Strategi**: Prediksi semua "Normal"

```
Accuracy = 9990 / 10000 = 99.9%
```

**Terlihat sangat bagus!** ✨

**Tapi...**
```
TP (Fraud detected) = 0
FN (Fraud missed) = 10

Recall = 0 / 10 = 0%
```

**Model gagal total mendeteksi fraud!** ❌

### Kenapa Accuracy Misleading?

Accuracy memberikan "bobot sama" untuk setiap kelas:

$$Accuracy = \frac{TP + TN}{Total}$$

Pada imbalanced data:
- TN (mayoritas class) sangat besar → dominasi accuracy
- TP (minoritas class) sangat kecil → terabaikan

### Solusi untuk Imbalanced Data

#### 1. Balanced Accuracy

$$Balanced\ Accuracy = \frac{Recall_{class1} + Recall_{class2}}{2}$$

Memberikan bobot sama untuk setiap kelas!

**Contoh**:
```
Recall_Fraud = 0%
Recall_Normal = 100%

Balanced Accuracy = (0 + 100) / 2 = 50%
```

Lebih realistis!

#### 2. F1-Score

Fokus pada balance precision & recall untuk kelas positif.

#### 3. ROC-AUC

Tidak sensitif terhadap class imbalance.

#### 4. Confusion Matrix Visual

Lihat distribusi error per kelas secara eksplisit.

### Kapan Accuracy Bagus?

✅ **Gunakan Accuracy jika**:
- Dataset balanced (proporsi kelas mirip)
- Semua kelas sama pentingnya
- Error type (FP vs FN) sama cost-nya

❌ **Hindari Accuracy jika**:
- Dataset imbalanced (99:1, 90:10)
- Satu kelas jauh lebih penting
- Business impact FP ≠ FN

### Analogi

**Analogi Ujian**:

**Kasus 1 - Balanced**:
- 50 soal benar/salah
- 50 soal multiple choice
- Accuracy 80% → Bagus!

**Kasus 2 - Imbalanced**:
- 99 soal mudah (dapat semua benar)
- 1 soal penting (dapat salah)
- Accuracy 99% → Terlihat bagus, tapi gagal di soal penting!

---

## 4. Hubungan R² dengan Error Metrics

### R² vs MAE/RMSE

**R²** dan **MAE/RMSE** mengukur hal berbeda:

| Aspect | R² | MAE/RMSE |
|--------|----|----------|
| **Apa yang diukur** | Proporsi variance explained | Magnitude of error |
| **Satuan** | Dimensionless (0-1) | Sama dengan target |
| **Interpretasi** | "Model baik sebesar X%" | "Error rata-rata Y unit" |
| **Perbandingan** | Antar dataset ✅ | Dalam dataset ✅ |

### Formula Connection

$$R^2 = 1 - \frac{MSE}{Var(y)}$$

**Insight**:
- R² kecil → MSE besar relative to variance
- R² besar → MSE kecil relative to variance

### Contoh Ilustrasi

**Dataset 1: Harga Rumah (500-5000 juta)**
```
RMSE = 200 juta
Variance = 1,000,000
R² = 1 - (40,000 / 1,000,000) = 0.96 (96%)
```

**Dataset 2: Harga Laptop (5-50 juta)**
```
RMSE = 200 juta  ← SAMA!
Variance = 100,000
R² = 1 - (40,000 / 100,000) = -3.0 (NEGATIF!)
```

**Observasi**:
- RMSE sama (200 juta)
- Tapi R² sangat berbeda!
- Kenapa? Karena scale data berbeda

### R² Negatif?!

**Ya, R² bisa negatif!**

$$R^2 < 0 \rightarrow Model\ lebih\ jelek\ dari\ prediksi\ mean$$

**Contoh**:
```
Aktual: [100, 200, 150, 250]
Mean: 175

Prediksi Mean: [175, 175, 175, 175]
Error Mean²: (75² + 25² + 25² + 75²) = 11,875

Prediksi Model: [50, 300, 100, 300]
Error Model²: (50² + 100² + 50² + 50²) = 12,500

R² = 1 - (12,500 / 11,875) = -0.05
```

**Model lebih buruk dari "tebak mean"!** ❌

### Kapan R² Misleading?

#### 1. Data Non-linear tanpa Feature Engineering

Model linear di data non-linear:
```
R² = 0.3 (jelek!)
MAE = 5 (actual range: 100-1000)
```

MAE sebenarnya tidak terlalu buruk, tapi R² rendah karena model tidak capture pattern.

#### 2. Outliers

Outliers sangat pengaruhi R² (karena based on MSE).

**Solusi**: Lihat **MAE** dan **Median AE** juga!

#### 3. Different Datasets

**TIDAK BISA** bandingkan R² antar dataset berbeda!
```
Dataset A: R² = 0.85, RMSE = 100
Dataset B: R² = 0.90, RMSE = 500
```

Dataset B punya R² lebih tinggi tapi error lebih besar! Kenapa? Variance data berbeda.

### Best Practice

**Laporkan keduanya**:
```python
print(f"R²: {r2:.3f} ({r2*100:.1f}%)")
print(f"RMSE: {rmse:.2f} units")
print(f"MAE: {mae:.2f} units")
print(f"RMSE/MAE ratio: {rmse/mae:.2f}")
```

**Contoh Output**:
```
R²: 0.875 (87.5%)           ← Overall performance
RMSE: 123.45 units          ← Typical error with penalty
MAE: 98.76 units            ← Typical error
RMSE/MAE ratio: 1.25        ← Error consistency
```

---

## 5. Cross-Metric Insights

### Regression: MAE + RMSE + R²

**Kombinasi ideal untuk comprehensive evaluation**:

```python
def evaluate_regression(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    
    print("="*50)
    print("REGRESSION EVALUATION")
    print("="*50)
    print(f"MAE:  {mae:.2f} → Typical error")
    print(f"RMSE: {rmse:.2f} → Error with penalty")
    print(f"R²:   {r2:.4f} ({r2*100:.2f}%) → Variance explained")
    print(f"RMSE/MAE: {rmse/mae:.2f} → Error consistency")
    
    if rmse/mae > 1.5:
        print("⚠️  High ratio → Check for outliers!")
    if r2 < 0:
        print("❌ Negative R² → Model worse than mean!")
    elif r2 < 0.5:
        print("⚠️  Low R² → Model needs improvement")
    elif r2 > 0.9:
        print("✅ Excellent R²!")
```

### Classification: Confusion Matrix + Precision + Recall + F1 + AUC

```python
def evaluate_classification(y_true, y_pred, y_proba=None):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred)
    rec = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    
    print("="*50)
    print("CLASSIFICATION EVALUATION")
    print("="*50)
    print(f"Accuracy:  {acc:.2%}")
    print(f"Precision: {prec:.2%} → When predicting +, how often correct?")
    print(f"Recall:    {rec:.2%} → Of all actual +, how many found?")
    print(f"F1-Score:  {f1:.2%} → Harmonic mean of P & R")
    
    if y_proba is not None:
        auc = roc_auc_score(y_true, y_proba)
        print(f"AUC:       {auc:.3f} → Discrimination ability")
    
    # Confusion Matrix
    cm = confusion_matrix(y_true, y_pred)
    print("\nConfusion Matrix:")
    print(cm)
    
    # Recommendations
    if prec < 0.5:
        print("\n⚠️  Low Precision → Too many false positives!")
    if rec < 0.5:
        print("⚠️  Low Recall → Missing many actual positives!")
    if abs(prec - rec) > 0.2:
        print("⚠️  Imbalance: Consider adjusting threshold")
```

---

## 6. Threshold Tuning: Menentukan Threshold Optimal

### Apa itu Threshold?

Model classification (Logistic Regression, Random Forest, dll.) tidak langsung output "Spam" atau "Normal". Model output **probabilitas** antara 0-1, lalu kita tentukan **threshold** (ambang batas) untuk memutuskan kelas.

```
Default: threshold = 0.5
  → Proba ≥ 0.5 → Prediksi Positif
  → Proba < 0.5 → Prediksi Negatif
```

**Tapi 0.5 belum tentu optimal!**

### Kenapa Threshold Default Sering Tidak Optimal?

**Kasus 1: Data Imbalanced**
- 99% Normal, 1% Fraud
- Model cenderung output probabilitas rendah untuk Fraud
- Threshold 0.5 mungkin terlalu tinggi → banyak fraud miss

**Kasus 2: Cost Berbeda**
- False Negative (miss fraud) → Kerugian Rp 100 juta
- False Positive (false alarm) → Biaya investigasi Rp 1 juta
- Threshold rendah lebih baik (prefer false alarm daripada miss)

### Metode 1: Maximize F1-Score

Cari threshold yang menghasilkan F1-Score tertinggi.

```python
from sklearn.metrics import precision_recall_curve, f1_score
import numpy as np

# Dapatkan precision dan recall di berbagai threshold
precisions, recalls, thresholds = precision_recall_curve(y_true, y_proba)

# Hitung F1 untuk setiap threshold
f1_scores = 2 * (precisions * recalls) / (precisions + recalls + 1e-8)

# Cari threshold dengan F1 tertinggi
best_idx = np.argmax(f1_scores)
best_threshold = thresholds[best_idx]
best_f1 = f1_scores[best_idx]

print(f"Best Threshold: {best_threshold:.3f}")
print(f"Best F1-Score:  {best_f1:.3f}")
print(f"Precision:      {precisions[best_idx]:.3f}")
print(f"Recall:         {recalls[best_idx]:.3f}")
```

### Metode 2: Youden's J Statistic (ROC-based)

Cari threshold yang **maximize (Sensitivity + Specificity - 1)**, yaitu titik terjauh dari garis random di ROC curve.

```python
from sklearn.metrics import roc_curve

fpr, tpr, thresholds = roc_curve(y_true, y_proba)

# Youden's J = Sensitivity + Specificity - 1 = TPR - FPR
j_scores = tpr - fpr
best_idx = np.argmax(j_scores)
best_threshold = thresholds[best_idx]

print(f"Best Threshold (Youden's J): {best_threshold:.3f}")
print(f"Sensitivity (TPR): {tpr[best_idx]:.3f}")
print(f"Specificity (1-FPR): {1-fpr[best_idx]:.3f}")
```

### Metode 3: Cost-Sensitive Threshold

Tentukan threshold berdasarkan biaya FP dan FN.

```python
# Definisikan cost
cost_FP = 1       # Biaya false alarm (rendah)
cost_FN = 100     # Biaya miss fraud (tinggi!)

# Hitung total cost di setiap threshold
fpr, tpr, thresholds = roc_curve(y_true, y_proba)
n_pos = sum(y_true)
n_neg = len(y_true) - n_pos

total_costs = []
for i in range(len(thresholds)):
    fp_count = fpr[i] * n_neg
    fn_count = (1 - tpr[i]) * n_pos
    total_cost = (fp_count * cost_FP) + (fn_count * cost_FN)
    total_costs.append(total_cost)

# Threshold dengan cost minimum
best_idx = np.argmin(total_costs)
best_threshold = thresholds[best_idx]

print(f"Cost-Optimal Threshold: {best_threshold:.3f}")
print(f"Total Cost: {total_costs[best_idx]:,.0f}")
```

### Metode 4: Precision at Target Recall

Jika requirement: "Recall harus minimal 90%", cari threshold yang memenuhi.

```python
# Target: Recall >= 90%
target_recall = 0.90

precisions, recalls, thresholds = precision_recall_curve(y_true, y_proba)

# Cari threshold tertinggi yang masih punya recall >= target
valid_idx = np.where(recalls[:-1] >= target_recall)[0]
if len(valid_idx) > 0:
    # Ambil yang precision-nya tertinggi (threshold tertinggi)
    best_idx = valid_idx[np.argmax(precisions[valid_idx])]
    best_threshold = thresholds[best_idx]
    
    print(f"Threshold untuk Recall ≥ {target_recall:.0%}: {best_threshold:.3f}")
    print(f"Precision di threshold ini: {precisions[best_idx]:.3f}")
    print(f"Recall di threshold ini: {recalls[best_idx]:.3f}")
```

### Visualisasi: Metrics vs Threshold

```python
import matplotlib.pyplot as plt

precisions, recalls, thresholds_pr = precision_recall_curve(y_true, y_proba)
f1s = 2 * (precisions * recalls) / (precisions + recalls + 1e-8)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Precision, Recall, F1 vs Threshold
axes[0].plot(thresholds_pr, precisions[:-1], label='Precision', color='blue')
axes[0].plot(thresholds_pr, recalls[:-1], label='Recall', color='red')
axes[0].plot(thresholds_pr, f1s[:-1], label='F1-Score', color='green')
axes[0].axvline(x=0.5, color='gray', linestyle='--', label='Default (0.5)')
axes[0].axvline(x=best_threshold, color='black', linestyle='--', label=f'Optimal ({best_threshold:.2f})')
axes[0].set_xlabel('Threshold')
axes[0].set_ylabel('Score')
axes[0].set_title('Metrics vs Threshold')
axes[0].legend()

# Plot 2: Precision-Recall Curve
axes[1].plot(recalls, precisions)
axes[1].set_xlabel('Recall')
axes[1].set_ylabel('Precision')
axes[1].set_title('Precision-Recall Curve')

plt.tight_layout()
plt.show()
```

### Tips Praktis Threshold Tuning

| Situasi | Metode | Threshold Cenderung |
|---------|--------|---------------------|
| **Balance P & R** | Maximize F1 | Dekat 0.5 |
| **Balance Sens & Spec** | Youden's J | Bervariasi |
| **FN sangat mahal** | Cost-sensitive | Rendah (<0.5) |
| **FP sangat mahal** | Cost-sensitive | Tinggi (>0.5) |
| **Minimum recall 90%** | Target recall | Rendah |

**⚠️ PENTING**: Tentukan threshold di **validation set**, bukan test set!

```python
# CORRECT workflow
from sklearn.model_selection import train_test_split

# Split: train / validation / test
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5)

# 1. Train model
model.fit(X_train, y_train)

# 2. Cari best threshold di VALIDATION set
y_val_proba = model.predict_proba(X_val)[:, 1]
best_threshold = find_best_threshold(y_val, y_val_proba)

# 3. Evaluasi final di TEST set
y_test_proba = model.predict_proba(X_test)[:, 1]
y_test_pred = (y_test_proba >= best_threshold).astype(int)
```

---

## 7. Cross-Validation untuk Estimasi Metric yang Robust

### Problem: Metric dari Single Split Tidak Stabil

Metric dari satu kali train/test split bisa sangat **bervariasi** tergantung bagaimana data di-split.

**Contoh**:
```
Split 1 → F1 = 85%
Split 2 → F1 = 72%
Split 3 → F1 = 91%

Mana yang benar? Semua benar! Tapi kita butuh estimasi yang STABIL.
```

### Solusi: K-Fold Cross-Validation

Bagi data menjadi K fold, gunakan setiap fold sebagai test set bergantian.

```
5-Fold Cross-Validation:

Fold 1: [TEST] [Train] [Train] [Train] [Train] → F1 = 85%
Fold 2: [Train] [TEST] [Train] [Train] [Train] → F1 = 82%
Fold 3: [Train] [Train] [TEST] [Train] [Train] → F1 = 88%
Fold 4: [Train] [Train] [Train] [TEST] [Train] → F1 = 81%
Fold 5: [Train] [Train] [Train] [Train] [TEST] → F1 = 84%

Mean F1 = 84% ± 2.5% ← STABIL dan ADA confidence interval!
```

### Kode Python: Basic Cross-Validation

```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)

# F1-Score dengan 5-Fold CV
f1_scores = cross_val_score(model, X, y, cv=5, scoring='f1')

print(f"F1 per fold: {f1_scores}")
print(f"Mean F1:     {f1_scores.mean():.3f}")
print(f"Std F1:      {f1_scores.std():.3f}")
print(f"F1 range:    {f1_scores.mean():.3f} ± {f1_scores.std()*2:.3f} (95% CI)")
```

### Stratified K-Fold (untuk Data Imbalanced)

**K-Fold biasa** bisa membuat fold dengan distribusi kelas tidak rata.
**Stratified K-Fold** memastikan setiap fold punya proporsi kelas yang SAMA.

```python
from sklearn.model_selection import StratifiedKFold, cross_val_score

# Stratified: pastikan setiap fold proporsional
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

f1_scores = cross_val_score(model, X, y, cv=skf, scoring='f1')
print(f"Stratified 5-Fold F1: {f1_scores.mean():.3f} ± {f1_scores.std():.3f}")
```

### Multiple Metrics Sekaligus

```python
from sklearn.model_selection import cross_validate

# Evaluasi banyak metric sekaligus
scoring = {
    'accuracy': 'accuracy',
    'precision': 'precision',
    'recall': 'recall',
    'f1': 'f1',
    'roc_auc': 'roc_auc'
}

results = cross_validate(model, X, y, cv=5, scoring=scoring)

print("="*60)
print("CROSS-VALIDATION RESULTS (5-Fold)")
print("="*60)
for metric_name in scoring:
    scores = results[f'test_{metric_name}']
    print(f"{metric_name:>12}: {scores.mean():.3f} ± {scores.std():.3f}")
```

### Cross-Validation untuk Regression

```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100, random_state=42)

# Multiple scoring
scoring_reg = {
    'r2': 'r2',
    'neg_mae': 'neg_mean_absolute_error',
    'neg_rmse': 'neg_root_mean_squared_error'
}

results = cross_validate(model, X, y, cv=5, scoring=scoring_reg)

print("R²:   {:.3f} ± {:.3f}".format(
    results['test_r2'].mean(), results['test_r2'].std()))
print("MAE:  {:.3f} ± {:.3f}".format(
    -results['test_neg_mae'].mean(), results['test_neg_mae'].std()))
print("RMSE: {:.3f} ± {:.3f}".format(
    -results['test_neg_rmse'].mean(), results['test_neg_rmse'].std()))
```

⚠️ **Catatan**: Sklearn menggunakan "neg_" (negatif) untuk error metrics karena `cross_val_score` selalu maximize (lebih tinggi = lebih baik). Jadi MAE = 100 menjadi -100.

### Repeated K-Fold (Lebih Stabil Lagi)

Ulangi K-Fold beberapa kali dengan shuffle berbeda.

```python
from sklearn.model_selection import RepeatedStratifiedKFold

# 5 fold × 10 repetitions = 50 evaluasi!
rskf = RepeatedStratifiedKFold(n_splits=5, n_repeats=10, random_state=42)

f1_scores = cross_val_score(model, X, y, cv=rskf, scoring='f1')
print(f"Repeated 5×10 F1: {f1_scores.mean():.3f} ± {f1_scores.std():.3f}")
print(f"Number of evaluations: {len(f1_scores)}")
```

### Kapan Pakai CV Apa?

| Metode | Folds | Stabil? | Waktu | Kapan Pakai |
|--------|-------|---------|-------|-------------|
| **Hold-out** | 1 split | ❌ | Cepat | Quick test, dataset besar |
| **5-Fold CV** | 5 | ✅ | Medium | Standard, dataset sedang |
| **10-Fold CV** | 10 | ✅✅ | Lambat | Paper, dataset kecil |
| **Stratified KF** | 5-10 | ✅✅ | Medium | Imbalanced data |
| **Repeated KF** | 5×10 | ✅✅✅ | Sangat lambat | Butuh estimasi sangat stabil |
| **Leave-One-Out** | N | ✅✅✅ | Sangat lambat | Dataset sangat kecil (<50) |

### Tips Penting

**1. CV untuk model comparison, BUKAN final evaluation**
```python
# CORRECT: Gunakan CV untuk pilih model terbaik
f1_rf = cross_val_score(RandomForestClassifier(), X_trainval, y_trainval, cv=5, scoring='f1').mean()
f1_lr = cross_val_score(LogisticRegression(), X_trainval, y_trainval, cv=5, scoring='f1').mean()

# Pilih yang terbaik
best_model = RandomForestClassifier() if f1_rf > f1_lr else LogisticRegression()

# Final evaluation di test set (yang BELUM pernah disentuh)
best_model.fit(X_trainval, y_trainval)
final_f1 = f1_score(y_test, best_model.predict(X_test))
```

**2. Jangan pernah leak test data ke CV!**
```python
# ❌ WRONG: Test data ikut di CV
scores = cross_val_score(model, X_ALL, y_ALL, cv=5)

# ✅ CORRECT: CV hanya di train+val, test terpisah
scores = cross_val_score(model, X_trainval, y_trainval, cv=5)
```

**3. Gunakan `cross_validate` (bukan `cross_val_score`) untuk multiple metrics**

---

## Kesimpulan Bab

### Key Takeaways

✅ **MAE vs RMSE**: 
- MAE untuk typical error
- RMSE untuk penalty error besar
- RMSE/MAE ratio untuk konsistensi

✅ **Precision vs Recall**:
- Trade-off fundamental
- Pilih based on business impact
- F1 untuk balance

✅ **Accuracy**:
- Bagus untuk balanced data
- Misleading untuk imbalanced data
- Selalu check confusion matrix

✅ **R² vs Error Metrics**:
- R² untuk "overall goodness"
- MAE/RMSE untuk magnitude error
- Laporkan keduanya!

✅ **Threshold Tuning**:
- Default 0.5 belum tentu optimal
- Gunakan F1-maximize, Youden's J, atau cost-based
- Tentukan threshold di **validation set**, bukan test set

✅ **Cross-Validation**:
- Single split → metric tidak stabil
- 5/10-Fold CV → estimasi lebih robust
- Stratified untuk imbalanced data
- Laporkan mean ± std

✅ **Never use single metric in isolation!**

---

*Modul 3 — Evaluation Metrics dalam Machine Learning*

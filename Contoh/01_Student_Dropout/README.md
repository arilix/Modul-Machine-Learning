# 📚 Student Dropout — Panduan Dataset & Notebook

> Dataset: `student_dropout_dataset_v3.csv`  
> Lokasi: `Contoh/student_dropout_dataset_v3.csv`  
> Jumlah data: **10.000 baris × 19 kolom**

---

## 🎯 Tujuan

Dataset ini dirancang untuk mempelajari dan memprediksi **risiko dropout (putus studi)** mahasiswa berdasarkan berbagai faktor akademik, demografis, dan sosial-ekonomi.

Tujuan utama penggunaan dataset ini:

| Tujuan | Deskripsi |
|--------|-----------|
| **Prediksi Dropout** | Mengidentifikasi mahasiswa yang berpotensi tidak menyelesaikan studi |
| **Prediksi CGPA** | Memprediksi nilai akhir kumulatif (CGPA) berdasarkan perilaku belajar |
| **Analisis Faktor Risiko** | Mengetahui variabel mana yang paling berpengaruh terhadap dropout |
| **Segmentasi Mahasiswa** | Mengelompokkan mahasiswa berdasarkan pola akademik dan sosial |
| **Sistem Peringatan Dini** | Membangun model yang bisa digunakan institusi untuk intervensi lebih awal |

---

## 📋 Penjelasan Kolom

### 🪪 Identitas

| Kolom | Tipe | Keterangan |
|-------|------|------------|
| `Student_ID` | int | ID unik setiap mahasiswa (1–10000) |
| `Age` | float | Usia mahasiswa (tahun) |
| `Gender` | object | Jenis kelamin: `Male` / `Female` |

### 🏫 Akademik

| Kolom | Tipe | Keterangan |
|-------|------|------------|
| `Department` | object | Jurusan: `Science`, `Arts`, `Business`, `CS`, `Engineering` |
| `Semester` | object | Tingkat semester: `Year 1` – `Year 4` |
| `GPA` | float | IPK keseluruhan (skala 0–4) |
| `Semester_GPA` | float | IPK semester terakhir |
| `CGPA` | float | Cumulative GPA (rata-rata kumulatif) |
| `Attendance_Rate` | float | Persentase kehadiran kuliah (0–100%) |
| `Assignment_Delay_Days` | int | Rata-rata keterlambatan mengumpulkan tugas (hari) |
| `Study_Hours_per_Day` | float | Rata-rata jam belajar per hari ⚠️ *ada missing value* |

### 💰 Sosial-Ekonomi

| Kolom | Tipe | Keterangan |
|-------|------|------------|
| `Family_Income` | float | Pendapatan keluarga per tahun (dalam mata uang lokal) ⚠️ *ada missing value* |
| `Parental_Education` | object | Tingkat pendidikan orang tua: `High School`, `Bachelor`, `Master`, `PhD` ⚠️ *ada missing value* |
| `Scholarship` | object | Penerima beasiswa: `Yes` / `No` |
| `Part_Time_Job` | object | Status kerja paruh waktu: `Yes` / `No` |
| `Internet_Access` | object | Akses internet: `Yes` / `No` |
| `Travel_Time_Minutes` | float | Waktu tempuh ke kampus (menit) |

### 🧠 Psikologis

| Kolom | Tipe | Keterangan |
|-------|------|------------|
| `Stress_Index` | float | Indeks stres mahasiswa (skala 1–10) ⚠️ *ada missing value* |

### 🎯 Target

| Kolom | Tipe | Keterangan |
|-------|------|------------|
| `Dropout` | int | Label dropout: `1` = dropout, `0` = tidak dropout |

---

## 🔍 Melihat Bentuk & Isi Data (EDA)

### Langkah 1 — Load & Cek Struktur Awal

```python
import pandas as pd

df = pd.read_csv('../student_dropout_dataset_v3.csv')

print(df.shape)       # (10000, 19)  → 10.000 baris, 19 kolom
df.head()             # 5 baris pertama
df.tail()             # 5 baris terakhir
df.info()             # tipe data tiap kolom + jumlah non-null
df.describe()         # min, max, mean, std, kuartil (kolom numerik)
df.describe(include='object')  # frekuensi nilai (kolom kategorikal)
```

### Langkah 2 — Cek Missing Value

```python
import matplotlib.pyplot as plt
import seaborn as sns

missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)
print(missing)
# Family_Income       500
# Study_Hours_per_Day 500
# Stress_Index        500
# Parental_Education  511

# Visualisasi missing value
plt.figure(figsize=(7, 4))
missing.plot(kind='bar', color='salmon')
plt.title('Jumlah Missing Value per Kolom')
plt.ylabel('Jumlah')
plt.tight_layout()
plt.show()
```

### Langkah 3 — Distribusi Target (Dropout)

```python
plt.figure(figsize=(5, 4))
df['Dropout'].value_counts().plot(kind='bar', color=['steelblue', 'tomato'])
plt.xticks([0, 1], ['Tidak Dropout (0)', 'Dropout (1)'], rotation=0)
plt.title('Distribusi Label Dropout')
plt.ylabel('Jumlah Mahasiswa')
plt.tight_layout()
plt.show()

# Persentase
print(df['Dropout'].value_counts(normalize=True) * 100)
# 0 → 76.5%  |  1 → 23.5%
```

### Langkah 4 — Distribusi Kolom Numerik

```python
num_cols = ['Age', 'Study_Hours_per_Day', 'Attendance_Rate',
            'GPA', 'CGPA', 'Stress_Index', 'Family_Income', 'Travel_Time_Minutes']

df[num_cols].hist(bins=30, figsize=(14, 8), color='steelblue', edgecolor='white')
plt.suptitle('Distribusi Kolom Numerik', fontsize=14)
plt.tight_layout()
plt.show()
```

### Langkah 5 — Perbandingan Fitur berdasarkan Status Dropout

```python
# Boxplot: apakah ada perbedaan antara mahasiswa dropout vs tidak?
fig, axes = plt.subplots(2, 3, figsize=(14, 8))
compare_cols = ['GPA', 'Attendance_Rate', 'Study_Hours_per_Day',
                'Stress_Index', 'Family_Income', 'CGPA']

for ax, col in zip(axes.flatten(), compare_cols):
    sns.boxplot(data=df, x='Dropout', y=col, palette=['steelblue', 'tomato'], ax=ax)
    ax.set_xticklabels(['Tidak Dropout', 'Dropout'])
    ax.set_title(col)

plt.suptitle('Perbandingan Fitur: Dropout vs Tidak', fontsize=14)
plt.tight_layout()
plt.show()
```

### Langkah 6 — Distribusi Kolom Kategorikal

```python
cat_cols = ['Gender', 'Department', 'Semester', 'Scholarship',
            'Part_Time_Job', 'Internet_Access', 'Parental_Education']

fig, axes = plt.subplots(2, 4, figsize=(16, 7))
for ax, col in zip(axes.flatten(), cat_cols):
    df[col].value_counts().plot(kind='bar', ax=ax, color='mediumpurple', edgecolor='white')
    ax.set_title(col)
    ax.tick_params(axis='x', rotation=30)

plt.suptitle('Distribusi Kolom Kategorikal', fontsize=14)
plt.tight_layout()
plt.show()
```

### Langkah 7 — Korelasi Antar Fitur Numerik

```python
plt.figure(figsize=(10, 8))
corr = df[num_cols + ['Dropout']].corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, square=True, linewidths=0.5)
plt.title('Heatmap Korelasi Fitur Numerik')
plt.tight_layout()
plt.show()
```

> 💡 **Apa yang bisa dibaca dari heatmap?**  
> - `GPA` dan `CGPA` berkorelasi _negatif_ dengan `Dropout` → mahasiswa dengan GPA tinggi cenderung tidak dropout  
> - `Attendance_Rate` berkorelasi _negatif_ dengan `Dropout` → semakin sering hadir, semakin kecil risiko dropout  
> - `Stress_Index` berkorelasi _positif_ dengan `Dropout` → semakin stres, semakin berisiko

### Langkah 8 — Dropout Rate per Kategori

```python
cat_target_cols = ['Department', 'Semester', 'Gender', 'Scholarship', 'Part_Time_Job']

fig, axes = plt.subplots(1, len(cat_target_cols), figsize=(18, 4))
for ax, col in zip(axes, cat_target_cols):
    dropout_rate = df.groupby(col)['Dropout'].mean().sort_values(ascending=False)
    dropout_rate.plot(kind='bar', ax=ax, color='tomato', edgecolor='white')
    ax.set_title(f'Dropout Rate\nper {col}')
    ax.set_ylabel('Proporsi Dropout')
    ax.set_ylim(0, 0.5)
    ax.tick_params(axis='x', rotation=30)

plt.suptitle('Dropout Rate per Kelompok', fontsize=14)
plt.tight_layout()
plt.show()
```

---

## ⚠️ Missing Values

Beberapa kolom memiliki nilai kosong yang perlu ditangani sebelum modeling:

| Kolom | Jumlah Missing | Cara Penanganan yang Disarankan |
|-------|---------------|--------------------------------|
| `Family_Income` | 500 | Isi dengan **median** (distribusi skewed) |
| `Study_Hours_per_Day` | 500 | Isi dengan **median** per semester/jurusan |
| `Stress_Index` | 500 | Isi dengan **median** atau nilai tengah skala |
| `Parental_Education` | 511 | Isi dengan **modus** atau tambahkan kategori `Unknown` |

```python
# Contoh handling missing value
df['Family_Income'].fillna(df['Family_Income'].median(), inplace=True)
df['Study_Hours_per_Day'].fillna(df['Study_Hours_per_Day'].median(), inplace=True)
df['Stress_Index'].fillna(df['Stress_Index'].median(), inplace=True)
df['Parental_Education'].fillna('Unknown', inplace=True)
```

---

## 🔧 Preprocessing Umum

```python
from sklearn.preprocessing import LabelEncoder, StandardScaler

# 1. Encode kolom kategorikal
cat_cols = ['Gender', 'Internet_Access', 'Part_Time_Job',
            'Scholarship', 'Semester', 'Department', 'Parental_Education']

le = LabelEncoder()
for col in cat_cols:
    df[col] = le.fit_transform(df[col])

# 2. Pisahkan fitur dan target
X = df.drop(columns=['Student_ID', 'Dropout'])
y = df['Dropout']

# 3. Split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Normalisasi (opsional, diperlukan untuk SVM & Neural Network)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)
```

---

## 🤖 Apa Saja yang Bisa Dilakukan dengan Data Ini?

### 1. 📌 Klasifikasi Dropout (Binary Classification)

**Target:** kolom `Dropout` (0 atau 1)  
**Metrik evaluasi:** Accuracy, F1-Score, ROC-AUC

```python
# Contoh dengan Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score

model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

print(classification_report(y_test, y_pred))
print("AUC:", roc_auc_score(y_test, model.predict_proba(X_test_scaled)[:,1]))
```

> Notebook tersedia: `01_dropout_logistic_regression.ipynb`, `02_dropout_random_forest.ipynb`, `03_dropout_xgboost.ipynb`, `04_dropout_svm.ipynb`, `05_dropout_neural_network.ipynb`

---

### 2. 📈 Regresi CGPA (Regression)

**Target:** kolom `CGPA` (nilai numerik kontinu)  
**Metrik evaluasi:** MAE, RMSE, R²

```python
# Contoh dengan Random Forest Regressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

X_reg = df.drop(columns=['Student_ID', 'Dropout', 'GPA', 'Semester_GPA', 'CGPA'])
y_reg = df['CGPA']

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train_r, y_train_r)
y_pred_r = rf.predict(X_test_r)

print("MAE :", mean_absolute_error(y_test_r, y_pred_r))
print("R²  :", r2_score(y_test_r, y_pred_r))
```

> Notebook tersedia: `06_cgpa_linear_regression.ipynb`, `07_cgpa_random_forest_regressor.ipynb`, `08_cgpa_xgboost_regressor.ipynb`

---

### 3. 🏆 Perbandingan Semua Model

Lihat perbandingan lengkap semua model (klasifikasi + regresi) dalam satu notebook:

> `00_dropout_model_comparison.ipynb`

---

## 📊 Distribusi Data

```
Distribusi Target (Dropout):
  - Tidak Dropout (0) : 7.646 mahasiswa (76.5%)
  - Dropout (1)       : 2.354 mahasiswa (23.5%)

⚠️ Data TIDAK seimbang (imbalanced). Perlu strategi:
  - class_weight='balanced' pada model
  - SMOTE / oversampling
  - Threshold tuning pada prediksi probabilitas
```

```
Distribusi Jurusan:
  Science     : 2.061
  Arts        : 2.026
  Business    : 2.002
  CS          : 1.974
  Engineering : 1.937
```

---

## 📁 Struktur Notebook

| File | Tugas | Target |
|------|-------|--------|
| `00_dropout_model_comparison.ipynb` | Perbandingan semua model | Dropout & CGPA |
| `01_dropout_logistic_regression.ipynb` | Logistic Regression | `Dropout` |
| `02_dropout_random_forest.ipynb` | Random Forest Classifier | `Dropout` |
| `03_dropout_xgboost.ipynb` | XGBoost Classifier | `Dropout` |
| `04_dropout_svm.ipynb` | Support Vector Machine | `Dropout` |
| `05_dropout_neural_network.ipynb` | Neural Network (MLP) | `Dropout` |
| `06_cgpa_linear_regression.ipynb` | Linear Regression | `CGPA` |
| `07_cgpa_random_forest_regressor.ipynb` | Random Forest Regressor | `CGPA` |
| `08_cgpa_xgboost_regressor.ipynb` | XGBoost Regressor | `CGPA` |

---

## 🏅 Ringkasan Hasil Model (dari `00_dropout_model_comparison.ipynb`)

### Klasifikasi Dropout

| Peringkat | Model | Accuracy | F1-Score | ROC-AUC |
|-----------|-------|----------|----------|---------|
| 🥇 1 | Logistic Regression | ~0.68 | ~0.587 | **0.821** |
| 🥈 2 | XGBoost | ~0.67 | ~0.575 | ~0.809 |
| 🥉 3 | Random Forest | ~0.67 | ~0.569 | ~0.806 |
| 4 | SVM | ~0.66 | ~0.556 | ~0.800 |
| 5 | Neural Network | ~0.65 | ~0.545 | ~0.793 |

> ℹ️ Performa model relatif moderat karena data tidak seimbang (76:24). Logistic Regression unggul karena hubungan fitur–target cenderung linear.

---

## 💡 Tips Eksplorasi Lanjutan

1. **Feature Importance** — gunakan `.feature_importances_` dari Random Forest/XGBoost untuk melihat fitur paling berpengaruh terhadap dropout
2. **Korelasi** — cek korelasi `Attendance_Rate`, `CGPA`, dan `Study_Hours_per_Day` dengan `Dropout`
3. **Cross-validation** — gunakan `StratifiedKFold` karena data tidak seimbang
4. **SMOTE** — coba oversampling dengan `imbalanced-learn` untuk meningkatkan recall kelas dropout
5. **Hyperparameter tuning** — gunakan `GridSearchCV` atau `Optuna` untuk optimasi lebih lanjut

---

*Dataset ini cocok sebagai bahan latihan kompetisi Kaggle bertema education analytics atau student success prediction.*

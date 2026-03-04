# 🎓 Student Productivity — Panduan Dataset & Notebook

> Dataset: `ultimate_student_productivity_dataset_5000.csv`  
> Lokasi: `Contoh/ultimate_student_productivity_dataset_5000.csv`  
> Jumlah data: **5.000 baris × 21 kolom**

---

## 🎯 Tujuan

Dataset ini merekam kebiasaan belajar, gaya hidup, kondisi psikologis, dan performa akademik mahasiswa.  
Tujuan utama penggunaan dataset ini:

| Tujuan | Deskripsi |
|--------|-----------|
| **Prediksi Produktivitas** | Memprediksi skor produktivitas belajar (`productivity_score`) |
| **Prediksi Nilai Ujian** | Memprediksi `exam_score` berdasarkan kebiasaan mahasiswa |
| **Klasifikasi Produktivitas Tinggi/Rendah** | Mengkategorikan mahasiswa sebagai produktif atau tidak |
| **Analisis Faktor Produktivitas** | Mengetahui variabel apa (jam tidur, media sosial, olahraga, dll.) yang paling berpengaruh |
| **Deteksi Risiko Burnout** | Mengidentifikasi mahasiswa yang berisiko mengalami kelelahan ekstrem |
| **Segmentasi / Clustering** | Mengelompokkan mahasiswa berdasarkan pola kebiasaan belajar dan gaya hidup |

---

## 📋 Penjelasan Kolom

### 🪪 Identitas

| Kolom | Tipe | Keterangan |
|-------|------|------------|
| `student_id` | int | ID unik setiap mahasiswa (1–5000) |
| `age` | int | Usia mahasiswa (16–25 tahun) |
| `gender` | object | Jenis kelamin: `Male`, `Female`, `Other` |
| `academic_level` | object | Jenjang pendidikan: `High School`, `Undergraduate`, `Postgraduate` |

### 📚 Aktivitas Belajar

| Kolom | Tipe | Keterangan |
|-------|------|------------|
| `study_hours` | float | Total jam belajar per hari |
| `self_study_hours` | float | Jam belajar mandiri per hari |
| `online_classes_hours` | float | Jam mengikuti kelas online per hari |
| `upcoming_deadline` | int | Ada deadline mendekat: `1` = Ya, `0` = Tidak |

### 📱 Gaya Hidup & Kesehatan

| Kolom | Tipe | Keterangan |
|-------|------|------------|
| `sleep_hours` | float | Jam tidur per hari |
| `social_media_hours` | float | Jam penggunaan media sosial per hari |
| `gaming_hours` | float | Jam bermain game per hari |
| `screen_time_hours` | float | Total jam layar per hari |
| `exercise_minutes` | int | Menit olahraga per hari (0–150 menit) |
| `caffeine_intake_mg` | int | Konsumsi kafein per hari (mg) |
| `part_time_job` | int | Status kerja paruh waktu: `1` = Ya, `0` = Tidak |
| `internet_quality` | object | Kualitas internet: `Good`, `Average`, `Poor` |

### 🧠 Kondisi Psikologis & Kognitif

| Kolom | Tipe | Keterangan |
|-------|------|------------|
| `mental_health_score` | int | Skor kesehatan mental (1–10, semakin tinggi semakin baik) |
| `focus_index` | float | Indeks fokus belajar (kontinu) |
| `burnout_level` | float | Tingkat kelelahan/burnout (kontinu, semakin tinggi semakin buruk) |

### 🎯 Target / Output

| Kolom | Tipe | Keterangan |
|-------|------|------------|
| `productivity_score` | float | Skor produktivitas belajar (1–98) — **target regresi utama** |
| `exam_score` | float | Nilai ujian (1–64) — target regresi alternatif |

> ✅ **Tidak ada missing value** pada dataset ini. Semua 5.000 baris lengkap.

---

## 🔍 Melihat Bentuk & Isi Data (EDA)

### Langkah 1 — Load & Cek Struktur Awal

```python
import pandas as pd

df = pd.read_csv('../ultimate_student_productivity_dataset_5000.csv')

print(df.shape)       # (5000, 21)
df.head()             # 5 baris pertama
df.tail()             # 5 baris terakhir
df.info()             # tipe data + jumlah non-null
df.describe()         # statistik dasar kolom numerik
df.describe(include='object')  # ringkasan kolom kategorikal
```

### Langkah 2 — Cek Missing Value & Duplikat

```python
# Missing value
print(df.isnull().sum())   # semua 0 — tidak ada missing value

# Duplikat
print("Duplikat:", df.duplicated().sum())   # 0

# Nilai unik per kolom kategorikal
for col in ['gender', 'academic_level', 'internet_quality']:
    print(f"{col}: {df[col].value_counts().to_dict()}")
```

### Langkah 3 — Distribusi Target Utama

```python
import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(1, 2, figsize=(13, 4))

# Histogram productivity_score
axes[0].hist(df['productivity_score'], bins=40, color='steelblue', edgecolor='white')
axes[0].set_title('Distribusi productivity_score')
axes[0].set_xlabel('Skor Produktivitas')
axes[0].set_ylabel('Frekuensi')

# Histogram exam_score
axes[1].hist(df['exam_score'], bins=40, color='mediumpurple', edgecolor='white')
axes[1].set_title('Distribusi exam_score')
axes[1].set_xlabel('Nilai Ujian')

plt.suptitle('Distribusi Kolom Target', fontsize=13)
plt.tight_layout()
plt.show()

# Statistik ringkas
print("productivity_score — min:", df['productivity_score'].min(),
      "| max:", df['productivity_score'].max(),
      "| median:", df['productivity_score'].median().round(2))
print("exam_score         — min:", df['exam_score'].min(),
      "| max:", df['exam_score'].max(),
      "| median:", df['exam_score'].median().round(2))
```

### Langkah 4 — Distribusi Kolom Numerik

```python
num_cols = ['study_hours', 'self_study_hours', 'online_classes_hours',
            'sleep_hours', 'social_media_hours', 'gaming_hours',
            'screen_time_hours', 'exercise_minutes', 'caffeine_intake_mg',
            'mental_health_score', 'focus_index', 'burnout_level']

df[num_cols].hist(bins=30, figsize=(16, 10), color='teal', edgecolor='white')
plt.suptitle('Distribusi Kolom Numerik', fontsize=14)
plt.tight_layout()
plt.show()
```

### Langkah 5 — Distribusi Kolom Kategorikal

```python
cat_cols = ['gender', 'academic_level', 'internet_quality']

fig, axes = plt.subplots(1, 3, figsize=(13, 4))
colors = ['steelblue', 'mediumpurple', 'tomato']

for ax, col, color in zip(axes, cat_cols, colors):
    df[col].value_counts().plot(kind='bar', ax=ax, color=color, edgecolor='white')
    ax.set_title(f'Distribusi {col}')
    ax.tick_params(axis='x', rotation=30)

plt.suptitle('Distribusi Kolom Kategorikal', fontsize=13)
plt.tight_layout()
plt.show()
```

### Langkah 6 — Korelasi Antar Fitur Numerik

```python
plt.figure(figsize=(13, 10))
corr_cols = num_cols + ['productivity_score', 'exam_score']
corr = df[corr_cols].corr()

sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, square=True, linewidths=0.5, annot_kws={'size': 8})
plt.title('Heatmap Korelasi Fitur Numerik')
plt.tight_layout()
plt.show()
```

> 💡 **Temuan dari heatmap:**  
> - `focus_index` berkorelasi **positif kuat** dengan `productivity_score`  
> - `burnout_level` berkorelasi **negatif** dengan `productivity_score`  
> - `mental_health_score` berkorelasi **positif** dengan produktivitas  
> - `social_media_hours` & `gaming_hours` berkorelasi **negatif** dengan produktivitas

### Langkah 7 — Produktivitas berdasarkan Kelompok

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for ax, col in zip(axes, ['gender', 'academic_level', 'internet_quality']):
    group = df.groupby(col)['productivity_score'].mean().sort_values(ascending=False)
    group.plot(kind='bar', ax=ax, color='steelblue', edgecolor='white')
    ax.set_title(f'Rata-rata Produktivitas\nper {col}')
    ax.set_ylabel('Rata-rata Skor')
    ax.tick_params(axis='x', rotation=30)

plt.suptitle('Produktivitas Rata-rata per Kategori', fontsize=13)
plt.tight_layout()
plt.show()
```

### Langkah 8 — Scatter Plot Fitur Kunci vs Produktivitas

```python
key_features = ['study_hours', 'sleep_hours', 'social_media_hours',
                'mental_health_score', 'focus_index', 'burnout_level']

fig, axes = plt.subplots(2, 3, figsize=(15, 9))

for ax, feat in zip(axes.flatten(), key_features):
    ax.scatter(df[feat], df['productivity_score'],
               alpha=0.2, s=10, color='steelblue')
    ax.set_xlabel(feat)
    ax.set_ylabel('productivity_score')
    ax.set_title(f'{feat} vs Produktivitas')

plt.suptitle('Hubungan Fitur Kunci dengan Produktivitas', fontsize=13)
plt.tight_layout()
plt.show()
```

### Langkah 9 — Analisis Burnout & Kesehatan Mental

```python
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Burnout vs Produktivitas (boxplot per level)
df['burnout_bin'] = pd.cut(df['burnout_level'], bins=4,
                            labels=['Rendah', 'Sedang', 'Tinggi', 'Sangat Tinggi'])
sns.boxplot(data=df, x='burnout_bin', y='productivity_score',
            palette='Reds', ax=axes[0])
axes[0].set_title('Produktivitas per Level Burnout')
axes[0].set_xlabel('Level Burnout')

# Mental Health Score vs Produktivitas
sns.boxplot(data=df, x='mental_health_score', y='productivity_score',
            palette='Blues', ax=axes[1])
axes[1].set_title('Produktivitas per Skor Kesehatan Mental')
axes[1].set_xlabel('Mental Health Score (1–10)')

plt.tight_layout()
plt.show()
```

---

## ⚙️ Persiapan Data untuk Modeling

```python
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# 1. Encode kolom kategorikal
le = LabelEncoder()
for col in ['gender', 'academic_level', 'internet_quality']:
    df[col] = le.fit_transform(df[col])

# 2. Buat target klasifikasi (high_productivity)
median_score = df['productivity_score'].median()   # ~36.9
df['high_productivity'] = (df['productivity_score'] >= median_score).astype(int)
print(f"High productivity (≥{median_score:.1f}):", df['high_productivity'].value_counts().to_dict())

# 3. Fitur yang digunakan (buang ID)
feature_cols = df.columns.drop(['student_id', 'productivity_score',
                                 'exam_score', 'high_productivity', 'burnout_bin']).tolist()

# 4. Split data — Regresi
X = df[feature_cols]
y_reg = df['productivity_score']
X_train, X_test, y_train, y_test = train_test_split(
    X, y_reg, test_size=0.2, random_state=42
)

# 5. Split data — Klasifikasi
y_clf = df['high_productivity']
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
    X, y_clf, test_size=0.2, random_state=42, stratify=y_clf
)

# 6. Normalisasi (opsional, untuk model berbasis jarak)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)
```

---

## 🤖 Bisa Digunakan untuk Apa Saja?

### 1. 📈 Regresi Produktivitas

**Target:** `productivity_score` (nilai kontinu 1–98)  
**Metrik:** MAE, RMSE, R², MAPE

```python
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np

model = Ridge()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("MAE :", mean_absolute_error(y_test, y_pred).round(4))
print("R²  :", r2_score(y_test, y_pred).round(4))
```

> Notebook tersedia: `01_productivity_linear_regression.ipynb`, `02_productivity_rf_regressor.ipynb`, `03_productivity_xgb_regressor.ipynb`

---

### 2. 🏷️ Klasifikasi Produktivitas Tinggi/Rendah

**Target:** `high_productivity` (0 = rendah, 1 = tinggi)  
**Metrik:** Accuracy, F1-Score, ROC-AUC

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train_scaled, y_train_c)
y_pred_c = clf.predict(X_test_scaled)

print(classification_report(y_test_c, y_pred_c))
```

> Notebook tersedia: `04_productivity_logistic.ipynb`, `05_productivity_rf_clf.ipynb`, `06_productivity_xgb_clf.ipynb`

---

### 3. 🔵 Clustering / Segmentasi Mahasiswa

**Algoritma:** KMeans, DBSCAN  
**Metrik:** Silhouette Score, Davies-Bouldin Index

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

X_clust = StandardScaler().fit_transform(X)
km = KMeans(n_clusters=2, random_state=42, n_init=10)
labels = km.fit_predict(X_clust)
print("Silhouette:", silhouette_score(X_clust, labels).round(4))
```

> Notebook tersedia: `07_productivity_kmeans.ipynb`, `08_productivity_dbscan.ipynb`

---

### 4. 🏆 Perbandingan Semua Model

Lihat perbandingan lengkap semua model (regresi + klasifikasi + clustering) dalam satu notebook:

> `00_productivity_model_comparison.ipynb`

---

## 📊 Karakteristik Data

```
Jumlah mahasiswa  : 5.000
Jumlah kolom      : 21
Missing value     : Tidak ada ✅
Nilai duplikat    : Tidak ada ✅

Distribusi gender:
  Male   : 1.719 (34.4%)
  Other  : 1.651 (33.0%)
  Female : 1.630 (32.6%)

Distribusi jenjang:
  Postgraduate : 1.687
  High School  : 1.672
  Undergraduate: 1.641

Rentang usia      : 16 – 25 tahun

productivity_score:
  Min    : 1.0
  Max    : 98.02
  Median : ~36.9
  Mean   : ~37.3

exam_score:
  Min    : 1.0
  Max    : 64.09
  Median : ~18.0
```

---

## 📁 Struktur Notebook

| File | Tugas | Target |
|------|-------|--------|
| `00_productivity_model_comparison.ipynb` | Perbandingan semua model | Semua |
| `01_productivity_linear_regression.ipynb` | Ridge Regression | `productivity_score` |
| `02_productivity_rf_regressor.ipynb` | Random Forest Regressor | `productivity_score` |
| `03_productivity_xgb_regressor.ipynb` | XGBoost Regressor | `productivity_score` |
| `04_productivity_logistic.ipynb` | Logistic Regression | `high_productivity` |
| `05_productivity_rf_clf.ipynb` | Random Forest Classifier | `high_productivity` |
| `06_productivity_xgb_clf.ipynb` | XGBoost Classifier | `high_productivity` |
| `07_productivity_kmeans.ipynb` | KMeans Clustering | Unsupervised |
| `08_productivity_dbscan.ipynb` | DBSCAN Clustering | Unsupervised |

---

## 🏅 Ringkasan Hasil Model (dari `00_productivity_model_comparison.ipynb`)

### Regresi (`productivity_score`)

| Peringkat | Model | MAE | RMSE | R² |
|-----------|-------|-----|------|-----|
| 🥇 1 | Ridge Regression | 4.1261 | 5.0068 | **0.9037** |
| 🥈 2 | XGBoost | 4.3215 | 5.2909 | 0.8925 |
| 🥉 3 | Random Forest | 4.5602 | 5.6450 | 0.8776 |

### Klasifikasi (`high_productivity`)

| Peringkat | Model | Accuracy | F1-Score | ROC-AUC |
|-----------|-------|----------|----------|---------|
| 🥇 1 | Logistic Regression | 0.914 | **0.9131** | **0.9773** |
| 🥈 2 | XGBoost | 0.904 | 0.9028 | 0.9744 |
| 🥉 3 | Random Forest | 0.898 | 0.8961 | 0.9660 |

> ℹ️ Ridge Regression unggul di regresi karena hubungan linier antara `focus_index`/`burnout_level` dan `productivity_score` sangat kuat. Semua model klasifikasi mencapai akurasi >90% karena target biner cenderung well-separated.

---

## 💡 Tips Eksplorasi Lanjutan

1. **Feature Importance** — gunakan `.feature_importances_` dari XGBoost/RF untuk tahu faktor terpenting
2. **Pair Plot** — `sns.pairplot(df[key_features + ['productivity_score']], hue='high_productivity')` untuk melihat separasi kelas
3. **PCA Visualization** — reduksi ke 2D untuk melihat pola clustering
4. **Target Alternatif** — coba `exam_score` sebagai target regresi selain `productivity_score`
5. **Interaction Features** — buat fitur baru seperti `study_efficiency = productivity_score / study_hours`

---

*Dataset ini cocok sebagai bahan latihan kompetisi Kaggle bertema student well-being, education analytics, atau lifestyle & academic performance prediction.*

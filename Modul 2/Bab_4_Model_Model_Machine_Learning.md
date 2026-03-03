# Bab 4 — Model-model Machine Learning untuk Data Tabel

Mari kita bahas model-model populer untuk data tabel dengan bahasa sederhana!

## Linear Regression (Regresi Linear)

**Apa itu?**
Model yang mencari garis lurus terbaik untuk memprediksi nilai numerik.

**Analogi**: Seperti menebak harga rumah dari luasnya. Makin luas, makin mahal — hubungannya linear (garis lurus).

**Formula Sederhana**: $y = mx + b$

**Kapan Digunakan**:
- ✅ Hubungan antara X dan Y linear
- ✅ Data tidak terlalu kompleks
- ✅ Butuh model yang mudah diinterpretasi

**Kelebihan**: Simple, cepat, mudah dijelaskan
**Kekurangan**: Hanya bisa tangkap hubungan linear, sensitif terhadap outlier

**Contoh Kasus**: Prediksi harga rumah dari luas, prediksi gaji dari pengalaman kerja

## Logistic Regression (Regresi Logistik)

**Apa itu?**
Model untuk klasifikasi yang memprediksi probabilitas suatu kategori.

**Analogi**: Seperti menebak apakah email adalah spam (0 atau 1).

**Kapan Digunakan**:
- ✅ Binary classification (2 kelas)
- ✅ Butuh probabilitas prediksi
- ✅ Hubungan linear antara fitur dan log-odds

**Kelebihan**: Output probabilitas, cepat, bagus untuk baseline
**Kekurangan**: Hanya untuk linear decision boundary

**Contoh Kasus**: Deteksi spam, prediksi churn, klasifikasi penyakit

## Decision Tree (Pohon Keputusan)

**Apa itu?**
Model yang membuat keputusan seperti flowchart dengan serangkaian pertanyaan.

**Analogi**: Seperti game "tebak binatang" — bertanya satu per satu sampai ketemu jawaban.

**Kapan Digunakan**:
- ✅ Butuh model yang mudah diinterpretasi
- ✅ Ada hubungan non-linear
- ✅ Fitur kategorikal banyak

**Kelebihan**: Sangat mudah dipahami, tidak perlu scaling, bisa tangkap non-linear
**Kekurangan**: Mudah overfit, tidak stabil

**Contoh Kasus**: Diagnosis medis, approval kredit, klasifikasi customer

## Random Forest

**Apa itu?**
Kumpulan banyak Decision Tree yang voting untuk hasil akhir.

**Analogi**: Seperti bertanya ke 100 orang ahli, lalu ambil jawaban mayoritas.

**Cara Kerja**:
1. Buat 100 decision tree dengan data random
2. Setiap tree memberikan prediksi
3. Ambil hasil mayoritas (classification) atau rata-rata (regression)

**Kapan Digunakan**:
- ✅ Data tabular dengan banyak fitur
- ✅ Butuh model yang robust dan akurat
- ✅ Tidak mau ribet tuning hyperparameter
- ✅ Baseline model yang bagus

**Kelebihan**: Sangat akurat, tidak mudah overfit, bagus out-of-the-box
**Kekurangan**: Lebih lambat, tidak mudah diinterpretasi

**Contoh Kasus**: Hampir semua kasus! Prediksi harga, klasifikasi fraud

## Gradient Boosting

**Apa itu?**
Model yang membangun tree secara bertahap, fokus memperbaiki kesalahan tree sebelumnya.

**Analogi**: Seperti belajar dari kesalahan. Tree pertama salah 20%, tree kedua fokus perbaiki 20% itu.

**Kapan Digunakan**:
- ✅ Kompetisi (sering menang!)
- ✅ Butuh akurasi tinggi
- ✅ Data tabular

**Kelebihan**: Sangat akurat, flexible
**Kekurangan**: Lebih lambat, mudah overfit jika tidak careful

## XGBoost (Extreme Gradient Boosting)

**Apa itu?**
Versi optimized dari Gradient Boosting. Lebih cepat, lebih akurat!

**Kenapa Populer?**
- Pemenang banyak kompetisi Kaggle
- Super cepat (optimized dengan C++)
- Built-in handling missing values

**Kapan Digunakan**:
- ✅ Kompetisi machine learning
- ✅ Data tabular besar
- ✅ Butuh akurasi maksimal

**Kelebihan**: Sangat cepat dan akurat, handle missing values otomatis
**Kekurangan**: Banyak hyperparameter, butuh tuning

**Contoh Kasus**: Hampir semua kompetisi Kaggle dengan data tabular!

## LightGBM (Light Gradient Boosting Machine)

**Apa itu?**
Gradient boosting yang sangat cepat dan efisien untuk dataset besar.

**Analogi**: XGBoost yang "diet" — lebih ringan dan lebih cepat.

**Kapan Digunakan**:
- ✅ Dataset sangat besar (>100k rows)
- ✅ Butuh training cepat
- ✅ Memory terbatas

**Kelebihan**: Sangat cepat, efisien memory, akurasi tinggi
**Kekurangan**: Mudah overfit di data kecil

**Contoh Kasus**: Dataset besar (clickstream, transactions)

## CatBoost (Categorical Boosting)

**Apa itu?**
Gradient boosting yang sangat bagus untuk data dengan banyak fitur kategorikal.

**Analogi**: Gradient boosting yang "spesialis kategori" — tidak perlu encoding manual!

**Keunikan**: Handle categorical features tanpa encoding

**Kapan Digunakan**:
- ✅ Banyak fitur kategorikal
- ✅ Tidak mau ribet encoding
- ✅ Butuh model robust

**Kelebihan**: Tidak perlu encoding manual, robust, default parameters bagus
**Kekurangan**: Lebih lambat dari LightGBM

## KNN (K-Nearest Neighbors)

**Apa itu?**
Model yang memprediksi berdasarkan "tetangga terdekat" dalam data.

**Analogi**: Seperti bertanya ke 5 tetangga terdekat untuk voting.

**Kapan Digunakan**:
- ✅ Data kecil
- ✅ Decision boundary kompleks
- ✅ Butuh model simple

**Kelebihan**: Sangat simple, tidak ada training phase
**Kekurangan**: Sangat lambat untuk prediksi, sensitif terhadap scale (WAJIB scaling!)

**Contoh Kasus**: Recommendation system, pattern recognition

## SVM (Support Vector Machine)

**Apa itu?**
Model yang mencari "jalan tengah" terbaik untuk memisahkan dua kelas.

**Analogi**: Menggambar garis di tengah dua kelompok, dengan jarak semaksimal mungkin.

**Kapan Digunakan**:
- ✅ Binary classification
- ✅ Data high-dimensional
- ✅ Clear margin antara kelas

**Kelebihan**: Efektif di high-dimensional space, memory efficient
**Kekurangan**: Lambat untuk dataset besar, sensitif terhadap scaling (WAJIB scaling!)

**Contoh Kasus**: Text classification, image recognition

## Naive Bayes

**Apa itu?**
Model probabilistik yang menggunakan Teorema Bayes dengan asumsi "naive" (fitur independen).

**Analogi**: Detective yang menghitung probabilitas tersangka berdasarkan bukti.

**Kapan Digunakan**:
- ✅ Text classification (spam filter)
- ✅ Dataset kecil
- ✅ Butuh model cepat
- ✅ Real-time prediction

**Kelebihan**: Sangat cepat, bagus untuk text data
**Kekurangan**: Asumsi independen jarang benar di real world

**Contoh Kasus**: Spam detection, sentiment analysis

## Neural Network / MLP (Multi-Layer Perceptron)

**Apa itu?**
Jaringan neuron buatan yang terinspirasi dari otak manusia.

**Analogi**: Seperti otak dengan banyak neuron yang saling terhubung.

**Kapan Digunakan**:
- ✅ Data sangat besar
- ✅ Pola sangat kompleks
- ✅ Image, audio, text

**Kelebihan**: Bisa tangkap pola sangat kompleks, flexible
**Kekurangan**: Butuh data banyak, sangat lambat, black box (WAJIB scaling!)

**Contoh Kasus**: Image recognition, NLP, speech recognition

---

## Tabel Ringkasan Model

### Perbandingan Model untuk Classification

| Model | Kecepatan | Akurasi | Interpretability | Butuh Scaling? | Cocok untuk |
|-------|-----------|---------|------------------|----------------|-------------|
| Logistic Regression | ⚡⚡⚡ | ⭐⭐ | ✅ Mudah | Ya | Baseline, linear |
| Decision Tree | ⚡⚡⚡ | ⭐⭐ | ✅ Sangat mudah | Tidak | Interpretasi |
| Random Forest | ⚡⚡ | ⭐⭐⭐⭐ | ❌ Sulit | Tidak | General purpose |
| XGBoost | ⚡⚡ | ⭐⭐⭐⭐⭐ | ❌ Sulit | Tidak | Kompetisi |
| LightGBM | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ | ❌ Sulit | Tidak | Data besar |
| CatBoost | ⚡⚡ | ⭐⭐⭐⭐⭐ | ❌ Sulit | Tidak | Banyak kategori |
| KNN | ⚡ | ⭐⭐⭐ | ✅ Mudah | Ya! | Data kecil |
| SVM | ⚡ | ⭐⭐⭐⭐ | ❌ Sulit | Ya! | High-dimensional |
| Naive Bayes | ⚡⚡⚡ | ⭐⭐ | ✅ Mudah | Tidak | Text, real-time |
| Neural Network | ⚡ | ⭐⭐⭐⭐⭐ | ❌ Black box | Ya! | Data sangat besar |

### Kapan Pakai Model Apa?

| Situasi | Model Rekomendasi |
|---------|-------------------|
| **Baru mulai, butuh baseline cepat** | Logistic Regression, Random Forest |
| **Kompetisi Kaggle** | XGBoost, LightGBM, CatBoost + Ensemble |
| **Data sangat besar (jutaan rows)** | LightGBM, Neural Network |
| **Banyak fitur kategorikal** | CatBoost, Random Forest |
| **Butuh interpretasi model** | Decision Tree, Logistic Regression |
| **Data kecil (<1000 rows)** | Logistic Regression, KNN, Naive Bayes |
| **Text classification** | Naive Bayes, Logistic Regression |
| **Image/Audio data** | Neural Network (CNN, RNN) |
| **Real-time prediction** | Logistic Regression, Naive Bayes |
| **Tidak tahu harus pakai apa** | Random Forest (selalu safe!) |

---

## Hyperparameter: Apa Itu dan Bagaimana Menggunakannya?

### 🔧 Apa itu Hyperparameter?

**Hyperparameter** adalah parameter yang kita **set SEBELUM training** model dimulai. Berbeda dengan parameter biasa (weights/coefficients) yang dipelajari model saat training.

**Analogi Sederhana**:
- **Parameter** = Skill yang dipelajari pemain sepak bola saat latihan (passing accuracy, shooting power)
- **Hyperparameter** = Aturan latihan yang kita set (durasi latihan, intensitas, jumlah repetisi)

### 🎯 Kenapa Hyperparameter Penting?

Hyperparameter yang tepat bisa:
- ✅ **Meningkatkan akurasi** model (dari 80% ke 90%!)
- ✅ **Mencegah overfitting** (model tidak hafalan)
- ✅ **Mempercepat training** (efisiensi waktu)
- ✅ **Menghemat memori** (untuk deployment)

### 📊 Hyperparameter Penting per Model

#### 1. **Random Forest**

| Hyperparameter | Default | Range Umum | Fungsi | Kapan Diubah? |
|----------------|---------|------------|--------|---------------|
| `n_estimators` | 100 | 50-500 | Jumlah pohon | Akurasi kurang, tambah! |
| `max_depth` | None | 3-20 | Kedalaman pohon | Overfitting, kurangi! |
| `min_samples_split` | 2 | 2-20 | Min samples untuk split | Overfitting, naikkan! |
| `min_samples_leaf` | 1 | 1-10 | Min samples di leaf | Generalisasi, naikkan! |
| `max_features` | 'sqrt' | 'sqrt', 'log2', None | Fitur per split | Variance tinggi, ubah! |

**Tips Praktis:**
- Start dengan **default** dulu (n_estimators=100, max_depth=None)
- Jika **overfitting**: Turunkan `max_depth` ke 10-15, naikkan `min_samples_split` ke 5-10
- Jika **akurasi kurang**: Naikkan `n_estimators` ke 200-500
- Baseline bagus: `RandomForestClassifier(n_estimators=100, max_depth=10, min_samples_split=5)`

#### 2. **XGBoost / Gradient Boosting**

| Hyperparameter | Default | Range Umum | Fungsi | Kapan Diubah? |
|----------------|---------|------------|--------|---------------|
| `n_estimators` | 100 | 50-1000 | Jumlah boosting rounds | Underfitting, tambah! |
| `learning_rate` | 0.3 | 0.001-0.3 | Kecepatan belajar | Overfitting, kurangi! |
| `max_depth` | 6 | 3-10 | Kedalaman pohon | Overfitting, kurangi! |
| `subsample` | 1.0 | 0.5-1.0 | Proporsi data per tree | Overfitting, kurangi! |
| `colsample_bytree` | 1.0 | 0.5-1.0 | Proporsi fitur per tree | Variance tinggi, kurangi! |

**Tips Praktis:**
- Baseline: `learning_rate=0.1, n_estimators=100, max_depth=6`
- **Trade-off penting**: `learning_rate` kecil perlu `n_estimators` besar
- Jika **overfitting**: Kurangi `max_depth` ke 3-5, `learning_rate` ke 0.01, `subsample` ke 0.8
- Jika **underfitting**: Naikkan `n_estimators` ke 500-1000, `max_depth` ke 8-10

#### 3. **Logistic Regression**

| Hyperparameter | Default | Range Umum | Fungsi | Kapan Diubah? |
|----------------|---------|------------|--------|---------------|
| `C` | 1.0 | 0.001-100 | Regularization strength (inverse) | Overfitting/underfitting |
| `penalty` | 'l2' | 'l1', 'l2', 'elasticnet' | Jenis regularization | Feature selection |
| `max_iter` | 100 | 100-5000 | Maksimum iterasi | Model tidak converge |
| `solver` | 'lbfgs' | 'lbfgs', 'liblinear', 'sag' | Algorithm optimisasi | Tipe penalty |

**Tips Praktis:**
- Baseline: `C=1.0, penalty='l2', max_iter=1000`
- Jika **overfitting**: Kurangi `C` ke 0.01-0.1 (regularization lebih kuat)
- Jika **underfitting**: Naikkan `C` ke 10-100 (regularization lebih lemah)
- Jika **tidak converge**: Naikkan `max_iter` ke 2000-5000

#### 4. **Decision Tree**

| Hyperparameter | Default | Range Umum | Fungsi | Kapan Diubah? |
|----------------|---------|------------|--------|---------------|
| `max_depth` | None | 3-20 | Kedalaman maksimum | SELALU SET! (prevent overfit) |
| `min_samples_split` | 2 | 2-20 | Min samples untuk split | Overfitting |
| `min_samples_leaf` | 1 | 1-10 | Min samples di leaf | Generalisasi |
| `criterion` | 'gini' | 'gini', 'entropy' | Ukuran split quality | Experiment |

**Tips Praktis:**
- **JANGAN pakai default `max_depth=None`** → 99% overfit!
- Baseline: `max_depth=5, min_samples_split=10, min_samples_leaf=5`
- Decision Tree sangat **mudah overfit** → WAJIB regularisasi!

#### 5. **KNN (K-Nearest Neighbors)**

| Hyperparameter | Default | Range Umum | Fungsi | Kapan Diubah? |
|----------------|---------|------------|--------|---------------|
| `n_neighbors` | 5 | 3-20 | Jumlah tetangga terdekat | Bias-variance trade-off |
| `metric` | 'minkowski' | 'euclidean', 'manhattan' | Distance metric | Tipe data |
| `weights` | 'uniform' | 'uniform', 'distance' | Bobot tetangga | Improve accuracy |

**Tips Praktis:**
- Baseline: `n_neighbors=5, weights='uniform'`
- **K kecil (3)**: Lebih sensitive, risk overfit
- **K besar (20)**: Lebih smooth, risk underfit
- **Rule of thumb**: K ≈ √n (akar jumlah sampel), tapi coba 3-20

### 🎯 Cara Menentukan Hyperparameter Terbaik

Ada beberapa metode:

#### **1. Manual Trial-and-Error** 😓
Coba satu-satu, lihat mana yang terbaik.
- **Pros**: Simple, belajar banyak tentang model
- **Cons**: Lama, tidak exhaustive

#### **2. Grid Search** 🔍
Coba SEMUA kombinasi dari list parameter yang kita tentukan.

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15],
    'min_samples_split': [2, 5, 10]
}

grid = GridSearchCV(
    RandomForestClassifier(),
    param_grid,
    cv=5,  # 5-fold cross-validation
    scoring='f1'
)

grid.fit(X_train, y_train)
print(f"Best params: {grid.best_params_}")
print(f"Best score: {grid.best_score_}")
```

- **Pros**: Exhaustive, menemukan best combination
- **Cons**: SANGAT LAMA untuk banyak parameter (3×3×3×5fold = 135 training!)

#### **3. Random Search** 🎲
Coba kombinasi RANDOM dari parameter distribution.

```python
from sklearn.model_selection import RandomizedSearchCV

param_dist = {
    'n_estimators': [50, 100, 200, 300, 500],
    'max_depth': [3, 5, 7, 10, 15, 20],
    'min_samples_split': [2, 5, 10, 20]
}

random = RandomizedSearchCV(
    RandomForestClassifier(),
    param_dist,
    n_iter=20,  # Coba 20 kombinasi random
    cv=5,
    scoring='f1'
)

random.fit(X_train, y_train)
```

- **Pros**: Lebih cepat dari Grid Search, good balance
- **Cons**: Mungkin tidak menemukan absolut best

#### **4. Bayesian Optimization** 🧠
Smart search yang belajar dari hasil sebelumnya. Advanced!

### 📌 Best Practices Hyperparameter Tuning

#### **DO ✅**

1. **Start dengan default** dulu sebagai baseline
2. **Fokus pada parameter paling impactful** (n_estimators, max_depth, learning_rate)
3. **Gunakan cross-validation** untuk avoid overfitting to validation set
4. **Monitor training time** - kadang improvement sedikit tapi waktu 10x lebih lama
5. **Dokumentasi hasil** - catat parameter apa yang sudah dicoba
6. **Prioritas metric** sesuai use case (medical = recall, spam = precision)

#### **DON'T ❌**

1. **Jangan tune semua parameter sekaligus** - mulai dari yang impactful
2. **Jangan tune tanpa validation set** - risk overfit test data!
3. **Jangan percaya hanya 1 fold** - gunakan k-fold CV (minimal 5)
4. **Jangan pakai model kompleks untuk data kecil** (<100 samples → simple model!)
5. **Jangan lupa scaling** untuk model yang sensitif (Logistic Regression, KNN, SVM)
6. **Jangan tune terlalu lama** jika gain sudah minimal (80%→81% butuh 10x waktu?)

### 🚀 Workflow Praktis Tuning

```
1. Split data → Train/Validation/Test (60/20/20)

2. Baseline model (default parameters)
   ├─ Evaluate pada validation set
   └─ Catat score baseline

3. Tuning parameter 1-by-1 (most impactful first)
   ├─ Random Forest: n_estimators → max_depth → min_samples_split
   ├─ XGBoost: learning_rate → n_estimators → max_depth
   └─ Logistic Reg: C → penalty → solver

4. Grid/Random Search untuk fine-tuning
   ├─ Parameter range yang sudah narrowed down
   └─ Cross-validation 5-fold

5. Evaluate best model pada TEST set (ONLY ONCE!)
   └─ Jika hasilnya jauh dari validation → cek overfitting

6. Re-train dengan ALL data (train+val+test) untuk production
   └─ Gunakan best parameters yang sudah ditemukan
```

### 💡 Rule of Thumb per Use Case

| Use Case | Prioritas Parameter | Target Metric | Rekomendasi |
|----------|-------------------|---------------|-------------|
| **Medical Diagnosis** | max_depth (avoid overfit) | **Recall** | Turunkan threshold, prioritas FN rendah |
| **Spam Detection** | C (regularization) | **Precision** | Naikkan threshold, prioritas FP rendah |
| **Kompetisi Kaggle** | Semua parameter! | Leaderboard score | Ensemble, stacking, blending |
| **Production (real-time)** | n_estimators (speed) | Speed + Acc balance | Kurangi n_estimators, simple model |
| **Interpretability** | max_depth (shallow tree) | Accuracy + Explain | Decision Tree depth=3-5 |

### 🔬 Contoh Tuning Step-by-Step

**Problem**: Prediksi Diabetes (Recall prioritas)

```
Step 1: Baseline Random Forest
- Default params → Recall: 0.75

Step 2: Tune n_estimators
- Try [50, 100, 200, 500]
- Best: 200 → Recall: 0.78 (+3%)

Step 3: Tune max_depth
- Try [5, 10, 15, 20, None]
- Best: 15 → Recall: 0.82 (+4%)

Step 4: Tune min_samples_split
- Try [2, 5, 10, 20]
- Best: 5 → Recall: 0.83 (+1%)

Step 5: Fine-tuning dengan GridSearch
- n_estimators: [150, 200, 250]
- max_depth: [12, 15, 18]
- min_samples_split: [3, 5, 7]
- Best combo → Recall: 0.85

Improvement: 0.75 → 0.85 (+13% relative!)
```

### 📊 Tabel Cheat Sheet Hyperparameter

| Model | Must-Tune | Nice-to-Tune | Usually Default OK |
|-------|-----------|--------------|-------------------|
| **Random Forest** | n_estimators, max_depth | min_samples_split | max_features, criterion |
| **XGBoost** | learning_rate, n_estimators | max_depth, subsample | gamma, reg_alpha |
| **Logistic Reg** | C | penalty, solver | max_iter (if converge) |
| **Decision Tree** | max_depth | min_samples_split | criterion, splitter |
| **KNN** | n_neighbors | weights, metric | algorithm, leaf_size |

---

*Modul 2 — Cara Mengolah Data Tabel dengan Machine Learning*

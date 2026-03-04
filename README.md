# 📚 Module Kaggle & Machine Learning

> **Repository pembelajaran lengkap tentang Kaggle, Machine Learning, dan Evaluation Metrics**  
> Lengkap dengan teori, 3 studi kasus nyata, dan **26 Jupyter Notebook** yang siap dijalankan!

---

## 📖 Tentang Repository Ini

Repository ini berisi materi pembelajaran komprehensif untuk memahami:
1. **Cara membuat kompetisi data di Kaggle**
2. **Dasar-dasar Machine Learning dengan data tabel**
3. **Evaluation metrics untuk mengukur performa model**
4. **Praktik langsung dengan dataset real dan Jupyter Notebook**
5. **Studi kasus: Student Dropout, Toyota Stock Price, Student Productivity**

**Cocok untuk:** Pemula, mahasiswa, data science enthusiast, dan siapa saja yang ingin memahami ML secara mendalam!

---

## 📁 Struktur Repository

```
module-kaggle/
│
├── Modul 1/                              # 📘 Cara Membuat Event Kompetisi Data di Kaggle
│   ├── Bab_1_Pendahuluan.md
│   ├── Bab_2_Persiapan_Sebelum_Membuat_Kompetisi.md
│   ├── Bab_3_Langkah_Langkah_Membuat_Kompetisi.md
│   ├── Bab_4_Tips_Agar_Kompetisi_Menarik.md
│   ├── Bab_5_Studi_Kasus_Sederhana.md
│   └── Bab_6_Kesimpulan.md
│
├── Modul 2/                              # 📗 Cara Mengolah Data Tabel dengan Machine Learning
│   ├── Bab_1_Apa_itu_Data_Tabel.md
│   ├── Bab_2_Tahapan_Mengolah_Data.md
│   ├── Bab_3_Jenis_Jenis_Machine_Learning.md
│   ├── Bab_4_Model_Model_Machine_Learning.md
│   ├── Bab_5_Workflow_Machine_Learning.md
│   └── Bab_6_Kesimpulan.md
│
├── Modul 3/                              # 📙 Evaluation Metrics untuk Mengantarkan Model Produksi
│   ├── Bab_1_Kenapa_Evaluation_Metric_Penting.md
│   ├── Bab_2_Evaluation_Regression.md
│   ├── Bab_3_Evaluation_Classification.md
│   ├── Bab_4_Korelasi_Antar_Metric.md
│   ├── Bab_5_Tabel_Ringkasan_Metric.md
│   └── Bab_6_Kesimpulan.md
│
├── Contoh/                               # 💻 Praktik Langsung dengan Jupyter Notebook
│   ├── student_dropout_dataset_v3.csv    # Dataset student dropout
│   ├── Toyota_Stock_Prices_1980_2026.csv # Dataset harga saham Toyota
│   ├── ultimate_student_productivity_dataset_5000.csv  # Dataset produktivitas mahasiswa
│   ├── requirements.txt
│   ├── README_Praktik_ML.md
│   │
│   ├── 01_Student_Dropout/               # Prediksi dropout & prediksi CGPA
│   │   ├── README.md                     # 📄 Panduan dataset & EDA
│   │   ├── 00_dropout_model_comparison.ipynb  # ⭐ Perbandingan semua model
│   │   ├── 01_dropout_logistic_regression.ipynb
│   │   ├── 02_dropout_random_forest.ipynb
│   │   ├── 03_dropout_xgboost.ipynb
│   │   ├── 04_dropout_svm.ipynb
│   │   ├── 05_dropout_neural_network.ipynb
│   │   ├── 06_cgpa_linear_regression.ipynb
│   │   ├── 07_cgpa_random_forest_regressor.ipynb
│   │   ├── 08_cgpa_xgboost_regressor.ipynb
│   │   └── saved_models/
│   │
│   ├── 02_Toyota_Stock/                  # Prediksi harga saham Toyota
│   │   ├── README.md                     # 📄 Panduan dataset & EDA
│   │   ├── 00_stock_model_comparison.ipynb    # ⭐ Perbandingan semua model
│   │   ├── 01_stock_arima.ipynb
│   │   ├── 02_stock_prophet.ipynb
│   │   ├── 03_stock_lstm.ipynb
│   │   ├── 04_stock_gru.ipynb
│   │   ├── 05_stock_random_forest.ipynb
│   │   ├── 06_stock_xgboost.ipynb
│   │   ├── 07_stock_linear_regression.ipynb
│   │   └── saved_models/
│   │
│   └── 03_Student_Productivity/          # Analisis & prediksi produktivitas mahasiswa
│       ├── README.md                     # 📄 Panduan dataset & EDA
│       ├── 00_productivity_model_comparison.ipynb  # ⭐ Perbandingan semua model
│       ├── 01_productivity_linear_regression.ipynb
│       ├── 02_productivity_rf_regressor.ipynb
│       ├── 03_productivity_xgb_regressor.ipynb
│       ├── 04_productivity_logistic.ipynb
│       ├── 05_productivity_rf_clf.ipynb
│       ├── 06_productivity_xgb_clf.ipynb
│       ├── 07_productivity_kmeans.ipynb
│       ├── 08_productivity_dbscan.ipynb
│       └── saved_models/
│
├── fix_xgb.py                            # 🔧 Utility: fix XGBoost early_stopping_rounds
├── fix_xgb2.py                           # 🔧 Utility: fix XGBoost API compatibility
├── LICENSE
└── README.md                             # 📄 File ini
```

---

## 🎓 Modul Pembelajaran

### 📘 Modul 1: Cara Membuat Event Kompetisi Data di Kaggle

**Deskripsi:**  
Pelajari langkah demi langkah cara membuat kompetisi data di platform Kaggle, mulai dari persiapan dataset hingga meluncurkan kompetisi yang menarik.

**Topik yang Dibahas:**
- ✅ Pengenalan Kaggle dan manfaat kompetisi data
- ✅ Persiapan sebelum membuat kompetisi (dataset, problem definition, evaluation metric)
- ✅ Langkah-langkah teknis membuat kompetisi di Kaggle
- ✅ Tips membuat kompetisi yang engaging dan sukses
- ✅ Studi kasus kompetisi sederhana
- ✅ Best practices dan hal yang perlu dihindari

**Target Pembaca:** Pendidik, peneliti, organisasi, atau siapa saja yang ingin membuat kompetisi data.

---

### 📗 Modul 2: Cara Mengolah Data Tabel dengan Machine Learning

**Deskripsi:**  
Memahami fundamental machine learning untuk data tabel, dari konsep dasar hingga workflow lengkap.

**Topik yang Dibahas:**
- ✅ Pengertian data tabel dan ciri-cirinya
- ✅ Tahapan mengolah data (EDA, cleaning, feature engineering, scaling)
- ✅ Jenis-jenis machine learning (Supervised, Unsupervised, Reinforcement)
- ✅ Model-model ML populer (Linear/Logistic Regression, Decision Tree, Random Forest, XGBoost, Neural Network)
- ✅ Workflow ML end-to-end (dari data mentah hingga deployment)
- ✅ Handling overfitting, underfitting, dan cross-validation

**Target Pembaca:** Pemula yang ingin memahami ML secara konseptual dengan bahasa yang mudah dipahami.

---

### 📙 Modul 3: Evaluation Metrics untuk Mengantarkan Model Produksi

**Deskripsi:**  
Deep dive ke evaluation metrics untuk regression dan classification, lengkap dengan formula matematis dan interpretasi praktis.

**Topik yang Dibahas:**
- ✅ Kenapa evaluation metric sangat penting
- ✅ **Regression metrics:** MAE, MSE, RMSE, R², MAPE
- ✅ **Classification metrics:** Accuracy, Precision, Recall, F1-Score, ROC-AUC, Confusion Matrix
- ✅ Korelasi antar metric dan kapan menggunakan metric tertentu
- ✅ Tabel ringkasan lengkap semua metric
- ✅ Trade-off precision vs recall
- ✅ Interpretasi metric di berbagai use case

**Target Pembaca:** Praktisi ML yang ingin memahami cara evaluasi model secara komprehensif.

---

## 💻 Praktik dengan Jupyter Notebook

Folder `Contoh/` berisi **26 Jupyter Notebook** yang diorganisasi dalam 3 studi kasus nyata.  
Setiap studi kasus dilengkapi **README.md** berisi panduan dataset, EDA langkap-demi-langkah, dan ringkasan hasil.

### 1️⃣ Student Dropout Prediction (`01_Student_Dropout/`)
**Dataset:** `student_dropout_dataset_v3.csv` — 10.000 baris × 19 kolom  
📄 [Lihat README lengkap →](Contoh/01_Student_Dropout/README.md)

Dua problem sekaligus: **klasifikasi dropout** dan **prediksi CGPA (regresi)**.

| # | File | Task | Model |
|---|------|------|-------|
| ⭐ | `00_dropout_model_comparison.ipynb` | Perbandingan | Semua model |
| 01 | `01_dropout_logistic_regression.ipynb` | Classification | Logistic Regression |
| 02 | `02_dropout_random_forest.ipynb` | Classification | Random Forest |
| 03 | `03_dropout_xgboost.ipynb` | Classification | XGBoost |
| 04 | `04_dropout_svm.ipynb` | Classification | SVM |
| 05 | `05_dropout_neural_network.ipynb` | Classification | Neural Network |
| 06 | `06_cgpa_linear_regression.ipynb` | Regression | Linear Regression |
| 07 | `07_cgpa_random_forest_regressor.ipynb` | Regression | Random Forest |
| 08 | `08_cgpa_xgboost_regressor.ipynb` | Regression | XGBoost |

- **Metrics (Klasifikasi):** Accuracy, Precision, Recall, F1, ROC-AUC, Confusion Matrix
- **Metrics (Regresi):** MAE, RMSE, R²
- Model terbaik disimpan di `saved_models/`

**Hasil Perbandingan Model (Klasifikasi Dropout):**

| Peringkat | Model | Accuracy | F1-Score | ROC-AUC |
|-----------|-------|----------|----------|---------|
| 🥇 1 | Logistic Regression | ~0.68 | 0.587 | **0.821** |
| 🥈 2 | XGBoost | ~0.67 | 0.575 | 0.809 |
| 🥉 3 | Random Forest | ~0.67 | 0.569 | 0.806 |

---

### 2️⃣ Toyota Stock Price Prediction (`02_Toyota_Stock/`)
**Dataset:** `Toyota_Stock_Prices_1980_2026.csv` — 11.508 baris, 1980–2026  
📄 [Lihat README lengkap →](Contoh/02_Toyota_Stock/README.md)

Prediksi harga saham Toyota menggunakan berbagai pendekatan **time series** dan **ML klasik**.

| # | File | Model |
|---|------|-------|
| ⭐ | `00_stock_model_comparison.ipynb` | Perbandingan semua model |
| 01 | `01_stock_arima.ipynb` | ARIMA |
| 02 | `02_stock_prophet.ipynb` | Prophet |
| 03 | `03_stock_lstm.ipynb` | LSTM (Deep Learning) |
| 04 | `04_stock_gru.ipynb` | GRU (Deep Learning) |
| 05 | `05_stock_random_forest.ipynb` | Random Forest |
| 06 | `06_stock_xgboost.ipynb` | XGBoost |
| 07 | `07_stock_linear_regression.ipynb` | Linear Regression |

- **Metrics:** MAE, RMSE, MAPE, Directional Accuracy, R²
- Model disimpan di `saved_models/` (format `.json`, `.h5`, `.pth`)

**Hasil Perbandingan Model:**

| Peringkat | Model | Pendekatan | Keunggulan |
|-----------|-------|------------|------------|
| 🥇 1 | Ridge Regression | ML + fitur lag | MAE & R² terbaik |
| 🥈 2 | XGBoost | ML + fitur lag | RMSE rendah |
| 🥉 3 | Random Forest | ML + fitur lag | Robust terhadap outlier |
| 4 | GRU | Deep Learning | Tangkap pola sekuensial |
| 5 | LSTM | Deep Learning | Memori jangka panjang |
| 6 | Prophet | Statistik | Deteksi seasonality |
| 7 | ARIMA | Statistik | Baseline klasik |

---

### 3️⃣ Student Productivity Analysis (`03_Student_Productivity/`)
**Dataset:** `ultimate_student_productivity_dataset_5000.csv` — 5.000 baris × 21 kolom  
📄 [Lihat README lengkap →](Contoh/03_Student_Productivity/README.md)

Analisis produktivitas mahasiswa — mencakup **regresi**, **klasifikasi**, dan **clustering**.

| # | File | Task | Model |
|---|------|------|-------|
| ⭐ | `00_productivity_model_comparison.ipynb` | Perbandingan | Semua model |
| 01 | `01_productivity_linear_regression.ipynb` | Regression | Linear Regression |
| 02 | `02_productivity_rf_regressor.ipynb` | Regression | Random Forest |
| 03 | `03_productivity_xgb_regressor.ipynb` | Regression | XGBoost |
| 04 | `04_productivity_logistic.ipynb` | Classification | Logistic Regression |
| 05 | `05_productivity_rf_clf.ipynb` | Classification | Random Forest |
| 06 | `06_productivity_xgb_clf.ipynb` | Classification | XGBoost |
| 07 | `07_productivity_kmeans.ipynb` | Clustering | K-Means |
| 08 | `08_productivity_dbscan.ipynb` | Clustering | DBSCAN |

- Model terbaik disimpan di `saved_models/`

**Hasil Perbandingan Model:**

*Regresi (`productivity_score`):*

| Peringkat | Model | MAE | RMSE | R² |
|-----------|-------|-----|------|----|
| 🥇 1 | Ridge Regression | 4.126 | 5.007 | **0.904** |
| 🥈 2 | XGBoost | 4.322 | 5.291 | 0.893 |
| 🥉 3 | Random Forest | 4.560 | 5.645 | 0.878 |

*Klasifikasi (`high_productivity`):*

| Peringkat | Model | Accuracy | F1-Score | ROC-AUC |
|-----------|-------|----------|----------|---------|
| 🥇 1 | Logistic Regression | 0.914 | **0.913** | **0.977** |
| 🥈 2 | XGBoost | 0.904 | 0.903 | 0.974 |
| 🥉 3 | Random Forest | 0.898 | 0.896 | 0.966 |

---

## 🚀 Cara Menggunakan Repository Ini

### 1. Clone Repository
```bash
git clone <repository-url>
cd module-kaggle
```

### 2. Setup Virtual Environment (Opsional tapi Disarankan)
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# atau
.venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
cd Contoh
pip install -r requirements.txt
```

### 4. Baca Modul Teori
Mulai dari **Modul 1 → 2 → 3** untuk memahami konsep dasar.

### 5. Jalankan Notebook
```bash
jupyter notebook
```

Buka file `.ipynb` dan jalankan cell-by-cell untuk melihat hasilnya.

---

## 📦 Dependencies

Library yang digunakan di praktik:

```txt
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
scikit-learn>=1.3.0
xgboost>=2.0.0
prophet>=1.1.0
tensorflow>=2.13.0   # LSTM & GRU
torch>=2.0.0         # PyTorch models
jupyter>=1.0.0
notebook>=7.0.0
ipykernel>=6.25.0
```

Install semua dengan:
```bash
pip install -r Contoh/requirements.txt
```

---

## 🎯 Learning Path yang Disarankan

### Untuk Pemula Absolut:
1. 📗 **Modul 2** → Pahami dasar ML dulu
2. 📙 **Modul 3** → Pelajari evaluation metrics
3. 💻 **01_Student_Dropout** (notebook 01–05) → Klasifikasi dengan berbagai model
4. 💻 **03_Student_Productivity** (notebook 01–03) → Regresi dengan dataset besar
5. 📘 **Modul 1** → Belajar buat kompetisi (opsional)

### Untuk yang Sudah Paham Konsep:
1. 💻 **02_Toyota_Stock** → Time series (ARIMA, Prophet, LSTM, GRU)
2. 📙 **Modul 3** → Deep dive metrics
3. 💻 **03_Student_Productivity** (notebook 07–08) → Clustering (K-Means & DBSCAN)
4. 📘 **Modul 1** → Buat kompetisi sendiri

### Untuk Persiapan Interview:
1. 📗 **Modul 2 Bab 4** → Review model-model ML
2. 📙 **Modul 3** → Hafal semua metrics
3. 💻 Pilih satu studi kasus dan pelajari perbandingan antar model
4. Pahami trade-off setiap algoritma dari hasil notebook

---

## 🌟 Highlight Features

### ✨ Teori yang Mudah Dipahami
- Bahasa Indonesia yang jelas
- Analogi sederhana untuk konsep kompleks
- Banyak contoh konkret
- Dari dasar hingga advanced

### ✨ Praktik yang Langsung Bisa Dipakai
- Dataset real (bukan toy dataset)
- Notebook yang well-documented
- Visualisasi yang informatif
- Interpretasi hasil yang lengkap

### ✨ Studi Kasus Nyata dengan Dataset Real
- 3 studi kasus: Student Dropout, Stock Price, Student Productivity
- 23 notebook yang bisa langsung dijalankan
- Perbandingan berbagai model pada dataset yang sama
- Model disimpan dan siap digunakan ulang

### ✨ End-to-End Learning
- Dari konsep → praktik → implementasi
- Dari data mentah → model → evaluasi
- Dari pemula → intermediate → advanced

---

## 🎓 Siapa yang Cocok Menggunakan Repository Ini?

✅ **Mahasiswa** yang belajar data science / machine learning  
✅ **Self-learner** yang ingin belajar ML secara terstruktur  
✅ **Praktisi** yang ingin refresh konsep dasar  
✅ **Pendidik** yang butuh materi ajar ML  
✅ **Job seeker** yang persiapan interview data science  
✅ **Peneliti** yang ingin buat kompetisi di Kaggle

---

## 📚 Referensi & Resources Tambahan

### Platform Belajar:
- [Kaggle Learn](https://www.kaggle.com/learn) - Free courses
- [Kaggle Competitions](https://www.kaggle.com/competitions) - Ikut kompetisi!
- [Scikit-Learn Documentation](https://scikit-learn.org/stable/documentation.html)

### Buku Rekomendasi:
- "Hands-On Machine Learning" by Aurélien Géron
- "Introduction to Statistical Learning" by James, Witten, Hastie, Tibshirani
- "Pattern Recognition and Machine Learning" by Christopher Bishop

### Dataset untuk Latihan:
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Google Dataset Search](https://datasetsearch.research.google.com/)

---

## 🤝 Kontribusi

Jika Anda menemukan kesalahan, typo, atau ingin menambah konten:
1. Fork repository ini
2. Buat branch baru (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -m 'Menambah fitur X'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

**Kontribusi yang diterima:**
- Perbaikan typo/grammar
- Tambahan contoh
- Implementasi algoritma baru
- Dataset baru
- Visualisasi yang lebih baik
- Dokumentasi yang lebih jelas

---

## 📝 Lisensi

Repository ini dibuat untuk tujuan edukatif dan pembelajaran. Silakan gunakan, modifikasi, dan distribusikan dengan menyebutkan sumber.

---

## 📧 Kontak & Support

Jika ada pertanyaan atau butuh bantuan:
- Create an **Issue** di repository ini
- Diskusi di **Discussions** tab
- Atau kontak langsung (jika tersedia)

---

## 🙏 Acknowledgments

Terima kasih kepada:
- **Kaggle** - Platform luar biasa untuk belajar data science
- **Scikit-Learn** - Library ML terbaik untuk Python
- **Komunitas Data Science Indonesia** - Inspirasi dan dukungan
- **Semua kontributor** yang telah membantu

---

## 🚀 Next Steps

Setelah menyelesaikan repository ini, Anda bisa:

1. **Ikut kompetisi Kaggle** - Terapkan ilmu yang sudah dipelajari
2. **Buat project sendiri** - Mulai dari problem real di sekitar Anda
3. **Belajar Deep Learning** - Lanjut ke neural networks
4. **Belajar MLOps** - Deployment dan monitoring model
5. **Kontribusi open source** - Bantu project ML lainnya

---

<div align="center">

**⭐ Jika repository ini bermanfaat, jangan lupa beri Star! ⭐**

*Happy Learning! 🚀📊🤖*

</div>

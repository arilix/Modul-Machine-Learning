# 📚 Module Kaggle & Machine Learning

> **Repository pembelajaran lengkap tentang Kaggle, Machine Learning, dan Evaluation Metrics**  
> Lengkap dengan teori, praktik, dan implementasi manual algoritma ML!

---

## 📖 Tentang Repository Ini

Repository ini berisi materi pembelajaran komprehensif untuk memahami:
1. **Cara membuat kompetisi data di Kaggle**
2. **Dasar-dasar Machine Learning dengan data tabel**
3. **Evaluation metrics untuk mengukur performa model**
4. **Praktik langsung dengan dataset real dan Jupyter Notebook**
5. **Implementasi algoritma ML dari nol (tanpa library)**

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
├── 01_Student_Dropout
│   ├── 01_dropout_logistic_regression.ipynb
│   ├── 02_dropout_random_forest.ipynb
│   ├── 03_dropout_xgboost.ipynb
│   ├── 04_dropout_svm.ipynb
│   ├── 05_dropout_neural_network.ipynb
│   ├── 06_cgpa_linear_regression.ipynb
│   ├── 07_cgpa_random_forest_regressor.ipynb
│   ├── 08_cgpa_xgboost_regressor.ipynb
│   └── saved_models
│       ├── feature_columns_dropout.pkl
│       ├── feature_columns_linreg.pkl
│       ├── feature_columns_nn.pkl
│       ├── feature_columns_rf.pkl
│       ├── feature_columns_rf_reg.pkl
│       ├── feature_columns_svm.pkl
│       ├── feature_columns_xgb.pkl
│       ├── feature_columns_xgb_reg.pkl
│       ├── linear_regression_cgpa.pkl
│       ├── logistic_regression_dropout.pkl
│       ├── neural_network_dropout.pkl
│       ├── random_forest_dropout.pkl
│       ├── rf_regressor_cgpa.pkl
│       ├── scaler_dropout.pkl
│       ├── scaler_linreg.pkl
│       ├── scaler_nn.pkl
│       ├── scaler_svm.pkl
│       ├── svm_dropout.pkl
│       ├── xgboost_dropout.json
│       ├── xgboost_dropout.pkl
│       ├── xgb_regressor_cgpa.json
│       └── xgb_regressor_cgpa.pkl
├── 02_Toyota_Stock
│   ├── 01_stock_arima.ipynb
│   ├── 02_stock_prophet.ipynb
│   ├── 03_stock_lstm.ipynb
│   ├── 04_stock_gru.ipynb
│   ├── 05_stock_random_forest.ipynb
│   ├── 06_stock_xgboost.ipynb
│   ├── 07_stock_linear_regression.ipynb
│   └── saved_models
│       ├── arima_order.pkl
│       ├── arima_toyota.pkl
│       ├── feature_cols_rf_stock.pkl
│       ├── feature_cols_ridge_stock.pkl
│       ├── feature_cols_xgb_stock.pkl
│       ├── gru_config.pkl
│       ├── gru_toyota.h5
│       ├── gru_toyota.pth
│       ├── lstm_config.pkl
│       ├── lstm_toyota.h5
│       ├── lstm_toyota.pth
│       ├── prophet_toyota.json
│       ├── prophet_toyota.pkl
│       ├── rf_stock.pkl
│       ├── ridge_stock.pkl
│       ├── scaler_gru.pkl
│       ├── scaler_lstm.pkl
│       ├── xgb_stock.json
│       └── xgb_stock.pkl
├── 03_Student_Productivity
│   ├── 01_productivity_linear_regression.ipynb
│   ├── 02_productivity_rf_regressor.ipynb
│   ├── 03_productivity_xgb_regressor.ipynb
│   ├── 04_productivity_logistic.ipynb
│   ├── 05_productivity_rf_clf.ipynb
│   ├── 06_productivity_xgb_clf.ipynb
│   ├── 07_productivity_kmeans.ipynb
│   ├── 08_productivity_dbscan.ipynb
│   └── saved_models
│       ├── dbscan_params.pkl
│       ├── dbscan_productivity.pkl
│       ├── feature_cols_dbscan.pkl
│       ├── feature_cols_kmeans.pkl
│       ├── feature_cols_logistic_prod.pkl
│       ├── feature_cols_prod_linreg.pkl
│       ├── feature_cols_rf_prod_clf.pkl
│       ├── feature_cols_rf_prod_reg.pkl
│       ├── feature_cols_xgb_prod_clf.pkl
│       ├── feature_cols_xgb_prod_reg.pkl
│       ├── kmeans_productivity.pkl
│       ├── knn_for_dbscan_predict.pkl
│       ├── logistic_productivity.pkl
│       ├── prod_clf_config.pkl
│       ├── rf_clf_productivity.pkl
│       ├── rf_reg_productivity.pkl
│       ├── ridge_productivity.pkl
│       ├── scaler_dbscan.pkl
│       ├── scaler_kmeans.pkl
│       ├── xgb_clf_productivity.json
│       ├── xgb_clf_productivity.pkl
│       ├── xgb_reg_productivity.json
│       └── xgb_reg_productivity.pkl
├── README_Praktik_ML.md
├── requirements.txt
├── student_dropout_dataset_v3.csv
├── Toyota_Stock_Prices_1980_2026.csv
└── ultimate_student_productivity_dataset_5000.csv
│
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

Folder `Contoh/` berisi **3 Jupyter Notebook** yang bisa langsung dijalankan:

### 1️⃣ Prediksi Harga Rumah (Regression)
**File:** `01_Regression_Harga_Rumah.ipynb`

- **Dataset:** 30 data rumah (luas, kamar, umur, jarak ke kota → harga)
- **Models:** Linear Regression vs Random Forest
- **Metrics:** MAE, RMSE, R²
- **Fitur:** EDA lengkap, visualisasi, feature importance, cross-validation

### 2️⃣ Deteksi Diabetes (Binary Classification)  
**File:** `02_Classification_Diabetes.ipynb`

- **Dataset:** 40 data pasien (glucose, BMI, age, blood pressure → diabetes)
- **Models:** Logistic Regression vs Random Forest
- **Metrics:** Accuracy, Precision, Recall, F1, ROC-AUC, Confusion Matrix
- **Fitur:** Class distribution, ROC curve, classification report

### 3️⃣ Machine Learning Manual - From Scratch ⭐
**File:** `03_Manual_ML_From_Scratch.ipynb`

- **Implementasi manual:** Linear Regression & Logistic Regression **TANPA scikit-learn!**
- **Tools:** NumPy, Pandas, Matplotlib saja
- **Yang Diimplementasikan:**
  - Linear Regression (Normal Equation)
  - Logistic Regression (Gradient Descent)
  - Sigmoid function
  - Binary Cross-Entropy loss
  - Semua metrics (MAE, RMSE, R², Accuracy, Precision, Recall, F1, Confusion Matrix)
  - Train-test split manual
  - Standardization manual
- **Penjelasan matematis lengkap** dengan formula LaTeX
- **Comparison dengan scikit-learn** (hasilnya hampir identik!)

**🎯 Kenapa belajar implementasi manual?**
- Memahami matematis di balik algoritma
- Tahu exactly apa yang terjadi di black box
- Bisa custom algoritma sesuai kebutuhan
- Persiapan interview (sering ditanya!)
- Foundation untuk deep learning

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
jupyter>=1.0.0
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
3. 💻 **Notebook 01 & 02** → Praktik dengan scikit-learn
4. 📘 **Modul 1** → Belajar buat kompetisi (opsional)
5. 💻 **Notebook 03** → Implementasi manual (advanced)

### Untuk yang Sudah Paham Konsep:
1. 💻 **Notebook 01 & 02** → Refresh dengan praktik
2. 📙 **Modul 3** → Deep dive metrics
3. 💻 **Notebook 03** → Pahami algoritma dari dalam
4. 📘 **Modul 1** → Buat kompetisi sendiri

### Untuk Persiapan Interview:
1. 📗 **Modul 2 Bab 4** → Review model-model ML
2. 📙 **Modul 3** → Hafal semua metrics
3. 💻 **Notebook 03** → Implementasi manual (PENTING!)
4. Praktik coding whiteboard dengan algoritma dari scratch

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

### ✨ Implementasi Manual Algoritma ML
- **Pertama di Indonesia!** (mungkin 😄)
- Memahami math di balik ML
- Comparison dengan library standar
- Educational value tinggi

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

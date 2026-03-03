# 📚 Panduan Praktik Machine Learning dengan Data Tabel

Repository ini berisi contoh lengkap machine learning menggunakan data CSV dan Jupyter Notebook yang bisa langsung dijalankan.

---

## 📁 Struktur File

```
module-kaggle/
├── data_harga_rumah.csv                  # Dataset untuk regression
├── data_diabetes.csv                      # Dataset untuk classification
├── 01_Regression_Harga_Rumah.ipynb       # Notebook regression (scikit-learn)
├── 02_Classification_Diabetes.ipynb      # Notebook classification (scikit-learn)
├── 03_Manual_ML_From_Scratch.ipynb       # ML Manual (TANPA scikit-learn!)
├── requirements.txt                       # Dependencies
└── README_Praktik_ML.md                  # File ini
```

---

## 🎯 Contoh yang Tersedia

### 1. Prediksi Harga Rumah (Regression)
- **File:** `01_Regression_Harga_Rumah.ipynb`
- **Dataset:** `data_harga_rumah.csv` (30 samples)
- **Fitur:** Luas, Kamar, Umur, Jarak ke Kota
- **Target:** Harga (juta Rp)
- **Models:** Linear Regression vs Random Forest
- **Metrics:** MAE, RMSE, R²

**Isi Notebook:**
- ✅ Load data dari CSV
- ✅ EDA lengkap (descriptive stats, correlation, visualizations)
- ✅ Feature-target relationship analysis
- ✅ Model training & comparison
- ✅ Evaluation dengan interpretasi lengkap
- ✅ Residual plot untuk cek model quality
- ✅ Feature importance
- ✅ Cross-validation untuk cek overfitting
- ✅ Prediksi untuk data baru

### 2. Deteksi Diabetes (Binary Classification)
- **File:** `02_Classification_Diabetes.ipynb`
- **Dataset:** `data_diabetes.csv` (40 samples)
- **Fitur:** Glucose, BMI, Age, Blood Pressure
- **Target:** Diabetes (0/1)
- **Models:** Logistic Regression vs Random Forest
- **Metrics:** Accuracy, Precision, Recall, F1, ROC-AUC, Confusion Matrix

**Isi Notebook:**
- ✅ Load data dari CSV
- ✅ Class distribution analysis
- ✅ Feature distribution by class
- ✅ Model training & comparison
- ✅ Confusion matrix dengan interpretasi
- ✅ ROC curve visualization
- ✅ Classification report
- ✅ Feature importance
- ✅ Cross-validation
- ✅ Prediksi pasien baru dengan risk assessment

### 3. Machine Learning Manual - From Scratch
- **File:** `03_Manual_ML_From_Scratch.ipynb`
- **Dataset:** `data_harga_rumah.csv` & `data_diabetes.csv`
- **Tools:** NumPy, Pandas, Matplotlib (TANPA scikit-learn!)
- **Implemented:** Linear Regression, Logistic Regression, Metrics

**Isi Notebook:**
- ✅ Implementasi Linear Regression dengan Normal Equation
- ✅ Implementasi Logistic Regression dengan Gradient Descent
- ✅ Implementasi Sigmoid function manual
- ✅ Implementasi Binary Cross-Entropy loss
- ✅ Implementasi semua metrics manual (MAE, RMSE, R², Accuracy, Precision, Recall, F1, Confusion Matrix)
- ✅ Implementasi train-test split manual
- ✅ Implementasi standardization manual
- ✅ Penjelasan matematis lengkap dengan formula
- ✅ Visualisasi loss curve (gradient descent)
- ✅ Comparison dengan scikit-learn (hasilnya hampir sama!)
- ✅ Step-by-step explanation bagaimana algoritma bekerja

**Kenapa Belajar Manual Implementation?**
- Paham matematis di balik algoritma
- Tahu exactly apa yang terjadi di "black box"
- Bisa custom algoritma sesuai kebutuhan
- Interview prep (sering ditanya implementasi manual)
- Foundation untuk deep learning (neural networks dari scratch)

---

## 🆚 Scikit-Learn vs Manual Implementation

| Aspek | Scikit-Learn | Manual (From Scratch) |
|-------|-------------|----------------------|
| **Kecepatan** | Sangat cepat (C/Cython backend) | Lebih lambat (pure Python/NumPy) |
| **Kemudahan** | Simple API, 3-4 lines code | Perlu implement sendiri (~50-100 lines) |
| **Pemahaman** | Black box | Full understanding |
| **Customization** | Limited | Unlimited |
| **Production** | Ready | Not recommended |
| **Learning Value** | Medium | Very High |
| **Features** | Banyak (regularization, solver options, dll) | Basic only |
| **Debugging** | Sulit | Mudah (kontrol penuh) |

**Kapan Pakai Scikit-Learn?**
- Production code
- Dataset besar
- Butuh performance
- Prototyping cepat

**Kapan Implement Manual?**
- Belajar fundamental
- Research/eksperimen
- Custom algorithm
- Interview preparation
- Teaching/education

**Hasil Comparison:**
- Manual implementation menghasilkan hasil yang **sangat mirip** dengan scikit-learn (difference < 0.01%)
- Membuktikan bahwa kita benar-benar memahami algoritma!

---

## 🔬 Bagaimana Manual Implementation Bekerja?

### Linear Regression (Normal Equation Method):
```
1. Input: X (features), y (target)
   ↓
2. Add bias column: X_with_bias = [1, X]
   ↓
3. Calculate X^T X (matrix multiplication)
   ↓
4. Calculate (X^T X)^-1 (matrix inversion)
   ↓
5. Calculate (X^T X)^-1 X^T y
   ↓
6. Output: weights (w) dan bias (b)
   ↓
7. Prediction: ŷ = Xw + b
```

**Keuntungan:** Solusi exact, tidak perlu tuning
**Kekurangan:** Lambat untuk data besar (O(n³) karena inversion)

### Logistic Regression (Gradient Descent Method):
```
1. Initialize: w = 0, b = 0
   ↓
2. For each iteration:
   │
   ├─ Forward Pass:
   │  ├─ z = Xw + b
   │  └─ ŷ = sigmoid(z)
   │
   ├─ Calculate Loss:
   │  └─ L = -mean[y·log(ŷ) + (1-y)·log(1-ŷ)]
   │
   ├─ Calculate Gradients:
   │  ├─ ∂L/∂w = X^T·(ŷ - y) / n
   │  └─ ∂L/∂b = sum(ŷ - y) / n
   │
   └─ Update Weights:
      ├─ w = w - α·∂L/∂w
      └─ b = b - α·∂L/∂b
   ↓
3. After convergence:
   └─ Prediction: ŷ = sigmoid(Xw + b)
```

**Keuntungan:** Scalable, bisa handle data besar
**Kekurangan:** Perlu tuning (learning rate, iterations)

---

## 🚀 Cara Menggunakan

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### Langkah-langkah:

1. **Clone/Download repository ini**

2. **Jalankan Jupyter Notebook:**
   ```bash
   cd module-kaggle
   jupyter notebook
   ```

3. **Buka salah satu notebook:**
   - `01_Regression_Harga_Rumah.ipynb` untuk contoh regression
   - `02_Classification_Diabetes.ipynb` untuk contoh classification

4. **Run semua cell dari atas ke bawah**
   - Atau gunakan: `Cell → Run All`

5. **Lihat hasil:** Visualisasi dan evaluasi akan muncul inline

---

## � Formula Matematis yang Diimplementasikan

### Linear Regression (Normal Equation):
```
y = Xw + b
w = (X^T X)^-1 X^T y
```

### Logistic Regression (Gradient Descent):
```
z = Xw + b
σ(z) = 1 / (1 + e^-z)
ŷ = σ(z)

Loss (Binary Cross-Entropy):
L = -1/n * Σ[y·log(ŷ) + (1-y)·log(1-ŷ)]

Gradient:
∂L/∂w = 1/n * X^T·(ŷ - y)

Update:
w = w - α·∂L/∂w
```

### Evaluation Metrics:

**Regression:**
```
MAE  = 1/n * Σ|y_true - y_pred|
MSE  = 1/n * Σ(y_true - y_pred)²
RMSE = √MSE
R²   = 1 - (SS_res / SS_tot)
```

**Classification:**
```
Accuracy  = (TP + TN) / Total
Precision = TP / (TP + FP)
Recall    = TP / (TP + FN)
F1-Score  = 2 * (Precision * Recall) / (Precision + Recall)
```

---

## �📊 Cara Membaca Evaluation Metrics

### Untuk Regression:

| Metric | Formula | Interpretasi | Target Bagus |
|--------|---------|--------------|--------------|
| **MAE** | Mean Absolute Error | Rata-rata error dalam unit asli | < 10% dari range |
| **RMSE** | Root Mean Squared Error | Error dengan penalty untuk outlier | < 20% dari range |
| **R²** | R-squared | % variasi yang dijelaskan model | > 0.7 (good), > 0.9 (excellent) |

**Cara Cek:**
```python
price_range = y.max() - y.min()
error_percentage = (mae / price_range) * 100

if error_percentage < 10:
    print("✅ SANGAT BAGUS!")
elif error_percentage < 20:
    print("✅ BAGUS")
elif error_percentage < 30:
    print("⚠️ CUKUP")
else:
    print("❌ KURANG")
```

### Untuk Classification:

| Metric | Formula | Interpretasi | Kapan Penting? |
|--------|---------|--------------|----------------|
| **Accuracy** | (TP+TN)/Total | % prediksi benar | Dataset balanced |
| **Precision** | TP/(TP+FP) | Dari prediksi positif, berapa yang benar? | Cost of False Positive tinggi |
| **Recall** | TP/(TP+FN) | Dari aktual positif, berapa yang terdeteksi? | Cost of False Negative tinggi (MEDIS!) |
| **F1-Score** | 2×(Prec×Rec)/(Prec+Rec) | Balance precision & recall | Imbalanced data |
| **ROC-AUC** | Area under ROC curve | Kemampuan separasi kelas | Overall performance |

**Confusion Matrix:**
```
                Predicted
                Neg    Pos
Actual  Neg     TN     FP  ← False Positive (False alarm)
        Pos     FN     TP  ← False Negative (Missed detection!)
```

**Untuk Kasus Medis:**
- 🚨 **Prioritas #1: RECALL > 90%** (jangan sampai miss diagnosis!)
- False Negative = BERBAHAYA ❌
- False Positive = Tidak ideal tapi lebih aman ✓ (bisa test ulang)

**Target Benchmark:**

| Kualitas | Accuracy | Precision | Recall | F1 | ROC-AUC |
|----------|----------|-----------|--------|----|---------| 
| Excellent | > 95% | > 90% | > 90% | > 0.9 | > 0.9 |
| Good | 85-95% | 80-90% | 80-90% | 0.8-0.9 | 0.8-0.9 |
| Moderate | 75-85% | 70-80% | 70-80% | 0.7-0.8 | 0.7-0.8 |
| Poor | < 75% | < 70% | < 70% | < 0.7 | < 0.7 |

---

## 🔍 Checklist: Apakah Model Saya Bagus?

### ✅ Untuk Regression:
- [ ] MAE/RMSE < 20% dari range data
- [ ] R² > 0.7
- [ ] Residual plot tidak menunjukkan pola (acak di sekitar y=0)
- [ ] Cross-validation score stabil (std < 0.1)
- [ ] Prediksi masuk akal untuk nilai ekstrem
- [ ] Gap training vs test score < 10% (tidak overfitting)

### ✅ Untuk Classification:
- [ ] Accuracy > 80% (balanced) atau F1 > 0.8 (imbalanced)
- [ ] Confusion matrix: tidak ada kelas yang completely missed
- [ ] ROC-AUC > 0.8
- [ ] Recall tinggi untuk kelas penting (medis: > 90%)
- [ ] Cross-validation score stabil
- [ ] Gap training vs test score < 5% (tidak overfitting)
- [ ] Per-class performance seimbang

---

## 💡 Tips Interpretasi

### 1. Selalu Lihat Multiple Metrics
Jangan hanya percaya 1 metric! Contoh:
- Accuracy 95% tapi Recall 50% → Model tidak bagus untuk medical diagnosis!
- R² 0.9 tapi MAE 500 juta → Error masih terlalu besar untuk aplikasi real

### 2. Konteks adalah Kunci
- **Medical diagnosis:** Prioritaskan Recall (jangan sampai miss)
- **Spam filter:** Prioritaskan Precision (jangan sampai email penting ke spam)
- **Prediksi harga:** MAE lebih interpretable daripada MSE

### 3. Visualisasi Sangat Membantu
- Scatter plot (Actual vs Predicted) → Lihat seberapa dekat ke diagonal
- Residual plot → Cek apakah ada pola (jika ada = model belum optimal)
- ROC curve → Semakin dekat ke kiri atas = semakin bagus
- Confusion matrix → Lihat dimana model sering salah

### 4. Cross-Validation Wajib
- Jangan hanya percaya hasil single train-test split
- CV memastikan model robust dan tidak overfitting
- Jika CV std tinggi → Model tidak stabil (perlu lebih banyak data atau tuning)

### 5. Feature Importance
- Pahami fitur mana yang paling berpengaruh
- Bisa jadi insight untuk domain knowledge
- Bisa guide feature engineering selanjutnya

---

## 🚧 Troubleshooting

### Model Overfitting (Training score >> Test score)
```python
# Solution 1: Regularization
from sklearn.linear_model import Ridge, Lasso
model = Ridge(alpha=1.0)

# Solution 2: Reduce model complexity
model = RandomForestRegressor(max_depth=5, min_samples_split=10)

# Solution 3: More data atau cross-validation
```

### Recall Rendah (Classification)
```python
# Solution 1: Turunkan threshold
y_prob = model.predict_proba(X_test)[:, 1]
y_pred_new = (y_prob > 0.3).astype(int)  # Default: 0.5

# Solution 2: Class weight
model = RandomForestClassifier(class_weight='balanced')

# Solution 3: SMOTE (oversample minority)
from imblearn.over_sampling import SMOTE
smote = SMOTE()
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)
```

### R² Rendah (Regression)
```python
# Solution 1: Feature engineering
df['luas_per_kamar'] = df['luas'] / df['kamar']
df['umur_category'] = pd.cut(df['umur'], bins=[0, 5, 10, 100])

# Solution 2: Polynomial features
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Solution 3: Try non-linear model
from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor(n_estimators=200)
```

---

## 📚 Resources

### Library Documentation:
- [scikit-learn](https://scikit-learn.org/)
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)

### Tutorial:
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Kaggle Learn](https://www.kaggle.com/learn)

### Metrics Deep Dive:
- [Classification Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)
- [Regression Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics)

---

## 🎓 Next Steps

Setelah memahami contoh-contoh ini, kamu bisa:

1. **Modifikasi dataset** → Ganti dengan data sendiri
2. **Coba model lain** → XGBoost, LightGBM, Neural Network
3. **Feature engineering** → Buat fitur baru yang lebih informatif
4. **Hyperparameter tuning** → GridSearchCV, RandomizedSearchCV
5. **Ensemble methods** → Voting, Stacking, Blending
6. **Deploy model** → Flask API, Streamlit app, Docker container

---

## 🤝 Contributing

Ada pertanyaan atau saran? Feel free to:
- Open an issue
- Submit a pull request
- Contact: your-email@example.com

---

## 📝 License

This project is for educational purposes.

---

**Happy Learning! 🚀**

*"Model yang baik bukan hanya punya metric tinggi, tapi model yang solve real problem dengan acceptable cost!"*

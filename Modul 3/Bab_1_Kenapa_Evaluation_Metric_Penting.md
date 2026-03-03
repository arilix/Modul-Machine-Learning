# Bab 1 — Kenapa Evaluation Metric Itu Penting?

## Pengertian Evaluation Metric

Evaluation metric adalah **cara mengukur seberapa bagus model machine learning kita**. Seperti nilai ujian yang menunjukkan seberapa pintar kita, metric menunjukkan seberapa akurat model kita dalam memprediksi.

**Analogi Sederhana**: 
Bayangkan Anda belajar memanah. Evaluation metric itu seperti sistem penilaian:
- Berapa panah yang mengenai target? (Accuracy)
- Seberapa dekat panah dengan titik pusat? (Error)
- Apakah Anda konsisten atau kadang meleset jauh? (Variance)

## Kenapa Penting?

### 1. Mengukur Performa Model

Tanpa metric, kita tidak tahu apakah model kita bagus atau jelek!

**Contoh**:
- Model A prediksi harga rumah salah rata-rata Rp 50 juta
- Model B prediksi harga rumah salah rata-rata Rp 200 juta
- **Jelas Model A lebih baik!** ✅

### 2. Membandingkan Model

Kita bisa mencoba berbagai model dan pilih yang terbaik.

**Contoh**:
```
Linear Regression    → RMSE: 250
Random Forest        → RMSE: 180  ← Lebih baik!
XGBoost             → RMSE: 165  ← Paling bagus!
```

### 3. Tuning Hyperparameter

Metric membantu kita menemukan setting terbaik untuk model.

**Analogi**: Seperti mengatur suhu microwave. Kita coba berbagai suhu dan pilih yang paling pas — tidak gosong, tidak mentah.

### 4. Mendeteksi Overfitting

Metric di training vs test data memberitahu apakah model "terlalu hafalan".

**Contoh**:
```
Training Accuracy: 99%  ← Terlalu bagus!
Test Accuracy: 70%      ← Jelek di data baru!
❌ Model overfitting!
```

### 5. Komunikasi dengan Stakeholder

Metric adalah bahasa universal untuk menjelaskan performa ke non-teknikal.

**Contoh komunikasi**:
- ❌ Teknis: "Model punya R² 0.85 dengan residual error terdistribusi normal"
- ✅ Simple: "Model kita benar 85% dari waktu"

## Metric vs Loss Function

**Loss Function**: Digunakan **saat training** untuk mengoptimalkan model
**Evaluation Metric**: Digunakan **setelah training** untuk mengukur hasil final

**Analogi Perbedaan**:
- **Loss function** = Nilai harian saat belajar (untuk improve)
- **Evaluation metric** = Nilai ujian final (untuk tahu hasil akhir)

| Aspek | Loss Function | Evaluation Metric |
|-------|---------------|-------------------|
| **Kapan** | Saat training | Setelah training |
| **Tujuan** | Optimize parameter | Ukur performa |
| **Contoh** | Mean Squared Error | R², RMSE, Accuracy |
| **Audience** | Model (internal) | Manusia (eksternal) |

## Pentingnya Memilih Metric yang Tepat

**Tidak semua metric cocok untuk semua kasus!**

### Contoh Kasus: Deteksi Kanker

Dataset: 1000 orang, 10 punya kanker, 990 sehat

**Model Naif**: Tebak semua orang "Sehat"
- Accuracy: 990/1000 = **99%** ← Terlihat bagus!
- Tapi gagal deteksi semua kanker! ❌

**Solusi**: Gunakan metric lain seperti Recall, F1-Score, atau AUC.

### Contoh Kasus: Prediksi Harga Rumah

**Situasi 1**: Harga rumah Rp 500 juta - 5 miliar
- Gunakan **MAE** atau **RMSE** (error dalam rupiah)

**Situasi 2**: Ada outlier ekstrem (rumah mewah Rp 50 miliar)
- Gunakan **MAPE** atau **RMSLE** (error dalam persentase)

## Prinsip Memilih Metric

### 1. Sesuaikan dengan Problem Type

| Problem | Metric |
|---------|--------|
| Regression | MAE, MSE, RMSE, R² |
| Classification | Accuracy, Precision, Recall, F1 |
| Imbalanced Data | F1-Score, AUC-ROC |
| Ranking | AUC, NDCG |

### 2. Pertimbangkan Business Impact

**Contoh: Spam Detection**

- False Positive (email penting masuk spam) = **SANGAT BURUK** ❌
- False Negative (spam masuk inbox) = Tidak apa-apa
- **Solusi**: Prioritaskan **Precision** (minimal false positive)

**Contoh: Deteksi Fraud**

- False Negative (fraud tidak terdeteksi) = **SANGAT BURUK** ❌
- False Positive (transaksi normal dicurigai) = Tidak apa-apa
- **Solusi**: Prioritaskan **Recall** (deteksi semua fraud)

### 3. Interpretability

**Untuk Stakeholder**:
- ✅ Mudah: Accuracy, MAE (dalam satuan asli)
- ❌ Susah: Log Loss, RMSLE

### 4. Sensitivity

**Outlier-sensitive metrics**:
- MSE, RMSE → Sangat sensitif terhadap outlier
- MAE → Lebih robust

## Kesalahan Umum dalam Evaluation

### 1. Hanya Lihat Satu Metric

❌ **Salah**: "Model saya 95% accurate, pasti bagus!"
✅ **Benar**: Lihat juga Precision, Recall, dan F1-Score

### 2. Tidak Split Data

❌ **Salah**: Evaluasi di data training
✅ **Benar**: Evaluasi di data test (yang model belum pernah lihat)

### 3. Mengabaikan Context

❌ **Salah**: "RMSE saya 100, apa ini bagus?"
✅ **Benar**: "RMSE saya 100 untuk prediksi harga rumah yang range-nya 500-5000. Jadi error ~2-20%, lumayan bagus."

### 4. Salah Pilih Metric untuk Imbalanced Data

❌ **Salah**: Pakai Accuracy untuk data 99:1
✅ **Benar**: Pakai F1-Score atau AUC-ROC

## Rangkuman

**Key Points**:

✅ Evaluation metric adalah cara kita tahu apakah model bagus atau tidak

✅ Pilih metric yang sesuai dengan problem type (regression vs classification)

✅ Pertimbangkan business impact, bukan hanya angka

✅ Lihat beberapa metric, jangan cuma satu

✅ Selalu evaluasi di test set, bukan training set

**Next**: Mari kita pelajari metric-metric spesifik untuk Regression dan Classification!

---

*Modul 3 — Evaluation Metrics dalam Machine Learning*

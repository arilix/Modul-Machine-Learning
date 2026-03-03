# Bab 2 — Evaluation untuk Regression

Regression adalah prediksi nilai numerik kontinu (harga, suhu, jumlah, dll). Mari kita pelajari metric untuk mengukur seberapa akurat prediksi kita!

## Setup Contoh

Untuk semua penjelasan, kita akan gunakan contoh sederhana:

**Prediksi Harga Rumah (dalam juta rupiah)**:

| Rumah | Harga Aktual | Prediksi | Error |
|-------|--------------|----------|-------|
| A | 1000 | 1100 | +100 |
| B | 2000 | 1900 | -100 |
| C | 1500 | 1600 | +100 |
| D | 3000 | 2800 | -200 |

---

## 1. MAE (Mean Absolute Error)

### Apa itu?

**Rata-rata dari selisih mutlak (absolut) antara prediksi dan aktual.**

### Rumus

$$MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$

Atau dalam bahasa sederhana:
```
MAE = (|error1| + |error2| + ... + |errorN|) / N
```

### Contoh Hitung Manual

```
Error: |+100| + |-100| + |+100| + |-200|
     = 100 + 100 + 100 + 200
     = 500

MAE = 500 / 4 = 125 juta
```

**Artinya**: Rata-rata salah prediksi **125 juta rupiah** per rumah.

### Kapan Digunakan?

✅ **Cocok untuk**:
- Error dalam satuan yang sama dengan target (rupiah, meter, kg)
- Ingin interpretasi yang mudah
- Ada outlier (MAE lebih robust)
- Semua error dianggap sama pentingnya

❌ **Tidak cocok untuk**:
- Ingin lebih "hukum" error besar (gunakan MSE/RMSE)
- Butuh differentiable loss untuk optimization

### Kelebihan

- ✅ Mudah dipahami (dalam satuan asli)
- ✅ Robust terhadap outlier
- ✅ Memberikan gambaran "typical error"

### Kekurangan

- ❌ Tidak memberikan "penalty besar" untuk error besar
- ❌ Tidak differentiable di 0 (sedikit masalah untuk optimization)

### Kode Python

```python
from sklearn.metrics import mean_absolute_error

y_true = [1000, 2000, 1500, 3000]
y_pred = [1100, 1900, 1600, 2800]

mae = mean_absolute_error(y_true, y_pred)
print(f"MAE: {mae} juta")  # Output: 125.0
```

---

## 2. MSE (Mean Squared Error)

### Apa itu?

**Rata-rata dari kuadrat error.** Error besar lebih "dihukum" karena dikuadratkan!

### Rumus

$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

```
MSE = (error1² + error2² + ... + errorN²) / N
```

### Contoh Hitung Manual

```
Error²: 100² + (-100)² + 100² + (-200)²
      = 10,000 + 10,000 + 10,000 + 40,000
      = 70,000

MSE = 70,000 / 4 = 17,500
```

**Artinya**: Mean squared error adalah **17,500 (juta²)**

⚠️ **Perhatikan**: Satuannya jadi "juta kuadrat" — susah diinterpretasi!

### Analogi

**MAE** vs **MSE**:
- MAE seperti denda parkir: Telat 10 menit = Rp 10k, telat 60 menit = Rp 60k (linear)
- MSE seperti denda progresif: Telat 10 menit = Rp 10k, telat 60 menit = Rp 360k (kuadratik)

Error kecil tidak terlalu dihukum, tapi error besar sangat dihukum!

### Kapan Digunakan?

✅ **Cocok untuk**:
- Ingin "hukum berat" error besar (outlier penting)
- Loss function saat training (differentiable)
- Analisis statistik

❌ **Tidak cocok untuk**:
- Interpretasi langsung (satuannya aneh)
- Ada outlier yang ingin diabaikan

### Kelebihan

- ✅ Penalty lebih besar untuk error besar
- ✅ Smooth dan differentiable (bagus untuk optimization)
- ✅ Basis untuk banyak algoritma

### Kekurangan

- ❌ Satuan tidak intuitif (kuadrat)
- ❌ Sangat sensitif terhadap outlier
- ❌ Susah dijelaskan ke non-teknikal

### Kode Python

```python
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_true, y_pred)
print(f"MSE: {mse}")  # Output: 17500.0
```

---

## 3. RMSE (Root Mean Squared Error)

### Apa itu?

**Akar kuadrat dari MSE.** Mengembalikan satuan ke satuan asli!

### Rumus

$$RMSE = \sqrt{MSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$

### Contoh Hitung Manual

```
RMSE = √(MSE) = √17,500 = 132.29 juta
```

**Artinya**: Rata-rata salah prediksi **132.29 juta rupiah** per rumah.

### Perbandingan MAE vs RMSE

Pada contoh kita:
- **MAE = 125 juta** (rata-rata error biasa)
- **RMSE = 132.29 juta** (rata-rata dengan penalty error besar)

RMSE lebih besar karena error 200 juta "lebih dihukum" dengan kuadrat.

### Kapan Digunakan?

✅ **Cocok untuk**:
- Ingin satuan yang sama dengan target (seperti MAE)
- Tapi tetap ingin penalty untuk error besar
- Standard metric untuk banyak kompetisi
- Distribusi error mendekati normal

❌ **Tidak cocok untuk**:
- Banyak outlier ekstrem (akan sangat tinggi)

### Kelebihan

- ✅ Satuan mudah dipahami (seperti MAE)
- ✅ Penalty untuk error besar (seperti MSE)
- ✅ Most popular metric untuk regression

### Kekurangan

- ❌ Sensitif terhadap outlier
- ❌ Tidak seintuitif MAE

### Kode Python

```python
from sklearn.metrics import mean_squared_error
import numpy as np

rmse = np.sqrt(mean_squared_error(y_true, y_pred))
print(f"RMSE: {rmse:.2f} juta")  # Output: 132.29
```

---

## 4. RMSLE (Root Mean Squared Log Error)

### Apa itu?

**RMSE tapi dihitung di skala logaritma.** Fokus pada error **relatif** (persentase), bukan absolut.

### Rumus

$$RMSLE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (\log(y_i + 1) - \log(\hat{y}_i + 1))^2}$$

### Kenapa Pakai Log?

**Log membuat error relatif lebih penting daripada error absolut.**

**Contoh**:
- Prediksi 100 vs aktual 200 → Error 100 (100% salah)
- Prediksi 1100 vs aktual 1200 → Error 100 (9% salah)

Dengan **RMSE biasa**: Kedua error sama (100)
Dengan **RMSLE**: Error pertama lebih besar (karena persentasenya lebih besar)

### Kapan Digunakan?

✅ **Cocok untuk**:
- Target dengan range sangat luas (1 - 1,000,000)
- Error relatif/persentase lebih penting
- Data dengan exponential growth
- Tidak boleh under-predict (penalty lebih besar)

❌ **Tidak cocok untuk**:
- Target ada yang negatif (log tidak bisa negatif!)
- Error absolut yang penting

### Contoh

**Prediksi Jumlah View Video**:
- Video kecil: 100 view, prediksi 50 → Error 50 view
- Video viral: 1,000,000 view, prediksi 999,950 → Error 50 view

Kedua error sama (50), tapi video kecil salah 50%, video viral cuma 0.005%!
**RMSLE akan lebih "hukum" error di video kecil.**

### Kelebihan

- ✅ Fokus pada error relatif (persentase)
- ✅ Bagus untuk data skewed/exponential
- ✅ Under-prediction lebih dihukum

### Kekurangan

- ❌ Tidak bisa untuk nilai negatif
- ❌ Interpretasi lebih susah
- ❌ Asimetris (under-predict lebih dihukum)

### Kode Python

```python
from sklearn.metrics import mean_squared_log_error
import numpy as np

rmsle = np.sqrt(mean_squared_log_error(y_true, y_pred))
print(f"RMSLE: {rmsle:.4f}")
```

---

## 5. R² Score (Coefficient of Determination)

### Apa itu?

**Mengukur seberapa baik model dibanding baseline (mean).** Nilai 0-1 (atau bisa negatif!).

### Rumus

$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}} = 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \bar{y})^2}$$

Di mana:
- $SS_{res}$ = Sum of squared residuals (error model kita)
- $SS_{tot}$ = Total sum of squares (error kalau prediksi pakai mean)

### Interpretasi

| R² | Artinya |
|----|---------|
| **1.0** | Perfect prediction! ✨ |
| **0.8** | Model menjelaskan 80% variance |
| **0.5** | Model lumayan |
| **0.0** | Model sama aja dengan prediksi rata-rata |
| **< 0** | Model lebih jelek dari prediksi rata-rata! ❌ |

### Contoh Konsep

Bayangkan teman Anda tebak nilai ujian teman lain:

**Strategi 1**: Tebak semua 75 (nilai rata-rata) → Error besar
**Strategi 2**: Lihat jam belajar, lalu prediksi → Error lebih kecil

**R² mengukur**: Seberapa banyak Strategi 2 lebih baik dari Strategi 1?

### Contoh Hitung Manual

```
Rata-rata harga = (1000 + 2000 + 1500 + 3000) / 4 = 1875

SS_tot (error kalau prediksi pakai mean):
= (1000-1875)² + (2000-1875)² + (1500-1875)² + (3000-1875)²
= 765,625 + 15,625 + 140,625 + 1,265,625
= 2,187,500

SS_res (error model kita):
= 100² + (-100)² + 100² + (-200)²
= 70,000

R² = 1 - (70,000 / 2,187,500)
   = 1 - 0.032
   = 0.968 (96.8%)
```

**Artinya**: Model menjelaskan **96.8%** variasi dalam harga rumah! Sangat bagus! 🎉

### Kapan Digunakan?

✅ **Cocok untuk**:
- Ingin tahu "seberapa bagus model?"
- Membandingkan model berbeda
- Komunikasi ke non-teknikal ("model benar 85%")

❌ **Tidak cocok untuk**:
- Interpretasi absolut error (gunakan MAE/RMSE)
- Data dengan pola non-linear tanpa feature engineering

### Kelebihan

- ✅ Scale-independent (0-1)
- ✅ Mudah dipahami "model benar X%"
- ✅ Standard metric untuk reporting

### Kekurangan

- ❌ Bisa negatif (membingungkan)
- ❌ Tidak memberitahu satuan error
- ❌ Bisa misleading kalau model overfit

### Kode Python

```python
from sklearn.metrics import r2_score

r2 = r2_score(y_true, y_pred)
print(f"R²: {r2:.4f} ({r2*100:.2f}%)")
```

---

## 6. Adjusted R² (R² yang Disesuaikan)

### Apa itu?

**R² yang sudah diperbaiki untuk jumlah fitur.** Mencegah "cheating" dengan menambah banyak fitur!

### Rumus

$$Adjusted\ R^2 = 1 - \frac{(1-R^2)(n-1)}{n-p-1}$$

Di mana:
- $n$ = jumlah data
- $p$ = jumlah fitur

### Kenapa Perlu Adjusted R²?

**Problem dengan R² biasa**:
- Tambah fitur → R² naik (bahkan fitur random!)
- R² tidak "penalty" model yang terlalu kompleks

**Contoh**:
```
Model 1: 3 fitur → R² = 0.85
Model 2: 100 fitur → R² = 0.87 ← Naik sedikit!

Adjusted R²:
Model 1: 0.84
Model 2: 0.75 ← Turun! (Terlalu kompleks)
```

### Kapan Digunakan?

✅ **Cocok untuk**:
- Membandingkan model dengan jumlah fitur berbeda
- Feature selection
- Mencegah overfitting

❌ **Tidak cocok untuk**:
- Model sederhana dengan sedikit fitur (gunakan R² biasa)

### Kelebihan

- ✅ Penalty untuk fitur yang tidak berguna
- ✅ Lebih fair untuk perbandingan model

### Kekurangan

- ❌ Lebih susah dijelaskan ke non-teknikal
- ❌ Tetap tidak kasih tahu satuan error

### Kode Python

```python
from sklearn.metrics import r2_score

n = len(y_true)  # Jumlah data
p = X.shape[1]   # Jumlah fitur

r2 = r2_score(y_true, y_pred)
adjusted_r2 = 1 - (1-r2)*(n-1)/(n-p-1)

print(f"R²: {r2:.4f}")
print(f"Adjusted R²: {adjusted_r2:.4f}")
```

---

## 7. MAPE (Mean Absolute Percentage Error)

### Apa itu?

**Rata-rata error dalam persentase.** Fokus pada error relatif, mudah dipahami!

### Rumus

$$MAPE = \frac{100\%}{n} \sum_{i=1}^{n} \left|\frac{y_i - \hat{y}_i}{y_i}\right|$$

```
MAPE = rata-rata(|error / aktual| × 100%)
```

### Contoh Hitung Manual

```
Rumah A: |100 / 1000| = 0.10 = 10%
Rumah B: |-100 / 2000| = 0.05 = 5%
Rumah C: |100 / 1500| = 0.067 = 6.7%
Rumah D: |-200 / 3000| = 0.067 = 6.7%

MAPE = (10 + 5 + 6.7 + 6.7) / 4 = 7.1%
```

**Artinya**: Rata-rata salah **7.1%** dalam prediksi harga.

### Kapan Digunakan?

✅ **Cocok untuk**:
- Ingin error dalam persentase (mudah dipahami)
- Membandingkan dataset berbeda
- Komunikasi dengan stakeholder

❌ **Tidak cocok untuk**:
- Ada nilai aktual = 0 (pembagian dengan 0!)
- Nilai aktual sangat kecil (MAPE jadi sangat besar)
- Asymmetric (over-predict lebih dihukum)

### Kelebihan

- ✅ Sangat mudah dipahami (persentase)
- ✅ Scale-independent
- ✅ Intuitive untuk business

### Kekurangan

- ❌ Tidak bisa untuk nilai 0
- ❌ Asimetris (over-prediction lebih dihukum)
- ❌ Sensitif terhadap nilai kecil

### Kode Python

```python
def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

mape_score = mape(np.array(y_true), np.array(y_pred))
print(f"MAPE: {mape_score:.2f}%")
```

---

## 8. Median Absolute Error

### Apa itu?

**Median (bukan mean) dari absolute error.** Lebih robust terhadap outlier ekstrem!

### Rumus

$$Median\ AE = median(|y_1 - \hat{y}_1|, |y_2 - \hat{y}_2|, ..., |y_n - \hat{y}_n|)$$

### Contoh

```
Errors: [100, 100, 100, 200]
MAE = (100+100+100+200)/4 = 125
Median AE = median([100, 100, 100, 200]) = 100
```

Median AE lebih kecil karena tidak terpengaruh outlier (200).

### Kapan Digunakan?

✅ **Cocok untuk**:
- Banyak outlier
- Ingin "typical error" (tidak terpengaruh ekstrem)
- Data skewed

❌ **Tidak cocok untuk**:
- Ingin semua error diperhitungkan

### Kelebihan

- ✅ Sangat robust terhadap outlier
- ✅ Memberikan "typical" error

### Kekurangan

- ❌ Mengabaikan extreme errors
- ❌ Tidak differentiable

### Kode Python

```python
from sklearn.metrics import median_absolute_error

med_ae = median_absolute_error(y_true, y_pred)
print(f"Median AE: {med_ae}")
```

---

## 9. Explained Variance Score

### Apa itu?

**Mirip R², tapi mengukur variance yang dijelaskan tanpa mempertimbangkan bias.**

### Rumus

$$Explained\ Variance = 1 - \frac{Var(y - \hat{y})}{Var(y)}$$

### Perbedaan dengan R²

- **R²**: Memperhitungkan bias (systematic error)
- **Explained Variance**: Hanya variance, tidak peduli bias

**Analogi**: 
- R² seperti nilai total (akurasi + konsistensi)
- Explained Variance hanya konsistensi

### Kapan Digunakan?

✅ **Cocok untuk**:
- Fokus pada variance, bukan bias
- Analisis komponen

❌ **Tidak cocok untuk**:
- Evaluasi general (gunakan R²)

### Kode Python

```python
from sklearn.metrics import explained_variance_score

ev = explained_variance_score(y_true, y_pred)
print(f"Explained Variance: {ev:.4f}")
```

---

## Ringkasan Tabel Regression Metrics

| Metric | Satuan | Sensitif Outlier | Interpretasi | Kapan Pakai |
|--------|--------|------------------|--------------|-------------|
| **MAE** | Sama dengan target | ❌ Tidak | ✅ Mudah | Outlier, error typical |
| **MSE** | Target² | ✅ Sangat | ❌ Susah | Loss function, penalty besar |
| **RMSE** | Sama dengan target | ✅ Ya | ✅ Cukup | Standard, penalty besar |
| **RMSLE** | Log scale | ❌ Tidak | ❌ Susah | Error relatif, data skewed |
| **R²** | 0-1 | - | ✅ Mudah | Overall performance |
| **Adjusted R²** | 0-1 | - | ✅ Cukup | Banding model beda fitur |
| **MAPE** | Persen | ❌ Tidak | ✅ Sangat mudah | Komunikasi, persentase |
| **Median AE** | Sama dengan target | ❌ Sangat robust | ✅ Mudah | Banyak outlier |

---

*Modul 3 — Evaluation Metrics dalam Machine Learning*

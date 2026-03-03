# Bab 5 — Studi Kasus Sederhana

## Contoh: Kompetisi Prediksi Harga Rumah

Mari kita buat contoh konkret kompetisi untuk mahasiswa:

### Problem Statement

**Judul**: "Jakarta House Price Prediction Challenge"

**Deskripsi**:
Anda adalah seorang data scientist di perusahaan property tech. Tugas Anda adalah membuat model machine learning yang dapat memprediksi harga rumah di Jakarta berdasarkan berbagai fitur seperti luas tanah, luas bangunan, jumlah kamar, lokasi, dll.

### Dataset Structure

**train.csv** (8,000 rows):
```
| Column          | Type    | Description                    |
|-----------------|---------|--------------------------------|
| id              | int     | Unique identifier              |
| land_area       | float   | Luas tanah (m²)                |
| building_area   | float   | Luas bangunan (m²)             |
| bedrooms        | int     | Jumlah kamar tidur             |
| bathrooms       | int     | Jumlah kamar mandi             |
| floors          | int     | Jumlah lantai                  |
| age             | int     | Umur bangunan (tahun)          |
| district        | string  | Kecamatan                      |
| distance_to_cbd | float   | Jarak ke pusat kota (km)       |
| price           | float   | Harga rumah (juta rupiah) [TARGET] |
```

**test.csv** (2,000 rows):
- Sama seperti train.csv tapi tanpa kolom `price`

**sample_submission.csv**:
```
id,price
8001,2500.5
8002,1800.2
...
```

### Evaluation Metric

**Metric**: Root Mean Squared Error (RMSE)

**Formula**:
$$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$

Di mana:
- $y_i$ = harga aktual
- $\hat{y}_i$ = harga prediksi
- $n$ = jumlah data

**Interpretasi**:
- RMSE 100 = rata-rata error 100 juta rupiah
- Semakin kecil RMSE, semakin baik model

**Target**:
- Baseline (mean prediction): RMSE ~500
- Good model: RMSE < 300
- Excellent model: RMSE < 200

### Rules

```
📜 Aturan Kompetisi:

1. Peserta: Terbuka untuk mahasiswa S1/S2
2. Team: Max 3 orang per team
3. Submission: Max 5 submission per hari
4. Data: Tidak boleh menggunakan external data
5. Code: Wajib submit code untuk verifikasi (top 10)
6. Hardware: Gunakan Kaggle Notebooks (free tier OK)

⚠️ Pelanggaran akan menyebabkan diskualifikasi
```

### Timeline

```
📅 Jadwal Kompetisi:

Start Date    : 1 Maret 2026
End Date      : 15 April 2026 (23:59 WIB)
Duration      : 6 minggu

Week 1-2  : Data exploration & baseline model
Week 3-4  : Feature engineering & model improvement
Week 5-6  : Final tuning & submission
Week 7    : Code verification & winner announcement
```

### Starter Notebook

Berikan starter notebook dengan:

```python
# 1. Load Data
import pandas as pd
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# 2. Basic EDA
print(train.head())
print(train.info())
print(train.describe())

# 3. Simple Baseline Model
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Prepare data
X = train.drop(['id', 'price'], axis=1)
y = train['price']

# Simple feature engineering
X_encoded = pd.get_dummies(X, columns=['district'])

# Train simple model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

# Predict on test
X_test = test.drop(['id'], axis=1)
X_test_encoded = pd.get_dummies(X_test, columns=['district'])

# Align columns
X_test_encoded = X_test_encoded.reindex(columns=X_encoded.columns, fill_value=0)

predictions = model.predict(X_test_encoded)

# Create submission
submission = pd.DataFrame({
    'id': test['id'],
    'price': predictions
})
submission.to_csv('submission.csv', index=False)
```

**Baseline Score**: RMSE ~450

### Prizes

```
🏆 Hadiah:

Rank 1: Sertifikat + Merchandise + Bonus nilai 10 poin
Rank 2: Sertifikat + Merchandise + Bonus nilai 8 poin
Rank 3: Sertifikat + Merchandise + Bonus nilai 6 poin
Rank 4-10: Sertifikat + Bonus nilai 4 poin
```

## Contoh Penentuan Metric

Bagaimana memilih metric yang tepat? Berikut decision tree sederhana:

```
Apakah problem Anda prediction atau classification?
│
├── REGRESSION (prediksi nilai numerik)
│   │
│   ├── Apakah ada outlier ekstrem?
│   │   ├── YES → Gunakan MAE (Mean Absolute Error)
│   │   └── NO  → Gunakan RMSE (Root Mean Squared Error)
│   │
│   └── Apakah butuh interpretasi proporsi variance?
│       └── YES → Gunakan R² Score
│
└── CLASSIFICATION (prediksi kategori)
    │
    ├── Berapa jumlah kelas?
    │   ├── 2 kelas (binary)
    │   │   ├── Dataset balanced? → Accuracy
    │   │   ├── Dataset imbalanced? → F1-Score atau AUC-ROC
    │   │   └── Butuh probabilitas? → Log Loss
    │   │
    │   └── >2 kelas (multiclass)
    │       ├── Dataset balanced? → Accuracy
    │       └── Dataset imbalanced? → Weighted F1-Score
```

**Contoh Kasus**:

1. **Prediksi Harga Rumah** → RMSE atau MAE
   - Kenapa? Kita ingin minimize error dalam satuan harga

2. **Deteksi Spam Email** → F1-Score
   - Kenapa? Dataset biasanya imbalanced (spam < normal email)

3. **Prediksi Churn Pelanggan** → AUC-ROC
   - Kenapa? Kita ingin model yang baik dalam ranking risk

4. **Klasifikasi Jenis Bunga (balanced)** → Accuracy
   - Kenapa? Semua kelas sama penting dan balanced

---

*Modul 1 — Cara Membuat Event Kompetisi Data di Kaggle*

# 📈 Toyota Stock Prices — Panduan Dataset & Notebook

> Dataset: `Toyota_Stock_Prices_1980_2026.csv`  
> Lokasi: `Contoh/Toyota_Stock_Prices_1980_2026.csv`  
> Jumlah data: **11.508 baris × 6 kolom**  
> Rentang waktu: **18 Maret 1980 – 30 Januari 2026** (~46 tahun)

---

## 🎯 Tujuan

Dataset ini berisi harga saham harian Toyota Motor Corporation di pasar bursa.  
Tujuan utama penggunaan dataset ini:

| Tujuan | Deskripsi |
|--------|-----------|
| **Prediksi Harga** | Memprediksi harga penutupan (`Close`) hari berikutnya |
| **Forecasting Jangka Panjang** | Memproyeksikan tren harga saham ke depan (mingguan/bulanan) |
| **Analisis Tren Historis** | Memahami pola kenaikan/penurunan harga selama puluhan tahun |
| **Analisis Volatilitas** | Mengukur seberapa fluktuatif pergerakan harga per periode |
| **Perbandingan Model Time-Series** | Membandingkan performa model statistik vs deep learning vs ML klasik |
| **Simulasi Trading** | Menguji strategi beli/jual berdasarkan prediksi model |

---

## 📋 Penjelasan Kolom

| Kolom | Tipe | Keterangan |
|-------|------|------------|
| `Date` | datetime | Tanggal hari trading (format: YYYY-MM-DD) |
| `Open` | float | Harga pembukaan saham di hari tersebut |
| `High` | float | Harga tertinggi yang dicapai dalam sehari |
| `Low` | float | Harga terendah yang dicapai dalam sehari |
| `Close` | float | Harga penutupan saham — **target utama prediksi** |
| `Volume` | int | Jumlah lembar saham yang diperdagangkan |

> ✅ **Tidak ada missing value** pada dataset ini.  
> ⚠️ Terdapat **102 baris** dengan `Volume = 0` (hari tanpa transaksi / non-trading day).

---

## 🔍 Melihat Bentuk & Isi Data (EDA)

### Langkah 1 — Load & Cek Struktur Awal

```python
import pandas as pd

df = pd.read_csv('../Toyota_Stock_Prices_1980_2026.csv', parse_dates=['Date'])
df = df.sort_values('Date').reset_index(drop=True)

print(df.shape)       # (11508, 6)
df.head()             # 5 baris pertama
df.tail()             # 5 baris terakhir
df.info()             # tipe data + jumlah non-null
df.describe()         # min, max, mean, std per kolom numerik
```

### Langkah 2 — Cek Kualitas Data

```python
# Cek missing value
print(df.isnull().sum())          # semua 0

# Cek hari tanpa volume transaksi
print("Volume = 0:", (df['Volume'] == 0).sum())   # 102 baris

# Rentang tanggal
print("Dari  :", df['Date'].min().date())   # 1980-03-18
print("Sampai:", df['Date'].max().date())   # 2026-01-30
print("Total hari trading:", len(df))       # 11508

# Cek rentang harga Close
print("Close min:", df['Close'].min())   # ~1.78
print("Close max:", df['Close'].max())   # ~243.76
```

### Langkah 3 — Grafik Harga Penutupan Historis

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 5))
plt.plot(df['Date'], df['Close'], color='steelblue', linewidth=0.8)
plt.title('Toyota Stock — Harga Penutupan (Close) 1980–2026')
plt.xlabel('Tahun')
plt.ylabel('Harga (USD)')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### Langkah 4 — Distribusi Harga & Volume

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Histogram Close
axes[0].hist(df['Close'], bins=50, color='steelblue', edgecolor='white')
axes[0].set_title('Distribusi Close Price')
axes[0].set_xlabel('Harga')

# Histogram Volume (hilangkan hari tanpa transaksi)
axes[1].hist(df[df['Volume'] > 0]['Volume'], bins=50, color='mediumpurple', edgecolor='white')
axes[1].set_title('Distribusi Volume Trading')
axes[1].set_xlabel('Volume')

# High-Low spread (volatilitas harian)
df['Daily_Range'] = df['High'] - df['Low']
axes[2].hist(df['Daily_Range'], bins=50, color='tomato', edgecolor='white')
axes[2].set_title('Rentang Harian (High - Low)')
axes[2].set_xlabel('Selisih Harga')

plt.tight_layout()
plt.show()
```

### Langkah 5 — Analisis Tren per Dekade

```python
df['Year']  = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Decade'] = (df['Year'] // 10) * 10

avg_per_year = df.groupby('Year')['Close'].mean()

plt.figure(figsize=(14, 5))
avg_per_year.plot(kind='line', color='darkorange', marker='o', markersize=3)
plt.title('Rata-rata Harga Penutupan per Tahun')
plt.xlabel('Tahun')
plt.ylabel('Rata-rata Close (USD)')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### Langkah 6 — Pola Musiman (Rata-rata per Bulan)

```python
avg_per_month = df.groupby('Month')['Close'].mean()

plt.figure(figsize=(8, 4))
avg_per_month.plot(kind='bar', color='teal', edgecolor='white')
plt.xticks(range(12),
           ['Jan','Feb','Mar','Apr','Mei','Jun','Jul','Agu','Sep','Okt','Nov','Des'],
           rotation=30)
plt.title('Rata-rata Harga Close per Bulan (1980–2026)')
plt.ylabel('Rata-rata Harga')
plt.tight_layout()
plt.show()
```

### Langkah 7 — Volatilitas & Rolling Statistics

```python
df_plot = df.set_index('Date')

plt.figure(figsize=(14, 5))
plt.plot(df_plot['Close'], label='Close', alpha=0.5, linewidth=0.7)
plt.plot(df_plot['Close'].rolling(50).mean(),  label='MA-50',  linewidth=1.5)
plt.plot(df_plot['Close'].rolling(200).mean(), label='MA-200', linewidth=1.5)
plt.title('Close Price + Moving Average (MA-50 & MA-200)')
plt.xlabel('Tanggal')
plt.ylabel('Harga (USD)')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

> 💡 **MA-50** = tren jangka pendek | **MA-200** = tren jangka panjang  
> Titik persilangan MA-50 > MA-200 disebut **Golden Cross** (sinyal beli), sebaliknya **Death Cross** (sinyal jual).

### Langkah 8 — Return Harian & Volatilitas

```python
df['Daily_Return'] = df['Close'].pct_change() * 100   # dalam persen

fig, axes = plt.subplots(1, 2, figsize=(14, 4))

# Distribusi return harian
axes[0].hist(df['Daily_Return'].dropna(), bins=100, color='steelblue',
             edgecolor='white', range=(-10, 10))
axes[0].axvline(0, color='red', linestyle='--')
axes[0].set_title('Distribusi Return Harian (%)')
axes[0].set_xlabel('Return (%)')

# Rolling volatilitas (std 30 hari)
rolling_vol = df.set_index('Date')['Daily_Return'].rolling(30).std()
axes[1].plot(rolling_vol, color='tomato', linewidth=0.7)
axes[1].set_title('Volatilitas Rolling 30 Hari (Std Return)')
axes[1].set_xlabel('Tanggal')
axes[1].set_ylabel('Std Deviation (%)')

plt.tight_layout()
plt.show()
```

### Langkah 9 — Korelasi Antar Kolom

```python
import seaborn as sns

plt.figure(figsize=(7, 5))
corr = df[['Open', 'High', 'Low', 'Close', 'Volume', 'Daily_Range', 'Daily_Return']].corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, square=True, linewidths=0.5)
plt.title('Heatmap Korelasi Fitur Saham Toyota')
plt.tight_layout()
plt.show()
```

> 💡 `Open`, `High`, `Low`, `Close` berkorelasi sangat tinggi (>0.99) karena semuanya adalah harga pada hari yang sama. Untuk modeling, biasanya cukup gunakan `Close` sebagai target dan fitur berbasis lag/window.

---

## ⚙️ Persiapan Data untuk Modeling Time-Series

```python
# Fitur teknikal sederhana berbasis lag
df['Close_Lag1'] = df['Close'].shift(1)
df['Close_Lag5'] = df['Close'].shift(5)
df['MA_7']       = df['Close'].rolling(7).mean()
df['MA_30']      = df['Close'].rolling(30).mean()
df['Std_7']      = df['Close'].rolling(7).std()

# Hapus baris awal yang NaN akibat shift/rolling
df.dropna(inplace=True)

# Split: train (80%) / test (20%) — HARUS urut waktu, jangan random!
split = int(len(df) * 0.8)
train = df.iloc[:split]
test  = df.iloc[split:]

print(f"Train: {len(train)} baris ({train['Date'].min().date()} → {train['Date'].max().date()})")
print(f"Test : {len(test)}  baris ({test['Date'].min().date()}  → {test['Date'].max().date()})")
```

> ⚠️ **Penting:** Untuk data time-series, jangan gunakan `train_test_split` dengan `shuffle=True`.  
> Data HARUS dipotong secara urut agar tidak ada kebocoran data dari masa depan ke masa lalu.

---

## 🤖 Bisa Digunakan untuk Apa Saja?

### 1. 📉 Prediksi Harga Close (Regression / Forecasting)

**Target:** `Close` harga esok hari  
**Metrik:** MAE, RMSE, MAPE, R²

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

features = ['Close_Lag1', 'Close_Lag5', 'MA_7', 'MA_30', 'Std_7', 'Volume']
X_train = train[features]
X_test  = test[features]
y_train = train['Close']
y_test  = test['Close']

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

print("MAE :", mean_absolute_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
```

> Notebook tersedia: `05_stock_random_forest.ipynb`, `06_stock_xgboost.ipynb`, `07_stock_linear_regression.ipynb`

---

### 2. 📊 Forecasting dengan Model Statistik

**Model:** ARIMA, Prophet  
**Cocok untuk:** tren jangka panjang, seasonality

```python
# ARIMA — model klasik untuk time-series stasioner
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(train['Close'], order=(5, 1, 0))
result = model.fit()
forecast = result.forecast(steps=len(test))
```

> Notebook tersedia: `01_stock_arima.ipynb`, `02_stock_prophet.ipynb`

---

### 3. 🧠 Forecasting dengan Deep Learning

**Model:** LSTM, GRU  
**Cocok untuk:** menangkap pola sekuensial jangka panjang

```python
# Data perlu dinormalisasi dan diubah ke format sekuens [samples, timesteps, features]
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaled = scaler.fit_transform(df[['Close']])
```

> Notebook tersedia: `03_stock_lstm.ipynb`, `04_stock_gru.ipynb`

---

### 4. 🏆 Perbandingan Semua Model

Lihat perbandingan lengkap 7 model dalam satu notebook:

> `00_stock_model_comparison.ipynb`

---

## 📊 Distribusi & Karakteristik Data

```
Rentang harga Close : $1.78  → $243.76
Rata-rata Close     : $56.44
Median Close        : $41.57
Standar Deviasi     : $51.05

Periode tren naik signifikan:
  - 2012 → 2015 : dari ~$80 ke ~$180 (+125%)
  - 2019 → 2021 : dari ~$130 ke ~$200 (+54%)
  - 2023 → 2024 : dari ~$160 ke ~$243 (tertinggi sepanjang masa)

Volume 0 (no-trade) : 102 hari
```

---

## 📁 Struktur Notebook

| File | Model | Pendekatan |
|------|-------|------------|
| `00_stock_model_comparison.ipynb` | Semua model | Perbandingan lengkap |
| `01_stock_arima.ipynb` | ARIMA(5,1,0) | Statistik klasik |
| `02_stock_prophet.ipynb` | Prophet (Meta) | Additive time-series |
| `03_stock_lstm.ipynb` | LSTM | Deep Learning (PyTorch) |
| `04_stock_gru.ipynb` | GRU | Deep Learning (PyTorch) |
| `05_stock_random_forest.ipynb` | Random Forest | Machine Learning |
| `06_stock_xgboost.ipynb` | XGBoost | Machine Learning |
| `07_stock_linear_regression.ipynb` | Ridge Regression | Linear baseline |

---

## 🏅 Ringkasan Hasil Model (dari `00_stock_model_comparison.ipynb`)

| Peringkat | Model | MAE | RMSE | MAPE (%) | R² |
|-----------|-------|-----|------|----------|----|
| 🥇 1 | Ridge Regression | rendah | rendah | ~kecil | ~1.0 |
| 🥈 2 | XGBoost | rendah | rendah | ~kecil | tinggi |
| 🥉 3 | Random Forest | sedang | sedang | sedang | tinggi |
| 4 | GRU | sedang | sedang | sedang | tinggi |
| 5 | LSTM | sedang | sedang | sedang | tinggi |
| 6 | Prophet | lebih tinggi | lebih tinggi | lebih tinggi | sedang |
| 7 | ARIMA | tertinggi | tertinggi | tertinggi | rendah |

> ℹ️ Model ML (Ridge, XGBoost, RF) unggul karena menggunakan fitur lag harga yang sangat prediktif. ARIMA/Prophet bekerja murni pada pola waktu tanpa fitur tambahan.

---

## 💡 Tips Eksplorasi Lanjutan

1. **Bollinger Bands** — gabungkan MA + Std untuk melihat batas atas/bawah harga normal
2. **RSI (Relative Strength Index)** — indikator overbought/oversold
3. **Candlestick Chart** — gunakan `mplfinance` untuk visualisasi OHLC yang lebih profesional
4. **Anomali Deteksi** — cari hari dengan lonjakan/penurunan ekstrem (outlier volume/return)
5. **Multi-step Forecasting** — prediksi 5/10/30 hari ke depan sekaligus

```python
# Candlestick chart dengan mplfinance
import mplfinance as mpf

df_ohlc = df.set_index('Date')[['Open', 'High', 'Low', 'Close', 'Volume']]
mpf.plot(df_ohlc.tail(90), type='candle', volume=True,
         title='Toyota Stock — 90 Hari Terakhir',
         style='charles', mav=(20, 50))
```

---

*Dataset ini cocok sebagai bahan latihan kompetisi Kaggle bertema financial forecasting atau time-series prediction.*

# Bab 2 — Tahapan Mengolah Data dengan Machine Learning

Sebelum melatih model machine learning, data harus diolah terlebih dahulu. Ini seperti memasak — kita harus mencuci dan memotong bahan sebelum dimasak!

## Data Cleaning (Pembersihan Data)

**Apa itu?**
Proses membersihkan data dari kesalahan, duplikasi, dan data yang tidak konsisten.

**Masalah Umum**:
- **Duplikasi**: Data yang sama muncul lebih dari sekali
- **Typo**: Kesalahan penulisan (misal: "Jakrta" harusnya "Jakarta")
- **Inkonsistensi**: "Jakarta", "jakarta", "DKI Jakarta" seharusnya sama
- **Outlier**: Data yang sangat berbeda dari yang lain (misal: umur 200 tahun)

**Contoh**:
```python
import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Hapus duplikasi
df = df.drop_duplicates()

# Perbaiki inkonsistensi
df['lokasi'] = df['lokasi'].str.lower().str.strip()

# Hapus outlier sederhana
df = df[df['umur'] < 100]  # Hapus umur yang tidak masuk akal
```

**Analogi**: Seperti menyortir beras sebelum dimasak — buang yang rusak, bersihkan yang kotor.

## Handling Missing Value (Menangani Data Kosong)

**Apa itu?**
Menangani data yang tidak lengkap atau kosong (NULL, NaN, None).

**Strategi Penanganan**:

| Strategi | Kapan Digunakan | Cara Kerja |
|----------|-----------------|------------|
| **Drop/Hapus** | Missing value sedikit (<5%) | Hapus baris atau kolom yang kosong |
| **Fill dengan Mean** | Data numerik, distribusi normal | Isi dengan rata-rata |
| **Fill dengan Median** | Data numerik, ada outlier | Isi dengan nilai tengah |
| **Fill dengan Mode** | Data kategorikal | Isi dengan nilai paling sering muncul |
| **Forward Fill** | Data time series | Isi dengan nilai sebelumnya |
| **Prediksi** | Data penting, banyak missing | Gunakan model untuk prediksi nilai kosong |

**Contoh**:
```python
# Lihat missing value
print(df.isnull().sum())

# Strategi 1: Hapus baris dengan missing value
df_clean = df.dropna()

# Strategi 2: Isi dengan mean (untuk kolom numerik)
df['umur'].fillna(df['umur'].mean(), inplace=True)

# Strategi 3: Isi dengan mode (untuk kolom kategorikal)
df['lokasi'].fillna(df['lokasi'].mode()[0], inplace=True)
```

**Analogi**: Seperti mengisi formulir — jika ada yang kosong, bisa diabaikan, diisi dengan "tidak tahu", atau ditanyakan ulang.

## Encoding Data Kategorikal

**Apa itu?**
Mengubah data kategori (text) menjadi angka, karena komputer hanya mengerti angka!

**Jenis Encoding**:

### 1. Label Encoding
Mengubah kategori menjadi angka 0, 1, 2, 3, ...

**Contoh**:
```
Sebelum: ["Jakarta", "Bandung", "Surabaya", "Jakarta"]
Sesudah: [0, 1, 2, 0]
```

**Kapan Digunakan**: 
- Data ordinal (ada urutan): Pendidikan (SD=0, SMP=1, SMA=2, S1=3)
- Tree-based models (Decision Tree, Random Forest)

**Kode**:
```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['lokasi_encoded'] = le.fit_transform(df['lokasi'])
```

### 2. One-Hot Encoding
Mengubah tiap kategori menjadi kolom baru dengan nilai 0 atau 1.

**Contoh**:
```
Sebelum:
Lokasi: ["Jakarta", "Bandung", "Jakarta"]

Sesudah:
Lokasi_Jakarta: [1, 0, 1]
Lokasi_Bandung: [0, 1, 0]
Lokasi_Surabaya: [0, 0, 0]
```

**Kapan Digunakan**:
- Data nominal (tidak ada urutan): Warna, Kota, Jenis Kelamin
- Model linear (Linear Regression, Logistic Regression)

**Kode**:
```python
# Cara 1: Pandas
df_encoded = pd.get_dummies(df, columns=['lokasi'])

# Cara 2: Sklearn
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
encoded = encoder.fit_transform(df[['lokasi']])
```

**Analogi**: Seperti mengubah nama buah menjadi kode angka di gudang, agar komputer kasir bisa menghitung.

## Normalisasi / Scaling (Penskalaan Data)

**Apa itu?**
Mengubah skala data agar semua fitur memiliki rentang yang sama.

**Kenapa Perlu?**
Bayangkan dua fitur:
- Luas rumah: 50-500 m² (ratusan)
- Jumlah kamar: 1-5 (satuan)

Model mungkin akan menganggap luas rumah lebih penting hanya karena angkanya lebih besar! Padahal belum tentu.

**Jenis Scaling**:

### 1. Normalization (Min-Max Scaling)
Mengubah data ke rentang 0-1.

**Formula**: 
$$X_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}}$$

**Contoh**:
```
Sebelum: [10, 50, 100]
Sesudah: [0, 0.44, 1]
```

**Kapan**: Data tidak ada outlier ekstrem, butuh rentang tertentu (0-1).

**Kode**:
```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df[['luas', 'kamar']] = scaler.fit_transform(df[['luas', 'kamar']])
```

### 2. Standardization (Z-score Scaling)
Mengubah data agar mean=0 dan standard deviation=1.

**Formula**: 
$$X_{std} = \frac{X - \mu}{\sigma}$$

**Contoh**:
```
Sebelum: [10, 50, 100] (mean=53.3, std=45)
Sesudah: [-0.96, -0.07, 1.04]
```

**Kapan**: Ada outlier, algoritma sensitif terhadap distribusi (SVM, Neural Network).

**Kode**:
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df[['luas', 'kamar']] = scaler.fit_transform(df[['luas', 'kamar']])
```

**Tabel Perbandingan**:

| Aspek | Normalization | Standardization |
|-------|---------------|-----------------|
| Rentang | 0 to 1 | -∞ to +∞ |
| Sensitif Outlier | Ya | Tidak terlalu |
| Kapan | Data terbatas, KNN, Neural Net | Ada outlier, SVM, PCA |

**Analogi**: Seperti membandingkan tinggi badan dalam cm dengan berat badan dalam kg — kita perlu "samakan satuan" agar fair.

## Split Data (Train-Test Split)

**Apa itu?**
Membagi data menjadi dua bagian:
1. **Training Set**: Untuk melatih model (biasanya 70-80%)
2. **Test Set**: Untuk menguji model (biasanya 20-30%)

**Kenapa Perlu?**
Kita butuh "ujian" untuk mengetahui apakah model benar-benar pintar, bukan cuma hafalan!

**Visual**:
```
Dataset Lengkap (100%)
├── Training Set (80%) → Untuk belajar
└── Test Set (20%) → Untuk ujian
```

**Tambahan: Validation Set**
```
Dataset Lengkap (100%)
├── Training Set (70%) → Untuk belajar
├── Validation Set (15%) → Untuk tuning parameter
└── Test Set (15%) → Untuk ujian final
```

**Kode**:
```python
from sklearn.model_selection import train_test_split

# Pisahkan fitur dan target
X = df.drop('harga', axis=1)  # Fitur
y = df['harga']  # Target

# Split 80-20
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,  # 20% untuk test
    random_state=42  # Agar hasil konsisten
)

print(f"Training: {len(X_train)} samples")
print(f"Testing: {len(X_test)} samples")
```

**Analogi**: Seperti belajar untuk ujian. Kita belajar dari soal latihan (training), bukan dari soal ujian asli (test). Kalau belajar dari soal ujian, itu namanya nyontek!

**Best Practices**:
- ✅ Split **sebelum** preprocessing apapun
- ✅ Gunakan `random_state` agar reproducible
- ✅ Pastikan distribusi target seimbang (gunakan `stratify` untuk classification)
- ❌ Jangan lihat test set sampai model final
- ❌ Jangan fit scaler/encoder di seluruh data, hanya di training set

**Kode dengan Stratify (untuk classification)**:
```python
# Untuk memastikan proporsi kelas seimbang
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,
    stratify=y,  # Distribusi kelas sama di train dan test
    random_state=42
)
```

---

*Modul 2 — Cara Mengolah Data Tabel dengan Machine Learning*

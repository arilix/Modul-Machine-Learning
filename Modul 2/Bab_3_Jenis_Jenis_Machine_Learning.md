# Bab 3 — Jenis-jenis Machine Learning

Machine Learning bisa dibagi menjadi beberapa kategori berdasarkan cara belajarnya.

## Supervised Learning (Pembelajaran Terawasi)

**Apa itu?**
Model belajar dari data yang sudah diberi label/jawaban. Seperti belajar dengan kunci jawaban!

**Karakteristik**:
- Ada target/label yang jelas (Y)
- Model belajar pola dari X → Y
- Bisa dievaluasi dengan akurasi

**Jenis Task**:

1. **Classification (Klasifikasi)**: Prediksi kategori
   - Contoh: Spam atau bukan? Penyakit A, B, atau C?
   - Output: Kategori/Kelas
   
2. **Regression (Regresi)**: Prediksi nilai numerik
   - Contoh: Prediksi harga rumah, suhu besok
   - Output: Angka kontinu

**Contoh Real Life**:
```
Input (X)              → Output (Y)
-----------------      → ----------
Luas, lokasi rumah     → Harga rumah (Regression)
Gejala penyakit        → Jenis penyakit (Classification)
Gambar hewan           → Kucing/Anjing (Classification)
Data cuaca             → Suhu besok (Regression)
```

**Kode Sederhana**:
```python
from sklearn.ensemble import RandomForestClassifier

# Data training (dengan label)
X_train = [[120, 3], [80, 2], [200, 4]]  # [luas, kamar]
y_train = ['mahal', 'murah', 'mahal']     # Label

# Training
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Prediksi (data baru tanpa label)
X_new = [[150, 3]]
prediction = model.predict(X_new)
print(prediction)  # Output: ['mahal']
```

**Algoritma Populer**: Linear Regression, Logistic Regression, Decision Tree, Random Forest, XGBoost, SVM, Neural Network

## Unsupervised Learning (Pembelajaran Tanpa Pengawasan)

**Apa itu?**
Model belajar dari data **tanpa label**. Model mencari pola sendiri!

**Karakteristik**:
- Tidak ada target/label (tidak ada Y)
- Model mencari struktur tersembunyi dalam data
- Lebih eksploratif

**Jenis Task**:

1. **Clustering (Pengelompokan)**: Mengelompokkan data yang mirip
   - Contoh: Segmentasi customer, pemisahan topik
   
2. **Dimensionality Reduction**: Mengurangi jumlah fitur
   - Contoh: PCA, t-SNE untuk visualisasi
   
3. **Association**: Mencari hubungan antar item
   - Contoh: Market basket analysis (orang yang beli A juga beli B)

**Contoh Real Life**:
```
Input (X)                   → Output
----------------------      → ---------------------------
Data customer               → 3 kelompok: Premium, Reguler, Budget
Artikel berita              → Topik: Politik, Olahraga, Ekonomi
Transaksi belanja           → Pola: Beli roti → beli susu
```

**Kode Sederhana (Clustering)**:
```python
from sklearn.cluster import KMeans

# Data tanpa label
X = [[120, 3], [125, 3], [80, 2], [85, 2], [200, 5]]

# Training (mencari 2 kelompok)
model = KMeans(n_clusters=2)
clusters = model.fit_predict(X)

print(clusters)  # Output: [0, 0, 1, 1, 0]
# Artinya: data 1,2,5 satu grup; data 3,4 satu grup
```

**Algoritma Populer**: K-Means, DBSCAN, Hierarchical Clustering, PCA, t-SNE, Apriori

## Semi-Supervised Learning

**Apa itu?**
Kombinasi supervised dan unsupervised. Sebagian data punya label, sebagian tidak.

**Kenapa Berguna?**
- Labeling data mahal dan butuh waktu
- Contoh: Punya 10,000 gambar, tapi cuma 100 yang sudah dilabel

**Cara Kerja**:
1. Latih model dengan data berlabel (sedikit)
2. Gunakan model untuk label data tidak berlabel (banyak)
3. Latih ulang dengan data yang lebih banyak

**Contoh Real Life**:
- Google Photos: Sebagian foto kita tag manual, sisanya otomatis
- Speech recognition: Sebagian audio di-transcript manual, sisanya otomatis

**Algoritma**: Self-training, Co-training, Label Propagation

## Reinforcement Learning (Pembelajaran Penguatan)

**Apa itu?**
Model belajar dari trial-and-error dengan sistem reward (hadiah) dan punishment (hukuman).

**Analogi**: Seperti melatih anjing dengan memberikan snack kalau benar dan tidak memberikan apa-apa kalau salah.

**Karakteristik**:
- Ada agent (pelaku), environment (lingkungan), action (aksi), reward (hadiah)
- Agent belajar dari pengalaman sendiri
- Cocok untuk sequential decision making

**Contoh Real Life**:
- Game AI (AlphaGo, Dota 2 bot)
- Robot yang belajar jalan
- Self-driving car
- Recommendation system yang adapt

**Komponen**:
```
Agent (Robot) melakukan Action (jalan)
→ Environment berubah (posisi robot)
→ Agent dapat Reward (+10 kalau benar, -5 kalau nabrak)
→ Agent belajar: "Oh, jalan ke kanan lebih baik"
```

**Algoritma**: Q-Learning, Deep Q-Network (DQN), Policy Gradient, Actor-Critic

---

*Modul 2 — Cara Mengolah Data Tabel dengan Machine Learning*

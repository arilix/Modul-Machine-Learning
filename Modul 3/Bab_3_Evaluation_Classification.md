# Bab 3 — Evaluation untuk Classification

Classification adalah memprediksi kategori/kelas (spam/bukan, kucing/anjing, dll). Mari kita pelajari metric untuk mengukur seberapa akurat klasifikasi kita!

## Setup Contoh: Email Spam Detection

Kita punya 10 email yang sudah diklasifikasi:

| Email | Aktual | Prediksi |
|-------|--------|----------|
| 1 | Spam | Spam ✅ |
| 2 | Spam | Spam ✅ |
| 3 | Spam | Normal ❌ |
| 4 | Normal | Spam ❌ |
| 5 | Normal | Normal ✅ |
| 6 | Normal | Normal ✅ |
| 7 | Normal | Normal ✅ |
| 8 | Normal | Normal ✅ |
| 9 | Normal | Normal ✅ |
| 10 | Normal | Normal ✅ |

**Hasil**:
- Spam aktual: 3 email
- Normal aktual: 7 email
- Benar prediksi: 8 email
- Salah prediksi: 2 email

---

## 1. Confusion Matrix

### Apa itu?

**Tabel yang menunjukkan benar/salah prediksi untuk setiap kelas.**

### Struktur

```
                Predicted
                Spam  |  Normal
Actual  Spam    TP    |    FN
        Normal  FP    |    TN
```

**Istilah Penting**:
- **TP (True Positive)**: Prediksi Spam ✅, Aktual Spam
- **TN (True Negative)**: Prediksi Normal ✅, Aktual Normal
- **FP (False Positive)**: Prediksi Spam ❌, Aktual Normal (Type I Error)
- **FN (False Negative)**: Prediksi Normal ❌, Aktual Spam (Type II Error)

### Contoh Kita

```
                Predicted
                Spam  |  Normal
Actual  Spam     2    |    1      (TP=2, FN=1)
        Normal   1    |    6      (FP=1, TN=6)
```

- **TP** = 2 (Spam diprediksi Spam)
- **TN** = 6 (Normal diprediksi Normal)
- **FP** = 1 (Normal tapi diprediksi Spam) → Email penting masuk spam folder ❌
- **FN** = 1 (Spam tapi diprediksi Normal) → Spam masuk inbox ❌

### Analogi Supaya Ingat

**Analogi: Test Hamil**
- **TP**: Test bilang hamil ✅, memang hamil
- **TN**: Test bilang tidak hamil ✅, memang tidak hamil
- **FP**: Test bilang hamil ❌, tapi tidak hamil (False alarm!)
- **FN**: Test bilang tidak hamil ❌, tapi hamil (Missed detection!)

### Kode Python

```python
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

y_true = ['Spam', 'Spam', 'Spam', 'Normal', 'Normal', 
          'Normal', 'Normal', 'Normal', 'Normal', 'Normal']
y_pred = ['Spam', 'Spam', 'Normal', 'Spam', 'Normal', 
          'Normal', 'Normal', 'Normal', 'Normal', 'Normal']

cm = confusion_matrix(y_true, y_pred, labels=['Spam', 'Normal'])

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
```

---

## 2. Accuracy (Akurasi)

### Apa itu?

**Persentase prediksi yang benar dari semua prediksi.**

### Rumus

$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN} = \frac{Benar}{Total}$$

### Contoh Hitung

```
Accuracy = (2 + 6) / (2 + 6 + 1 + 1)
         = 8 / 10
         = 0.8 = 80%
```

**Artinya**: Model benar **80%** dari waktu.

### Kapan Digunakan?

✅ **Cocok untuk**:
- Dataset balanced (jumlah setiap kelas mirip)
- Semua error sama pentingnya
- Metric awal untuk baseline

❌ **Tidak cocok untuk**:
- Dataset imbalanced (99:1)
- Kelas tertentu lebih penting

### Contoh Imbalanced Data Problem

**Dataset**: 1000 email, 990 Normal, 10 Spam

**Model Naif**: Tebak semua "Normal"
```
Accuracy = 990 / 1000 = 99% ← Terlihat bagus!
```

Tapi model gagal deteksi semua spam! ❌

**Solusi**: Gunakan Precision, Recall, atau F1-Score.

### Kelebihan

- ✅ Sangat mudah dipahami
- ✅ Standar untuk banyak kasus
- ✅ Single number untuk performa

### Kekurangan

- ❌ Misleading untuk imbalanced data
- ❌ Tidak bedakan tipe error (FP vs FN)

### Kode Python

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_true, y_pred)
print(f"Accuracy: {accuracy:.2%}")  # 80.00%
```

---

## 3. Precision (Presisi)

### Apa itu?

**Dari semua yang diprediksi Spam, berapa yang benar-benar Spam?**

### Rumus

$$Precision = \frac{TP}{TP + FP} = \frac{True\ Positive}{All\ Predicted\ Positive}$$

### Contoh Hitung

```
Predicted Spam: Email 1, 2, 4 (3 email)
Yang benar Spam: Email 1, 2 (2 email)

Precision = 2 / 3 = 0.67 = 67%
```

**Artinya**: Kalau model bilang "Spam", **67%** kemungkinan memang Spam.

### Analogi

**Precision = Ketepatan**

Seperti pemanah:
- Precision tinggi = Panah mengelompok rapat (konsisten)
- Precision rendah = Panah menyebar kemana-mana

**Contoh Real Life**:
Sistem rekomendasi film: "Film ini 90% cocok untuk Anda"
- Precision tinggi → Rekomendasi tepat (film yang direkomendasikan memang bagus)
- Precision rendah → Banyak rekomendasi jelek

### Kapan Digunakan?

✅ **Cocok untuk**:
- False Positive SANGAT BURUK
- Contoh: Spam filter (email penting masuk spam = buruk!)
- Contoh: Medical diagnosis (bilang sakit padahal sehat = buruk!)

❌ **Tidak cocok untuk**:
- False Negative lebih buruk (gunakan Recall)

### Kelebihan

- ✅ Fokus pada "positives" yang benar
- ✅ Bagus untuk kasus "jangan sampai salah positive"

### Kekurangan

- ❌ Tidak peduli False Negative
- ❌ Bisa di-cheat (prediksi sedikit tapi sangat yakin)

### Kode Python

```python
from sklearn.metrics import precision_score

precision = precision_score(y_true, y_pred, pos_label='Spam')
print(f"Precision: {precision:.2%}")  # 66.67%
```

---

## 4. Recall (Sensitivitas / True Positive Rate)

### Apa itu?

**Dari semua Spam aktual, berapa yang berhasil dideteksi?**

### Rumus

$$Recall = \frac{TP}{TP + FN} = \frac{True\ Positive}{All\ Actual\ Positive}$$

### Contoh Hitung

```
Spam aktual: Email 1, 2, 3 (3 email)
Yang berhasil dideteksi: Email 1, 2 (2 email)

Recall = 2 / 3 = 0.67 = 67%
```

**Artinya**: Model berhasil deteksi **67%** dari semua spam.

### Analogi

**Recall = Kelengkapan**

Seperti jaring ikan:
- Recall tinggi = Jaring besar, tangkap banyak ikan (tapi mungkin ada sampah)
- Recall rendah = Jaring kecil, tangkap sedikit (tapi ikan yang ditangkap bagus)

**Contoh Real Life**:
Deteksi kanker:
- Recall tinggi → Semua pasien kanker terdeteksi (meski ada false alarm)
- Recall rendah → Banyak pasien kanker miss (berbahaya!)

### Kapan Digunakan?

✅ **Cocok untuk**:
- False Negative SANGAT BURUK
- Contoh: Deteksi penyakit (jangan sampai miss!)
- Contoh: Fraud detection (jangan sampai miss fraud!)
- Contoh: Airport security (jangan sampai lolos!)

❌ **Tidak cocok untuk**:
- False Positive lebih buruk (gunakan Precision)

### Kelebihan

- ✅ Fokus pada "jangan sampai miss"
- ✅ Bagus untuk safety-critical

### Kekurangan

- ❌ Tidak peduli False Positive
- ❌ Bisa di-cheat (prediksi semua positive!)

### Kode Python

```python
from sklearn.metrics import recall_score

recall = recall_score(y_true, y_pred, pos_label='Spam')
print(f"Recall: {recall:.2%}")  # 66.67%
```

---

## 5. F1-Score

### Apa itu?

**Harmonic mean dari Precision dan Recall.** Balance antara keduanya!

### Rumus

$$F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$

### Kenapa Harmonic Mean?

Harmonic mean "hukum berat" nilai yang rendah.

**Contoh**:
- Precision = 90%, Recall = 10%
- Arithmetic mean = (90+10)/2 = 50%
- Harmonic mean (F1) = 2×(90×10)/(90+10) = 18%

F1 lebih rendah karena salah satu metric jelek!

### Contoh Hitung

```
Precision = 0.67
Recall = 0.67

F1 = 2 × (0.67 × 0.67) / (0.67 + 0.67)
   = 2 × 0.45 / 1.34
   = 0.67 = 67%
```

### Kapan Digunakan?

✅ **Cocok untuk**:
- Dataset imbalanced
- Precision dan Recall sama pentingnya
- Butuh single metric tapi balance
- Kompetisi ML (sering jadi metric official)

❌ **Tidak cocok untuk**:
- Salah satu metric jauh lebih penting (gunakan yang spesifik)

### Variasi: F-beta Score

$$F_\beta = (1 + \beta^2) \times \frac{Precision \times Recall}{\beta^2 \times Precision + Recall}$$

- **β = 1** → F1-Score (balance)
- **β = 2** → F2-Score (Recall 2× lebih penting)
- **β = 0.5** → F0.5-Score (Precision 2× lebih penting)

### Kelebihan

- ✅ Single metric yang balance
- ✅ Bagus untuk imbalanced data
- ✅ Widely accepted

### Kekurangan

- ❌ Tidak intuitif untuk non-teknikal
- ❌ Mencampur dua konsep berbeda

### Kode Python

```python
from sklearn.metrics import f1_score

f1 = f1_score(y_true, y_pred, pos_label='Spam')
print(f"F1-Score: {f1:.2%}")  # 66.67%
```

---

## 6. Specificity (True Negative Rate)

### Apa itu?

**Dari semua Normal aktual, berapa yang benar diprediksi Normal?**

### Rumus

$$Specificity = \frac{TN}{TN + FP} = \frac{True\ Negative}{All\ Actual\ Negative}$$

### Contoh Hitung

```
Normal aktual: 7 email
Yang benar diprediksi Normal: 6 email

Specificity = 6 / 7 = 0.86 = 86%
```

**Artinya**: Model benar **86%** dalam mengidentifikasi email normal.

### Kapan Digunakan?

✅ **Cocok untuk**:
- False Positive sangat buruk
- Evaluasi bersamaan dengan Recall
- Medical testing

❌ **Tidak cocok untuk**:
- Standalone metric (kurang populer)

### Kelebihan

- ✅ Complement dari Recall
- ✅ Penting untuk evaluasi komprehensif

### Kekurangan

- ❌ Jarang dipakai sendirian
- ❌ Bisa misleading di imbalanced data

### Kode Python

```python
# Manual calculation
specificity = TN / (TN + FP)
print(f"Specificity: {specificity:.2%}")
```

---

## 7. ROC-AUC (Receiver Operating Characteristic - Area Under Curve)

### Apa itu?

**Mengukur kemampuan model membedakan kelas di berbagai threshold.** Nilai 0-1.

### Konsep

**ROC Curve**: Plot antara True Positive Rate (Recall) vs False Positive Rate

**AUC**: Area di bawah kurva ROC

### Interpretasi

| AUC | Artinya |
|-----|---------|
| **1.0** | Perfect classifier! ✨ |
| **0.9-1.0** | Excellent |
| **0.8-0.9** | Good |
| **0.7-0.8** | Fair |
| **0.5-0.7** | Poor |
| **0.5** | Random guess (sama dengan lempar koin) |
| **< 0.5** | Worse than random! ❌ |

### Analogi

Bayangkan Anda sorting email berdasarkan "spam score" 0-100:

**Good model** (AUC tinggi):
- Spam: Score 80, 85, 90, 95
- Normal: Score 5, 10, 15, 20
- **Mudah bedakan!**

**Bad model** (AUC rendah):
- Spam: Score 40, 50, 60, 45
- Normal: Score 35, 55, 48, 52
- **Susah bedakan!**

### Kapan Digunakan?

✅ **Cocok untuk**:
- Evaluasi model probabilistik
- Dataset imbalanced (lebih baik dari accuracy)
- Membandingkan model
- Tidak tergantung threshold tertentu

❌ **Tidak cocok untuk**:
- Multi-class (butuh adaptasi)
- Interpretasi untuk stakeholder (terlalu teknis)

### Kelebihan

- ✅ Threshold-independent
- ✅ Bagus untuk imbalanced data
- ✅ Standard untuk binary classification

### Kekurangan

- ❌ Susah dijelaskan ke non-teknikal
- ❌ Tidak memberitahu "berapa threshold terbaik"

### Kode Python

```python
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt

# Perlu probability predictions
y_proba = model.predict_proba(X_test)[:, 1]

# Calculate AUC
auc = roc_auc_score(y_true_binary, y_proba)
print(f"AUC: {auc:.3f}")

# Plot ROC Curve
fpr, tpr, thresholds = roc_curve(y_true_binary, y_proba)
plt.plot(fpr, tpr, label=f'AUC = {auc:.3f}')
plt.plot([0, 1], [0, 1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()
```

---

## 8. Log Loss (Cross-Entropy Loss)

### Apa itu?

**Mengukur "ketidakpastian" prediksi probabilitas.** Semakin rendah, semakin yakin dan benar!

### Rumus

$$Log\ Loss = -\frac{1}{n}\sum_{i=1}^{n}[y_i \log(p_i) + (1-y_i)\log(1-p_i)]$$

### Konsep

Log Loss tidak hanya peduli **benar/salah**, tapi juga **seberapa yakin**.

**Contoh**:

| Aktual | Prediksi Proba | Benar? | Log Loss |
|--------|----------------|--------|----------|
| Spam | 95% Spam | ✅ | 0.05 (rendah, bagus!) |
| Spam | 55% Spam | ✅ | 0.60 (tinggi, kurang yakin) |
| Normal | 60% Normal | ✅ | 0.51 |
| Normal | 45% Spam | ❌ | 0.80 (tinggi, salah!) |

**Key**: Model yang yakin (95%) lebih baik daripada yang ragu-ragu (55%), meski kedua benar!

### Kapan Digunakan?

✅ **Cocok untuk**:
- Model probabilistik (Logistic Regression, Neural Net)
- Butuh confidence dalam prediksi
- Loss function saat training
- Kompetisi (sering jadi metric)

❌ **Tidak cocok untuk**:
- Interpretasi untuk stakeholder (terlalu teknis)
- Model yang tidak output probabilitas

### Kelebihan

- ✅ Reward confidence yang benar
- ✅ Penalty besar untuk salah dengan yakin
- ✅ Differentiable (bagus untuk optimization)

### Kekurangan

- ❌ Susah diinterpretasi
- ❌ Sensitif terhadap probability calibration

### Kode Python

```python
from sklearn.metrics import log_loss

# Perlu probability predictions
y_proba = model.predict_proba(X_test)

logloss = log_loss(y_true, y_proba)
print(f"Log Loss: {logloss:.4f}")
```

---

## 9. PR-AUC (Precision-Recall Area Under Curve)

### Apa itu?

**Area di bawah kurva Precision-Recall.** Mengukur trade-off Precision vs Recall di berbagai threshold sekaligus.

### Perbedaan dengan ROC-AUC

| Aspek | ROC-AUC | PR-AUC |
|-------|---------|--------|
| **X-axis** | False Positive Rate | Recall |
| **Y-axis** | True Positive Rate | Precision |
| **Baseline random** | 0.5 (garis diagonal) | Proporsi kelas positif |
| **Sensitif imbalanced** | Kurang | Sangat sensitif |
| **Kapan lebih baik** | Data cukup balanced | Data sangat imbalanced |

### Kenapa PR-AUC Lebih Baik untuk Imbalanced Data?

**Contoh**: 10,000 data, 100 positif (1%), 9,900 negatif (99%)

**Model Jelek** yang prediksi 200 positif (100 benar, 100 salah):
```
ROC-AUC:
  TPR = 100/100 = 100%
  FPR = 100/9900 = 1%
  → ROC terlihat BAGUS (FPR rendah)

PR-AUC:
  Precision = 100/200 = 50%
  Recall = 100/100 = 100%
  → PR terlihat REALISTIS (Precision rendah)
```

ROC-AUC bisa "terlalu optimis" karena TN (9,900) mendominasi perhitungan FPR.

### Interpretasi

| PR-AUC | Artinya |
|--------|---------|
| **1.0** | Perfect! ✨ |
| **> 0.8** | Excellent |
| **0.5 - 0.8** | Good to Fair |
| **< 0.5** | Poor |
| **= proporsi positif** | Random guess |

⚠️ **Catatan**: Baseline PR-AUC = proporsi kelas positif, BUKAN 0.5!
- Data 50:50 → Baseline = 0.5
- Data 1:99 → Baseline = 0.01

### Kapan Digunakan?

✅ **Cocok untuk**:
- Data sangat imbalanced (99:1, 95:5)
- Kelas positif lebih penting
- Ingin evaluasi lebih realistis daripada ROC-AUC
- Fraud detection, rare disease, anomaly detection

❌ **Tidak cocok untuk**:
- Data balanced (ROC-AUC sudah cukup)
- Multi-class (butuh adaptasi)

### Kode Python

```python
from sklearn.metrics import precision_recall_curve, auc
import matplotlib.pyplot as plt

# Hitung PR Curve
precisions, recalls, thresholds = precision_recall_curve(y_true, y_proba)

# Hitung AUC
pr_auc = auc(recalls, precisions)
print(f"PR-AUC: {pr_auc:.3f}")

# Plot
plt.figure(figsize=(8, 6))
plt.plot(recalls, precisions, label=f'PR-AUC = {pr_auc:.3f}')

# Baseline (random classifier)
baseline = sum(y_true) / len(y_true)
plt.axhline(y=baseline, color='r', linestyle='--', label=f'Random = {baseline:.3f}')

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend()
plt.show()
```

### Tips: ROC-AUC vs PR-AUC

```
Kapan pakai apa?

Data balanced (50:50 s/d 70:30)
  → ROC-AUC ✅

Data imbalanced (90:10 s/d 99:1)
  → PR-AUC ✅ (lebih informatif)

Data sangat imbalanced (>99:1)
  → PR-AUC ✅ (WAJIB, ROC-AUC misleading)
```

---

## 10. Balanced Accuracy

### Apa itu?

**Rata-rata Recall per kelas.** Memberikan bobot yang sama untuk setiap kelas, tidak peduli seberapa besar kelasnya.

### Rumus

$$Balanced\ Accuracy = \frac{1}{K}\sum_{k=1}^{K} Recall_k$$

Untuk binary classification:

$$Balanced\ Accuracy = \frac{Sensitivity + Specificity}{2} = \frac{TPR + TNR}{2}$$

### Kenapa Perlu Balanced Accuracy?

**Problem Accuracy biasa**:
```
Data: 990 Normal, 10 Fraud
Model: Tebak semua "Normal"

Accuracy = 990/1000 = 99% ← Terlihat bagus!
Balanced Accuracy = (0% + 100%) / 2 = 50% ← Realistis!
```

Balanced Accuracy "membuka kedok" model malas!

### Contoh Perbandingan

**Model A (malas)**:
```
Recall_Normal = 100%  (semua normal benar)
Recall_Fraud  = 0%    (semua fraud miss)

Accuracy          = 99%   ← Misleading!
Balanced Accuracy = 50%   ← Jujur!
```

**Model B (good)**:
```
Recall_Normal = 95%   (5% normal salah)
Recall_Fraud  = 80%   (80% fraud detected)

Accuracy          = 94.5% ← Lebih rendah dari A
Balanced Accuracy = 87.5% ← Jauh lebih baik!
```

### Kapan Digunakan?

✅ **Cocok untuk**:
- Data imbalanced
- Semua kelas sama pentingnya
- Quick check apakah model "malas" di kelas minoritas
- Multi-class imbalanced

❌ **Tidak cocok untuk**:
- Butuh focus pada kelas tertentu (gunakan Precision/Recall)
- Data sudah balanced (sama dengan Accuracy biasa)

### Kode Python

```python
from sklearn.metrics import balanced_accuracy_score

ba = balanced_accuracy_score(y_true, y_pred)
print(f"Accuracy:          {accuracy_score(y_true, y_pred):.2%}")
print(f"Balanced Accuracy: {ba:.2%}")

# Bandingkan
if abs(ba - accuracy_score(y_true, y_pred)) > 0.1:
    print("⚠️  Gap besar! Data kemungkinan imbalanced!")
```

---

## 11. Cohen's Kappa

### Apa itu?

**Mengukur seberapa baik model dibanding prediksi random (by chance).** Mirip R² untuk classification — menunjukkan "improvement over random".

### Rumus

$$\kappa = \frac{p_o - p_e}{1 - p_e}$$

Di mana:
- $p_o$ = observed agreement (accuracy)
- $p_e$ = expected agreement (agreement by chance)

### Interpretasi

| Kappa | Artinya |
|-------|---------|
| **< 0** | Worse than random! ❌ |
| **0.0** | Sama dengan random |
| **0.01 - 0.20** | Slight agreement |
| **0.21 - 0.40** | Fair agreement |
| **0.41 - 0.60** | Moderate agreement |
| **0.61 - 0.80** | Substantial agreement |
| **0.81 - 1.00** | Almost perfect agreement ✨ |

### Contoh Hitung Manual

**Data**: 100 prediksi (70 kelas A, 30 kelas B)

```
Confusion Matrix:
              Pred A | Pred B
Actual A(60)    50   |   10
Actual B(40)    20   |   20

p_o (accuracy) = (50 + 20) / 100 = 0.70

p_e (expected by chance):
  P(pred A) = 70/100 = 0.70
  P(actual A) = 60/100 = 0.60
  P(pred B) = 30/100 = 0.30
  P(actual B) = 40/100 = 0.40
  
  p_e = P(pred A) × P(actual A) + P(pred B) × P(actual B)
      = 0.70 × 0.60 + 0.30 × 0.40
      = 0.42 + 0.12 = 0.54

Kappa = (0.70 - 0.54) / (1 - 0.54) = 0.16 / 0.46 = 0.35
```

**Artinya**: Fair agreement — model lumayan tapi masih banyak "keberuntungan".

### Kenapa Kappa Lebih Baik dari Accuracy?

**Accuracy hanya bilang**: "70% benar"
**Kappa juga bilang**: "Berapa dari 70% itu bukan kebetulan?"

**Analogi**: Ujian multiple choice 4 pilihan
- Random guess: ~25% benar
- Score 30%: Accuracy 30% (terlihat jelek), tapi Kappa = 0.07 (memang jelek)
- Score 50%: Accuracy 50%, Kappa = 0.33 (sedikit di atas random)
- Score 90%: Accuracy 90%, Kappa = 0.87 (excellent)

### Kapan Digunakan?

✅ **Cocok untuk**:
- Mengukur apakah model benar-benar "belajar" (bukan random)
- Inter-rater agreement (apakah 2 annotator setuju?)
- Data imbalanced (Kappa memperhitungkan distribusi kelas)
- Multi-class classification

❌ **Tidak cocok untuk**:
- Interpretasi untuk stakeholder (kurang intuitif)
- Sangat imbalanced data (Kappa bisa sangat rendah meski model OK)

### Kode Python

```python
from sklearn.metrics import cohen_kappa_score

kappa = cohen_kappa_score(y_true, y_pred)
print(f"Cohen's Kappa: {kappa:.3f}")

# Interpretasi
if kappa > 0.8:
    print("✅ Almost perfect agreement")
elif kappa > 0.6:
    print("✅ Substantial agreement")
elif kappa > 0.4:
    print("⚠️  Moderate agreement")
else:
    print("❌ Weak agreement")
```

---

## 12. MCC (Matthews Correlation Coefficient)

### Apa itu?

**Korelasi antara kelas aktual dan prediksi.** Dianggap oleh banyak peneliti sebagai **metric TERBAIK untuk binary classification** karena memperhitungkan semua elemen confusion matrix (TP, TN, FP, FN) secara seimbang.

### Rumus

$$MCC = \frac{TP \times TN - FP \times FN}{\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}}$$

### Interpretasi

| MCC | Artinya |
|-----|---------|
| **+1** | Perfect prediction ✨ |
| **0** | Random prediction (tidak lebih baik dari lempar koin) |
| **-1** | Totally wrong (kebalikan sempurna) |

### Kenapa MCC Dianggap Metric Terbaik?

**MCC memperhitungkan SEMUA 4 elemen confusion matrix secara seimbang:**

| Metric | TP | TN | FP | FN | Balanced? |
|--------|----|----|----|----|-----------|
| Accuracy | ✅ | ✅ | ✅ | ✅ | ❌ (bias ke majority) |
| Precision | ✅ | ❌ | ✅ | ❌ | ❌ |
| Recall | ✅ | ❌ | ❌ | ✅ | ❌ |
| F1-Score | ✅ | ❌ | ✅ | ✅ | ❌ (ignore TN) |
| **MCC** | **✅** | **✅** | **✅** | **✅** | **✅ Balanced!** |

**F1-Score mengabaikan TN** — ini bisa jadi masalah di beberapa kasus!

### Contoh: Kenapa MCC Lebih Informatif

**Skenario**: 100 data (95 negatif, 5 positif)

**Model A** — prediksi semua negatif:
```
TP=0, TN=95, FP=0, FN=5

Accuracy = 95%    ← Terlihat bagus!
F1 = 0%           ← Jelek
MCC = 0            ← Jujur: random level
```

**Model B** — prediksi 10 positif (4 benar, 6 salah):
```
TP=4, TN=89, FP=6, FN=1

Accuracy = 93%    ← Lebih rendah dari A
F1 = 53%          ← Lumayan
MCC = 0.51        ← Substantial! Jauh lebih baik dari A
```

### Contoh Hitung Manual

Dari setup contoh kita:
```
TP=2, TN=6, FP=1, FN=1

MCC = (2×6 - 1×1) / √((2+1)(2+1)(6+1)(6+1))
    = (12 - 1) / √(3 × 3 × 7 × 7)
    = 11 / √441
    = 11 / 21
    = 0.524
```

**Artinya**: Korelasi positif substansial antara prediksi dan aktual.

### Kapan Digunakan?

✅ **Cocok untuk**:
- **Evaluasi paling fair** untuk binary classification
- Data imbalanced (MCC tetap informatif)
- Ingin satu metric yang cover semua aspek
- Paper ilmiah / research

❌ **Tidak cocok untuk**:
- Komunikasi ke non-teknikal (kurang intuitif)
- Multi-class (perlu adaptasi)
- Kasus di mana satu tipe error jauh lebih penting (gunakan Precision/Recall)

### Kode Python

```python
from sklearn.metrics import matthews_corrcoef

mcc = matthews_corrcoef(y_true, y_pred)
print(f"MCC: {mcc:.3f}")

# Interpretasi
if mcc > 0.7:
    print("✅ Strong correlation - Excellent model!")
elif mcc > 0.4:
    print("✅ Moderate correlation - Good model")
elif mcc > 0.1:
    print("⚠️  Weak correlation - Model needs improvement")
else:
    print("❌ No correlation - Model not better than random")
```

### Tips: F1 vs MCC

```
Kapan F1-Score cukup?
  → Hanya peduli kelas positif
  → Komunikasi ke stakeholder
  → Kasus umum

Kapan MCC lebih baik?
  → Butuh evaluasi FAIR untuk kedua kelas
  → Data sangat imbalanced
  → Research / paper ilmiah
  → Ingin satu metric yang "tell the whole story"

Best Practice:
  → Laporkan keduanya! F1 + MCC
```

---

## 13. Multi-class Classification Metrics

### Problem: Lebih dari 2 Kelas

Semua metric di atas (Precision, Recall, F1) dirancang untuk **binary** (2 kelas). Bagaimana kalau kita punya 3+ kelas?

**Contoh**: Klasifikasi buah → Apel, Jeruk, Mangga

### Setup Contoh

```
Confusion Matrix (3 kelas):
              Pred Apel | Pred Jeruk | Pred Mangga
Actual Apel       8     |     1      |     1      (10 total)
Actual Jeruk      2     |     5      |     3      (10 total)
Actual Mangga     1     |     2      |     7      (10 total)
```

**Per-class metrics**:
```
Apel:   Precision = 8/(8+2+1)  = 73%    Recall = 8/10  = 80%
Jeruk:  Precision = 5/(1+5+2)  = 63%    Recall = 5/10  = 50%
Mangga: Precision = 7/(1+3+7)  = 64%    Recall = 7/10  = 70%
```

### 3 Cara Averaging: Macro, Micro, Weighted

#### 1. Macro Average

**Rata-rata biasa dari metric per kelas.** Setiap kelas punya bobot sama.

$$Macro\ Precision = \frac{P_{Apel} + P_{Jeruk} + P_{Mangga}}{3}$$

```
Macro Precision = (73% + 63% + 64%) / 3 = 66.7%
Macro Recall    = (80% + 50% + 70%) / 3 = 66.7%
Macro F1        = (76% + 56% + 67%) / 3 = 66.3%
```

**Kapan pakai**: Semua kelas sama pentingnya, data balanced

#### 2. Micro Average

**Hitung total TP, FP, FN lalu hitung metric.** Kelas besar lebih berpengaruh.

$$Micro\ Precision = \frac{\sum TP_k}{\sum(TP_k + FP_k)}$$

```
Total TP = 8 + 5 + 7 = 20
Total FP = (2+1) + (1+2) + (1+3) = 10
Total FN = (1+1) + (2+3) + (1+2) = 10

Micro Precision = 20 / (20+10) = 66.7%
Micro Recall    = 20 / (20+10) = 66.7%
Micro F1        = 66.7%
```

⚠️ **Catatan**: Micro Precision = Micro Recall = Micro F1 = **Accuracy** untuk multi-class!

**Kapan pakai**: Ingin overall performance, setiap sample sama pentingnya

#### 3. Weighted Average

**Rata-rata dengan bobot sesuai jumlah sample per kelas.**

$$Weighted\ Precision = \frac{n_{Apel} \times P_{Apel} + n_{Jeruk} \times P_{Jeruk} + n_{Mangga} \times P_{Mangga}}{n_{total}}$$

```
Semua kelas punya 10 sample, jadi Weighted = Macro di contoh ini.

Contoh lain: Apel=50, Jeruk=30, Mangga=20
Weighted Precision = (50×73% + 30×63% + 20×64%) / 100
                   = (36.5 + 18.9 + 12.8) / 100
                   = 68.2%
```

**Kapan pakai**: Data imbalanced, kelas besar lebih penting

### Tabel Perbandingan Averaging

| Method | Bobot Kelas | Data Balanced | Data Imbalanced | Kapan Pakai |
|--------|-------------|---------------|-----------------|-------------|
| **Macro** | Sama semua | ✅ Bagus | ⚠️ Bisa misleading | Semua kelas penting |
| **Micro** | Proporsi sample | ✅ Bagus | ❌ Bias ke majority | Overall performance |
| **Weighted** | Proporsi sample | ✅ = Macro | ✅ Realistis | Default terbaik |

### Analogi

**Macro** = Nilai rata-rata semua mata pelajaran (Matematika, Bahasa, IPA)
- Setiap mapel bobot sama, meski ada yang lebih banyak soal

**Micro** = Total soal benar / total soal
- Mapel dengan banyak soal lebih berpengaruh

**Weighted** = Nilai rata-rata tertimbang (dengan bobot SKS)
- Mapel dengan banyak SKS lebih berpengaruh

### Kode Python

```python
from sklearn.metrics import precision_score, recall_score, f1_score

# Macro - semua kelas sama penting
print("MACRO (equal weight per class):")
print(f"  Precision: {precision_score(y_true, y_pred, average='macro'):.3f}")
print(f"  Recall:    {recall_score(y_true, y_pred, average='macro'):.3f}")
print(f"  F1:        {f1_score(y_true, y_pred, average='macro'):.3f}")

# Micro - overall performance
print("\nMICRO (overall performance):")
print(f"  Precision: {precision_score(y_true, y_pred, average='micro'):.3f}")
print(f"  Recall:    {recall_score(y_true, y_pred, average='micro'):.3f}")
print(f"  F1:        {f1_score(y_true, y_pred, average='micro'):.3f}")

# Weighted - proporsional
print("\nWEIGHTED (proportional weight):")
print(f"  Precision: {precision_score(y_true, y_pred, average='weighted'):.3f}")
print(f"  Recall:    {recall_score(y_true, y_pred, average='weighted'):.3f}")
print(f"  F1:        {f1_score(y_true, y_pred, average='weighted'):.3f}")

# Per kelas (detail)
print("\nPER-CLASS:")
print(f"  Precision: {precision_score(y_true, y_pred, average=None)}")
print(f"  Recall:    {recall_score(y_true, y_pred, average=None)}")
print(f"  F1:        {f1_score(y_true, y_pred, average=None)}")
```

### Quick Guide: Pilih Averaging Mana?

```
START HERE
    ↓
Semua kelas sama pentingnya?
    ├─ YA → MACRO
    └─ TIDAK → Lanjut
           ↓
    Data balanced?
        ├─ YA → Semua sama (pakai MACRO atau WEIGHTED)
        └─ TIDAK → WEIGHTED (default terbaik)
                    ↓
    Butuh single overall number?
        └─ YA → MICRO (= Accuracy)
```

---

## 14. Classification Report: Cara Membaca

### Apa itu?

**`classification_report` dari sklearn** memberikan ringkasan lengkap semua metric per kelas + rata-rata. Ini adalah **tool paling penting** untuk evaluasi classification!

### Contoh Output

```python
from sklearn.metrics import classification_report

print(classification_report(y_true, y_pred))
```

**Output**:
```
              precision    recall  f1-score   support

       Apel       0.73      0.80      0.76        10
      Jeruk       0.63      0.50      0.56        10
     Mangga       0.64      0.70      0.67        10

    accuracy                           0.67        30
   macro avg       0.67      0.67      0.66        30
weighted avg       0.67      0.67      0.66        30
```

### Cara Membaca Setiap Kolom

| Kolom | Artinya | Pertanyaan yang Dijawab |
|-------|---------|-------------------------|
| **precision** | Dari yang diprediksi kelas X, berapa % benar? | "Kalau model bilang Apel, seberapa yakin?" |
| **recall** | Dari aktual kelas X, berapa % terdeteksi? | "Dari semua Apel asli, berapa yang ketangkap?" |
| **f1-score** | Harmonic mean precision & recall | "Balance antara precision dan recall" |
| **support** | Jumlah sample aktual kelas tersebut | "Berapa banyak data kelas ini?" |

### Cara Membaca Baris Terakhir

| Baris | Artinya |
|-------|---------|
| **accuracy** | Akurasi keseluruhan (semua kelas) |
| **macro avg** | Rata-rata biasa (setiap kelas bobot sama) |
| **weighted avg** | Rata-rata tertimbang (kelas besar > bobot besar) |

### Cara Interpretasi Cepat

**Step 1**: Lihat **accuracy** dulu → baseline performa

**Step 2**: Lihat **per-class recall** → kelas mana yang sering miss?
```
Jeruk recall = 0.50 ← 50% Jeruk tidak terdeteksi! Problem!
```

**Step 3**: Lihat **per-class precision** → kelas mana yang banyak false alarm?
```
Jeruk precision = 0.63 ← 37% prediksi Jeruk ternyata salah
```

**Step 4**: Lihat **support** → apakah data seimbang?
```
Semua 10 → Balanced ✅
Kalau ada kelas cuma 5 vs kelas 500 → Imbalanced!
```

**Step 5**: Bandingkan **macro avg vs weighted avg**
```
macro ≈ weighted → Data balanced
macro << weighted → Data imbalanced, kelas besar lebih bagus
macro >> weighted → Data imbalanced, kelas kecil lebih bagus (jarang)
```

### Contoh Interpretasi Real

```
              precision    recall  f1-score   support

      Normal       0.98      0.99      0.99       990
       Fraud       0.50      0.40      0.44        10

    accuracy                           0.98      1000
   macro avg       0.74      0.70      0.71      1000
weighted avg       0.98      0.98      0.98      1000
```

**Analisis**:
1. Accuracy 98% ← Terlihat bagus, tapi...
2. Fraud recall 40% ← **60% fraud tidak terdeteksi!** ❌
3. Fraud precision 50% ← Setengah "fraud alert" ternyata normal
4. Support: 990 vs 10 ← **Sangat imbalanced!**
5. Macro avg (71%) << Weighted avg (98%) ← Konfirmasi imbalanced
6. **Kesimpulan**: Model jelek untuk deteksi fraud, perlu improvement!

### Kode Python dengan Interpretasi

```python
from sklearn.metrics import classification_report
import pandas as pd

# Generate report sebagai dictionary (untuk analisis)
report = classification_report(y_true, y_pred, output_dict=True)
df_report = pd.DataFrame(report).T

print("="*60)
print("CLASSIFICATION REPORT")
print("="*60)
print(classification_report(y_true, y_pred))

# Auto-analysis
print("AUTO-ANALYSIS:")
for cls in df_report.index:
    if cls in ['accuracy', 'macro avg', 'weighted avg']:
        continue
    recall = df_report.loc[cls, 'recall']
    precision = df_report.loc[cls, 'precision']
    
    if recall < 0.5:
        print(f"  ⚠️  {cls}: Recall rendah ({recall:.0%}) - Banyak miss!")
    if precision < 0.5:
        print(f"  ⚠️  {cls}: Precision rendah ({precision:.0%}) - Banyak false alarm!")

# Check imbalance
macro_f1 = df_report.loc['macro avg', 'f1-score']
weighted_f1 = df_report.loc['weighted avg', 'f1-score']
if abs(macro_f1 - weighted_f1) > 0.1:
    print(f"  ⚠️  Data imbalanced! (Macro F1={macro_f1:.2f} vs Weighted F1={weighted_f1:.2f})")
```

---

## Precision vs Recall Trade-off

### Konsep

**Anda tidak bisa maksimalkan keduanya sekaligus!**

### Ilustrasi

**Skenario 1: Model Konservatif (High Precision)**
- Hanya prediksi "Spam" kalau SANGAT yakin
- Precision tinggi (yang diprediksi spam memang spam)
- Recall rendah (banyak spam yang miss)

```
Threshold tinggi (0.9):
TP=1, FP=0, FN=2
Precision = 1/1 = 100% ✅
Recall = 1/3 = 33% ❌
```

**Skenario 2: Model Agresif (High Recall)**
- Prediksi "Spam" untuk banyak email (curiga semua)
- Recall tinggi (tangkap semua spam)
- Precision rendah (banyak false alarm)

```
Threshold rendah (0.3):
TP=3, FP=4, FN=0
Precision = 3/7 = 43% ❌
Recall = 3/3 = 100% ✅
```

### Bagaimana Memilih?

**Pertanyaan kunci**: Mana yang lebih buruk?

| Kasus | Prioritas | Metric |
|-------|-----------|--------|
| **Spam Filter** | False Positive buruk (email penting ke spam) | Precision |
| **Cancer Detection** | False Negative buruk (cancer miss) | Recall |
| **Fraud Detection** | False Negative buruk (fraud lolos) | Recall |
| **Recommendation** | False Positive buruk (rekomendasi jelek) | Precision |

### Solusi Balance: F1-Score

Gunakan F1-Score kalau keduanya sama pentingnya!

---

## Ringkasan Tabel Classification Metrics

| Metric | Rumus | Range | Best Value | Kapan Pakai |
|--------|-------|-------|------------|-------------|
| **Accuracy** | (TP+TN)/Total | 0-1 | 1 | Balanced data, baseline |
| **Balanced Acc** | avg(Recall per class) | 0-1 | 1 | Imbalanced, quick check |
| **Precision** | TP/(TP+FP) | 0-1 | 1 | FP buruk (spam filter) |
| **Recall** | TP/(TP+FN) | 0-1 | 1 | FN buruk (disease detection) |
| **F1-Score** | 2×P×R/(P+R) | 0-1 | 1 | Imbalanced, balance |
| **Specificity** | TN/(TN+FP) | 0-1 | 1 | Evaluasi TN |
| **ROC-AUC** | Area under curve | 0-1 | 1 | Probabilistic, imbalanced |
| **PR-AUC** | Area under PR curve | 0-1 | 1 | Severely imbalanced (99:1) |
| **Log Loss** | -∑[y log(p)] | 0-∞ | 0 | Probability confidence |
| **Cohen's Kappa** | (po-pe)/(1-pe) | -1 to 1 | 1 | Agreement vs chance |
| **MCC** | (TP·TN-FP·FN)/√... | -1 to 1 | 1 | Fairest single metric |

---

*Modul 3 — Evaluation Metrics dalam Machine Learning*

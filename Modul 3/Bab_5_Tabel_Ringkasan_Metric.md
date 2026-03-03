# Bab 5 — Tabel Ringkasan Semua Metric

## Regression Metrics - Ringkasan Lengkap

| Metric | Formula | Range | Best | Unit | Interpretasi | Outlier Sensitive | Kapan Digunakan |
|--------|---------|-------|------|------|--------------|-------------------|-----------------|
| **MAE** | $\frac{1}{n}\sum\|y-\hat{y}\|$ | 0 to ∞ | 0 | Same as target | Rata-rata error | ❌ Robust | Error tipikal, ada outlier |
| **MSE** | $\frac{1}{n}\sum(y-\hat{y})^2$ | 0 to ∞ | 0 | Target² | Rata-rata squared error | ✅ Sangat | Loss function, penalty besar |
| **RMSE** | $\sqrt{MSE}$ | 0 to ∞ | 0 | Same as target | Rata-rata error + penalty | ✅ Ya | Standard metric, balance |
| **RMSLE** | $\sqrt{\frac{1}{n}\sum(\log-\log)^2}$ | 0 to ∞ | 0 | Log scale | Error relatif (%) | ❌ Robust | Range lebar, error relatif |
| **R²** | $1-\frac{SS_{res}}{SS_{tot}}$ | -∞ to 1 | 1 | Dimensionless | % variance explained | - | Overall performance |
| **Adjusted R²** | $1-\frac{(1-R^2)(n-1)}{n-p-1}$ | -∞ to 1 | 1 | Dimensionless | R² with penalty | - | Banding model beda fitur |
| **MAPE** | $\frac{100}{n}\sum\|\frac{y-\hat{y}}{y}\|$ | 0 to ∞ | 0 | Percentage | Error dalam % | ❌ Robust | Persentase, komunikasi |
| **MedAE** | $median(\|y-\hat{y}\|)$ | 0 to ∞ | 0 | Same as target | Median error | ❌ Sangat robust | Banyak outlier ekstrem |

### Quick Selection Guide - Regression

```
START HERE
    ↓
Apakah ada outlier ekstrem?
    ├─ YA → MAE atau Median AE atau MAPE
    └─ TIDAK → RMSE (standard)
           ↓
    Butuh error dalam %?
        ├─ YA → MAPE (interpretasi mudah)
        └─ TIDAK → RMSE + R²
               ↓
        Range target lebar (1-1M)?
            ├─ YA → RMSLE
            └─ TIDAK → Tetap RMSE + R²

ALWAYS REPORT: MAE + RMSE + R²
```

---

## Classification Metrics - Ringkasan Lengkap

| Metric | Formula | Range | Best | Interpretasi | Imbalanced OK? | Kapan Digunakan |
|--------|---------|-------|------|--------------|----------------|-----------------|
| **Accuracy** | $\frac{TP+TN}{Total}$ | 0-1 | 1 | % prediksi benar | ❌ Misleading | Balanced data, baseline |
| **Balanced Acc** | $\frac{Recall_{+}+Recall_{-}}{2}$ | 0-1 | 1 | Avg recall per class | ✅ Ya | Imbalanced, quick check |
| **Precision** | $\frac{TP}{TP+FP}$ | 0-1 | 1 | Dari pred +, % benar | ✅ Ya | FP buruk (spam filter) |
| **Recall** | $\frac{TP}{TP+FN}$ | 0-1 | 1 | Dari actual +, % found | ✅ Ya | FN buruk (disease) |
| **Specificity** | $\frac{TN}{TN+FP}$ | 0-1 | 1 | Dari actual -, % correct | ✅ Ya | TN penting |
| **F1-Score** | $\frac{2PR}{P+R}$ | 0-1 | 1 | Harmonic mean P&R | ✅ Ya | Balance P&R |
| **F2-Score** | $\frac{5PR}{4P+R}$ | 0-1 | 1 | R lebih penting | ✅ Ya | FN lebih buruk |
| **F0.5-Score** | $\frac{1.25PR}{0.25P+R}$ | 0-1 | 1 | P lebih penting | ✅ Ya | FP lebih buruk |
| **ROC-AUC** | Area under ROC | 0-1 | 1 | Discrimination ability | ✅ Ya | Probabilistic eval |
| **PR-AUC** | Area under PR curve | 0-1 | 1 | P-R over thresholds | ✅ Sangat | Imbalanced severe |
| **Log Loss** | $-\frac{1}{n}\sum[y\log p]$ | 0-∞ | 0 | Confidence penalty | ✅ Ya | Probability quality |
| **Cohen's Kappa** | $\frac{p_o - p_e}{1 - p_e}$ | -1 to 1 | 1 | Agreement vs chance | ✅ Ya | Inter-rater, imbalanced |
| **MCC** | $\frac{TP·TN-FP·FN}{\sqrt{...}}$ | -1 to 1 | 1 | Correlation pred vs actual | ✅ Sangat | Fairest single metric |

### Quick Selection Guide - Classification

```
START HERE
    ↓
Apakah data balanced?
    ├─ YA → Accuracy (simple)
    └─ TIDAK (imbalanced) → Lanjut
           ↓
    Mana yang lebih buruk?
        ├─ False Positive (FP) sangat buruk
        │   → Prioritas: PRECISION
        │   Contoh: Spam filter, surgery decision
        │
        ├─ False Negative (FN) sangat buruk
        │   → Prioritas: RECALL
        │   Contoh: Cancer detection, fraud
        │
        └─ Keduanya sama pentingnya
            → F1-SCORE (balance)
               ↓
    Butuh probability evaluation?
        ├─ YA → ROC-AUC + Log Loss
        │       (Sangat imbalanced? → PR-AUC!)
        └─ TIDAK → F1-Score cukup
               ↓
    Butuh single fairest metric?
        └─ YA → MCC (Matthews Correlation Coefficient)

Minimum: Confusion Matrix + Precision + Recall + F1
Ideal:   + MCC + AUC + Balanced Accuracy
Research: + Cohen's Kappa + classification_report
```

### Multi-class: Pilih Averaging Mana?

```
Semua kelas sama pentingnya?
    ├─ YA → MACRO average
    └─ TIDAK → Lanjut
           ↓
    Data balanced?
        ├─ YA → Semua sama (MACRO atau WEIGHTED)
        └─ TIDAK → WEIGHTED (default terbaik)
                    ↓
    Butuh single overall number?
        └─ YA → MICRO (= Accuracy)
```

---

## Confusion Matrix Cheat Sheet

### Definisi

```
                    PREDICTED
                 Positive | Negative
              ┌───────────┼──────────┐
ACTUAL   Pos  │    TP     │    FN    │
         Neg  │    FP     │    TN    │
              └───────────┴──────────┘
```

### Derived Metrics

| Metric | Formula | Also Known As |
|--------|---------|---------------|
| **Accuracy** | $(TP+TN)/(TP+TN+FP+FN)$ | Overall accuracy |
| **Precision** | $TP/(TP+FP)$ | Positive Predictive Value (PPV) |
| **Recall** | $TP/(TP+FN)$ | Sensitivity, True Positive Rate (TPR) |
| **Specificity** | $TN/(TN+FP)$ | True Negative Rate (TNR) |
| **False Positive Rate** | $FP/(FP+TN)$ | Type I Error, $1-Specificity$ |
| **False Negative Rate** | $FN/(FN+TP)$ | Type II Error, $1-Recall$ |
| **F1-Score** | $2TP/(2TP+FP+FN)$ | Harmonic mean |

### Memory Tricks

**Precision = "Pre-ci-sion" = Predicted +**
- Dari yang diprediksi positif, berapa yang benar?

**Recall = "Re-call" = Actual +**
- Dari yang aktual positif, berapa yang ter-recall (ingat)?

**Specificity = Specific to Negative**
- Dari yang aktual negatif, berapa yang benar?

---

## Metrics Comparison Tables

### Regression: When to Use What?

| Situation | Primary Metric | Secondary Metric | Why? |
|-----------|----------------|------------------|------|
| **Standard case** | RMSE | R², MAE | Most accepted, balance |
| **Many outliers** | MAE | Median AE | Robust to extremes |
| **Communication to non-tech** | MAPE | MAE | Percentage, intuitive |
| **Wide range (1-1M)** | RMSLE | MAPE | Focus on relative error |
| **Loss function** | MSE | - | Differentiable |
| **Comparing models (same data)** | RMSE, R² | - | Standard |
| **Comparing models (diff data)** | MAPE | - | Scale-independent |
| **Feature selection** | Adjusted R² | RMSE | Penalty for complexity |

### Classification: When to Use What?

| Situation | Primary Metric | Secondary Metric | Why? |
|-----------|----------------|------------------|------|
| **Balanced data, baseline** | Accuracy | Confusion Matrix | Simple, interpretable |
| **Imbalanced data** | F1-Score | AUC, MCC | Not mislead by majority |
| **FP very bad** | Precision | F0.5 | Minimize false alarms |
| **FN very bad** | Recall | F2 | Don't miss positives |
| **Severe imbalance (99:1)** | PR-AUC | MCC, F1 | Better than ROC-AUC |
| **Probability needed** | ROC-AUC | Log Loss | Threshold-independent |
| **Medical diagnosis** | Recall, Specificity | F1, Balanced Acc | Need both sensitivity |
| **Ranking/Recommendation** | Precision@K | AUC | Top-K accuracy |
| **Fairest single metric** | MCC | Cohen's Kappa | Uses all 4 CM elements |
| **Inter-rater agreement** | Cohen's Kappa | Accuracy | Accounts for chance |
| **Multi-class balanced** | Macro F1 | Macro Precision/Recall | Equal weight per class |
| **Multi-class imbalanced** | Weighted F1 | Balanced Accuracy | Proportional weight |
| **Quick imbalance check** | Balanced Accuracy | Macro vs Weighted F1 | Exposes lazy models |

---

## Threshold Tuning Cheat Sheet

| Metode | Optimize | Kapan Pakai | Threshold Cenderung |
|--------|----------|-------------|---------------------|
| **Maximize F1** | $F1 = \frac{2PR}{P+R}$ | Balance P & R | Dekat 0.5 |
| **Youden's J** | $TPR - FPR$ | Balance Sensitivity & Specificity | Bervariasi |
| **Cost-sensitive** | $min(FP×C_{FP} + FN×C_{FN})$ | FN & FP punya cost berbeda | Tergantung cost ratio |
| **Target Recall** | $Recall \geq target$ | Minimum recall requirement | Rendah (<0.5) |
| **Target Precision** | $Precision \geq target$ | Minimum precision requirement | Tinggi (>0.5) |

**⚠️ SELALU tentukan threshold di validation set, evaluasi di test set!**

---

## Cross-Validation Cheat Sheet

| Metode | Evaluasi | Stabil? | Waktu | Kapan Pakai |
|--------|----------|---------|-------|-------------|
| **Hold-out** | 1× | ❌ | Cepat | Dataset besar (>100K) |
| **5-Fold CV** | 5× | ✅ | Medium | Standard, dataset sedang |
| **10-Fold CV** | 10× | ✅✅ | Lambat | Paper, dataset kecil |
| **Stratified KF** | K× | ✅✅ | Medium | Imbalanced data (WAJIB!) |
| **Repeated KF** | K×N | ✅✅✅ | Lama | Butuh estimasi sangat stabil |
| **LOO (Leave-One-Out)** | N× | ✅✅✅ | Sangat lama | Dataset <50 sample |

```python
# Quick code reference
from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.model_selection import StratifiedKFold, RepeatedStratifiedKFold

# Basic
scores = cross_val_score(model, X, y, cv=5, scoring='f1')

# Stratified (imbalanced)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skf, scoring='f1')

# Multiple metrics
results = cross_validate(model, X, y, cv=5, 
    scoring=['accuracy', 'f1', 'precision', 'recall', 'roc_auc'])
```

---

## Real-World Examples

### Example 1: House Price Prediction

**Problem**: Prediksi harga rumah (Rp 500 juta - 5 miliar)

**Results**:
```
MAE:  175 juta   → Rata-rata salah 175 juta
RMSE: 225 juta   → Error dengan penalty (ada outlier)
R²:   0.87       → Menjelaskan 87% variance
MAPE: 8.5%       → Rata-rata salah 8.5%
```

**Interpretation**:
- ✅ R² bagus (>0.85)
- ✅ MAPE reasonable (<10%)
- ⚠️ RMSE/MAE = 1.29 → Sedikit outlier
- 💡 Model cukup bagus untuk production

**Report to stakeholder**:
> "Model kami rata-rata salah sekitar 8-9% dalam memprediksi harga rumah. Model menjelaskan 87% variasi harga, yang sangat bagus!"

### Example 2: Cancer Detection

**Problem**: Klasifikasi tumor (Benign vs Malignant)
**Data**: 1000 patients, 100 malignant (10%)

**Model A - Konservatif**:
```
Confusion Matrix:
              Pred Mal | Pred Ben
Actual Mal       80    |    20
Actual Ben       10    |   890

Metrics:
Accuracy:  97.0%  ← Terlihat bagus!
Precision: 88.9%  → Dari pred malignant, 88.9% benar
Recall:    80.0%  → Dari actual malignant, 80% detected
F1-Score:  84.2%
```

**Model B - Agresif**:
```
Confusion Matrix:
              Pred Mal | Pred Ben
Actual Mal       95    |     5
Actual Ben       50    |   850

Metrics:
Accuracy:  94.5%  ← Lebih rendah
Precision: 65.5%  → Banyak false alarm
Recall:    95.0%  → Hampir semua cancer detected ✅
F1-Score:  77.5%
```

**Decision**: 
Choose **Model B** (High Recall)!

**Why?**
- FN (miss cancer) = **SANGAT BURUK** ❌
- FP (false alarm) = Tidak apa-apa, bisa dikonfirmasi lagi
- Prioritas: **Don't miss cancer!**

**Report to stakeholder**:
> "Model B mendeteksi 95% dari semua kasus kanker, dengan konsekuensi 35% false alarm yang bisa dikonfirmasi dengan tes lanjutan. Model A lebih presisi tapi miss 20% kasus kanker, yang tidak acceptable."

### Example 3: Email Spam Filter

**Problem**: Klasifikasi email (Spam vs Ham)
**Data**: 10,000 emails, 500 spam (5%)

**Model Results**:
```
Confusion Matrix:
              Pred Spam | Pred Ham
Actual Spam      400    |   100
Actual Ham        50    |  9450

Metrics:
Accuracy:  98.5%
Precision: 88.9%  ← Penting! (jangan blok email penting)
Recall:    80.0%  → Boleh miss sedikit spam
F1-Score:  84.2%
```

**Decision**: Good! High Precision prioritized.

**Why?**
- FP (email penting → spam) = **SANGAT BURUK** ❌
- FN (spam → inbox) = Tidak apa-apa, user bisa delete
- Prioritas: **Don't block important emails!**

---

## Metric Selection Flowchart

```
┌─────────────────────────────────────┐
│  What type of problem?              │
└─────────────┬───────────────────────┘
              │
        ┌─────┴─────┐
        │           │
    REGRESSION   CLASSIFICATION
        │           │
        │           │
        │     ┌─────┴────────┐
        │     │              │
        │  Balanced?      Imbalanced?
        │     │              │
        │  Accuracy      ┌───┴────┐
        │              FP bad  FN bad
        │              Precision Recall
        │                  │       │
        │                  └───┬───┘
        │                      │
        │                  F1-Score
        │
    ┌───┴────┐
    │        │
 Outliers? No outliers?
    │        │
   MAE     RMSE + R²
    │        │
    └────┬───┘
         │
   Need % error?
    ┌────┴────┐
   YES       NO
    │         │
  MAPE    Stay with
           RMSE+R²
```

---

## Final Recommendations

### For Regression
```python
# Always compute these
mae = mean_absolute_error(y_true, y_pred)
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
r2 = r2_score(y_true, y_pred)

# Additional
mape = mean_absolute_percentage_error(y_true, y_pred)

# Report
print(f"Performance Summary:")
print(f"  MAE:  {mae:.2f} (typical error)")
print(f"  RMSE: {rmse:.2f} (with penalty)")
print(f"  R²:   {r2:.3f} ({r2*100:.1f}% variance)")
print(f"  MAPE: {mape:.2f}%")
```

### For Classification
```python
# Always compute these
from sklearn.metrics import classification_report, confusion_matrix

# Get all metrics
print(classification_report(y_true, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)
sns.heatmap(cm, annot=True, fmt='d')

# If probabilities available
if y_proba is not None:
    auc = roc_auc_score(y_true, y_proba)
    logloss = log_loss(y_true, y_proba)
    print(f"AUC: {auc:.3f}")
    print(f"Log Loss: {logloss:.3f}")
```

---

*Modul 3 — Evaluation Metrics dalam Machine Learning*

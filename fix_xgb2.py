import json
import re
from pathlib import Path

BASE = Path('/home/arilix/Documents/module-kaggle/Contoh')

def fix_notebook(path, transforms):
    """Apply list of (old_string, new_string) to all cell sources in a notebook."""
    nb = json.loads(path.read_text())
    changed = False
    for cell in nb.get('cells', []):
        src = ''.join(cell.get('source', []))
        new_src = src
        for old, new in transforms:
            if old in new_src:
                new_src = new_src.replace(old, new)
        if new_src != src:
            # Re-split into lines with \n
            lines = new_src.split('\n')
            cell['source'] = [line + '\n' for line in lines[:-1]] + ([lines[-1]] if lines[-1] else [])
            changed = True
    if changed:
        path.write_text(json.dumps(nb, ensure_ascii=False, indent=1))
        print(f'Fixed: {path.name}')
    else:
        print(f'No change: {path.name}')

# =============================================================================
# 1. 03_dropout_xgboost.ipynb
# Move early_stopping_rounds from fit() to constructor; add eval_metric if needed
# =============================================================================
fix_notebook(
    BASE / '01_Student_Dropout/03_dropout_xgboost.ipynb',
    [
        # Add early_stopping_rounds to constructor (after eval_metric='auc',)
        ("    eval_metric='auc',\n    random_state=42,",
         "    eval_metric='auc',\n    early_stopping_rounds=30,\n    random_state=42,"),
        # Remove from fit()
        ("    early_stopping_rounds=30,   # Stop jika tidak ada perbaikan 30 rounds\n",
         ""),
    ]
)

# =============================================================================
# 2. 08_cgpa_xgboost_regressor.ipynb
# =============================================================================
fix_notebook(
    BASE / '01_Student_Dropout/08_cgpa_xgboost_regressor.ipynb',
    [
        ("    eval_metric='rmse',\n    random_state=42,",
         "    eval_metric='rmse',\n    early_stopping_rounds=30,\n    random_state=42,"),
        ("    early_stopping_rounds=30,\n    verbose=False",
         "    verbose=False"),
    ]
)

# =============================================================================
# 3. 06_stock_xgboost.ipynb
# No eval_metric in constructor — add both
# =============================================================================
fix_notebook(
    BASE / '02_Toyota_Stock/06_stock_xgboost.ipynb',
    [
        ("    objective='reg:squarederror',\n    random_state=42",
         "    objective='reg:squarederror',\n    eval_metric='rmse',\n    early_stopping_rounds=30,\n    random_state=42"),
        ("    early_stopping_rounds=30,\n    verbose=False",
         "    verbose=False"),
    ]
)

# =============================================================================
# 4. 03_productivity_xgb_regressor.ipynb
# =============================================================================
fix_notebook(
    BASE / '03_Student_Productivity/03_productivity_xgb_regressor.ipynb',
    [
        ("    objective='reg:squarederror', eval_metric='rmse',\n    random_state=42",
         "    objective='reg:squarederror', eval_metric='rmse',\n    early_stopping_rounds=30,\n    random_state=42"),
        ("    early_stopping_rounds=30,\n    verbose=False",
         "    verbose=False"),
    ]
)

# =============================================================================
# 5. 06_productivity_xgb_clf.ipynb  — remove use_label_encoder
# =============================================================================
fix_notebook(
    BASE / '03_Student_Productivity/06_productivity_xgb_clf.ipynb',
    [
        ("    use_label_encoder=False, random_state=42\n)", "    random_state=42\n)"),
        ("                  use_label_encoder=False, random_state=42),", "                  random_state=42),"),
    ]
)

print('\nDone! Verifying...')
# Quick verify
for f in BASE.rglob('*.ipynb'):
    nb = json.loads(f.read_text())
    for cell in nb.get('cells', []):
        src = ''.join(cell.get('source', []))
        if 'use_label_encoder' in src:
            print(f'STILL HAS use_label_encoder: {f.name}')
        if '.fit(' in src and 'early_stopping_rounds' in src:
            # check if early_stopping_rounds appears after .fit(
            fit_idx = src.find('.fit(')
            es_idx = src.find('early_stopping_rounds', fit_idx)
            if es_idx > fit_idx:
                print(f'STILL HAS early_stopping in fit(): {f.name}')
print('Verification complete.')

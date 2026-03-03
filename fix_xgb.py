import json
import re
from pathlib import Path

BASE = Path('/home/arilix/Documents/module-kaggle/Contoh')

def get_cells(f):
    nb = json.loads(f.read_text())
    return nb

def fix_early_stopping(nb):
    """Move early_stopping_rounds from fit() to constructor in each cell"""
    changed = False
    for cell in nb.get('cells', []):
        src_lines = cell.get('source', [])
        src = ''.join(src_lines)
        
        # Check if cell has early_stopping_rounds in .fit() call
        if 'early_stopping_rounds' not in src:
            continue
        
        # Pattern: early_stopping_rounds=N inside fit() block
        # We need to find it after .fit(, before )
        # Strategy: extract the parameter from fit() and add to constructor
        
        # Remove early_stopping_rounds from fit() block
        new_src = re.sub(
            r',?\s*early_stopping_rounds\s*=\s*\d+\s*,?\s*(# [^\n]*)?\n',
            '\n',
            src
        )
        # Clean up double newlines / trailing commas before )
        new_src = re.sub(r',\s*\n\s*\)', '\n)', new_src)
        
        if new_src != src:
            # Rebuild source lines
            cell['source'] = [line + '\n' for line in new_src.split('\n')]
            # Remove last empty item if it was added
            if cell['source'] and cell['source'][-1] == '\n':
                cell['source'][-1] = ''
            changed = True
    return changed

issues = []
for f in BASE.rglob('*.ipynb'):
    nb = json.loads(f.read_text())
    for cell in nb.get('cells', []):
        src = ''.join(cell.get('source', []))
        if 'use_label_encoder' in src:
            issues.append(('USE_LABEL', f))
        # Check if early_stopping_rounds appears AFTER model.fit( in same cell
        m_pos = src.find('model.fit(')
        es_pos = src.find('early_stopping_rounds')
        if m_pos != -1 and es_pos != -1 and es_pos > m_pos:
            issues.append(('EARLY_IN_FIT', f))

print("Issues found:")
for kind, f in issues:
    print(f"  {kind}: {f.name}")

if not issues:
    print("No issues! All clean.")

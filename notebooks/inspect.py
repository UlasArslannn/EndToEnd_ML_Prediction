import json

notebook_path = r'c:\Users\ulas\Desktop\Full-Stack_AI\Regression_ML_EndtoEnd\notebooks\01_EDA_cleaning.ipynb'
output_path = r'c:\Users\ulas\Desktop\Full-Stack_AI\Regression_ML_EndtoEnd\notebooks\inspect_cells.txt'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

with open(output_path, 'w', encoding='utf-8') as f:
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            source = "".join(cell['source']).lower()
            if 'eval_df' in source or 'hold_df' in source:
                f.write(f"\n--- Cell {i} ---\n")
                f.write("".join(cell['source']))
                f.write("\n")

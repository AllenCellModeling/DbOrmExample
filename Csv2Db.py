import yaml
import pandas as pd
from orator import Model, DatabaseManager
from models.irena_classification import IrenaClassification

ydata = yaml.load(open('orator.yml', 'r'))

db = DatabaseManager(ydata['databases'])
Model.set_connection_resolver(db)

file = r'input_data/mini_input.csv'
df = pd.read_csv(file)

b_list = []

# the int() casts below are for postgres db, if you don't cast it to a normal int postgres get's handed a
# numpy.int64 which it doesn't know how to handle. For sqlite3 it isn't needed, for mysql I haven't tested yet.

for i in range(len(df)):
    x = df.iloc[i, :]
    ic = IrenaClassification()
    ic.input_folder = x['inputFolder']
    ic.input_filename = x['inputFilename']
    ic.output_cell_index = int(x['outputThisCellIndex'])
    ic.cell_id = x['cellID']
    ic.mitosis_label = int(x['MitosisLabel'])
    ic.mitotic_handoff = x['MitoticHandoff']
    ic.save_flat_reg_path = x['save_flat_reg_path']
    ic.save_flat_proj_reg_path = x['save_flat_proj_reg_path']
    ic.save_h5_reg_path = x['save_h5_reg_path']
    ic.png_file_size = int(x['png_file_size'])
    ic.target_numeric = int(x['targetNumeric'])
    try:
        ic.save()
    except Exception as e:
        b_list.append(i)
        print(e)
        print(f"index: {i}")
        print(x)
        print("Data not added")


if len(b_list) > 0:
    df.iloc[b_list, :].to_csv("omitted.txt", "w")

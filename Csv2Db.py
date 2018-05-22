import yaml
import pandas as pd
from orator import Model, DatabaseManager
from models.irena_classification import IrenaClassification

ydata = yaml.load(open('orator.yml', 'r'))

print(ydata)
db = DatabaseManager(ydata['databases'])
Model.set_connection_resolver(db)

file = r'input_data/mini_input.csv'
#file = r'/Users/jamies/Projects/pytorch_mito_2Dimages/second_pass/input_data_files/mito_annotations_only_with_pngs.csv'
df = pd.read_csv(file)
#for key in df.keys():
#    print(key)

#print("orm:keys")
#tc = IrenaClassification()
#for k in tc.attributes_to_dict().keys():
#    print(k)

b_list = []

for i in range(len(df)):
    x = df.iloc[i, :]
    ic = IrenaClassification()
    ic.input_folder = x['inputFolder']
    ic.input_filename = x['inputFilename']
    ic.output_cell_index = x['outputThisCellIndex']
    ic.cell_id = x['cellID']
    ic.mitosis_label = x['MitosisLabel']
    ic.mitotic_handoff = x['MitoticHandoff']
    ic.save_flat_reg_path = x['save_flat_reg_path']
    ic.save_flat_proj_reg_path = x['save_flat_proj_reg_path']
    ic.save_h5_reg_path = x['save_h5_reg_path']
    ic.png_file_size = x['png_file_size']
    ic.target_numeric = x['targetNumeric']
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

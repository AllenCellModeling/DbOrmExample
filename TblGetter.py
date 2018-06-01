import yaml
from orator import Model, DatabaseManager
from models.irena_classification import IrenaClassification

ydata = yaml.load(open('orator.yml', 'r'))

print(ydata)
db = DatabaseManager(ydata['databases'])
Model.set_connection_resolver(db)

ics = IrenaClassification.all()

print(len(ics))

#for ic in ics:
    #print(ic)
    #ic.delete()

mlabels = ics.pluck('mitosis_label').unique()
for label in mlabels:
    print(label)


mitoFive = IrenaClassification.where([['mitosis_label', '=', 5],['cell_id', '<', 'AICS-13_9']]).get()

for m in mitoFive:
    print(m.cell_id)

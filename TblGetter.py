import yaml
from orator import Model, DatabaseManager
from models.irena_classification import IrenaClassification

ydata = yaml.load(open('orator.yml', 'r'))

print(ydata)
db = DatabaseManager(ydata['databases'])
Model.set_connection_resolver(db)

ics = IrenaClassification.all()

print(len(ics))

for ic in ics:
    print(ic.mitosis_label)
    ic.delete()



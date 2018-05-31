import yaml
import pandas as pd
from sqlalchemy import create_engine


conn_info = yaml.load(open('sqlalchemy.yml', 'r'))
conn = create_engine(conn_info['database'])
dfio = pd.read_sql_table('irena_classifications', conn, index_col='id')

print(len(dfio))
for x in dfio['mitosis_label']:
    print(x)
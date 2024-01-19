# pip install pandas openpyxl psycopg2  sqlalchemy 

import psycopg2
import pandas as pd
from sqlalchemy import create_engine

data = pd.read_excel("Список сотрудников.xlsx")
#print(data.head())
engine = create_engine('postgresql+psycopg2://it4med:it4med@localhost/it4med')
with engine.connect() as conn:
    data.to_sql("PERSON_BUFF", conn, if_exists='replace')

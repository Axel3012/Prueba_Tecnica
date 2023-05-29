import sqlite3
import pandas

from . import RUTA_DB, RUTA_EXCEL

df_excel_to_db = pandas.read_excel(RUTA_EXCEL, sheet_name='data_prueba_1')

conexion = sqlite3.connect(RUTA_DB)
df_excel_to_db.to_sql('data_prueba_1', conexion, if_exists='replace', index=False)

conexion.close()


from constants import *

conn = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+DB_PATH+';')
cursor = conn.cursor()
cursor.tables()
rows = cursor.fetchall()

for row in rows:
    print(row.table_name)

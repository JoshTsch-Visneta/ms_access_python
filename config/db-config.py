from constants import *

conn = pyodbc.connect('Driver={'+DB_DRIVER+'};DBQ='+DB_PATH+';')
cursor = conn.cursor()
cursor.tables()
rows = cursor.fetchall()

for row in rows:
    print(row.table_name)

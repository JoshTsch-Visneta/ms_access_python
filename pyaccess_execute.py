import paths
from pyaccess import *
from modules import *
from constants import *

conn = pyodbc.connect('Driver={'+DB_DRIVER+'};DBQ='+DB_PATH+';')
cursor = conn.cursor()

print(table_exists(cursor,"an_common_field"))

sql = "CREATE TABLE TTable(symbol varchar(15), leverage double, shares integer, price double)"

cursor.execute(sql)
conn.commit()

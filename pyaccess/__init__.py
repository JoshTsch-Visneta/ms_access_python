def get_tables(db_cursor):
    tables = db_cursor.tables()
    tables = tables.fetchall()
    return tables

def get_table_names(db_cursor):
    tables = get_tables(db_cursor)
    table_names = []
    for table in tables:
        table_names.append(table.table_name)
    return table_names

def table_exists(db_cursor, table=None):
    tables = get_table_names(db_cursor)
    if table == None:
        return False
    elif table in tables:
        return True
    else:
        return False

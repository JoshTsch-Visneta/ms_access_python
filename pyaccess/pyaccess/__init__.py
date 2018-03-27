def table_exists(table=None):
    tables = ["one","two"]
    if table == None:
        return False
    elif table in tables:
        return True
    else:
        return False

import sqlite3
from sqlite3 import Error

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def create_connection():
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    
    db_file = "vaccineDB.db"
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = dict_factory
    except Error as e:
        print(e)

    return conn

def execute_select_query(selectQueryToRun):
    # create a database connection
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute(selectQueryToRun)
        rows = cur.fetchall()

        return rows

def execute_insert_update_query(insertUpdateQueryToRun):
    print(insertUpdateQueryToRun)
    # create a database connection
    rowID = 0
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute(insertUpdateQueryToRun)
        rowID = cur.lastrowid
        conn.commit()

    return rowID
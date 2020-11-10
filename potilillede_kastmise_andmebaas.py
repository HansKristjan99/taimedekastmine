import sqlite3, os
from sqlite3 import Error

path = os.getcwd()

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(f"{path}\pythonsqlite.db")
        return conn
    except Error as e:
        print(e)

    return conn
            
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def select_all_tables(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM taimed")

    rows = cur.fetchall()

    for row in rows:
        print(row)
        
def create_taim(conn, taim):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO taimed(nimi,kastmise_interval)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, taim)
    conn.commit()

    return cur.lastrowid

def update_taim(conn, taim):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE taimed
              SET nimi = ? ,
                  kastmise_interval = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, taim)
    conn.commit()
    
def delete_taim(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM taimed WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

database = f"{path}\pythonsqlite.db"

sql_create_table = """ CREATE TABLE IF NOT EXISTS taimed (
                                    id integer PRIMARY KEY,
                                    nimi text NOT NULL,
                                    kastmise_interval integer NOT NULL
                                ); """

conn = create_connection(database)

# create projects table
create_table(conn, sql_create_table)

while True:
    sisestus = input("Sisesta taime nimi andmebaasi (alternatiivid: 'välju', 'muuda', 'kustuta'): ")
    if sisestus == "välju":
        break
    if sisestus == "muuda":
        id_muutmine = input("Sisestage taime ID mida tahad muuta: ")
        uus_nimi = input("Sisesta uus taime nimi: ")
        uus_kastmine = input("Sisesta uus kastmise interval: ")
        update_taim(conn, (str(uus_nimi), uus_kastmine, id_muutmine))
    if sisestus == "kustuta":
        id_kustutamine = input("Sisestage taime ID mida tahad kustutada: ")
        delete_taim(conn, id_kustutamine);
    else:
        interval = input("Sisesta kastmise interval: ")
        if interval == "välju":
            break

        with conn:
            taim = (sisestus, interval)
            create_taim(conn, taim)
        
with conn:
    select_all_tables(conn)
    

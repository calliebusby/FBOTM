import sqlite3
from sqlite3 import Error


def add_new_images_collection(conn, the_boi, urls):
    for url in urls:
        add_new_image(conn, the_boi, url)

def create_images_table(conn):
    sql_create_images_table = """ CREATE TABLE IF NOT EXISTS images (
                                                id integer PRIMARY KEY,
                                                name text NOT NULL,
                                                url text NOT NULL
                                            ); """

    if conn is not None:
        create_table(conn, sql_create_images_table)
    else:
        print("Error! DB connection")


def add_new_image(conn, the_boi, url):
    with conn:
        task_1 = (the_boi, url)
        create_image(conn, task_1)


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_image(conn, task):
    sql = ''' INSERT INTO images(name, url)
                 VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid


def verify_data_created(conn, the_boi):
    query = 'SELECT * FROM images WHERE name = "%s"' % the_boi
    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()

    if len(rows) > 0:
        return True

    return False

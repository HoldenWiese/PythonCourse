"""
Holden Wiese
2020-02-19
This exercise followed Dan as he built a python program that created and populated a database with a table and some
contents.
"""

# SQLite3 is a database that allows you to create and use a basic database
import sqlite3

# sqlite3.connect('myDB.db) allows you to create a database you can connect to.
conn = sqlite3.connect('test.db')

# The with statement allows you to interact with files streams in a way that insures they are closed. I think including
# the conn.close in with statements may be redundant.
with conn:
    # The cursor object allows you to have multiple working environments through the same connection to the database.
    # It is how we make interact with the database. It is a control structure for traversing database.
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons\
    (ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_fname TEXT, \
    col_lname TEXT, \
    col_email TEXT  \
    )")
    #.commit() method commits the database modifications you are making.
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons (col_fname, col_lname, col_email) \
                VALUES (?, ?, ?)",
                ('Sally', 'May', 'mays@jmail.com'))
    cur.execute("INSERT INTO tbl_persons (col_fname, col_lname, col_email) \
                VALUES (?, ?, ?)",
                ('Sarah', 'Jones', 'sara@jmail.com'))
    cur.execute("INSERT INTO tbl_persons (col_fname, col_lname, col_email) \
                VALUES (?, ?, ?)",
                ('Makin', 'Bacon', 'baconboy@jmail.com'))
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute('SELECT col_fname, col_lname, col_email FROM tbl_persons \
                WHERE col_fname = "Sarah"')
    #
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = 'First name: {}\nLast Name: {}\nEmail: {}'.format(item[0], item[1], item[2])
    print(msg)

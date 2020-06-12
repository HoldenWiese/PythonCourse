"""
Your script will need to use Python 3 and the sqlite3 module.
Your database will require 2 fields, an auto-increment primary integer field and a field with the data type of string.
Your script will need to read from the supplied list of file names at the bottom of this page and determine only
the files from the list which ends with a “.txt” file extension.
Next, your script should add those file names from the list ending with “.txt” file extension within your database.
Finally, your script should legibly print the qualifying text files to the console.
"""


import sqlite3

conn = sqlite3.connect('db_104.db')
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles\
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_fileName TEXT \
                )")
    conn.commit()


for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_txtFiles (col_fileName) VALUES (?)", (x,))
        conn.commit()

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_txtFiles")
    result = cur.fetchall()
    print("\nThis is an array of tuples. Each tuple represents a row in the table and the rows respective "
          "data. \nThe following items were discovered as text files in the fileList tuple.\n" + str(result[0][1]))
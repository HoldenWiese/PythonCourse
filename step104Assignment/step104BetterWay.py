import sqlite3

conn = sqlite3.connect('db_104.db')
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles\
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_fileName TEXT \
                )")
    for x in fileList:
        if x.endswith('.txt'):
            cur.execute("INSERT INTO tbl_txtFiles (col_fileName) VALUES (?)", (x,))
    conn.commit()
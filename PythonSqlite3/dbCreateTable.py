
import sqlite3

conn = sqlite3.connect('test.db')
print "Baza de date a fost deschisa.";

conn.execute('''CREATE TABLE EXEMPLU
       (ID INT PRIMARY KEY     NOT NULL,
       NUME           TEXT    NOT NULL,
       VARSTA            INT     NOT NULL,
       ADRESA       CHAR(50),
       SALAR         REAL);''')
print "Proces incheiat.";

conn.close()

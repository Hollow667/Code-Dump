
import sqlite3

conn = sqlite3.connect('test.db')
print "Baza de date a fost deschisa.";

conn.execute("INSERT INTO EXEMPLU (ID,NUME,VARSTA,ADRESA,SALAR) \
      VALUES (1, 'Paul', 32, 'Brasov', 2000.00 )");

conn.execute("INSERT INTO EXEMPLU (ID,NUME,VARSTA,ADRESA,SALAR) \
      VALUES (2, 'Andrei', 25, 'Iasi', 2000.00 )");

conn.execute("INSERT INTO EXEMPLU (ID,NUME,VARSTA,ADRESA,SALAR) \
      VALUES (3, 'Teodor', 23, 'Timisoara', 1500.00 )");

conn.execute("INSERT INTO EXEMPLU (ID,NUME,VARSTA,ADRESA,SALAR) \
      VALUES (4, 'Adnana', 25, 'Bucuresti', 1800.00 )");

conn.commit()
print "Proces incheiat.";
conn.close()

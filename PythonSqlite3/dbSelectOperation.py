
import sqlite3

conn = sqlite3.connect('test.db')
print "Baza de date a fost deschisa.";

cursor = conn.execute("SELECT id, nume, adresa, salar  from EXEMPLU")
for row in cursor:
   print "ID = ", row[0]
   print "NUME = ", row[1]
   print "ADRES = ", row[2]
   print "SALAR = ", row[3], "\n"

print "Proces incheiat.";
conn.close()

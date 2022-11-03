import sqlite3

con = sqlite3.connect("agenda.db")
print("DB Connected!")

cur = con.cursor()
#cur.execute('DROP TABLE contatos')

#cur.execute('CREATE TABLE contatos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, empresa TEXT NOT NULL, telefone TEXT, email TEXT NOT NULL)')

#cur.execute('INSERT INTO contatos VALUES (NULL, "Contato A", "Empresa A", NULL, "emailA@gmail.com")')
#cur.execute('INSERT INTO contatos VALUES (NULL, "Contato B", "Empresa B", "(31) 99999-1111", "emailB@gmail.com")')
#cur.execute('INSERT INTO contatos VALUES (NULL,"Contato C", "Empresa C", "(31) 99999-2222", "emailC@gmail.com")')

con.commit()
cur.execute('SELECT * FROM contatos')
print(cur.fetchall())

import sqlite3

column_1 = 'name'
table_name='menu'
#conn = sqlite3.connect(sqlite_file)
conn = sqlite3.connect('menu.db')
c = conn.cursor()


print "Entire db"
c.execute("SELECT name FROM menu WHERE but LIKE 'rect' AND rect=1 AND tri = 0 AND croix = 0 AND up = 0 AND down = 0".\
	format(name=column_1, menu=table_name, but=column_1))
all_rows = c.fetchall()
print(all_rows)
#print('7): {}'.format(all_rows) )
#print(all_rows[1])
conn.close()

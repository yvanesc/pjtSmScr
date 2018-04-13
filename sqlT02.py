import sqlite3
#conn = sqlite3.connect(sqlite_file)
conn = sqlite3.connect('menu.db')
c = conn.cursor()


print "Entire db"
for row in c.execute("SELECT * FROM menu WHERE but LIKE 'rect' AND rect=1 AND tri = 0 AND croix = 0 AND up = 0 AND down = 0"):
	print row
c.close()

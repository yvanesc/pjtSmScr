import sqlite3
#conn = sqlite3.connect(sqlite_file)
conn = sqlite3.connect('menu.db')
c = conn.cursor()


print "Entire db"
for row in c.execute("SELECT * FROM menu"):
	print row
c.close()

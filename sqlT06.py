import sqlite3

#column_1 = 'name'
#column_2 = 'fctbt'
#column_3 = 'parambt'

table_name='menu'
conn = sqlite3.connect('menu.db')
c = conn.cursor()

def reqMenu(chpsGet):
	c.execute("SELECT "+ chpsGet +" FROM menu WHERE but LIKE 'rect' AND rect=1 AND tri = 0 AND croix = 0 AND up = 0 AND down = 0".\
        	format(name='name', menu=table_name))
	
	all_rows = c.fetchall()

	print(all_rows[0][0])

	conn.close()
	return

reqMenu("name")

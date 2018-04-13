import sqlite3

column_1 = 'name'
column_2 = 'fctbt'
column_3 = 'parambt'

table_name='menu'
conn = sqlite3.connect('menu.db')
c = conn.cursor()

c.execute("SELECT name,fctbt,parambt FROM menu WHERE but LIKE 'rect' AND rect=1 AND tri = 0 AND croix = 0 AND up = 0 AND down = 0".\
        format(name=column_1, fctbt=column_2, parambt=column_3, menu=table_name))
all_rows = c.fetchall()
print(all_rows)
#print(all_rows(1))
#print('7): {}'.format(all_rows) )
#print(all_rows[1])
conn.close()


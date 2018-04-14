import sqlite3

#column_1 = 'name'
#column_2 = 'fctbt'
#column_3 = 'parambt'

table_name='menu'
conn = sqlite3.connect('menu.db')
c = conn.cursor()
s=" "
def reqMenu(chpsGet, butGet, rectGet, triGet, croixGet, upGet, downGet):
	c.execute( "SELECT "+ chpsGet +" FROM menu WHERE but LIKE '" +butGet + "' AND rect="+rectGet+" AND tri ="+triGet+" AND croix ="+croixGet+" AND up ="+upGet+" AND down ="+downGet+"".\
                format(name=chpsGet, menu=table_name))

        all_rows = c.fetchall()

        #print(all_rows[0][0])
	
        conn.close()
	#return
        return(all_rows[0][0])

#reqMenu("name","rect")


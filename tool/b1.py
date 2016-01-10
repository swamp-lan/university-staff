import MySQLdb

conn = MySQLdb.connect('localhost', 'root', '', 'bablo')

cursor = conn.cursor()

cursor.execute("select * from ws order by ws_room")
res = cursor.fetchall()

for i in res:
	print i[3], i[1]
	


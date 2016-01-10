import MySQLdb
import string

db = MySQLdb.connect('localhost', 'root', '', 'bablo')
cur = db.cursor()

query = '''
select
  ws.ws_name,
  ws.ws_room as a,
  (300 - sum(t_size)) as yo
from
  money_trans right join ws on (ws.ws_id = money_trans.ws_id)

group by
  ws_name
having
  yo > 0
order by a

'''
cur.execute(query)
all = cur.fetchall()
dolg = 0
for res in all:
	print "_", res[1],string.ljust(res[0].capitalize(), 12),  int(res[2]/50),  "___", "____________________________________"
	dolg += res[2]

print "total: %s" % (len(all))
print "dolg: %s" % (dolg)
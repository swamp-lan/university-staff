import DNS
import kinterbasdb

DNS.AddNameServer('172.16.0.4')

r=DNS.Request()


con = kinterbasdb.connect(
	dsn="spider:/var/ib/swamp_test.gdb",
	user="DEVEL",
	password="DefPohNa"
	)

cur = con.cursor()


query = """
select * from s_computers
"""

cur.execute(query)
for i in cur.fetchall():
	name = i[4].lower()
	res = r.req('%s.swamp.lan' % name ,qtype='A')
	if len(res.answers):
		print "%s\t%s" % (name, res.answers[0]['data'])
		pass
	else:
		print "%s [not found]" % name




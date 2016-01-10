import MySQLdb

ws = {}

pidori = {}
all = {}

do_leta = {}
leto = {}
sent = {}



conn = MySQLdb.connect('localhost', 'root', '', 'bablo')
cursor = conn.cursor()
cursor.execute("select * from ws order by ws_room")
res = cursor.fetchall()

for comp in res:
	ws [comp[1]] = {'room':comp[3], 'dolg':0, 'do_leta':0, 'leto':0, 'sent':0}


for line in open("do_leta.txt").readlines():
	line = line.strip()
	if not ws.has_key(line):
		print line

	ws[line]['do_leta'] = 1

for line in open("leto.txt").readlines():
	line, sum = line.strip().split(" ")
	if not ws.has_key(line):
		print line

	ws[line]['leto'] = int(sum)

for line in open("sent.txt").readlines():
	line, sum = line.strip().split(" ")
	if not ws.has_key(line):
		print line

	ws[line]['sent'] = int(sum)

#===== перещёт
a = 0

for line in ws.keys():

	pidor = 0
	if ws[line]['do_leta'] == 1:
		pidor = 1
		a += 100
	
	ws[line]['dolg'] = (100 - ws[line]['leto']) + (100 - ws[line]['sent'])
	a += ws[line]['dolg']

	if ws[line]['dolg'] >0:
		pidor = 1

	if pidor:
		#print line, ws[line]['do_leta'], ws[line]['leto'], ws[line]['sent'], ":", ws[line]['dolg']
		pidori[line] = ws[line]
	all[line] = ws[line]

#print len(pidori), len(all)

# ======= рисуем пидоров в порядке как из базы (по комнатам)

for comp in res:
	out = ""
	name = comp[1]
	if not pidori.has_key(name):
		continue
# комната
	out += "__ %s(___) " % (ws[name]['room'])

# имя компа
	b = 25 - len(name + out)
	out += "%s%s " % (name.upper(), b*".")


# до лета

	if ws[name]['do_leta'] == 1:
		out += "в(___), "

# долг за лето
	dolg_leto = (100 - ws[name]['leto'])
	if dolg_leto > 0:
		out += "л.:%s " % (dolg_leto)

# сент
	dolg_sent = (100 - ws[name]['sent'])
	if dolg_sent > 0:
		out += "с.:%s " % (dolg_sent)

# общий долг
	b = 50 - len(out)
	out += "%sдолг:%s(___)" % (b*".", ws[name]['dolg'])
	#print "%s %s %s лето:%s, сент.:%s, %sдолг:%s" % (ws[name]['room'], name, b*" ", ws[name]['leto'], ws[name]['sent'], do_leta, ws[name]['dolg'])
	#out += "\n"

	out += "...................."
	print out

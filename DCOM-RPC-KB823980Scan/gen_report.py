import time
import locale

print

min_active = 30 * 60		#(полчаса)
max_active = 60 * 60 * 24 * 7	#(неделя)


locale.setlocale(locale.LC_ALL, "RU")
REPORT_NAME = "непропатченные.html"

def sss(a, b):
	if a>b:
		return 1
	if a<b:
		return -1
	if a==b:
		return 0


def load_hash():
	r1 = {}
	for line in open("res.txt", "r").readlines():
		host, stat = line.split("\t")
		r1[host] = stat
	return r1

ws_res = load_hash()

res = []

t1 = (time.time() - min_active)
t2 = (time.time() - max_active)

active = 0

for key in ws_res.keys():

	tt = float(ws_res[key])
	if key == "COOLSIDE-PC":
		continue

	if tt > t1:
		ch = "+ "
		active += 1
	else:
		ch = ""

	if tt < t2:
		continue

	if float(ws_res[key]) != 0:
		res.append(ch + key.capitalize())




res.sort(sss)

rep_f = open(REPORT_NAME, "w")

rep_f.write("<pre>\n")
rep_f.write("Машины имеющие уязвимость DCOM RPC\n==================================\n\n")

c = 0
t = ""
for line in res:
	hv = 17 - len(line)
	t += line + (" " * hv)
	c += 1
	if c == 3:
		rep_f.write(t + "\n")
		c = 0
		t = ""
rep_f.write(t + "\n")

rep_f.write("\n-----------\nВсего: %s\n" % len(res))
rep_f.write("Обновлено: %s" % (time.strftime("%H:%M, %d %b.")))
rep_f.write("\n\n\n(+) - Дырявые машины прямо щя")

print "reported ok"
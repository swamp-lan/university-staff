import DNS
DNS.AddNameServer('172.16.0.4')

res = []
res2 = []

for i in range(255):
	for j in range(254):
		yo = '172.16.%s.%s' % (i, j)
		try:
			print "%s - %s" % (yo, DNS.revlookup(yo))
			pizda = DNS.revlookup(yo)
			res.append([yo, pizda])
			res2.append(pizda.lower() + "\n")
		except:
			#print "%s - error" % (yo)
			pass

print len(res)
open("wss_1.txt", "w").writelines(res2)
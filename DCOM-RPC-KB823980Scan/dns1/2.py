import DNS
DNS.AddNameServer('172.16.0.4')

res = []
res2 = []

for i in range(255):
	for j in range(254):
		try:
			yo = '172.16.%s.%s' % (i, j)
			print "%s - %s" % (yo, DNS.revlookup(yo))
			res.append([yo, DNS.revlookup(yo)])
			res2.append(DNS.revlookup(yo).lower() + "\n")
		except:
			#print "error"
			pass

print len(res)
open("wss.txt", "w").writelines(res2)
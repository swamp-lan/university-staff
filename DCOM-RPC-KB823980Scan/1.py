import socket

l = []

def sss(a, b):
	if a>b:
		return 1
	if a<b:
		return -1
	if a==b:
		return 0


for line in open("1a.dat", "r").readlines():
	line = line[:14]
	try:
		a = socket.gethostbyaddr(line)[0].split(".")[0].upper()
		l.append(a)
	except:
		#print "%s: unknown" % line
		pass
l.sort(sss)

for i in l:
	print i



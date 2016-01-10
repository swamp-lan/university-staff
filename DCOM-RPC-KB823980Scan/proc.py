import sys
import socket
import DNS
import os
import time

LOGFILE = ""

print

for i in os.listdir("K:/__keks/__/pr files/KB823980Scan"):
	#print i
	if i.find(".log") > 0:
		LOGFILE = i

if not LOGFILE:
	print "log file not found"
	sys.exit(0)


DNS.AddNameServer('172.16.0.4')

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

def store_hash(hash):
	f = open("res.txt", "w")
	for key in hash.keys():
		f.write("%s\t%s\n" % (key.strip(), str(hash[key]).strip()))
	f.close()

PREF = "res"

ws_res = load_hash()

res = {}


for line in open(LOGFILE, "r").readlines():
	try:
		addr, status = line.split(":")
	except:
		#print "skipped: %s" % line.strip()
		continue

	status = status.strip()

	if status.split(" ")[0] == "unpatched":
		st = time.time()
	elif status.split(" ")[0] == "patched":
		st = 0
	else:
		continue

	#time.sleep(0.5)
	print "resolving %s ..." % addr
	try:
	#host = DNS.revlookup(addr).split(".")[0].upper()
		host = socket.gethostbyaddr(addr)[0].split(".")[0].upper()
		print "... %s" % (host)
	except:
		continue

	if not ws_res.has_key(host):
		print "%s added to list" % host

	ws_res[host] = st

store_hash(ws_res)
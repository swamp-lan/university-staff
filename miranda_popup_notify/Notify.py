import socket

def Notify(message, sender="", style=""):
	if sender:
		msg = "%s%s#%s" % (style, sender, message)
	else:
		msg = "%s%s%s" % (style, sender, message)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.sendto(msg, ('127.0.0.1', 12001))
	s.close()

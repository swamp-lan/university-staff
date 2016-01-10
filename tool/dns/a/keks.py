#!/opt/python/bin/python1.5

import DNS
# automatically load nameserver(s) from /etc/resolv.conf
# (works on unix - on others, YMMV)
DNS.ParseResolvConf()

# lets do an all-in-one request
# set up the request object
r = DNS.DnsRequest(qtype='MX')
# do the request
a=r.req('beetle.swamp.lan')
# and do a pretty-printed output
print a.show()

# now lets setup a reusable request object
#r = DNS.DnsRequest(qtype='ANY')
#res = r.req("a.root-servers.nex",qtype='ANY')
#res.show()
#res = r.req("proxy.connect.com.au")
#res.show()



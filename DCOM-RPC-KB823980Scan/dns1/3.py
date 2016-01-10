import DNS


DNS.AddNameServer('172.16.0.4')

r=DNS.Request()


res = r.req('%s.swamp.lan' % name ,qtype='A')
res.answers


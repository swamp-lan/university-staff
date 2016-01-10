import DNS

DNS.AddNameServer('172.16.0.4')


res = r.req('www.microsoft.com',qtype='A')
print len(res.answers),'different A records'
print map(lambda x:x['data'], res.answers)
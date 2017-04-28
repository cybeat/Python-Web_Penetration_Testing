import requests
# payload={'url':'http://www.freshdesk.com'}
req=requests.head('http://www.httpbin.org/ip')
# print req.text
print "Status_Code: -->" +str(req.status_code) +"\n"
print "Server_Headers\n***************************************"
for head in req.headers:
	print "\t" +head + ":" + req.headers[head]
print "----------------x-----------------\n"
print "Response Content\n" +req.text

import requests
customheader={'User-Agent':'Android 7.1.1'}
req=requests.get('http://www.httpbin.org/headers',headers=customheader)
# print req.text
print "Status_Code: -->" +str(req.status_code) +"\n"
print "Server_Headers\n***************************************"
for head in req.headers:
	print "\t" +head + ":" + req.headers[head]
print "----------------x-----------------\n"
print "Response Content\n" +req.text


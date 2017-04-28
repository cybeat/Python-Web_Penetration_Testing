import requests
target_url='http://www.httpbin.org/redirect-to'
payload={'url':'http://www.example.com'}
req=requests.get(target_url,params=payload)
print req.text
print "Response_Status_Code: --> " +str(req.status_code)
for response in req.history:
	print str(response.status_code) + ':' + response.url
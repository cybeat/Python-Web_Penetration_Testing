import requests
payload={'url':'http://www.freshdesk.com'}
req=requests.get('http://www.httpbin.org/redirect-to', params=payload)
# print req.text
print "Status_Code: " +str(req.status_code)
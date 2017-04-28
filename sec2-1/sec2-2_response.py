import requests
target_url='http://www.httpbin.org/fail'
req=requests.get(target_url)
print "Response_Status_Code: --> " +str(req.status_code)

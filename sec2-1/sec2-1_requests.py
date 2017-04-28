import requests
req=requests.get('http://www.httpbin.org/ip')
print req.text

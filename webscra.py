#https://youtu.be/FQuskLyitPI?list=PLlvFEn0NKwXKqRBEMaCY6f7CDatHceeYL
#https://httpbin.org/#/ link useful for requests lib
#inside the link there is  methods: get, post,put, delete
#https://youtu.be/FQuskLyitPI?list=PLlvFEn0NKwXKqRBEMaCY6f7CDatHceeYL&t=1086

import requests 
payload= {"fname": "rita","lname": "josephine"}
#when send change get to post u can change to 'put' also
# auth=("michel","123")
r = requests.put(url="https://httpbin.org/put",data=payload)
# print(r.status_code)
# print(r.text)
r_json = r.json()
print(r_json)

# headers = r_json["headers"]
# print (headers)
#print(r.json())
# {'args': {'capitale': 'jerusalem', 'country': 'palestine'},
# 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip,
# deflate', 'Host': 'httpbin.org', 
# 'User-Agent': 'python-requests/2.31.0',
# 'X-Amzn-Trace-Id':
# 'Root=1-66028091-21cb5439193b7da630da8315'}, 
# 'origin': '78.40.177.17', 
# 'url': 'http://httpbin.org/get?country=palestine&capitale=jerusalem'}
#print (r.status_code)#output:200 means successful
# print(r.url)http://httpbin.org/get?country=palestine&capitale=jerusalem
#print(r.text)Traceback (most recent call last):
#   File "/Users/michelkadi/Desktop/webscraping/webscra.py", line 5, in <module>
#     r = requests.get(url="http://httpbin.org/get",param=payload)
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/requests/api.py", line 73, in get
#     return request("get", url, params=params, **kwargs)
        
 #sion.request() got an unexpected keyword argument 'param'
# (base) michelkadi@mss-MacBook webscraping % /usr/local/bin/python3 /Users/michelkadi/Desktop/webscraping/webscra.py
# 200
# (base) michelkadi@mss-MacBook webscraping % /usr/local/bin/python3 /Users/michelkadi/Desktop/
# webscraping/webscra.py
# http://httpbin.org/get?country=palestine&capitale=jerusalem
# (base) michelkadi@mss-MacBook webscraping % /usr/local/bin/python3 /Users/michelkadi/Desktop/
# # webscraping/webscra.py
# {
#   "args": {
#     "capitale": "jerusalem", 
#     "country": "palestine"
#   }, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.31.0", 
#     "X-Amzn-Trace-Id": "Root=1-66027f59-5bfe9332692d2a5f555fa453"
#   }, 
#   "origin": "78.40.177.17", 
#   "url": "http://httpbin.org/get?country=palestine&capitale=jerusalem"
# }

#r = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/242px-Python-logo-notext.svg.png')
# print(r.headers)
  #" with open("python-logo.png",'wb')as f: 
#"f.write(r.content)#create file with the link picture above
# f.write(r.content)"
# print(r)#0utput <Response [200]>
# print(r.status_code)#200 ur request submitted

#attributes and methods used with r
# print(dir(r))#print all r attribute
# print(help(r))#print information about attributes
# print(r.content)


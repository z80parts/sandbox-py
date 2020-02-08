import requests

rq = requests.get('http://www.yahoo.co.jp')
print(rq.status_code)


print(rq.headers)
print(rq.encoding)

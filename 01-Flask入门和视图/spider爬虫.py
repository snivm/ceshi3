import requests

# 发送GET请求，请求参数为name=lisi&age=33
res = requests.get('http://127.0.0.1:5000/request/?name=lisi&age=33',
                   cookies={"name": "hello"})
print(res.text)

# 发送GET请求，请求参数为data
# res = requests.get('http://127.0.0.1:5000/request/', data={'name': 'lucy', 'age': 33})
# print(res.text)
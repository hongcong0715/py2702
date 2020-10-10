import requests

# 1-1，准备请求的相关数据（接口地址 + 请求的参数）
# 接口地址
url = "http://api.lemonban.com/futureloan/member/register"

# 1-2、请求的参数
data = {
    "mobile_phone": "18710003456",
    "pwd":"lemonban"
}

headers = {"X-Lemonban-Media-Type":"lemonban.v1"}   # 请求头
# 2、发送请求
response = requests.post(url=url,json=data,headers=headers)

#
# 3、打印返回内容
print(response.text)


# 4、打印请求头内容
print(response.request.headers)
"""
{'User-Agent': 'python-requests/2.23.0', 
'Accept-Encoding': 'gzip, deflate', 
'Accept': '*/*', 
'Connection': 'keep-alive', 
'Content-Length': '44',
 'Content-Type': 'application/json'}

"""


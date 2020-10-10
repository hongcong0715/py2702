import requests
import jsonpath
url ="http://api.lemonban.com/futureloan/member/login"
data = {
    "mobile_phone": "18710003456",
    "pwd":"lemonban"

}
headers = {"X-Lemonban-Media-Type":"lemonban.v2"}   # 请求头


response  = requests.post(url=url,json=data,headers=headers)
res = response.json()
# print(res)   # res 是一个字典
member_id = jsonpath.jsonpath(res,"$..id")[0]    # 此处是列表取下标
token = jsonpath.jsonpath(res,"$..token")[0]     # 此处是列表取下标
# print(member_id)
# print(token)

# 请求鉴权的接口

re_url ="http://api.lemonban.com/futureloan/member/recharge"
re_data = {
    "member_id":member_id,
    "amount":100

}
headers = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "Authorization":"Bearer"+" "+ token
}
response2 = requests.post(url=re_url,json=re_data,headers=headers)
print(response2.content.decode("utf-8"))


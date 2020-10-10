import requests

url = "http://api.lemonban.com/futureloan/member/login"

data = {
    "mobile_phone": "18710003456",
    "pwd":"lemonban"
}

headers = {"X-Lemonban-Media-Type":"lemonban.v2"}   # 请求头
# 2、发送请求
response = requests.post(url=url,json=data,headers=headers)

#
# 3、打印返回内容
res1 = response.text
print(res1,type(res1))      # 打印出来的类型是字符串
# json方法，将字符串中的json类型数据转换为对应的python值。。不能使用eval强转！！！
# 使用json方法的前提，返回数据必须是json格式的。



res4 = response.content.decode("utf-8")
print(res4)
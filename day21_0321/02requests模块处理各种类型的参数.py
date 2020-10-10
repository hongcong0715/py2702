import requests
# -------------------------------post请求--------------------------
url = "http://httpbin.org/post"

data = {
    "name":"haha",
    "age":18
}
"""
 一、
  "data": "{\"name\": \"haha\", \"age\": 18}", 
当使用json来传递，数据在data里面； "Content-Type": "application/json", 
"""

# response = requests.post(url=url,json=data)  # json
"""
 二，
 "form": {
    "age": "18", 
    "name": "haha"
  }, 
当使用data来传递，数据在form里面；  "Content-Type": "application/x-www-form-urlencoded", 
  
"""
# response = requests.post(url=url,data=data)  # data

"""
三，
当使用files来传递，数据在"files"里面； "Content-Type": "multipart/form-data;
"""

# file = {
#     "pic": ("timg.png",open(r"/Users/momo/Documents/py2702/day21_0321/timg.png","rb"),"png/image")
# }
#
# response = requests.post(url=url,files=file)   # file
# print(response.text)


# --------------------------------------------get请求----------------------
# 放到url地址后面
# url = "http://httpbin.org/get?name=haha&age=18"
# response = requests.get(url=url)
# print(response.text)

# 使用params来传递
url = "http://httpbin.org/get"
data = {
    "name":"hahah",
    "age":18
}

response = requests.get(url=url,params=data)
print(response.text)
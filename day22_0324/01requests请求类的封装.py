
"""
封装的需求：
excel文件中：   请求方法、请求的url地址，请求的参数
请求头，放置到配置文件中
"""
# import requests
# def send(case):
#     """
#
#     :param case: 字典格式的用例数据
#     :return:
#     """
#     headers = {
#
#     }
#     if case["method"] == "get":
#         return requests.get(url=case["url"],params=case["data"],headers=headers)
#     elif case["method"] == "post":
#         return requests.post(url=case["url"], params=case["data"], headers=headers)
#     elif case["method"] == "patch":
#         return requests.patch(url=case["url"], params=case["data"], headers=headers)
#





import requests
res = requests.request("get",url="http://api.lemonban.com/futureloan/member/login",json={"mobile_phone": "18710003457"})
print(res.text)
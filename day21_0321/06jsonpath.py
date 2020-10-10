
res = {"code":0,"msg":"OK",
"data":{"id":7806530,"leave_amount":0.0,"mobile_phone":"18710003456","reg_name":"小柠檬","reg_time":"2020-03-27 11:23:02.0","type":1,
"token_info":
{"token_type":"Bearer",
"expires_in":"2020-03-27 23:22:17",
"token":"eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjc4MDY1MzAsImV4cCI6MTU4NTMyMjUzN30.UuHqcMNoXyQ7b70Qqj6VLt9IN_hMdcHwPTMEP1aRojq6IeQOYjlFEu-_8AFPTPcG-RrAlBtvuxELa4oR7wu-tA"}},
"copyright":"Copyright 柠檬班 © 2017-2019 湖南省零檬信息技术有限公司 All Rights Reserved"}

import jsonpath
member_id = jsonpath.jsonpath(res,"$..id")[0]
token = jsonpath.jsonpath(res,"$..token")[0]
print(member_id)
print(token)


"""
.  代表直接紫节点
..  代表子孙节点（不管层级）
"""

# 还可以通过之前的字典取key去获取

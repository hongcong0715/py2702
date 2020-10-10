import unittest
from day15_0307.demo1.test_register import RegisterTestCase

from BeautifulReport import BeautifulReport


# 1、创建套件
suite = unittest.TestSuite()
# 2、加载测试用例
# # （1）单条
# case_data =  {"expected": {"code": 1, "msg": "注册成功"}, "data": ['python1', '123456', '123456']}
# case = RegisterTestCase("test_register",case_data)
# suite.addTest(case)


# （2）多条用例
cases = [
    {"expected": {"code": 1, "msg": "注册成功"}, "data": ['python1', '123456', '123456']},
    {"expected": {"code": 0, "msg": "两次密码不一致"}, "data": ['python12', '1234567', '123456']},
    {"expected": {"code": 0, "msg": "该账户已存在"}, "data": ['python26', '1234567', '1234567']}
]

for case_data in cases:
    case = RegisterTestCase("test_register",case_data)
    suite.addTest(case)


# 3、执行测试用例，生成报告
br = BeautifulReport(suite)
br.report("注册测试",filename= "report.html" )
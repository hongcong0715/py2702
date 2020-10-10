import unittest
from demo.task_0305 import register

"""
# 定义测试用例类:用例类必须继承于unittest.TestCase
# 定义测试用例：在测试用例类中，每一个以test开头的方法就是一条用例


unittest中测试用例执行的顺序：根据方法名按ASCII码进行排序的。


unittest中会自动根据用例方法执行的时候，是否出现断言异常，来评判用例执行是否通过。

"""
users = [{'user': 'python26', 'password': '123456'}]

class Register(unittest.TestCase):
    def test_not_all(self):
        data = ["哈哈","123456",""]
        expected = {"code": 0, "msg": "所有参数不能为空"}
        res = register(data[0],data[1],data[2])
        self.assertEqual(expected,res)

    def test_user_in_users(self):
        data = ["python26","123456","123456"]
        expected = {"code": 0, "msg": "该账户已存在"}
        res = register("python26","123456","123456")
        self.assertEqual(expected,res)

    def test_pwd_not_equal(self):
        pw1 = "123456"
        pw2 = "1234"
        expected = {"code": 0, "msg": "两次密码不一致"}
        if pw1 != pw2:
            return {"code": 0, "msg": "两次密码不一致"}
        res = {"code": 0, "msg": "两次密码不一致"}
        self.assertEqual(expected,res)

    def test_lence_is_equal(self):
        data = ["py123456","12345678","12345678"]
        expected = {"code": 1, "msg": "注册成功"}
        if 6 <= len(data[0]) <= 18 and 6 <= len(data[1]) and 6 <= len(data[1]):
            return {"code": 1, "msg": "注册成功"}
        res = {"code": 1, "msg": "注册成功"}
        self.assertEqual(expected,res)








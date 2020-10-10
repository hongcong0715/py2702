import unittest
from day15_0307.task_15day.login import login_check
from day15_0307.task_15day.myddt import ddt,data


@ddt
class Test_Login_Case(unittest.TestCase):
    cases = [
        {
            "title":"登录成功",
            "expected": {"code": 0, "msg": "登录成功"},
            "data": {"username": "111", "password": "222"}
        },
        {
            "title": "账号或密码不正确",
            "expected": {"code": 1, "msg": "账号或密码不正确"},
            "data": {"username": "python8888", "password": "lemonban"}
        },
        {
            "title": "账号或密码不正确",
            "expected": {"code": 1, "msg": "账号或密码不正确"},
            "data": {"username": "python27", "password": "l1111111"}
        },
        {
            "title": "所有的参数不能为空",
            "expected": {"code": 1, "msg": "所有的参数不能为空"},
            "data": {"username": "python27"}
        },
        {
            "title": "所有的参数不能为空",
            "expected": {"code": 1, "msg": "所有的参数不能为空"},
            "data": {"password": "l1111111"}
        }

    ]
    @data(*cases)
    def test_login(self,case):
        expected = case["expected"]
        da = case["data"]
        res = login_check(**da)
        self.assertEqual(expected,res)
        print("hhhhhhh")

if __name__ == '__main__':
    unittest.main()

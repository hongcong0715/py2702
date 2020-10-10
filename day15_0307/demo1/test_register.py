import unittest
from day15_0307.demo1.register import register


class RegisterTestCase(unittest.TestCase):
    def __init__(self,methodName,case_data):
        super().__init__(methodName)

        self.case_data = case_data


    def test_register(self):
        # 1、准备用例参数
        expected = self.case_data["expected"]
        data = self.case_data["data"]
        # 2、调用被测试的功能函数，传入参数，获取实际结果
        res = register(*data)
        # 3、断言（比对预期结果和实际结果
        self.assertEqual(expected,res)


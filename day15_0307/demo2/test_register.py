import unittest
from day15_0307.demo2.register import register
from day15_0307.demo2.myddt import ddt,data

# 告诉下我这个测试用例类要使用ddt来处理，@ddt是装饰器,这个类使用ddt来做数据驱动
@ddt
class RegisterTestCase(unittest.TestCase):
    # 把测试数据定义为测试类的类属性
    cases = [
        {"title":"注册成功","expected": {"code": 1, "msg": "注册成功"}, "data": ['python1', '123456', '123456']},
        {"title":"密码不一致","expected": {"code": 0, "msg": "两次密码不一致"}, "data": ['python12', '1234567', '123456']},
        {"title":"该账户已存在","expected": {"code": 0, "msg": "该账户已存在"}, "data": ['python26', '1234567', '1234567']}
    ]

    # data 用来传用例数据，此时用例数据作为类属性了，把用例数据传给data，data会帮我们自动去遍历用例数据，自动生成测试用例
    @data(*cases)
    def test_register(self,case):
        # print("打印的case",case)

        expected = case["expected"]
        data = case["data"]
        res = register(*data)
        self.assertEqual(expected,res)



if __name__ == '__main__':
    unittest.main()



# v 是用例数据，修改了ddt的源码，284行
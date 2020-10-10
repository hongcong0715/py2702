import unittest
from day16_0310.task_16day.login import login_check
from day16_0310.task_16day.myddt import ddt,data
from day16_0310.task_16day.handle_excel import HandleExcel


@ddt
class Test_Login_Case(unittest.TestCase):
    excel = HandleExcel("cases.xlsx", "login")
    cases = excel.read_data()


    @data(*cases)
    def test_login(self,case):
        expected = eval(case["expected"])
        da = eval(case["data"])
        row = case["case_id"] + 1
        res = login_check(**da)
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            # excel写入结果：未通过
            self.excel.write_data(row=row, column=5, value="未通过")
            # 主动抛出异常
            raise e
        else:
            # excel写入结果：通过
            self.excel.write_data(row=row, column=5, value="通过")
        self.assertEqual(expected,res)



if __name__ == '__main__':
    unittest.main()

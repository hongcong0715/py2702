import unittest
from day18_0314.task_16day.login import login_check
from day18_0314.task_16day.myddt import ddt,data
from day18_0314.task_16day.handle_excel import HandleExcel
from day18_0314.task_16day.handle_logging import log


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
            log.error("用例执行{}--{}-未通过".format(case["title"]))

            raise e
        else:
            # excel写入结果：通过
            self.excel.write_data(row=row, column=5, value="通过")
            log.error("用例执行--{}--通过".format(case["title"]))

        self.assertEqual(expected,res)




if __name__ == '__main__':
    unittest.main()

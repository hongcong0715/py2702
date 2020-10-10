import unittest
from demo.testcases import Register



# 第一步：创建测试套件
suite = unittest.TestSuite()


# 第二步：加载测试用例到测试套件
# 第一种：通过测试用例类去加载
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(Register))




# 使用 HTMLTestRunner来生成测试报告
from HTMLTestRunnerNew import HTMLTestRunner

runner = HTMLTestRunner(stream=open("task_new_report.html","wb",),
                        title="测试报告",
                        tester="大胖",
                        description="第一个版本的测试"
                        )
runner.run(suite)
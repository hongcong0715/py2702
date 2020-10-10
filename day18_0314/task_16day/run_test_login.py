import unittest
from BeautifulReport import BeautifulReport
suite = unittest.defaultTestLoader.discover(r"/Users/momo/Documents/py2702/day18_0314/task_16day")

br = BeautifulReport(suite)
br.report("task中打印的报告",filename = "task_report.html")



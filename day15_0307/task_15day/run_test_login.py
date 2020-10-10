import unittest
from BeautifulReport import BeautifulReport
suite = unittest.defaultTestLoader.discover(r"/Users/momo/Documents/py2702/day15_0307/task_15day")

br = BeautifulReport(suite)
br.report("task中打印的报告",filename = "task_report.html")



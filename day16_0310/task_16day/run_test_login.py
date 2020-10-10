import unittest
from BeautifulReport import BeautifulReport
suite = unittest.defaultTestLoader.discover(r"/Users/momo/Documents/py2702/day16_0310/task_16day")

br = BeautifulReport(suite)
br.report("task中打印的报告",filename = "task16_report.html")



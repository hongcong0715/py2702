import unittest
from BeautifulReport import BeautifulReport
suite = unittest.defaultTestLoader.discover(r"/Users/momo/Documents/py2702/day15_0307/demo2")

br = BeautifulReport(suite)
br.report("demo2中生成的报告",filename= "report.html")
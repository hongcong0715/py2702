import logging

# 创建一个日志收集器，如果不传参数name  会返回默认的日志收集器root，

mylog = logging.getLogger()


mylog.setLevel("DEBUG")
logging.debug("这是debug")
logging.info("这是info")
logging.warning("这是warning")      # WARNING:root:这是warning
logging.error("这是error")          # ERROR:root:这是error
logging.critical("这是critical")    #  CRITICAL:root:这是critical



import yaml

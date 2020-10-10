import logging
mylog = logging.getLogger()
mylog.setLevel("DEBUG")

# 设置日志输出的等级
# 1、创建一个输出到控制台输出渠道
sh = logging.StreamHandler()
# 2、设置输出渠道的输出等级
sh.setLevel("ERROR")
# 3、将输出渠道和日志收集器绑定
mylog.addHandler(sh)

# 创建一个输出到文件的输出渠道
fh = logging.FileHandler("all.log",encoding="utf8")
fh.setLevel("DEBUG")
mylog.addHandler(fh)


logging.debug("这是debug")
logging.info("这是info")
logging.warning("这是warning")
logging.error("这是error")
logging.critical("这是critical")


import logging
from logging.handlers import TimedRotatingFileHandler,RotatingFileHandler
# 第一步，创建一个日志收集器
log = logging.getLogger("dapang")

# 第二步，设置收集器收集的等级
log.setLevel("DEBUG")

# 第三步，设置输出渠道
# 创建一个按时间进行轮转的文件输出渠道
fh = TimedRotatingFileHandler("user.log",encoding="utf8",when="S",interval=1,backupCount=7)
fh.setLevel("ERROR")
log.addHandler(fh)

# (2)文件进行轮转
fh = RotatingFileHandler("dapang",encoding="utf8",maxBytes=1024*1024*20,backupCount=7)
fh.setLevel("ERROR")
log.addHandler(fh)


# 第四步，设置输出格式
formats='%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
# 创建一个输出格式对象
form = logging.Formatter(formats)
# 将输出格式添加到输出渠道
fh.setFormatter(form)

log.error("error记录的")
log.error("critical记录的")



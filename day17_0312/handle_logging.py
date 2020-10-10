import logging
def create_logger():
    # 第一步，创建一个日志收集器
    log = logging.getLogger("dapang")

    # 第二步，设置收集器收集的等级
    log.setLevel("DEBUG")

    # 第三步，设置输出渠道

    fh = logging.FileHandler("mylog.log", encoding="utf8")
    fh.setLevel("ERROR")
    log.addHandler(fh)

    sh = logging.StreamHandler()
    sh.setLevel("INFO")
    log.addHandler(sh)

    # 第四步，设置输出格式
    formats = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
    # 创建一个输出格式对象
    form = logging.Formatter(formats)
    # 将输出格式添加到输出渠道
    fh.setFormatter(form)
    sh.setFormatter(form)

    return log
log = create_logger()




#
# log.error("error记录的")
# log.error("critical记录的")

from configparser import ConfigParser


class HandleConfig(ConfigParser):
    def __init__(self,filename):
        super().__init__()
        self.read(filename,encoding="utf-8")


conf = HandleConfig("lemon.ini")

res = conf.get("mysql","port")
print(res)
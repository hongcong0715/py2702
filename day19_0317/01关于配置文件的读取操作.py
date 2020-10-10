from configparser import ConfigParser
# 第一步，创建一个配置文件解析器对象

conf = ConfigParser()
# 第二部，将配置文件读取到配置文件解析器对象中

conf.read("lemon.ini",encoding="utf-8")

# 第三步，读取相关的配置内容

# 方法一：get  读取的所有内容都会当成字符串来处理
res = conf.get("log","file_name")
print(res)


# 方法二，getint  专门用来读取数值类型的数据(只能读  int类型)
res2 = conf.getint("mysql","port")
print(res2)

# 方法三，getfloat  专门用来读取 浮点数（float）
res3 = conf.getfloat("mysql","n")
print(res3)

# 方法四，getboolean 专门用来读取布尔值（false  true 大小写都可以）
res4 = conf.getboolean("mysql","b1")
print(res4)
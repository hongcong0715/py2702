from configparser import ConfigParser
# 第一步，创建一个配置文件解析器对象

conf = ConfigParser()
# 第二部，将配置文件读取到配置文件解析器对象中

conf.read("lemon.ini",encoding="utf-8")

# 第三步，配置文件写入
conf.set("mysql","dapang","大胖")
conf.write(fp=open("lemon.ini","w",encoding="utf-8"))

"""
写入之后，会发现配置文件ini中的注释被清空了。
不能使用a模式去写，因为如果是a模式写的话，之前配置文件中的内容在全部读取出来重新写入。一个配置文件中不能有两个配置块！！！
"""

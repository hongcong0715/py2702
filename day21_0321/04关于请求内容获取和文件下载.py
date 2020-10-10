import requests
url ="http://www.lemonban.com/"
response = requests.post(url=url)
# 通过text 自动识别内容的编码方式，有可能识别不准确，会出现乱码
print(response.text)
# 通过content ，手动指定编码方式，对页面内容进行解码，不会出现乱码
print(response.content.decode("utf-8"))



# 文件下载
res = requests.get(url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1585333325057&di=e568163add7c3c36ed08c802b966bcaa&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fq_70%2Cc_zoom%2Cw_640%2Fimages%2F20200204%2F7f91866f6f424490b8f9f1a3a9fe96b4.jpeg")
print(res.content)

with open("lemon.png","wb") as f:
    f.write(res.content)
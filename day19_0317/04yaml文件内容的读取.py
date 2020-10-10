import yaml
with open("lemon.yaml","r",encoding="utf-8") as f:
    file = yaml.load(f,Loader=yaml.FullLoader)
    print(file)     # file 是一个字典

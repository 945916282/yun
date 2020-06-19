import os

re=os.popen("ping 192.168.0.119")
print(re.read())
print(type(re.read()))
r=re.read()
if "100%" in r:
    print("通讯失败")
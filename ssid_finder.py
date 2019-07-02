import os

interface = input("interface: ")
result = os.popen("sudo iw {} scan ".format(interface)).read()
resultList = result.split("\n")
SSID = list()
for i in resultList:
    if "SSID" in i:
        SSID.append(i[7:])
        
print(SSID)

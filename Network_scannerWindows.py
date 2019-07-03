import os

result = os.popen("netsh wlan show networks").read()
resultList = result.split("\n")
SSID = list()
for i in resultList:
    if "SSID" in i:
        SSID.append(i[i.index(":")+2:])

print(SSID)
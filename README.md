# Python-script-that-gets-ssid-s-of-visible-networks-for-linux-
That script gets visible wifi's ssid's as a list. You can entegrate this script in your projects.


```
import os

interface = input("interface: ")
result = os.popen("sudo iw {} scan ".format(interface)).read()
resultList = result.split("\n")
SSID = list()
for i in resultList:
    if "SSID" in i:
        SSID.append(i[6:])
        
print(SSID)
```

# Python-script-that-gets-ssid-s-of-visible-networks-for-linux-
That script gets visible wifi's ssid's as a list. You can entegrate this script in your projects.


```
#Code for linux
import os

interface = input("interface: ")
result = os.popen("sudo iw {} scan ".format(interface)).read()
resultList = result.split("\n")
SSID = list()
for i in resultList:
    if "SSID" in i:
        SSID.append(i[7:])
        
print(SSID)
```

```
#Code for windows
import os

result = os.popen("netsh wlan show networks").read()
resultList = result.split("\n")
SSID = list()
for i in resultList:
    if "SSID" in i:
        SSID.append(i[i.index(":")+2:])

print(SSID)
```

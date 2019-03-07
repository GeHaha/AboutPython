# Untitled - By: Gehaha - 周四 3月 7 2019

import network
SSID = ''
KEY = ''

print("Trying to connect ...(may take a while)...")
wlan = network.WINC()
wlan.connect(SSID,key = KEY ,security = waln.WPA_PSK)
print(wlan.ifconfig())

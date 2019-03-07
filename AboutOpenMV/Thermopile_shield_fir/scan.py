# Untitled - By: Gehaha - 周四 3月 7 2019

import time,network

wlan = network.WINC()
print("\nFirmware version:", wlan.fw_version())

while(True):
    scan_result = wlan.scan()
    for ap in scan_result:
        print("channel:%d RSSI:%d Auth : %d BSSID :%s"%(ap))
        print()
        time.sleep(1000)

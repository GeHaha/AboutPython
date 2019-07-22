# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:07:51 2019

@author: Gehaha
"""

import requests
url = "https://developer.nrel.gov/docs/solar/nsrdb/psm3_data_download.json?api_key=3tZmQmERpT8H948da4d7rNKOP3ycIJPPYNLOoZbi"
payload = "names=2012&leap_day=false&interval=60&utc=false&full_name=Honored%2BUser&email=honored.user%40gmail.com&affiliation=NREL&mailing_list=true&reason=Academic&attributes=dhi%2Cdni%2Cwind_speed_10m_nwp%2Csurface_air_temperature_nwp&wkt=MULTIPOINT(-106.22%2032.9741%2C-106.18%2032.9741%2C-106.1%2032.9741)"
headers = {
        'content-type':"application/x-www-form-urlencoded",
        'cache-control':"no-cache"}
response = requests.request("POST",url,data = payload,headers= headers)
print(response.text)

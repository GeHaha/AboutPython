yeenni# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests

from pypvwatts import PVWatts

PVWatts.api_key = '3tZmQmERpT8H948da4d7rNKOP3ycIJPPYNLOoZbi'

result = PVWatts.request(system_capacity = 4,module_type=1,array_type=1,
                         azimuth =190,tilt = 30,dataset ='tmy2',
                         losses = 13,lat = 40,lon = -105)
print(result.ac_annual)


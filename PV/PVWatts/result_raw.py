# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 21:31:01 2019

@author: Gehaha
"""
from pypvwatts import PVWatts

result = PVWatts.request(
        system_capacity=4, module_type=1, array_type=1,
        azimuth=190, tilt=30, dataset='tmy2',
        losses=13, lat=40, lon=-105
        )
print(result.raw)
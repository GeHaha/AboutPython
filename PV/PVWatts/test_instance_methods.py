# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 21:08:52 2019

@author: Gehaha
"""

from pypvwatts import PVWatts


p = PVWatts(api_key='myapikeyHLM6x2In2KmX4fxsTRRBT2r9KfDagJjU')
result = p.request(
        system_capacity=4, module_type=1, array_type=1,
        azimuth=190, tilt=30, dataset='tmy2',
        losses=13, lat=40, lon=-105)
print(result.ac_annual)
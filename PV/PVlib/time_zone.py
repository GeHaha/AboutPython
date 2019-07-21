# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 15:43:28 2019

@author: Gehaha
"""

import datetime
import pandas as pd
import pytz


print(len(pytz.all_timezones))

print(pytz.all_timezones[::20])

#print(pytz.country_timezones('')

print(pd.Timestamp('2015-1-1 00:00',tz='America/Denver'))

print(pd.Timestamp('2015-1-1 00:00').tz_localize('Etc/GMT+8'))
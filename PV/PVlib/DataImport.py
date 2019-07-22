# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:07:35 2019

@author: Gehaha
"""

import os

import inspect
import pvlib

pvlib_abspath = os.path.dirname(os.path.abspath(inspect.getfile(pvlib)))

file_abspath = os.path.join(pvlib_abspath,'data','703165TY.csv')

tmy3_data, tmy3_metadata = pvlib.iotools.read_tmy3(file_abspath)
print(tmy3_metadata)

tmy3_data.index.tz
pytz.FixedOffset(-540)
print(tmy3_data.loc[tmy3_data.index[0:5],['GHI','DNI','aod']])


solar_position = pvlib.solarposition.get_solarposition(tmy3_data.index,
                                                       tmy3_metadata['latitude'],
                                                       tmy3_metadata['longitude'])


ax = solar_position.loc[solar_position.index[0:24],['apparent_zenith','apparent_elevation', 'azimuth']].plot()
ax.legend(loc=1)

ax.axhline(0,color='darkgray');
ax.axhline(180,color='darkgray');
ax.set_ylim(-60,200);
ax.set_xlabel('Local time({})'.format(solar_position.index.tz));
ax.set_ylabel('(degress)');



# =============================================================================
# solar position
#如果我们有一个没有本地化的DatetimeIndex，比如下面的这个，会怎么样?太阳位置计算器将假设UTC时间。
# =============================================================================

index = pd.DatetimeIndex(start='1997-01-01 01:00',freq='1h',periods=24)
print(index)
solar_position_notz = pvlib.solarposition.get_solarposition(index,
                                                        tmy3_metadata['latitude'],
                                                        tmy3_metadata['longitude'])

ax = solar_position_notz.loc[solar_position_notz.index[0:24], ['apparent_zenith', 'apparent_elevation', 'azimuth']].plot()
ax.legend(loc=1);
ax.axhline(0, color='darkgray');  # add 0 deg line for sunrise/sunset
ax.axhline(180, color='darkgray');  # add 180 deg line for azimuth at solar noon
ax.set_ylim(-60, 200);  # zoom in, but cuts off full azimuth range
ax.set_xlabel('Time (UTC)');
ax.set_ylabel('(degrees)'); 

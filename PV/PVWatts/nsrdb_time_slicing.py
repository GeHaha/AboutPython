# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:46:19 2019

@author: Gehaha
"""

import h5pyd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.spatial import cKDTree


f = h5pyd.File("/nrel/nsrdb/nsrdb_2012.h5",username= 'Gehaha', mode= 'r',endpoint= 'https://developer.nrel.gov/api/hsds/',api_key='3tZmQmERpT8H948da4d7rNKOP3ycIJPPYNLOoZbi')

time_index = pd.to_datetime(f['time_index'][...].astype(str))

# extract indexes for a particular span of time
march = time_index.month == 3
np.where (march)[0]

#or a particular date
timestep = np.where(time_index == '2012-07-04 00:00:00')[0][0]
print(timestep)



# =============================================================================
# Map Data
# =============================================================================
# extract coordinates (lat,lon)
print(dict(f['coordinates'].attrs))
coords = f['coordinates'][...]


dset = f['ghi']
# extract every 10th location at a particular time
print("4")
data = dset[timestep,::10]
print("3")
#combine data with coordinates in a DataFram
df = pd.DataFrame()
df['longitude'] = coords[::10,1]
df['latitude'] = coords[::10,0]
#unscale dataset
df['ghi'] = data / dset.attrs['psm_scale_factor']

df.shape()
print("2")
df.plot.scatter(x='longitude',y='latitude',c='ghi',
                colormap= 'YlOrRd',
                title = str(time_index[timestep]))
print("1")
plt.show()
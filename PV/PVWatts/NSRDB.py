# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 13:38:49 2019

@author: Gehaha
"""

import h5pyd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mping
from scipy.spatial import cKDTree


f = h5pyd.File("/nrel/nsrdb/nsrdb_2012.h5",username= 'Gehaha', mode= 'r',endpoint= 'https://developer.nrel.gov/api/hsds/',api_key='3tZmQmERpT8H948da4d7rNKOP3ycIJPPYNLOoZbi')
f.attrs['version']

#list the datasets in the file
list(f)
#print(list(f))

#datasets are stored in a 2d array of time x location
dset = f['ghi']
print(dset.shape)


#Extract datetime index for datasets
time_index = pd.to_datetime(f['time_index'][...].astype(str))
#Temporal resolution is 30min
#time_index
#print(time_index)

#Location information is stored in either 'meta' or 'coordinates'
#meta = pd.DataFrame(f['meta'][...])
#meta.head()
#print(meta.head())

# Datasets  have been saved as integers
dset.dtype
print(dset.dtype)

#70GB per dataset
dset.shape[0] * dset.shape[1] * 2 *10 ** - 9 # 2MB per  chunk
print(dset.shape[0] * dset.shape[1] * 2 *10 ** - 6)

dset.chunks #chunk by week
print(dset.chunks)

#2MB per chunk
dset.chunks[0] * dset.chunks[1] * 2 * 10** -6
print(dset.chunks[0] * dset.chunks[1] * 2 * 10** -6)

# To convert dataset values back to floats use the 'psm_scale_factor'
dset.attrs['psm_scale_factor'] #
print(dset.attrs['psm_scale_factor'])

# wind speed on the other hand has single decimal percision when scaled by 10
scale_factor = f['wind_speed'].attrs['psm_scale_factor']
units = f['wind_speed'].attrs['psm_units']
print('wind_speed scale factor =',scale_factor)
print('wind_speed units after unscaling =',units)
f['wind_speed'][0,0]/scale_factor #divide by scale_factor to return native value
print(f['wind_speed'][0,0]/scale_factor)


#time_index = pd.to_datetime(f['time_index'][...].astype(str))

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

data = dset[timestep,::10]

#combine data with coordinates in a DataFram
df = pd.DataFrame()
df['longitude'] = coords[::10,1]
df['latitude'] = coords[::10,0]
#unscale dataset
df['ghi'] = data / dset.attrs['psm_scale_factor']
df.shape
print(df.shape)

#df.plot.scatter(x='longitude',y='latitude',c='ghi',
#                colormap= 'YlOrRd',
#                title = str(time_index[timestep]))

#plt.show()

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 22:18:03 2019

@author: Gehaha
"""

import pandas as pd
import matplotlib.pyplot as plt
import pvlib


from pvlib.pvsystem import PVSystem
from pvlib.location import Location
from pvlib.modelchain import ModelChain

naive_times = pd.DatetimeIndex(start='2018',end='2019',freq='1h')

# very approximate
# latitude, longitude, name, altitude, timezone

coordinates =[(30, -110, 'Tucson', 700, 'Etc/GMT+7'),
                   (35, -105, 'Albuquerque', 1500, 'Etc/GMT+7'),
                   (40, -120, 'San Francisco', 10, 'Etc/GMT+8'),
                   (50, 10, 'Berlin', 34, 'Etc/GMT-1')]


#get the module and inverter specifications from SAM
sandia_modules = pvlib.pvsystem.retrieve_sam('SandiaMod')
sapm_inverters = pvlib.pvsystem.retrieve_sam('cecinverter')

module = sandia_modules['Canadian_Solar_CS5P_220M___2009_']
inverter = sapm_inverters['ABB__MICRO_0_25_I_OUTD_US_208_208V__CEC_2014_']

#speciify constant ambient air temp and wind for simplicity

temp_air = 20
wind_speed = 0
system = PVSystem(module_parameters=module,inverter_parameters=inverter)
energies = {}


for latitude, longitude, name, altitude, timezone in coordinates:

    times = naive_times.tz_localize(timezone)
    location = Location(latitude, longitude, name=name, altitude=altitude,
                          tz=timezone)
    weather = location.get_clearsky(times)
    mc = ModelChain(system, location,
                      orientation_strategy='south_at_latitude_tilt')
    mc.run_model(times=times, weather=weather)
    annual_energy = mc.ac.sum()
    energies[name] = annual_energy
    
energies = pd.Series(energies)

#base on the parameters specified above ,these are in W*hrs

print(energies.round(0))

energies.plot(kind='bar',rot=0)

plt.ylabel('Yearly energyyield(W hr)')

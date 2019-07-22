# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 10:14:47 2019

@author: Gehaha
"""

import pandas as pd
import matplotlib.pyplot as plt
import pvlib


from pvlib.pvsystem import PVSystem
from pvlib.location import Location
from pvlib.modelchain import ModelChain
from pvlib.pvsystem import LocalizedPVSystem


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

for latitude,longitude,name,altitude,timezone in coordinates:
    localized_system = LocalizedPVSystem(module_parameters=module,
                                           inverter_parameters=inverter,
                                          surface_tilt=latitude,
                                        surface_azimuth=180,
                                            latitude=latitude,
                                            longitude=longitude,
                                             name=name,
                                             altitude=altitude,
                                             tz=timezone)
    times = naive_times.tz_localize(timezone)
    clearsky = localized_system.get_clearsky(times)
    solar_position = localized_system.get_solarposition(times)
    total_irrad = localized_system.get_irradiance(solar_position['apparent_zenith'],
                                                     solar_position['azimuth'],
                                                    clearsky['dni'],
                                                      clearsky['ghi'],
                                                    clearsky['dhi'])
    temps = localized_system.sapm_celltemp(total_irrad['poa_global'],
                                              wind_speed, temp_air)
    aoi = localized_system.get_aoi(solar_position['apparent_zenith'],
                                      solar_position['azimuth'])
    airmass = localized_system.get_airmass(solar_position=solar_position)
    effective_irradiance = localized_system.sapm_effective_irradiance(
             total_irrad['poa_direct'], total_irrad['poa_diffuse'],
             airmass['airmass_absolute'], aoi)
    dc = localized_system.sapm(effective_irradiance, temps['temp_cell'])
    ac = localized_system.snlinverter(dc['v_mp'], dc['p_mp'])
    annual_energy = ac.sum()
    energies[name] = annual_energy
    
energies = pd.Series(energies)

#base on the parameters specified above,these are in W*hr
print(energies.round(0))

energies.plot(kind='bar',rot=0)

plt.ylabel('Yearly energy yield(W hr)')


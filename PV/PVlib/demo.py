# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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

system = {'module':module,'inverter':inverter,'surface_azimuth':180}
energies = {}

for latitude,longitude,name,altitude,timezone in coordinates:
    times = naive_times.tz_localize(timezone)
    system['surface_tilt'] = latitude
    solpos = pvlib.solarposition.get_solarposition(times, latitude, longitude)
    dni_extra = pvlib.irradiance.get_extra_radiation(times)
    airmass = pvlib.atmosphere.get_relative_airmass(solpos['apparent_zenith'])
    pressure = pvlib.atmosphere.alt2pres(altitude)
    am_abs = pvlib.atmosphere.get_absolute_airmass(airmass, pressure)
    tl = pvlib.clearsky.lookup_linke_turbidity(times, latitude, longitude)
    cs = pvlib.clearsky.ineichen(solpos['apparent_zenith'], am_abs, tl,
                                  dni_extra=dni_extra, altitude=altitude)
    aoi = pvlib.irradiance.aoi(system['surface_tilt'], system['surface_azimuth'],
                                  solpos['apparent_zenith'], solpos['azimuth'])
    total_irrad = pvlib.irradiance.get_total_irradiance(system['surface_tilt'],
                                                            system['surface_azimuth'],
                                                          solpos['apparent_zenith'],
                                                         solpos['azimuth'],
                                                         cs['dni'], cs['ghi'], cs['dhi'],
                                                            dni_extra=dni_extra,
                                                            model='haydavies')
    temps = pvlib.pvsystem.sapm_celltemp(total_irrad['poa_global'],
                                             wind_speed, temp_air)
    effective_irradiance = pvlib.pvsystem.sapm_effective_irradiance(
            total_irrad['poa_direct'], total_irrad['poa_diffuse'],
            am_abs, aoi, module)
    dc = pvlib.pvsystem.sapm(effective_irradiance, temps['temp_cell'], module)
    ac = pvlib.pvsystem.snlinverter(dc['v_mp'], dc['p_mp'], inverter)
    annual_energy = ac.sum()
    energies[name] = annual_energy
    
energies = pd.Series(energies)

#base on the parameters specified above .these are in W*hrs
print(energies.round(0))

energies.plot(kind='bar',rot=0)

plt.ylabel('Yearly energy yield(W hr)')

  

    


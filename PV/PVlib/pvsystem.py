# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 13:47:14 2019

@author: Gehaha
"""

from pvlib.pvsystem import PVSystem

#内部数据存储在对象属性中。例如，描述PV系统模块参数的数据存储在PVSystem.module_parameters中
module_parameters = {'pdc0': 10, 'gamma_pdc': -0.004}
system = pvlib.pvsystem.PVSystem(module_parameters=module_parameters)
#gammma_dc 模块温度系数。通常以1/C为单位。

print(system.module_parameters)

#pdc = system.pvwatts_dc(1000,30) #pvwatts_dc 接受外部传入的辐照度和温度
#print(pdc)
#pdc 直流电源

system.module_parameters['temp_ref']=0

#lower temp_ref should lead to lower DC power than calculated above 
pdc = system.pvwatts_dc(1000,3) #计算直流功率
loss = system.pvwatts_losses()
print(pdc)


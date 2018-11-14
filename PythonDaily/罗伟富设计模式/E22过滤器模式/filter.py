# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 09:04:17 2018

@author: Gehaha
"""

class FilterScreen:
    "过滤网"
    def doFilter(self,rawMaterials):
        for material in rawMaterials:
            if (material == "豆渣"):
                rawMaterials.remove(material)
            return rawMaterials

    #测试代码
    def testFilterScreen():
        rawMaterials = ["豆浆","豆渣"]
        print("过滤前：",rawMaterials)
        filter = FilterScreen()
        filteredMaterials = filter.doFilter(rawMaterials)
        print("过滤后：",filteredMaterials)
        
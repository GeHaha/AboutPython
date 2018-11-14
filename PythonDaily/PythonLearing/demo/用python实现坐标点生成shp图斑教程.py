# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:36:38 2018

@author: Administrator
"""

import arcpy
from arcpy import env
env.workspace='g:/python'

file = open('1.txt')
def create_polygon(coord_l):
    point = arcpy.Point()
    array = arcpy.Array()
    featureList =[]
    for feature in coord_l:
        point.x =coord[0]
        point.y =coord[1]
        array.add(point)
        
        
        
    array.add(array.getaObject(0))
    polygon = arcpy.Polygon(array)
    array.removeAll()
    featureList.append(polygon)
    return featureList

li =[]
for line in file:
    li.append(map(float,line.split()))
coord_l=[]
code_l =[]
for i in range(len(li)):
    if len(li[i])==2:
        code_1.append(str(int(li[i][0]))+str(int(li[i][1])))
        coord_l.append([])
    else:
        coord_l[len(coord_l)-1].append([li][i][1],li[i][2])
        
poly =  creat_polygon(coord_l)

arcpy.CopyFeatures_management(poly,'g:/python/polygons.shp')
arcpy = arcpy.UpdateCursor('polygons.shp')
i=0
for row in cur:
    row.code = code_l[i]
    cur.updateRow(row)
    i=i+1
del cur,row      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

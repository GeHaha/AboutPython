# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:00:48 2019

@author: Gehaha
"""

import numpy as np
a = np.array([[1,2,4],[1,2,3],[2,1,3]])
print(np.mean(a,axis=0))
#沿轴0调用mean（）
#结果[1.33333333 1.66666667 3.33333333]是将每个列表1+1+2/3，2+2+1/3.。。。。


#沿轴1调用mean（）
a = np.array([[1,2,4],[1,2,3],[2,1,3]])
print(np.mean(a,axis=1))
#结果[2.33333333 2.         2.        ] 是将1+2+4/3.。。。。
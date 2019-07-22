# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 21:46:29 2019

@author: Gehaha
"""

import numpy as np
import operator

#距离度量为欧氏距离，分类决策规则为多数表决。
#classify0()函数有4个输入参数：用于分类的输入向量是inX，
#输入的训练集为dataSet，类别为labels，k表示用于选择最近邻的数目。

#group和labels为训练集，其中group为特征向量，labels为类别。
#输入测试实例[0,0]，选取与测试实例距离最近的3个元素，
#最后返回这3个元素中发生频率最高的元素类别，即为kNN近邻法的预测值。

def createDataSet():
    # 创建训练集
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels
    
def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0] 
    # 根据欧式距离计算训练集中每个样本到测试点的距离 
    diffMat = tile(inX, (dataSetSize,1)) - dataSet 
    sqDiffMat = diffMat**2 
    sqDistances = sqDiffMat.sum(axis=1) 
    distances = sqDistances**0.5 
    # 计算完所有点的距离后，对数据按照从小到大的次序排序 
    sortedDistIndicies = distances.argsort() 
    # 确定前k个距离最小的元素所在的主要分类，最后返回发生频率最高的元素类别 
    classCount={} 
    for i in range(k): 
        voteIlabel = labels[sortedDistIndicies[i]] 
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1 
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True) 
    return sortedClassCount[0][0]


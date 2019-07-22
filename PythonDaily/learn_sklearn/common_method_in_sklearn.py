# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:33:15 2019

@author: Gehaha
"""

# 拟合模型
model.fit(X_train,y_train)

#模型的预测
model.predict(X_test)

#获得这个模型的参数
model.get_params()

#为模型进行打分
model.score(data_X,data_y)#回归问题：以R2参数为标准 分类问题：以准确率为标准


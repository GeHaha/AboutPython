# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:20:13 2019

@author: Gehaha
"""

from sklearn.svm import SVR

#创建svr回归模型的对象
clf = SVR()
#利用训练集训练SVR回归模型
clf.fit(X_train,y_train)
"""
SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.1,
    gamma='auto_deprecated', kernel='rbf', max_iter=-1, shrinking=True,
    tol=0.001, verbose=False)
"""
clf.predict(X_test)


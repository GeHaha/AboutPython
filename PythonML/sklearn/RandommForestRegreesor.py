# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:00:29 2019

@author: Gehaha
"""

from sklearn.ensemble import RandomForestRegressor
regr = RandomForestRegressor(max_depth=2,random_state=0,n_estimators=100)

regr.fit(X_train,y_train)
pred= regr.predict(X_test)

# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:14:57 2019

@author: Gehaha
"""

import xgboost as xgb
xgb_model = xgb.XGBRegressor(max_depth=3.learning_rate=0.1,
                             n_estimators=100,
                             objective = 'reg:linear',
                             n_jobs=-1)

xgb_model.fit(X_train,y_train,eval_set=[(X_train,y_train)],
                  eval_metric ='loglosss',verbose=100)

y_pred =xgb_model.predict(X_test)

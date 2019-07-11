# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:26:40 2019

@author: Gehaha
"""

import lightgbm as lgb

gbm = lgb.LGBMRegressor(num_leaves=31,learning_rate=0.05,n_estimators=20)

gbm.fit(X_train,y_train,eval_set=[(X_train,y_train)],
        eval_metric='logloss',
        ver)
y_pred = gbm.predict(X_test)

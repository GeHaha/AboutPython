# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:22:26 2019

@author: Gehaha
"""

from sklearn.neural_network import MLPRegressor
mlp = MLPRegressor()
mlp.fit(X_train,y_train)
"""
MLPRegressor(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(100,), learning_rate='constant',
       learning_rate_init=0.001, max_iter=200, momentum=0.9,
       n_iter_no_change=10, nesterovs_momentum=True, power_t=0.5,
       random_state=None, shuffle=True, solver='adam', tol=0.0001,
       validation_fraction=0.1, verbose=False, warm_start=False)

"""
y_pred = mlp.predict(X_test)

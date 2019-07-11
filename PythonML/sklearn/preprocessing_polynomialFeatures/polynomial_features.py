# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 20:32:05 2019

@author: Gehaha
"""
    
# =============================================================================
# 在机器学习中，通过增加一些输入数据的非线性特征来增加模型的复杂度通常是有效的。
# 一个简单通用的办法是使用多项式特征，这可以获得特征的更高维度和互相间关系的项。
# 这在 PolynomialFeatures 中实现:
# =============================================================================


import numpy as np
from sklearn.preprocessing import PolynomialFeatures

X = np.arange(6).reshape(3,2)
#print(X)

poly = PolynomialFeatures(2)
#print(poly)
X= poly.fit_transform(X)
#X 的特征已经从 (X_1, X_2) 转换为 (1, X1, X2, X1**2, X1*X2, X2**2) 。
#print(X)


# =============================================================================
# 在一些情况下，只需要特征间的交互项，这可以通过设置 interaction_only=True 来得到:
#X的特征已经从 (X1, X2, X3) 转换为 (1, X1, X2, X3, X1*X2, X1*X3, X2*X3, X1*X2*X3)
# =============================================================================
X = np.arange(9).reshape(3,3)
poly = PolynomialFeatures(degree=3,interaction_only=True)
B = poly.fit_transform(X)
print(B)
A = poly.transform(X)
print(A)
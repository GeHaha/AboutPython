# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:20:49 2019

@author: Gehaha
"""

import numpy as np
import pandas as pd
 
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.externals import joblib 
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.feature_selection import SelectFromModel
from sklearn.decomposition import PCA
from sklearn.cross_validation import cross_val_score
from sklearn.model_selection import KFold
from sklearn.linear_model import Ridge
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.svm import SVR
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
import xgboost as xgb
from lightgbm import LGBMRegressor
import math
#%matplotlib inline

pd.set_option('display.max_colwidth',1000)
pd.set_option('display.height',1000)
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)




#数据预处理
#读取数据
train_data = pd.read_csv(r'C:\Users\Gehaha\Desktop\pv_test/data/public.train.csv')
test_data = pd.read_csv(r'C:\Users\Gehaha\Desktop\pv_test/data/public.test.csv')

df_result = pd.DataFrame()
df_result['ID'] = list(test_data['ID'])
special_missing_ID = test_data[test_data[(test_data == 0) | (test_data == 0.)].count(axis=1) > 13]['ID']



#异常值处理
def drop_all_outlier(df):
    df.drop_duplicates(df.columns.drop('ID'), keep='first', inplace=True)
    df.drop(df[(df.电压A > 800) | (df.电压A < 500)].index,inplace=True)
    df.drop(df[(df.电压B > 800) | (df.电压B < 500)].index,inplace=True)
    df.drop(df[(df.电压C > 800) | (df.电压C < 500)].index,inplace=True)
    df.drop(df[(df.现场温度 > 30) | (df.现场温度 < -30)].index,inplace=True)
    df.drop(df[(df.转换效率A > 100)].index,inplace=True)
    df.drop(df[(df.转换效率B > 100)].index,inplace=True)
    df.drop(df[(df.转换效率C > 100)].index,inplace=True)
    df.drop(df[(df.风向 > 360)].index,inplace=True)
    df.drop(df[(df.风速 > 20)].index,inplace=True)
    return df

cleaned_train_data = train_data.copy()
cleaned_train_data = drop_all_outlier(cleaned_train_data)

cleaned_sub_data = test_data.copy()
cleaned_sub_data = drop_all_outlier(cleaned_sub_data)
cleaned_sub_data_ID = cleaned_sub_data['ID']


all_data = pd.concat([train_data, test_data], axis=0).sort_values(by='ID').reset_index().drop(['index'], axis=1)
bad_feature = ['ID', '功率A', '功率B', '功率C', '平均功率', '现场温度', '电压A', '电压B', '电压C', '电流B', '电流C', '转换效率', '转换效率A', '转换效率B', '转换效率C']
bad_index = all_data[bad_feature][
    (all_data[bad_feature] > all_data[bad_feature].mean() + 2 * all_data[bad_feature].std()) | 
    (all_data[bad_feature] < all_data[bad_feature].mean() - 2 * all_data[bad_feature].std())
].dropna(how='all').index

nn_bad_data = all_data.loc[np.concatenate([bad_index - 1, bad_index, bad_index + 1])].sort_values(by='ID', ascending=True).drop_duplicates()
bad_data = all_data.loc[bad_index].sort_values(by='ID', ascending=True)
len(bad_data)


# 上下记录均值替代异常值
for idx, line in bad_data.iterrows():
    ID = line['ID']
    col_index = line[bad_feature][ 
        (line[bad_feature] > all_data[bad_feature].mean() + 2 * all_data[bad_feature].std())| 
        (line[bad_feature] < all_data[bad_feature].mean() - 2 * all_data[bad_feature].std())
    ].index
    index = all_data[all_data['ID'] == ID].index
    
    before_offset = 1
    while (idx + before_offset)in bad_index:
        before_offset += 1

    after_offset = 1
    while (idx + after_offset) in bad_index:
        after_offset += 1
    
    replace_value = (all_data.loc[index - before_offset, col_index].values + all_data.loc[index + after_offset, col_index].values) / 2
    all_data.loc[index, col_index] = replace_value[0]
    
    
#拆分数据
train_data = all_data.drop(all_data[all_data['ID'].isin(df_result['ID'])].index).reset_index().drop(['index'], axis=1)
test_data = all_data[all_data['ID'].isin(df_result['ID'])].drop(['发电量'], axis=1).reset_index().drop(['index'], axis=1)
len(train_data), len(test_data)


#去除重复值
train_data = train_data.drop_duplicates(train_data.columns.drop('ID'), keep='first')

#生成数据
def generate_train_data(train_data, test_data, poly=False, select=False):
    y = train_data['发电量']
    X = train_data.drop(['发电量','ID'], axis=1)
    sub_data = test_data.drop(['ID'], axis=1)
    
    polynm = None
    if poly:
        from sklearn.preprocessing import PolynomialFeatures
        polynm = PolynomialFeatures(degree=2, interaction_only=True)
        X = polynm.fit_transform(X)
        sub_data = polynm.transform(sub_data)
        
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
    
    sm = None
    if select:
        from sklearn.feature_selection import SelectFromModel
        sm = SelectFromModel(GradientBoostingRegressor(random_state=2))
        X_train = sm.fit_transform(X_train, y_train)
        X_test = sm.transform(X_test)
        sub_data = sm.transform(sub_data)
        
    return X_train, X_test, y_train, y_test, sub_data, sm, polynm

def cal_score(mse):
    if isinstance(mse, float):
        return 1 / (1 + math.sqrt(mse))
    else:
        return np.divide(1, 1 + np.sqrt(mse))
    
    
X_train, X_test, y_train, y_test, sub_data, sm, polynm = generate_train_data(train_data, test_data, poly=True, select=True)


clean_X_train, clean_X_test, clean_y_train, clean_y_test, clean_sub_data, _, _ = generate_train_data(cleaned_train_data, cleaned_sub_data, poly=False, select=False)

clean_X = np.concatenate([clean_X_train, clean_X_test])
clean_y = np.concatenate([clean_y_train, clean_y_test])
clean_X = polynm.transform(clean_X)
clean_X = sm.transform(clean_X)

clean_sub_data = polynm.transform(clean_sub_data)
clean_sub_data = sm.transform(clean_sub_data)


#叠加模式
all_X_train = np.concatenate([X_train, X_test])
all_y_train = np.concatenate([y_train, y_test])

def cross_validation_test(models, train_X_data, train_y_data, cv=5):
    model_name, mse_avg, score_avg = [], [], []
    for i, model in enumerate(models):
        print(i + 1,'- Model:', str(model).split('(')[0])
        model_name.append(str(i + 1) + '.' + str(model).split('(')[0])
        nmse = cross_val_score(model, train_X_data[i], train_y_data[i], cv=cv, scoring='neg_mean_squared_error')
        avg_mse = np.average(-nmse)
        scores = cal_score(-nmse)
        avg_score = np.average(scores)
        mse_avg.append(avg_mse)
        score_avg.append(avg_score)
        print('MSE:', -nmse)
        print('Score:', scores)
        print('Average XGB - MSE:', avg_mse, ' - Score:', avg_score, '\n')
    res = pd.DataFrame()
    res['Model'] = model_name
    res['Avg MSE'] = mse_avg
    res['Avg Score'] = score_avg
    return res


xgbt1 = xgb.XGBRegressor(n_estimators=950, max_depth=3, max_features='sqrt', random_state=2, n_jobs=8)
xgbt2 = xgb.XGBRegressor(n_estimators=1000, max_depth=3, max_features='sqrt', random_state=3, n_jobs=8)
xgbt3 = xgb.XGBRegressor(n_estimators=1100, max_depth=3, max_features='sqrt', random_state=4, n_jobs=8)

gbdt1 = GradientBoostingRegressor(n_estimators=500, max_depth=3, max_features='sqrt', random_state=2)
gbdt2 = GradientBoostingRegressor(n_estimators=400, max_depth=3, max_features='sqrt', random_state=3)
gbdt3 = GradientBoostingRegressor(n_estimators=500, max_depth=4, max_features='log2', random_state=4)

forest1 = RandomForestRegressor(n_estimators=300, max_features='sqrt', random_state=2, n_jobs=8)
forest2 = RandomForestRegressor(n_estimators=300, max_features='log2', random_state=3, n_jobs=8)
forest3 = RandomForestRegressor(n_estimators=600, max_features='sqrt', random_state=4, n_jobs=8) 

lgb1 = LGBMRegressor(n_estimators=900, max_depth=5, random_state=2, n_jobs=8) 
lgb2 = LGBMRegressor(n_estimators=850, max_depth=4, random_state=3, n_jobs=8)
lgb3 = LGBMRegressor(n_estimators=720, max_depth=4, random_state=4, n_jobs=8)


cross_validation_test(
    models=[    
        xgbt1, xgbt2, xgbt3,
        gbdt1, gbdt2, gbdt3,
        forest1, forest2, forest3,
        lgb1, lgb2, lgb3
    ],
    train_X_data=[
        all_X_train, all_X_train, all_X_train, all_X_train,
        all_X_train, all_X_train, all_X_train, all_X_train,
        all_X_train, all_X_train, all_X_train, all_X_train
    ],
    train_y_data=[
        all_y_train, all_y_train, all_y_train, all_y_train,
        all_y_train, all_y_train, all_y_train, all_y_train,
        all_y_train, all_y_train, all_y_train, all_y_train
    ]
)


















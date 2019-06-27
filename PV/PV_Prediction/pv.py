# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:16:23 2019

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
#from sklearn.cross_validation import cross_val_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.linear_model import Ridge
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.svm import SVR
from sklearn.utils import shuffle

import xgboost as xgb
from lightgbm import LGBMRegressor
import math




# 数据预处理
def clean_data(train_data_X):    
    for j in range(len(np.array(train_data_X.columns))):
        if train_data_X.columns[j] != "ID":
            print("正在处理第%d列数据"%j)
            array = train_data_X[train_data_X.columns[j]]
            num = 0
            len_ = len(train_data_X[train_data_X.columns[j]])
            for i in range(len_):   
                std_ = array.std()
                min_ = array.min()
                max_ = array.max()
                mean_ = array.mean()
                num = array[i]
                std_max =np.float(mean_+3*std_)
                std_min = np.float(mean_-3*std_)
                if (array[0]>std_max) | (array[0]<std_min):
    #                 mean_del = mean_-(array[0]-mean_)/len_
    #                 array[0] = mean_del
                    array[0] = mean_
                if (array[len_-1]>std_max) | (array[len_-1]<std_min):
                    array[len_-1] = mean_
                if i>0 and i<(len_-1):
                    if (array[i]>std_max) | (array[i]<std_min):
                        if (array[i-1]<std_max) and (array[i-1]>std_min) and (array[i+1]<std_max) and (array[i+1]>std_min):
                            array[i]= np.float(array[i-1]+array[i+1])/2
                        elif ((array[i-1]<std_max) and (array[i-1]>std_min))| (array[i+1]>std_max) | (array[i+1]<std_min): 
                            array[i] = array[i-1]
                        elif (array[i-1]<std_max) | (array[i-1]>std_min)|((array[i+1]<std_max) and (array[i+1]>std_min)):
                            array[i] = array[i+1]
            train_data_X[train_data_X.columns[j]] = array
        else:
            pass           
    return train_data_X


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


# 生成数据
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
    
    
#  定义交叉验证函数  
def cross_validation_test(models, train_X_data, train_y_data, cv=5):
    model_name, mse_avg, score_avg = [], [], []
    for i, model in enumerate(models):
        print(i + 1,'- Model:', str(model).split('(')[0])
        model_name.append(str(i + 1) + '.' + str(model).split('(')[0])
        #cross_val_score 通过交叉验证来评估分数
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



#增加历史数据均值
def add_avg(df):
    array = np.array(df["平均功率"])
    newarray=[]
    num = 0
    for i in np.arange(len(array)):
        for j in np.arange(10):
            sum_1=0
            for m in np.arange(j):
                sum_1 += array[m]
            if i<10:
                num = sum_1/(j+1)
            else:
                num = (array[i-1]+array[i-2]+array[i-3]+array[i-4]+array[i-5]+array[i-6]+array[i-7]+array[i-8]+array[i-9])/9
        newarray.append(num)
    df["old平均功率"] = newarray
    return df



# 对上面的函数 add_avg(df) 做了一层封装
# 输入矩阵df 源列名str1 目标列名str2
# 输出 增加一列历史数据均值的矩阵
def add_avgs(df,str1,str2):
    array = np.array(df[str1])
    newarray=[]
    num = 0
    for i in np.arange(len(array)):
        for j in np.arange(10):
            sum_1=0
            for m in np.arange(j):
                sum_1 += array[m]
            if i<10:
                num = sum_1/(j+1)
            else:
                num = (array[i-1]+array[i-2]+array[i-3]+array[i-4]+array[i-5]+array[i-6]+array[i-7]+array[i-8]+array[i-9])/9
        newarray.append(num)
    df[str2] = newarray
    return df
 

#读取数据
train_data = pd.read_csv(r'C:\Users\Gehaha\Desktop\pv_test/data/public.train.csv')
test_data = pd.read_csv(r'C:\Users\Gehaha\Desktop\pv_test/data/public.test.csv')

df_result = pd.DataFrame()
df_result['ID'] = list(test_data['ID'])
special_missing_ID = test_data[test_data[(test_data == 0) | (test_data == 0.)].count(axis=1) > 13]['ID']

#异常值处理
cleaned_train_data = train_data.copy()
cleaned_train_data = drop_all_outlier(cleaned_train_data)

cleaned_sub_data = test_data.copy()
cleaned_sub_data = drop_all_outlier(cleaned_sub_data)
cleaned_sub_data_ID = cleaned_sub_data['ID']

all_data  = pd.concat([train_data, test_data], axis=0).sort_values(by='ID').reset_index().drop(['index'], axis=1)
bad_feature = ['ID','功率A', '功率B', '功率C', '平均功率', '现场温度', '电压A', '电压B', '电压C', '电流B', '电流C', '转换效率', '转换效率A', '转换效率B', '转换效率C']
bad_index1 = all_data[bad_feature][
    (all_data[bad_feature] > all_data[bad_feature].mean() + 2 * all_data[bad_feature].std()) | 
    (all_data[bad_feature] < all_data[bad_feature].mean() - 2 * all_data[bad_feature].std())
].dropna(how='all').index
bad_index2 = all_data[
    ((all_data['电压A']<500)&(all_data['电压A']!=0))|
    ((all_data['电压B']<500)&(all_data['电压B']!=0))|
    ((all_data['电压C']<500)&(all_data['电压C']!=0))].index
bad_index = pd.Int64Index(list(bad_index1)+list(bad_index2))
# all_data.loc[np.concatenate([bad_index -1,bad_index,bad_index+1])].sort_values(by='ID', ascending=True)


nn_bad_data = all_data.loc[np.concatenate([bad_index - 1, bad_index, bad_index + 1])].sort_values(by='ID', ascending=True).drop_duplicates()
bad_data = all_data.loc[bad_index].sort_values(by='ID', ascending=True)



#上下记录均值替代异常值
for idx, line in bad_data.iterrows():
    ID = line['ID']
    col_index = line[bad_feature][ 
        (line[bad_feature] > all_data[bad_feature].mean() + 3 * all_data[bad_feature].std())| 
        (line[bad_feature] < all_data[bad_feature].mean() - 3 * all_data[bad_feature].std())
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
# 去除重复值
train_data = train_data.drop_duplicates(train_data.columns.drop('ID'), keep='first')

# 增加 历史平均功率
train_data = add_avg(train_data)
test_data = add_avg(test_data)
cleaned_train_data = add_avg(cleaned_train_data)
cleaned_sub_data = add_avg(cleaned_sub_data)

# 增加 历史平均功率A 历史平均功率B 历史平均功率C 
train_data = add_avgs(train_data,"功率A","功率Ahistory")
train_data = add_avgs(train_data,"功率B","功率Bhistory")
train_data = add_avgs(train_data,"功率C","功率Chistory")

test_data = add_avgs(test_data,"功率A","功率Ahistory")
test_data = add_avgs(test_data,"功率B","功率Bhistory")
test_data = add_avgs(test_data,"功率C","功率Chistory")

cleaned_train_data = add_avgs(cleaned_train_data,"功率A","功率Ahistory")
cleaned_train_data = add_avgs(cleaned_train_data,"功率B","功率Bhistory")
cleaned_train_data = add_avgs(cleaned_train_data,"功率C","功率Chistory")

cleaned_sub_data = add_avgs(cleaned_sub_data,"功率A","功率Ahistory")
cleaned_sub_data = add_avgs(cleaned_sub_data,"功率B","功率Bhistory")
cleaned_sub_data = add_avgs(cleaned_sub_data,"功率C","功率Chistory")



X_train, X_test, y_train, y_test, sub_data, sm, polynm = generate_train_data(train_data, test_data, poly=True, select=True)

clean_X_train, clean_X_test, clean_y_train, clean_y_test, clean_sub_data, _, _ = generate_train_data(cleaned_train_data, cleaned_sub_data, poly=False, select=False)

clean_X = np.concatenate([clean_X_train, clean_X_test])
clean_y = np.concatenate([clean_y_train, clean_y_test])
clean_X = polynm.transform(clean_X)
clean_X = sm.transform(clean_X)

clean_sub_data = polynm.transform(clean_sub_data)
clean_sub_data = sm.transform(clean_sub_data)



##叠加模式
#树模型
all_X_train = np.concatenate([X_train, X_test])
all_y_train = np.concatenate([y_train, y_test])



xgbt1 = xgb.XGBRegressor(silent=1,max_leaf_nodes=255,seed=789,eta=0.03,scoring='neg_mean_squared_error',n_estimators=351, max_depth=5, max_features='sqrt', random_state=777, n_jobs=12)
xgbt2 = xgb.XGBRegressor(silent=1,max_leaf_nodes=255,seed=1000,eta=0.03,scoring='neg_mean_squared_error',n_estimators=361, max_depth=5, max_features='sqrt', random_state=999, n_jobs=12)
xgbt3 = xgb.XGBRegressor(silent=1,max_leaf_nodes=255,seed=1515,eta=0.03,scoring='neg_mean_squared_error',n_estimators=371, max_depth=5, max_features='sqrt', random_state=367, n_jobs=12)

# n_estimators=1000  max_depth=5  'sqrt'  GradientBoostingRegressor 最佳参数 ,learning_rate=0.08
gbdt1 = GradientBoostingRegressor(n_estimators=1060, max_depth=5, max_features='log2', random_state=789,learning_rate=0.08)
gbdt2 = GradientBoostingRegressor(n_estimators=1100, max_depth=5, max_features='log2', random_state=123,learning_rate=0.08)
gbdt3 = GradientBoostingRegressor(n_estimators=1090, max_depth=5, max_features='log2', random_state=1999,learning_rate=0.08)

# n_estimators=700, max_features='auto', random_state=2, n_jobs=8,max_depth=10
forest1 = RandomForestRegressor(n_estimators=740, max_features='sqrt', random_state=7, n_jobs=12)
forest2 = RandomForestRegressor(n_estimators=730, max_features='sqrt', random_state=9, n_jobs=12)
forest3 = RandomForestRegressor(n_estimators=745, max_features='sqrt', random_state=11, n_jobs=12) 

# n_estimators 850 num_leaves=14,learning_rate=0.1 max_depth=5  seed
lgb1 = LGBMRegressor(n_estimators=840, max_depth=4, random_state=789, n_jobs=12,num_leaves=14,learning_rate=0.08,seed=666) 
lgb2 = LGBMRegressor(n_estimators=845, max_depth=4, random_state=798, n_jobs=12,num_leaves=13,learning_rate=0.1,seed=777)
lgb3 = LGBMRegressor(n_estimators=850, max_depth=4, random_state=777, n_jobs=12,num_leaves=10,learning_rate=0.1,seed=999)

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


#satcking
regrs = [
     xgbt1, gbdt1, forest1, lgb1,
     xgbt2, gbdt2, forest2, lgb2,
     xgbt3, gbdt3, forest3, lgb3
]



class Stacker(object):
    def __init__(self, n_splits, stacker, base_models):
        self.n_splits = n_splits
        self.stacker = stacker
        self.base_models = base_models
    
    # X: 原始训练集, y: 原始训练集真实值, predict_data: 原始待预测数据
    def fit_predict(self, X, y, predict_data):
        X = np.array(X)
        y = np.array(y)
        T = np.array(predict_data)

        folds = list(KFold(n_splits=self.n_splits, shuffle=False, random_state=2018).split(X, y))
        
        # 以基学习器预测结果为特征的 stacker的训练数据 与 stacker预测数据
        S_train = np.zeros((X.shape[0], len(self.base_models)))
        S_predict = np.zeros((T.shape[0], len(self.base_models)))
        
        for i, regr in enumerate(self.base_models):
            print(i + 1, 'Base model:', str(regr).split('(')[0])
            S_predict_i = np.zeros((T.shape[0], self.n_splits))
            
            for j, (train_idx, test_idx) in enumerate(folds):
                # 将X分为训练集与测试集
                X_train, y_train, X_test, y_test = X[train_idx], y[train_idx], X[test_idx], y[test_idx]
                print ('Fit fold', (j+1), '...')
                regr.fit(X_train, y_train)
                y_pred = regr.predict(X_test)                
                S_train[test_idx, i] = y_pred
                S_predict_i[:, j] = regr.predict(T)
            
            S_predict[:, i] = S_predict_i.mean(axis=1)

        nmse_score = cross_val_score(self.stacker, S_train, y, cv=5, scoring='neg_mean_squared_error')
        print('CV MSE:', -nmse_score)
        print('Stacker AVG MSE:', -nmse_score.mean(), 'Stacker AVG Score:', np.mean(np.divide(1, 1 + np.sqrt(-nmse_score))))

        self.stacker.fit(S_train, y)
        res = self.stacker.predict(S_predict)
        return res, S_train, S_predict
    

# stacking_mode1 = Ridge(alpha=0.008, copy_X=True, fit_intercept=False, solver='auto', random_state=2)
# 用SVR融合是一个关键的步骤
stacking_model = SVR(C=100, gamma=0.01, epsilon=0.01)
stacker = Stacker(5, stacking_model, regrs)
pred_stack, S_train_data, S_predict_data = stacker.fit_predict(all_X_train, all_y_train, sub_data)
                


##output
#
#df_result['score'] = pred_stack
#
## 对结果用固定值进行修改 b榜过拟合，可以删掉
#index = df_result[df_result['ID'].isin(special_missing_ID)].index
#df_result.loc[index, 'score'] = 0.379993053
#
#
#
#c_index = df_result[df_result['ID'].isin(cleaned_sub_data_ID)].index
#df_result.loc[c_index, 'score'] = pred_clean_stack
#
#df_result.to_csv('submit.csv', index=False, header=False)
#            
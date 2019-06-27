# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 19:18:02 2019

@author: Gehaha
"""
#导入sklearn 的数据集
import sklearn.datasets as sk_datasets
import sklearn.datasets.samples_generator as sk_sample_generator
import sklearn.model_selection as sk_model_selection
import sklearn.preprocessing as sk_preprocessing

#PCA
import sklearn.decomposition as sk_decomposition
#LDA
import sklearn.discriminant_analysis as sk_discriminant_analysis


#线性回归，使用最小二乘法实现，线性回归是回归问题，score使用R2系数作为评价标准
import sklearn.linear_model as sk_linear


#逻辑回归
import sklearn.linear_model as sk_linear

#朴素贝叶斯
import sklearn.naive_bayes as sk_bayes

#决策树
import sklearn.tree as sk_tree

#SVM支持向量机
import sklearn.svm as sk_svm


#神经网络
import sklearn.neural_network as sk_nn

#KNN(k-近邻算法)
import sklearn.neighbors as sk_neighbors

#采用KNN作为训练模型，采用十折交叉验证
import sklearn.model_selection as sk_model_selection


#模型的保存和载入
import sklearn.externals as sk_externals



iris = sk_datasets.load_iris()
iris_X = iris.data #导入数据
iris_y = iris.target #导入标签



#以分类问题创建样本数据集
X,y = sk_sample_generator.make_classification(n_samples = 6,n_features = 5,n_informative= 2,
                                              n_classes = 2,n_clusters_per_class=2,scale=1,
                                              random_state = 20)
for x_,y_ in zip(X,y):
    print(y_,end = ":")
    print(x_)
    
#以鸢尾花数据集为例进行划分
X_train,X_test,y_train,y_test = sk_model_selection.train_test_split(iris_X,iris_y,train_size=0.3,
                                                                    random_state = 20)
#基于mean和std的标准化
scaler = sk_preprocessing.StandardScaler().fit(X)
new_X = scaler.transform(X)
print("基于mean和std的标准化：",new_X)
#规范化到一定区间内feature_range为数据规范化的范围
scaler = sk_preprocessing.MinMaxScaler(feature_range=(0,1)).fit(X)
new_X = scaler.transform(X)
print("规范化到一定区间内：",new_X)
#数据的正则化
new_X = sk_preprocessing.normalize(X,norm= 'l2')
print('求二范数',new_X)



# PCA 实现
pca = sk_decomposition.PCA(n_components='mle',whiten=False,svd_solver='auto')
pca.fit(iris_X)
reduced_X = pca.transform(iris_X) #reduced_X为降维后的数据
print('PCA:')
print('降维后的各主成分的方差值占总方差值的比例:',pca.explained_variance_ratio_)
print('降维后的各主成分的方差值:',pca.explained_variance_)
print('降维后的特征数:',pca.n_components_) #n_components 指定希望PCA降维后的特征维度数目(>1)



# LDA(线性评价分析)
lda = sk_discriminant_analysis.LinearDiscriminantAnalysis(n_components=2)
lda.fit(iris_X,iris_y)
reduced_X = lda.transform(iris_X) #reduced_X为降维后的数据
print('LDA:')
print('LDA的数据中心点：',lda.means_)#中心点
print('LDA做分类时的正确率：',lda.score(X_test,y_test))#score是指分类的正确率
print('LDA降维后 特征空间的类中心：',lda.scalings_)#降维后特征空间的中心类



#线性回归
model = sk_linear.LinearRegression(fit_intercept=True,normalize=False,copy_X=True,n_jobs=1)
#fit_intercept:是否计算截距，False-模型没用截距，normalize：当fit_intercept设置为False时，该参数将被忽略。 
#如果为真，则回归前的回归系数X将通过减去平均值并除以l2-范数而归一化。
model.fit(X_train,y_train)
acc=model.score(X_test,y_test)#返回预测的确定系数R2
print('线性回归：')
print('截距：',model.intercept_)#输出截距
print('线性回归模型评价：',acc)



#逻辑回归是分类问题，score使用准确率做为评价指标
model=sk_linear.LogisticRegression(penalty='l2',dual=False,C=1.0,n_jobs=1,random_state=20,fit_intercept=True)
model.fit(X_train,y_train)#对模型进行训练
acc=model.score(X_test,y_test)#根据给定数据与标签返回正确率的均值
print('逻辑回归模型评价:',acc)
#参数说明：
#penalty：使用指定正则化项（默认：l2）
#dual: n_samples > n_features取False（默认）
#C：正则化强度的反，值越小正则化强度越大
#n_jobs: 指定线程数
#random_state：随机数生成器
#fit_intercept: 是否需要常量




# 朴素贝叶斯
#贝叶斯分类是一类分类算法的总称，这类算法均以贝叶斯定理为基础，故统称为贝叶斯分类。而朴素朴素贝叶斯分类是贝叶斯分类中最简单，也是常见的一种分类方法
model = sk_bayes.MultinomialNB(alpha=1.0,fit_prior=True,class_prior=None)#多项式分布的朴素贝叶斯
model = sk_bayes.BernoulliNB(alpha=1.0,binarize=0.0,fit_prior=True,class_prior=None)#伯努利分布的朴素贝叶斯
model = sk_bayes.GaussianNB() # 高斯分布的朴素贝叶斯
model.fit(X_train,y_train)
acc = model.score(X_test,y_test) #根据给定数据与标签返回正确率的均值
print('朴素贝叶斯（高斯分布）模型评价:',acc)
#参数说明：
#alpha：平滑参数
#fit_prior：是否要学习类的先验概率；false-使用统一的先验概率
#class_prior: 是否指定类的先验概率；若指定则不能根据参数调整
#binarize: 二值化的阈值，若为None，则假设输入由二进制向量组成




#决策树
model = sk_tree.DecisionTreeClassifier(criterion='entropy',max_depth=None,min_samples_leaf=1,
                                       max_features=None,max_leaf_nodes=None,min_impurity_decrease=0)
model.fit(X_train,y_train)
acc=model.score(X_test,y_test)#根据给定数据与标签返回正确率的均值
print('决策树模型评价：',acc)
#参数说明：
#criterion ：特征选择准则gini/entropy
#max_depth：树的最大深度，None-尽量下分
#min_samples_split：分裂内部节点，所需要的最小样本树
#min_samples_leaf：叶子节点所需要的最小样本数
#max_features: 寻找最优分割点时的最大特征数
#max_leaf_nodes：优先增长到最大叶子节点数
#min_impurity_decrease：如果这种分离导致杂质的减少大于或等于这个值，则节点将被拆分。



#SVM
model = sk_svm.SVC(C=1.0,kernel='rbf',gamma='auto')
model.fit(X_train,y_train)
acc = model.score(X_test,y_test)#根据给定数据与标签返回正确率的均值
print('SVM模型评价:',acc)
#参数说明：
#C：误差项的惩罚参数C
#kernel：核函数选择 默认：rbf(高斯核函数)，可选：‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
#gamma: 核相关系数。浮点数，If gamma is ‘auto’ then 1/n_features will be used instead.点将被拆分。



#神经网络
model = sk_nn.MLPClassifier(activation='tanh',solver='adam',alpha=0.0001,learning_rate='adaptive',learning_rate_init=0.001,max_iter=200)
model.fit(X_train,y_train)
acc = model.score(X_test,y_test)#根据给定数据与标签返回正确率的均值
print('神经网络模型评价:',acc)
#参数说明：
#hidden_layer_sizes: 元祖
#activation：激活函数 {‘identity’, ‘logistic’, ‘tanh’, ‘relu’}, 默认 ‘relu’
#solver ：优化算法{‘lbfgs’, ‘sgd’, ‘Adam’}
#alpha：L2惩罚(正则化项)参数
#learning_rate：学习率 {‘constant’, ‘invscaling’, ‘adaptive’}
#learning_rate_init：初始学习率，默认0.001
#max_iter：最大迭代次数 默认200



#KNN(K-近邻算法)
model = sk_neighbors.KNeighborsClassifier(n_neighbors=5,n_jobs=1)#KNN分类
model.fit(X_train,y_train)
acc = model.score(X_test,y_test) #根据给定数据与标签返回正确率的均值
print('KNN模型(分类)评价:',acc)
#参数说明：
#n_neighbors： 使用邻居的数目
#n_jobs：并行任务数


model = sk_neighbors.KNeighborsRegressor(n_neighbors=5,n_jobs=1)
model.fit(X_train,y_train)
acc = model.score(X_test,y_test)#返回预测的确定系数R2
print('KNN模型(回归)评价：',acc)
#参数说明：
#n_neighbors： 使用邻居的数目
#n_jobs：并行任务数
 

#KNN作为训练模型，采用十折交叉验证
model = sk_neighbors.KNeighborsClassifier(n_neighbors=5,n_jobs=1)#KNN分类
accs = sk_model_selection.cross_val_score(model,iris_X,y= iris_y,scoring=None,cv=10,
                                          n_jobs=1)
print('交叉验证结果:',accs)
#参数说明：
#model：拟合数据的模型
#cv ： 子集个数 就是k
#scoring: 打分参数 默认‘accuracy’、可选‘f1’、‘precision’、‘recall’ 、‘roc_auc’、'neg_log_loss'



#模型的保存和载入
sk_externals.joblib.dump(model,'model.pickle') #保存
model = sk_externals.joblib.load('model.pickle') #载入·


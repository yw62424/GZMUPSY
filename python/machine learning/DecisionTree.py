



from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split 
from sklearn import tree
from sklearn.metrics import accuracy_score
dc_tree = tree.DecisionTreeClassifier(criterion='entropy',min_samples_leaf=1)

iris=load_iris()
#split datas set 
#x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,random_state=2457,)
x_train,y_train=iris['data'],iris['target']
dc_tree.fit(x_train,y_train)
print(type(x_train))
print(x_train,y_train)
y_predict = dc_tree.predict(x_train)

accuracy = accuracy_score(y_train,y_predict)
print(accuracy)

import matplotlib as mpl
font2 = {'family' : 'SimHei',
'weight' : 'normal',
'size'   : 20,
}
mpl.rcParams['font.family'] = 'SimHei'
mpl.rcParams['axes.unicode_minus'] = False
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(20,20))
tree.plot_tree(dc_tree,filled='True',
               feature_names=['花萼长', '花萼宽', '花瓣长', '花瓣宽'],
               class_names=['山鸢尾', '变色鸢尾', '维吉尼亚鸢尾'])
plt.show()






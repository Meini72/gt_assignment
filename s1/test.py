from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.datasets import load_iris

# 加载数据集
iris = load_iris()

# 定义参数网格
param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [0.001, 0.01, 0.1, 1], 'kernel': ['rbf', 'linear']}

# 定义SVM模型
svc = SVC()

# 进行网格搜索
grid_search = GridSearchCV(svc, param_grid, cv=5)
grid_search.fit(iris.data, iris.target)

# 输出最佳参数组合
print("Best parameters: {}".format(grid_search.best_params_))

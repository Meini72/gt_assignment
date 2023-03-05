import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

# the parameter list for grid searching
parameters = {'nthread':[4], # num of thread
              'objective':['reg:linear'], # linear regression
              'learning_rate': [0.05], # learning rate
              'max_depth': [5, 6, 7], # max depth of the tree
              'min_child_weight': [4], # weight
              'subsample': [0.7], # sampling ratio
              'colsample_bytree': [0.7], # 
              'n_estimators': [500]} # 


# load the data
data = pd.read_csv('sourceData/car.data', header=None)

# specify columns for the source dataset
data.columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']

# codec the columns to convert to numeric values
le = LabelEncoder()
data['buying'] = le.fit_transform(data['buying'])
data['maint'] = le.fit_transform(data['maint'])
data['doors'] = le.fit_transform(data['doors'])
data['persons'] = le.fit_transform(data['persons'])
data['lug_boot'] = le.fit_transform(data['lug_boot'])
data['safety'] = le.fit_transform(data['safety'])
data['class'] = le.fit_transform(data['class'])



# segregate the features and the target 
X = data.drop(["buying"], axis=1)
y = data["buying"]


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# create the sgboost model
model = xgb.XGBClassifier()

# grid search for the best parameters
grid_search = GridSearchCV(model, parameters, n_jobs=5, cv=5, scoring='neg_mean_squared_error', verbose=2, refit=True)
grid_search.fit(X_train, y_train)

# output the best parameters
print("Best parameters: {}".format(grid_search.best_params_))

# create the XGboost classifier
xgb_model = xgb.XGBClassifier(**grid_search.best_params_)

# train the classifier
xgb_model.fit(X_train.values, y_train.values)

# evaluate the model
y_pred = xgb_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

#print(classification_report(y_test.values, y_pred))

# predict using the trained model
persons = data['persons'].value_counts().idxmax() # the feature 'persons' is missing so that use the most frequent value to fill up 
maint = 0 # high
doors = 2 # 4
lug_boot = 0 # big
safety = 0 # high
cclass = 1 # good

new_car = [[maint,doors,persons,lug_boot,safety,cclass]]
y_new_pred = xgb_model.predict(new_car)[0]

if y_new_pred==0:
	y_new_pred = 'high'
elif y_new_pred==1:
	y_new_pred = 'low'
elif y_new_pred==2:
	y_new_pred = 'med'
else:
	y_new_pred = 'v-high'
print("Predicted buying price for new car: ", y_new_pred)

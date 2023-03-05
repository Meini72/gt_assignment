import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

# load the data
data = pd.read_csv('sourceData/car.data', header=None)

# specify columns for the source dataset
data.columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']

param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [0.001, 0.01, 0.1, 1], 'kernel': ['rbf', 'linear']}

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
X = data.drop("buying", axis=1)
y = data["buying"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)


# create the SVC model
svc = SVC()

# grid search for the best parameters
grid_search = GridSearchCV(svc, param_grid, cv=5)
grid_search.fit(X_train.values, y_train.values)

# output the best parameters
print("Best parameters: {}".format(grid_search.best_params_))


# Train decision tree model using the best parameters
svm = SVC(**grid_search.best_params_)
svm.fit(X_train.values, y_train.values)

# evaluate the model
y_pred = svm.predict(X_test.values)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")


# predict using the trained model
persons = data['persons'].value_counts().idxmax() # the feature 'persons' is missing so that use the most frequent value to fill up 
maint = 0 # high
doors = 2 # 4
lug_boot = 0 # big
safety = 0 # high
cclass = 1 # good

new_car = [[maint,doors,persons,lug_boot,safety,cclass]]
y_new_pred = svm.predict(new_car)[0]

if y_new_pred==0:
	y_new_pred = 'high'
elif y_new_pred==1:
	y_new_pred = 'low'
elif y_new_pred==2:
	y_new_pred = 'med'
else:
	y_new_pred = 'v-high'
print("Predicted buying price for new car: ", y_new_pred)

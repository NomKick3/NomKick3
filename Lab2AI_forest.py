import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn import preprocessing
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns

knn_data_frame = pd.read_csv("3-titanic.csv", dtype="category")
knn_data_frame = knn_data_frame.dropna()
# knn_data_frame.pop("Parch")
# knn_data_frame.pop("Embarked")
# knn_data_frame.pop("SibSp")
knn = KNeighborsClassifier(n_neighbors=3)


le = preprocessing.LabelEncoder()
z = knn_data_frame.iloc[:,2:]
y = knn_data_frame.iloc[:,1]

for i in z:
    knn_data_frame[i] = le.fit_transform(knn_data_frame[i])


X = knn_data_frame.iloc[:,2:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42069) # 70% training and 30% test

rclf = RandomForestClassifier(n_estimators=69, random_state=42069,min_impurity_decrease=0.001,max_depth=5,)

clf=tree.DecisionTreeClassifier()
rclf.fit(X_train,y_train)

# feature_imp = pd.Series(rclf.feature_importances_,index=knn_data_frame.columns[2:]).sort_values(ascending=False)
# feature_imp
# # Creating a bar plot
# sns.barplot(x=feature_imp, y=feature_imp.index)
# # Add labels to your graph
# plt.xlabel('Feature Importance Score')
# plt.ylabel('Features')
# plt.title("Visualizing Important Features")
# plt.legend()
# plt.show()

y_pred=rclf.predict(X_test)

roc = roc_auc_score(y_test, rclf.predict_proba(X_test)[:,1]) # VET EJ VILKA X OCH y SOM ÄR RÄTT clf.predict_proba(X)[:, 1]

accracy = (accuracy_score(y_test, y_pred))
precision = precision_score(y_test, y_pred, average='macro')
recall= recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')
print(f'Accuracy:    {accracy*100}\nPrecision:   {precision*100}')
print(f'Recall:      {recall*100}\nF1:          {f1*100}\nROC:         {roc*100}')


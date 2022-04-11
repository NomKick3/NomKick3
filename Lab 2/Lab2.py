import pandas as pd
from sklearn.tree import DecisionTreeClassifier

load_data_frame = pd.read_csv("3-titanic.csv", dtype="category", sep=",")
male_surviviors = 0
female_surviviors = 0
for index, row in load_data_frame.iterrows():
    if row["Sex"] == "male" and row["Survived"] == "0":
        male_surviviors += 1
    elif row["Sex"] == "female" and row["Survived"] == "0":
        female_surviviors += 1
print(male_surviviors)
print(female_surviviors)
print(load_data_frame.describe())
print(load_data_frame.shape)
print()
load_data_frame.DecisionTree()
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

df = pd.read_csv("titanic-survival-prediction/data/titanic.csv")

# print(df.head())

# print(df.shape)
# print(df.info())
# print(df.describe())


df = df.drop("Cabin",axis=1)

df["Age"] = df["Age"].fillna(df["Age"].median())

# print(df.isnull().sum())

# print(df["Embarked"].mode())

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df = df.drop(["PassengerId","Name","Ticket"], axis=1)

df["Sex"] = df["Sex"].map({
    "male":0,
    "female":1
})
df["Embarked"] = df["Embarked"].map({
    "S":0,
    "C":1,
    "Q":2
})

X = df.drop("Survived",axis=1)
y = df["Survived"]

X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2,random_state = 42)
# print("X_train:",X_train.shape)
# print("X_test:",X_test.shape)
# print("y_train:",y_train.shape)
# print("y_test:",y_test.shape)

model = LogisticRegression(max_iter=1000)

model.fit(X_train,y_train)

joblib.dump(model,"titanic-survival-prediction/model/titanic_model.pkl")
print("Model saved successfully!")
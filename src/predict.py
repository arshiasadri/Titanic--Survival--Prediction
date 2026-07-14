import joblib
import pandas as pd


model = joblib.load("titanic-survival-prediction/model/titanic_model.pkl")

print("Model loaded successfully!")


pclass = int(input("Pclass (1-3): "))
sex = int(input("Sex (0=Male, 1=Female): "))
age = float(input("Age: "))
sibsp = int(input("Sibling / Spouses: "))
parch = int(input("Parents / Children: "))
fare = float(input("Fare: "))
embarked = int(input("Embarked (0=S, 1=C, 2=Q): "))


new_passenger = pd.DataFrame([{
    "Pclass": pclass,
    "Sex": sex,
    "Age": age,
    "SibSp": sibsp,
    "Parch": parch,
    "Fare": fare,
    "Embarked": embarked
}])


prediction = model.predict(new_passenger)


if prediction[0] == 1:
    print("Passenger Survived")
else:
    print("Passenger Did Not Survive")
# Titanic Survival Prediction

Predict whether a Titanic passenger would survive using Machine Learning.

A Machine Learning project that predicts whether a Titanic passenger would survive using Logistic Regression.

---

## Screenshot

![Application](images/demo.png)

## Features

- Data cleaning
- Handle missing values
- Encode categorical features
- Train Logistic Regression model
- Evaluate model performance
- Save trained model with Joblib
- Load trained model for prediction
- Predict survival for a new passenger from user input

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib

---

## Project Structure

```
titanic-survival-prediction/
│
├── data/
│   └── titanic.csv
│
├── model/
│   └── titanic_model.pkl
│
├── src/
│   ├── train.py
│   ├── predict.py
│   └── main.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/titanic-survival-prediction.git
```

Go to the project folder:

```bash
cd titanic-survival-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Train the Model

```bash
python src/train.py
```

This will:

- Load the dataset
- Clean the data
- Train the Logistic Regression model
- Save the trained model inside the `model` folder

---

## Predict Survival

```bash
python src/predict.py
```

Example:

```
Pclass (1-3): 3
Sex (0=Male, 1=Female): 0
Age: 22
Sibling / Spouses: 1
Parents / Children: 0
Fare: 7.25
Embarked (0=S, 1=C, 2=Q): 0
```

Output:

```
Passenger Did Not Survive
```

---

## Model Performance

- Algorithm: Logistic Regression
- Accuracy: **80%**

---

## Dataset

Titanic Survival Dataset

---

## Future Improvements

- Decision Tree
- Random Forest
- KNN
- Feature Engineering
- Hyperparameter Tuning
- Flask Web Application

---

## Author

**Your Name**

GitHub:
https://github.com/YOUR_USERNAME

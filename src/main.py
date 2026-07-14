import subprocess

while True :
    print("\n ===== Titanic Survival Prediction =====")
    print("1. Train Model")
    print("2. Predict Passenger")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1" :
        subprocess.run(["python","titanic-survival-prediction/src/train.py"])

    elif choice == "2" :
        subprocess.run(["python","titanic-survival-prediction/src/predict.py"]) 
    
    elif choice == "3" :
        print("Good Bye!")
        break
    else:
        print("Invalid choice!")

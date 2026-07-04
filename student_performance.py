import pandas as pd 
from sklearn.linear_model import LinearRegression

data = pd.read_csv("students.csv")
x = data[["Hours", "Attendance"]]
y = data["Marks"]
model = LinearRegression()
model.fit(x, y)

hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance: "))

prediction = model.predict([[hours, attendance]])
print("\nPredicted Marks:", round(prediction[0], 2))

if prediction[0] >= 75:
    print("Performance: Excellent")
elif prediction[0] >= 60:
    print("Performance: Good")
elif prediction[0] >= 40:
    print("Performance: Average")
else:
    print("Performance: Needs Improvement")

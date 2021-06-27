#Import Necessary Packages/Modules
from sklearn.linear_model import LinearRegression
import pandas as pd

#Load-in datasets
df = pd.read_csv("C:\\Users\\mihir\\OneDrive\\Desktop\\arasor.csv")

#PreProcessing
dummies_df = pd.get_dummies(df['CarModel'])
merged = pd.concat([df, dummies_df], axis="columns")
final = merged.drop(['CarModel', 'Mercedes Benz C class'], axis="columns")
X = final.drop(['Sell Price($)'], axis='columns')
y = final['Sell Price($)']

#Model Creation
model = LinearRegression()
model.fit(X,y)

#User Input
Mileage = int(input("What is the current mileage of the car?\n"))
Age = int(input("What is the current age of the car\n"))
Name = input("What car do you want to look at? The options are "
                 "(Audi A5, BMW X5, and Mercedes Benz C class)\n")

#Data Matching
while True:
    if Name == "Audi A5":
        parameter1 = 1
        parameter2 = 0
        break
    elif Name == "BMW X5":
        parameter1 = 0
        parameter2 = 1
        break
    elif Name == "Mercedes Benz C class":
        parameter1 = 0
        parameter2 = 0
        break
    else:
        Name = input("Please select a car from the three options.\n")

#Final Output
print("The expected price with the given parameters is:",model.predict([[Mileage, Age, parameter1, parameter2]]))

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

col_list = ['State','percAllPets','percDogOwners','percCatOwners']
csv = pd.read_csv('C:\\Users\\mihir\\Downloads\\csvData.csv', usecols=col_list)
doglist = []
catlist = []
doglist2 = []
catlist2 = []
for i in range(len(csv['percDogOwners'])):
    doglist.append(csv.iloc[i]['percDogOwners'])
    catlist.append(csv.iloc[i]['percCatOwners'])
for i in range(len(doglist)):
    doglist2.append(int(doglist[i]*100))
for i in range(len(catlist)):
    catlist2.append(int(catlist[i]*100))

doglist2 = np.array(doglist2)
doglist2 = np.reshape(doglist2, (50, 1))
catlist2 = np.array(catlist2)

#Regression
regressor = LinearRegression()
regressor.fit(doglist2, catlist2)
print(regressor.predict([[0]]))

#Print Graph
plt.scatter(catlist2, doglist2)
plt.show()

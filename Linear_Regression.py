#Basic linear regression


'''
from sklearn import linear_model
import seaborn as sns
import pandas as pd
reg=linear_model.LinearRegression()

X=[[13],[23],[32],[101],[21],[11]]
Y=[12,22,31,100,20,10]

reg.fit(X,Y)

print(reg.coef_)
print(reg.intercept_)

data=list(zip(X,Y))
print (data)
'''


#linear reg on csv file

import pandas as pd

#loading csv file
df=pd.read_csv(r'C:\Users\Admin\Contacts\Desktop\sangita\test.csv')

#slicing x and y from dataframe
df=df[['x','y']]

#define feature list x and target y
X=df[['x']]
Y=df[['y']]
print(X)

#trainTestSplit divides the data set in 75% training and 25% testing data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

xTrain,xTest,yTrain,yTest=train_test_split(X,Y)
lr=LinearRegression().fit(xTrain,yTrain)

#formula y= coef*x+intecept final weight and final bias which give best fit

coef=lr.coef_
print(coef)
intercept=lr.intercept_
print(intercept)

#ploting the data
import matplotlib.pyplot as plt
plt.scatter(X,Y)
plt.xlabel('x value')
plt.ylabel('y value')
plt.title('linear regression ')
plt.plot(X,coef*X+intercept,'-r')
plt.show()


#you can predict a value using
x=[[25.00]]
print("y =",lr.predict(x))
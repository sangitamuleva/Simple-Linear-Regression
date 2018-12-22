
#Basic linear regression



from sklearn import linear_model

reg=linear_model.LinearRegression()

X=[[13],[23],[32],[101],[21],[11]]
Y=[12,22,31,100,20,10]

#fit data into model 
#train the model

reg.fit(X,Y)

print(reg.coef_)
print(reg.intercept_)

data=list(zip(X,Y))
print (data)


#you can predict a value using predict method

print(reg.predict(11))




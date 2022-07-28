import pandas as pd
import matplotlib.pyplot as plt
import pickle
from pandas_profiling import ProfileReport
import numpy as np
import Widgets
from sklearn import linear_model



df= pd.read_csv("Advertising.csv")
# print(df)

# Override default pandas configuration
pd.options.display.width = 0
pd.options.display.max_rows = 10000
pd.options.display.max_info_columns = 10000

# #Create a profile report
# a = ProfileReport(df)
#
# #this will create a report in html format in the folder where project resides
# a.to_file('pandas_profile_test.html')

# #call widgets_create function to create the widgets
# Widgets.widgets_create(a)

view1 = df[['TV','Sales']]

x = df[['TV']]
y = df[['Sales']]
linear1 =linear_model.LinearRegression()
linear1.fit(x,y)

#Calculating the co-efficient value
m = linear1.coef_
#Calculating the Intercept values
c = linear1.intercept_
#formula is Y = mx + c
# Sales = m * TV value + c

print(f"Co-efficient value: {m}")
print(f"Linear Intercept value : {c}")

file = "linear1_reg.sav"
pickle.dump(linear1,open(file,'wb'))

#prediction based on TV value given by user and it will predict the sales values
sale_prediction = True
while (sale_prediction):
    tv_value = float(input("Enter the TV value for which you want to see the prediction  or enter 0 to exit: "))
    if tv_value == 0:
        sale_prediction = False
        print("Have a good Day")
    else:
        print(f"Sales of TV : {linear1.predict([[tv_value]])}")


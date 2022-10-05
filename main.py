import pandas as pd
import matplotlib.pyplot as plt
import pickle
from pandas_profiling import ProfileReport
import numpy as np
import Widgets
from sklearn import linear_model
import statsmodels.api as sm


# Loading the dataset Advertising
df= pd.read_csv("Advertising.csv")


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


def tv_linear_model(df):
    view1 = df[['TV','Sales']]
    #Printing View of TV and Sales
    print(view1)

    #Set the X value based on Feature and Labels
    x = df[['TV']] #Feature is TV
    y = df[['Sales']] #Label is Sales

    #Creating an object of LinearRegression
    linear =linear_model.LinearRegression()

    #Generating Linear Model based on Feature TV and label Sale and fitting the model
    linear.fit(x,y)

    #Calculating the co-efficient value
    m = linear.coef_
    #Calculating the Intercept values
    c = linear.intercept_

    # Linear Regression formula is Y = mx + c
    # Sales = m * TV value + c

    print(f"Co-efficient value: {m}")
    print(f"Linear Intercept value : {c}")

    #prediction based on TV value given by user and it will predict the sales values
    tv_sale_prediction = True
    while (tv_sale_prediction):
        tv_value = float(input("Enter the TV value for which you want to see the prediction  or enter 0 to exit: "))
        if tv_value == 0:
            tv_sale_prediction = False
            print("Have a good Day")
        else:
            print(f"Sales of TV : {linear.predict([[tv_value]])}")


    #dumping the model in pickle file which can be shared with others
    file = "linear1_reg.sav"
    pickle.dump(linear,open(file,'wb'))

    #we can load the model created by someone else and run the process
    saved_model = pickle.load(open(file,'rb'))

    # Once model is loaded we can use it for prediction
    # Prediction based on TV value given by user and it will predict the sales values
    tv_sale_prediction1 = True
    while (tv_sale_prediction1):
        tv_value1 = float(input("Enter the TV value for which you want to see the prediction from saved model or enter 0 to exit: "))
        if tv_value1 == 0:
            tv_sale_prediction1 = False
            print("Have a good Day")
        else:
            print(f"Sales of TV : {saved_model.predict([[tv_value1]])}")

    #To check accuracy of the model which is R**2
    score = "{:.2%}".format(linear.score(x,y))
    print(f"Accuracy of the model with just TV as Feature is : {score}")


# We will Include TV Radio as Feature Columns
def tv_radio_linear_model(df):
    x1 = df[['TV', 'Radio']]
    y1 = df[['Sales']]
    linear1 = linear_model.LinearRegression()
    linear1.fit(x1, y1)

    # Calculating the co-efficient value
    m1 = linear1.coef_
    # Calculating the Intercept values
    c1 = linear1.intercept_
    # Linear Regression formula is y = mx + c
    # Sales1 = m[0] * TV value + m[1]*radio value + m[2]  + c1

    print(f"Co-efficient value for x1 having TV and Radio: {m1}")
    print(f"Linear Intercept value for x1 having TV and  Radio: {c1}")

    #To check accuracy of the model which is R**2
    score1 = "{:.2%}".format(linear1.score(x1,y1))
    print(f"Accuracy of the model having TV and  Radio as feature columns : {score1}")


# We will Include TV Radio, Newspaper as Feature Columns
def tv_radio_newspaper_linear_model(df):
    x2 = df[['TV','Radio', 'Newspaper']]
    y2 = df[['Sales']]
    linear2 =linear_model.LinearRegression()
    linear2.fit(x2,y2)

    #Calculating the co-efficient value
    m2 = linear2.coef_
    #Calculating the Intercept values
    c2 = linear2.intercept_

    # Linear Regression formula is y = mx + c
    # Sales1 = m[0] * TV value +m[1]*radio value + m[2] * newspaper value + c1

    print(f"Co-efficient value for x1 having TV, Radio and Newspaper: {m2}")
    print(f"Linear Intercept value for x1 having TV, Radio and Newspaper: {c2}")

    #To check accuracy of the model which is R**2
    score2 = "{:.2%}".format(linear2.score(x2,y2))
    print(f"Accuracy of the model having TV, Radio and Newspaper as feature columns : {score2}")


sale_prediction = True
while (sale_prediction):

    model_input = int(input("Kindly let us know you want to see model based on which Features value\n1: Based on Feature TV"
                            "\n2: Based on TV and Radio \n3: Based on TV, Radio and Newspaper\n0: To Exit \nEnter Your choice :"))
    if model_input == 1:
        tv_linear_model(df)
    elif model_input == 2:
        tv_radio_linear_model(df)
    elif model_input == 3:
        tv_radio_newspaper_linear_model(df)
    else:
        print("Thank You")
        sale_prediction = False


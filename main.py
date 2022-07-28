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
c = linear1.intercept_
m = linear1.coef_
print(f"c: {c}")
print(f"m: {m}")
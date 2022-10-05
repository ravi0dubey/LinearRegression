import pandas as pd
import matplotlib.pyplot as plt
import pickle
from pandas_profiling import ProfileReport
import numpy as np
import Widgets
from sklearn import linear_model
import statsmodels.api as sm
# Loading the dataset Advertising
df1= pd.read_csv("Advertising.csv")
print(df1)
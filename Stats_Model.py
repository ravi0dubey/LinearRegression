import pandas as pd
import statsmodels.formula.api as smf
df1= pd.read_csv("Advertising.csv")
#print(df1.head(2))

# Ols is Ordinary Least Squared model
linear_model_2 = smf.ols(formula='Sales ~ TV',data=df1).fit()
print("\n\nPrinting Ordinary Least Squared Model using TV as Feature columns\n")
print(linear_model_2.summary())


# Ols is Ordinary Least Squared model
linear_model_2 = smf.ols(formula='Sales ~ TV + Radio',data=df1).fit()
print("\n\nPrinting Ordinary Least Squared Model using TV and Radio as Feature columns\n")
print(linear_model_2.summary())

# Ols is Ordinary Least Squared model
linear_model_2 = smf.ols(formula='Sales ~ TV + Radio + Newspaper',data=df1).fit()
print("\n\nPrinting Ordinary Least Squared Model using TV,Radio and Newspaper as Feature columns\n")
print(linear_model_2.summary())
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import *

password = "admin123"

df = pd.read_csv("C:/data/file.csv")

a = df.drop("price", axis=1)
b = df["price"]

def fun(x):
    if x > 0:
        return x * 2
    else:
        return x * 2

model = LinearRegression()

try:
    model.fit(a, b)
except:
    pass

if False:
    print("dead code")

eval("print('hello')")

# bad_ml.py

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import *

# hardcoded path
df = pd.read_csv("C:/data/file.csv")

# bad variable names
a = df.drop("price", axis=1)
b = df["price"]

# duplicate code
def fun(x):
    if x > 0:
        return x * 2
    else:
        return x * 2

# empty exception
model = LinearRegression()

try:
    model.fit(a, b)
except:
    pass

# hardcoded password
password = "admin123"

# dead code
if False:
    print("never runs")

print("done")

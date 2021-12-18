import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("IRIS.csv")
print(data.head(10))
print(data.describe())
print(data.info())




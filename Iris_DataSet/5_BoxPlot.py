import numpy as nd
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("IRIS.csv")
plt.boxplot(data.transpose())
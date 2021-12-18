import numpy as nd
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("IRIS.csv")
plt.plot(data.petal_length, data["sepal_length"],"r--")
plt.title('PLOTTING IRIS DATA SET')
plt.show()



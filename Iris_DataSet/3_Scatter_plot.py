import numpy as nd
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("IRIS.csv")
data.plot(kind="scatter",x="sepal_length",y="petal_length")
plt.title('Scatter Plot')
plt.grid()
plt.show()
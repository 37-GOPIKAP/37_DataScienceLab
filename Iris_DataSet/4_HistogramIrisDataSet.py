import numpy as nd
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("IRIS.csv")
x=data["sepal_length"]
plt.hist(x,bins=20,color="green")
plt.title('Sepal Length')
plt.xlabel("Sepal_Length in cm")
plt.ylabel("count")
plt.grid()
plt.show()

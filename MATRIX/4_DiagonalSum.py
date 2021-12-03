#calculate the sum of diagonal elements of a numpy array.
import numpy as np
newarray = np.array([[12, 25],[30, 32]])
print("\nMatrix :\n",newarray)
trace = np.trace(newarray)
print("Sum of diagonal elements of given matrix:",trace)

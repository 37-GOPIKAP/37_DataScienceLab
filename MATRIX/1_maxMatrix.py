#python program to get the maximum and minimum value  from the given matrix using numpy.
import numpy as np
arr = np.matrix('[6, 71; 1, 3]')
maxEle=np.max(arr)
minEle=np.min(arr)
    
print("Maximum value:",maxEle)
print("Minimum value:",minEle)
#find the sum of values in a matrix.
import numpy as np
Matrix= np.matrix('[[[4,7,6];[ 12, 3,9];[7,2,6]]]')
print("\n Matrix :\n", Matrix)
SumMatrix = Matrix.sum()
print("Sum of values :",SumMatrix)

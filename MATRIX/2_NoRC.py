#find the no.of rows and colums of a given matrix using numpy
import numpy as np
matrix= np.array([[1, 2, 3, 4, 5, 6] ,[7, 8, 9, 10, 11, 12]])
print("\nMatrix A:\n",matrix)
rows,columns=matrix.shape
Dimension=matrix.shape
print("Dimension of the matrix:",Dimension)
print("No.of rows:", rows)
print("No.of columns:",columns)
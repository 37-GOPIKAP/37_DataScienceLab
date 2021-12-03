import numpy as np
A = np.array([[2, 4], [5, -6]])
B = np.array([[9, -3], [3, 6]])
print("\nMatrix A=\n",A)
print("\nMatrix B=\n",B)
C = np.add(A,B) 
D=np.subtract(A,B)
E=np.divide(A,B )    # element wise addition
print("\nSum of matrices:\n",C)
print("\nDifference of matrices:\n",D)
print("\nMatrix A divides B:\n",E)

import numpy as np

R = int(input()) # rows
C = int(input()) # columns

# output prints 2D array where elements are modified from a base array of 1s using the described alternating pattern
matrix = np.ones((R, C), dtype = float)
row, column = np.indices((R, C))
# np.indices is used to get the index of each of the element in the matrix
matrix[column % 2 == 1] = 0
print(matrix)

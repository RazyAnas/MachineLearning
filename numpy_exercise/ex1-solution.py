import numpy as np

matrix = np.zeros((R, C), dtype=int) # first generate a zero matrix of the size asked

# then change the zeroes matrix to the desired numbers as asked in the question
for i in range(R):
    for j in range(C):
        matrix[i][j] = i*j
print("Generated 2D Matrix:")
print(matrix)

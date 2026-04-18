import numpy as np

num_dimensions = int(input())

arr = list(map(int, input().split()))

matrix = np.array(arr, ndmin=num_dimensions)

print("Shape of the array:", matrix.shape)

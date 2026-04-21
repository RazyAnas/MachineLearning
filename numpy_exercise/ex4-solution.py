'''
The first line contains two space-separated integers, n and m, representing the number of rows and columns of the array, respectively.
The next n lines contain m space-separated integers, each representing the elements of the array.
'''
import numpy as np

input1 = list(map(int, input().split()))
n = input1[0] # rows
m = input1[1] # columns
lists = []
for _ in range(n):
    row = list(map(int, input().split()))
    lists.append(row)

'''
The first line of output prints "Sorted based on last axis(1):" followed by the array sorted row-wise.
The second line prints "Sorted flattened array:" followed by the flattened and sorted array.
The third line prints "Sorted based on axis 0:" followed by the array sorted column-wise.
'''

# axis 0 = columns
# axis 1 = rows

matrix = np.array(lists).reshape(n,m)
matrix_axis1 = np.copy(matrix)
matrix_axis1 = np.sort(matrix_axis1, axis=1, kind=None, order=None)

print("Sorted based on last axis(1): ")
print(matrix_axis1)

matrix_flattened = np.copy(matrix).reshape(1, np.size(matrix))
matrix_flattened = np.sort(matrix_flattened)

print("Sorted flattened array:")
print(matrix_flattened)

matrix_axis0 = np.copy(matrix)
matrix_axis0 = np.sort(matrix_axis0, axis = 0)

print("Sorted based on axis 0: ")
print(matrix_axis0)

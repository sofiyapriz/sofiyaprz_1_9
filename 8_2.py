import numpy as np

N = int(input("Введіть розмір матриці N: "))

elements = np.arange(N * N, 0, -1)

matrix = elements.reshape(N, N)

print("Матриця розміру N x N, заповнена елементами у порядку спадання:")
print(matrix)

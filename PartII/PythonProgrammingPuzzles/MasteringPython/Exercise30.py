import random
matrix = [[random.random() for _ in range(4)] for _ in range(3)]
matrix[0], matrix[1] = matrix[1], matrix[0]
print(matrix)

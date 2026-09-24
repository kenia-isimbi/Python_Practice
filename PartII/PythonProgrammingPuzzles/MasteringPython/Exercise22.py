import random
matrix = [[random.random() for _ in range(4)] for _ in range(4)]
diagonal_elements = [matrix[i][i] for i in range(4)]
print(diagonal_elements)
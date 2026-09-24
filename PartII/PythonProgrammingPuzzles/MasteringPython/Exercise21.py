import random
matrix = [[random.random() for _ in range(4)] for _ in range(3)]
row_means = [sum(row) / len(row) for row in matrix]
print(row_means)
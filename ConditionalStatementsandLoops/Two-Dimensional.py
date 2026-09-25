m = int(input("Input number of rows: "))
n = int(input("Input number of columns: "))

matrix = [[i * j for j in range(n)] for i in range(m)]

print(matrix)

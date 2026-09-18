def sum_three(x, y, z):
    if x == y or x == z or y == z:
        return 0
    else:
        return x + y + z

print(sum_three(2, 1, 2))
print(sum_three(3, 2, 2))
print(sum_three(2, 2, 2))
print(sum_three(1, 2, 3))
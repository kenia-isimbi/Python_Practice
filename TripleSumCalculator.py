def sum_triple(x, y, z):
    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum

print(sum_triple(1, 2, 3))
print(sum_triple(3, 3, 3))

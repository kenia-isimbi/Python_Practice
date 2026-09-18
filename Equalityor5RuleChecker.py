def sum_two(a, b):
    if a == b or a + b == 5 or a - b == 5:
        return True

    else:
        return False

print(sum_two(2, 3))
print(sum_two(7, 7))
print(sum_two(20, 15))
print(sum_two(3, 8))
print(sum_two(4, 90))

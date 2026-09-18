def calculate_difference(n):
    if n > 17:
        return 2 * abs(n - 17)
    else:
        return abs(n - 17)

print(calculate_difference(23))  
print(calculate_difference(14))  
print(calculate_difference(17))  

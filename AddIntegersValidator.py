def add_only_integers(obj1, obj2):
    if isinstance(obj1, int) and isinstance(obj2, int):
        return obj1 + obj2
    else:
        return "Error: Both objects must be integers!"

print(add_only_integers(43, 80))
print(add_only_integers(6, 67.1))
print(add_only_integers('say', 'Hello'))
print(add_only_integers(4, 12))

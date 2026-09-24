lst = [1, 5, 6, 8, 12, 15, 10, 11]
count_within_range = sum(5 <= x <= 12 for x in lst)
print(count_within_range)
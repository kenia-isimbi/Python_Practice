lst = [2, 5, 10, 8, 3]
min_val, max_val = min(lst), max(lst)
normalized_list = [(x - min_val) / (max_val - min_val) for x in lst]
print(normalized_list)
lst = [1, 2, 5, 7, 9, 26, 12, 11, 10, 11, 4, 13]
replaced_lst = [-1 if x % 2 != 0 else x for x in lst]
print(replaced_lst)
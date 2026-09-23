lst = [2, 5, 6, 9, 21, 12, 11, 10, 13]
replaced_lst = [-x if x % 2 == 0 else x for x in lst]
print(replaced_lst)
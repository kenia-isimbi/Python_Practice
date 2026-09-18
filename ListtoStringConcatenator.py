def concatenate_list_data(lst):
    result = ''

    for element in lst:
        result += str(element)

    return result

print(concatenate_list_data([3, 4, 6, 8]))


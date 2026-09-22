def check_occurences(nums):
        return nums.count(19) == 2 and nums.count(5) >= 3

test_1 = [2, 5, 6, 20, 19, 19, 6]
test_2 = [5, 6, 4, 5, 19, 2, 5, 19, 7]

print(f" list: {test_1} -> {check_occurences(test_1)}")
print(f" list: {test_2} -> {check_occurences(test_2)}")
def test(nums):
    ctr = 0

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            ctr += 1
    return ctr

nums = [1, 4, 7, 9, 11, 5]
print("Original list of numbers:", nums)
print("Count the numbers of the said list that are greater than the previous number!")
print(test(nums))

nums = [1, 3, 3, 2, 2]
print("\nOriginal list of numbers:", nums)
print("Count the numbers of the said list that are greater than the previous number!")
print(test(nums))

nums = [4, 3, 2, 1]
print("\nOriginal list of numbers:", nums)
print("Count the numbers of the said list that are greater than the previous number!")
print(test(nums))

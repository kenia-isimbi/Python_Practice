def test(nums):
      return nums[0] % 9 == nums[1] % 9 == nums[2] % 9

nums = [13, 4, 22]
print("Original list of numbers:", nums)
print("Check sum of the digits in each number of the said list is equal or not!")
print(test(nums))

nums = [-13, 4, 22]
print("\nOriginal list of numbers:", nums)
print("Check sum of the digits in each number of the said list is equal or not!")
print(test(nums))

nums = [45, 63, 90]
print("\nOriginal list of numbers:", nums)
print("Check sum of the digits in each number of the said list is equal or not!")
print(test(nums))

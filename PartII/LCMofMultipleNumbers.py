from functools import reduce

def test(nums):
    return reduce(lambda x, y: lcm(x, y), nums)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

nums = [4, 6, 8]
print("Original list elements:")
print(nums)
print("LCM of the numbers of the said array of positive integers: ", test(nums))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nOriginal list elements:")
print(nums)
print("LCM of the numbers of the said array of positive integers: ", test(nums))

nums = [48, 72, 108]
print("\nOriginal list elements:")
print(nums)
print("LCM of the numbers of the said array of positive integers: ", test(nums))

# Function to check if the square root of the first number is equal to the cube root of the second number.
def test(nums):
    # Extract the two numbers from the list.
    x = nums[0]
    y = nums[1]

    # Calculate the square root of y.
    t = y**0.5

    # Check if the square of the square root is equal to the cube of the first number.
    if(x == t*t*t):
        return True
    else:
        return False         

# Example usage of the function with different lists of positive numbers.
nums = [8, 4]
print("Original list of positive numbers:")
print(nums)
print("Check square root and cube root of the said numbers:")
print(test(nums))

nums = [64, 16]
print("\nOriginal list of positive numbers:")
print(nums)
print("Check square root and cube root of the said numbers:")
print(test(nums))

nums = [64, 36]
print("\nOriginal list of positive numbers:")
print(nums)
print("Check square root and cube root of the said numbers:")
print(test(nums))

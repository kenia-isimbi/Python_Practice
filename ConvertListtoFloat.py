# Define a list 'nums' containing string representations of decimal numbers.
nums = ['0.49', '0.54', '0.54', '0.54', '0.54', '0.54', '0.55', '0.54', '0.54', '0.54',
        '0.55', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54']

# Display the original list.
print("Original list:")
print(nums)

# Display a message indicating the next section.
print("\nList of Floats:")

# Create an empty list 'nums_of_floats' to store float representations of the decimal numbers.
nums_of_floats = []

# Iterate through each item in the original list.
for item in nums:
    # Convert each string representation to a float and append it to 'nums_of_floats'.
    nums_of_floats.append(float(item))

# Display the list of floats.
print(nums_of_floats)

# Prompt the user for input and convert it to an integer.
n = int(input("Input an integer: "))

# Calculate the sum of the first 'n' positive integers using the built-in 'sum' function and 'range'.
result = sum(range(n+1))

# Print the result, indicating the sum of the first 'n' positive integers.
print("Sum of the first", n, "positive integers:", result)

# Define a function 'add_without_plus_operator' that performs addition without using the '+' operator.
def add_without_plus_operator(a, b):
    # Continue the loop until the carry (b) becomes zero.
    while b != 0:
        # Calculate the bitwise AND of 'a' and 'b'.
        data = a & b
        # XOR 'a' and 'b' to get the sum without considering carry.
        a = a ^ b
        # Left shift the carry by 1 position.
        b = data << 1
    # Return the final sum.
    return a

# Test the function with different inputs and print the results.
print(add_without_plus_operator(2, 10))
print(add_without_plus_operator(-20, 10))
print(add_without_plus_operator(-10, -20))

# Define a function 'repeat_times' that repeatedly subtracts the sum of the digits
# of a number from the number until it becomes non-positive, and then returns the result.
def repeat_times(n):
    # Convert the input number 'n' to a string for digit manipulation.
    n_str = str(n)
    
    # Continue the loop while 'n' is greater than 0.
    while n > 0:
        # Subtract the sum of the digits of 'n' from 'n'.
        n -= sum([int(i) for i in list(n_str)])
        
        # Update 'n_str' with the string representation of the updated 'n'.
        n_str = list(str(n))
    
    # Return the final value of 'n'.
    return n

# Test the 'repeat_times' function with different values of 'n' and print the results.
print(repeat_times(9))
print(repeat_times(20))
print(repeat_times(110))
print(repeat_times(5674))

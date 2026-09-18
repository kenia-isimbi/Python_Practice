# Define a function 'test' that takes a string 's' as input.
def test(s):
    try:
        # Try to convert the input string to an integer.
        return int(s)
    except ValueError:
        # If the conversion to an integer raises a ValueError (i.e., it's not an integer), 
        # then try to convert the string to a floating-point number (float).
        return float(s)

# Call the 'test' function with different input values and print the results.
print(test('12'))       
print(test('233.12'))   

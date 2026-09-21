# Import sys and re modules
import sys
import re

# Define a function named 'test' that takes a string 'stri' as a parameter
def test(stri):
    # Print statement to instruct the user to input text and numeric values (terminate with )
    print("Input some text and numeric values ( to exit):")
    
    # Use regex to find all numeric values in the input string and sum them
    numeric_sum = sum(map(int, re.findall(r"[0-9]{1,5}", stri)))
    
    # Print the sum of the numeric values
    print("Sum of the numeric values: ", numeric_sum)

# Test the 'test' function with different input strings
print(test("sd1fdsfs23 dssd56"))
print(test("15apple2banana"))
print(test("flowers5fruit5"))

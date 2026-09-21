# Import the 'deque' class from the 'collections' module and the 're' module for regular expressions.
from collections import deque
import re

# Define operators, parentheses, and operator priorities.
__operators__ = "+-/*"
__parenthesis__ = "()"
__priority__ = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
}

# Define a function 'test_higher_priority' to compare the priorities of two operators.
def test_higher_priority(operator1, operator2):
    # Return True if the priority of 'operator1' is higher than or equal to 'operator2'.
    return __priority__[operator1] >= __priority__[operator2]

# Test the function with different operator pairs and print the results.
print(test_higher_priority('*','-'))
print(test_higher_priority('+','-'))
print(test_higher_priority('+','*'))
print(test_higher_priority('+','/'))
print(test_higher_priority('*','/'))

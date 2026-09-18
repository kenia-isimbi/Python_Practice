# Import the cProfile module, which provides a way to profile Python code.
import cProfile
# Define a function named 'sum'.
def sum():
   # Print the result of adding 1 and 2 to the console.
   print(1 + 2)
# Use cProfile to profile the 'sum' function.
cProfile.run('sum()')

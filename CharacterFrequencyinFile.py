# Import necessary modules.
import collections  # Import the 'collections' module for Counter.
import pprint  # Import 'pprint' for pretty printing.

# Get the file name as input from the user.
file_input = input('File Name: ')

# Open the file in read mode using a 'with' statement to ensure proper handling of resources.
with open(file_input, 'r') as info:
    # Read the contents of the file and count the occurrences of each uppercase character.
    count = collections.Counter(info.read().upper())
    # Use 'pprint' to format the count output for better readability.
    value = pprint.pformat(count)

# Print the formatted count of characters in the file.
print(value)

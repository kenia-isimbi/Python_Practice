# Import the 'os' module to access operating system-related functionality, including environment variables.
import os

# Iterate through all environment variables and their values using the 'os.environ.items()' method.
for item, value in os.environ.items():
    # Print the environment variable name and its corresponding value.
    print('{}: {}'.format(item, value))

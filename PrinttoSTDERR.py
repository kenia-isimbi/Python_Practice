import sys

# 1. The standard way using the print() function
print("Error: Something went wrong!", file=sys.stderr)

# 2. An alternative way using the write() method
sys.stderr.write("Critical Error: Process failed!\n")

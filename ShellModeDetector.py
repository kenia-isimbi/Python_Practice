# Import the 'struct' module, which provides pack and unpack functions for working with variable-length binary data.
import struct

# Use the 'calcsize' function to determine the size (in bytes) of the C int type for the current platform.
# The format string "P" is used to represent the C void pointer type, and multiplying it by 8 gives the size in bits.
# The result will be 32 for 32-bit platforms and 64 for 64-bit platforms.
print(struct.calcsize("P") * 8)

import re

def test(txt):
    # Use regular expressions to find all consecutive sequences of zeroes and ones and compare their lengths.
    return [len(i) for i in re.findall('0+', txt)] == [len(i) for i in re.findall('1+', txt)]

str1 = "001011"
print("\nOriginal sequence:", str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))

str1 = "01010101"
print("\nOriginal sequence:", str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))

str1 = "00"
print("\nOriginal sequence:", str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))

str1 = "000111000111"
print("\nOriginal sequence:", str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))

str1 = "00011100011"
print("\nOriginal sequence:", str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))

str1 = "0011101"
print("\nOriginal sequence:", str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))

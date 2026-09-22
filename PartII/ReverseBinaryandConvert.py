def test(n):
    reversed_binary = bin(n)[::-1][:-2]

    return int(reversed_binary, 2)

n1 = 13
print("Original number: ", n1)
print("Reverse the binary representation of the said integer and convert it into an integer:\n", test(n1))

n2 = 145
print("\nOriginal number: ", n2)
print("Reverse the binary representation of the said integer and convert it into an integer:\n", test(n2))

n3 = 1342
print("\nOriginal number: ", n3)
print("Reverse the binary representation of the said integer and convert it into an integer:\n", test(n3))

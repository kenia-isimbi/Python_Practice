def Largest_Smallest_digit(n):
    largest_digit = 0
    smallest_digit = 9

    while (n):
        digit = n % 10

        largest_digit = max(digit, largest_digit)

        smallest_digit = min(digit, smallest_digit)

        n = n // 10

    return largest_digit, smallest_digit

n = 9387422
print("Original Number:", n)
result = Largest_Smallest_digit(n)
print("Largest Digit of the said number:", result[0])
print("Smallest Digit of the said number:", result[1])

n = 500
print("\nOriginal Number:", n)
result = Largest_Smallest_digit(n)
print("Largest Digit of the said number:", result[0])
print("Smallest Digit of the said number:", result[1])

n = 231548
print("\nOriginal Number:", n)
result = Largest_Smallest_digit(n)
print("Largest Digit of the said number:", result[0])
print("Smallest Digit of the said number:", result[1])

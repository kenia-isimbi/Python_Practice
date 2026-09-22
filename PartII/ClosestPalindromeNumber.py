def test(n):
    x = n
    y = n
    
    while True:
        
        if str(x) == str(x)[::-1]:
            
            return x
        
        x -= 1
        
        if str(y) == str(y)[::-1]:
            
            return y
        y += 1


n1 = 120
print("Original number: ", n1)
print("Closest Palindrome number of the said number: ", test(n1))


n2 = 321
print("\nOriginal number: ", n2)
print("Closest Palindrome number of the said number: ", test(n2))


n3 = 43
print("\nOriginal number: ", n3)
print("Closest Palindrome number of the said number: ", test(n3))


n4 = 1234
print("\nOriginal number: ", n4)
print("Closest Palindrome number of the said number: ", test(n4))

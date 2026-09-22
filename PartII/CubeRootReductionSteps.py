# Function to count the number of times a positive integer can be cubed until it is less than 3.
def test(n):
    ctr = 0
    
    while n >= 3:
        n = n ** (1./3.)
        
        ctr = ctr + 1
    
    return 'Not a positive number!' if n < 0 else ctr

n = int(input("Input a positive integer:"))

print(test(n))

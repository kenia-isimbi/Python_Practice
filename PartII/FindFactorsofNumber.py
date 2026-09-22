from functools import reduce

def test(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


n = 1
print("\nOriginal Number:", n)
print("Factors of the said number:", test(n))
n = 12
print("\nOriginal Number:", n)
print("Factors of the said number:", test(n))
n = 100
print("\nOriginal Number:", n)
print("Factors of the said number:", test(n))

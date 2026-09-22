def test(txt):

    result_str = ""
    s = True
    for i in txt:
        result_str += i.upper() if s else i.lower()
        
        if i.isalpha():
            s = not s
    
    return result_str

str1 = "Python Exercises"
print("Original string: ", str1)
print("After alternating the case of each letter of the said string:")
print(test(str1))

str1 = "C# is used to develop web apps, desktop apps, mobile apps, games and much more."
print("\nOriginal string: ", str1)
print("After alternating the case of each letter of the said string:")
print(test(str1))

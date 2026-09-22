def test(txt):
    return ' '.join(i[::-1] if len(i) % 2 else i for i in txt.split())


text1 = "The quick brown fox jumps over the lazy dog"
print("Original string:")
print(text1)
print("Reverse all the words of the said string which have odd length:")
print(test(text1))

text2 = "Python Exercises"
print("\nOriginal string:")
print(text2)
print("Reverse all the words of the said string which have odd length:")
print(test(text2))

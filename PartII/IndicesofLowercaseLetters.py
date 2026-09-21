def test(text):
   return [x for x in range(len(text)) if text[x].islower()]

text = "Python"

print("Original string:", text)

print("Indices of all lower case letters of the said string:\n", test(text))


text = "JavaScript"
# Print the original text.
print("\nOriginal string:", text)

print("Indices of all lower case letters of the said string:\n", test(text))

text = "PHP"

print("\nOriginal string:", text)
print("Indices of all lower case letters of the said string:\n", test(text))

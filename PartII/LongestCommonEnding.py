def test(str1, str2):
    for i in range(len(str2)):
        while str2[i:] in str1 and str2[-1] == str1[-1]:
            return str2[i:]
    
    return ""

str1_1 = "running"
str2_1 = "ruminating"
print("Original strings: " + str1_1 + "  " + str2_1)
print("Common ending between said two strings: " + test(str1_1, str2_1))

str1_2 = "thisisatest"
str2_2 = "testing123testing"
print("\nOriginal strings: " + str1_2 + "  " + str2_2)
print("Common ending between said two strings: " + test(str1_2, str2_2))

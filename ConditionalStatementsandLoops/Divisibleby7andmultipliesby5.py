matching_numbers = []
for i in range(1500, 2701):
    if (i % 7 == 0) and (i % 5 == 0):
         matching_numbers.append(i)

print("Numbers divisible by 7 and multiples of 5 :")
print(matching_numbers)
def check_valid_list(nums):
    no_consecutive = all(nums[i] != nums[i + 1] for i in range(19))
    four_distinct = len(set(nums[:20])) == 4
    return no_consecutive and four_distinct

generated_list = [1, 2, 3, 4] * 5

print("Generated List (first 20 entries):")
print(generated_list)

print("\nDoes the list satisfy the conditions?")
print(check_valid_list(generated_list))

def check_prefix_sum_matches_index(nums: list[int]) -> bool:
    
    running_sum = 0
    
    for i, num in enumerate(nums, start=1):
        running_sum += num
        if running_sum != i:
            return False
            
    return True

def check_prefix_sum_optimized(nums: list[int]) -> bool:
    
    if not nums:
        return False
    return all(num == 1 for num in nums)


test_list_true = [1, 1, 1, 1, 1]
test_list_false = [1, 1, 3, 1, 1]
test_list_empty = []

print("Running Sum Approach:")
print(f"Is {test_list_true} valid? -> {check_prefix_sum_matches_index(test_list_true)}")
print(f"Is {test_list_false} valid? -> {check_prefix_sum_matches_index(test_list_false)}")

print("\nOptimized All-Ones Approach:")
print(f"Is {test_list_true} valid? -> {check_prefix_sum_optimized(test_list_true)}")
print(f"Is {test_list_false} valid? -> {check_prefix_sum_optimized(test_list_false)}")

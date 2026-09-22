def test_list(nums: list[int]) -> bool:
    if len(nums) != 100:
        return False
    
    if any(x < 0 or x > 999 for x in nums):
        return False
        
    sorted_nums = sorted(nums)
    
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] - sorted_nums[i - 1] != 10:
            return False
            
    return True

valid_list = list(range(0, 1000, 10))
print("Valid List Result:", test_list(valid_list))  
invalid_list_step = list(range(0, 1000, 20))
print("Invalid Step Result:", test_list(invalid_list_step))  

invalid_list_bounds = list(range(10, 1010, 10))
print("Invalid Bounds Result:", test_list(invalid_list_bounds))  

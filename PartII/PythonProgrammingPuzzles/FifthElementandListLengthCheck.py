def check_list_conditions(nums):
    if len(nums) == 8:
        
        fifth_element = nums[4]
        
        if nums.count(fifth_element) == 3:
            return True
            
    return False

# Test cases
print(check_list_conditions([19, 19, 15, 5, 5, 5, 1, 2]))  
print(check_list_conditions([19, 15, 5, 7, 5, 5, 2]))     
print(check_list_conditions([11, 12, 14, 13, 14, 13, 15, 14]))

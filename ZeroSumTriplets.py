def three_sum(nums):
    # Initialize an empty list to store the results.
    result = []
    # Sort the input list in ascending order.
    nums.sort()
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
         l, r = i + 1, len(nums) - 1
        
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                # Found a triplet with the sum equal to zero, add it to the result.
                result.append((nums[i], nums[l], nums[r]))
                
                # Remove duplicates in the left and right pointers.
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                
                # Move the pointers towards the center.
                l += 1
                r -= 1
    
    # Return the final result containing unique triplets.
    return result

# Create a list of numbers.
x = [1, -6, 4, 2, -1, 2, 0, -2, 0]

# Call the 'three_sum' function with the list and print the result.
print(three_sum(x))


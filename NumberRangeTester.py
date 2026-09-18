def is_within_range(num):
    """
    Returns True if the number is within 100 of 1000 or 2000, 
    otherwise returns False.
    """
    return (abs(num - 1000) <= 100) or (abs(num - 2000) <= 100)

# Test cases
print(is_within_range(30))   
print(is_within_range(1050))  
print(is_within_range(1900))  
print(is_within_range(1500))  
print(is_within_range(2150))  

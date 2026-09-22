def check_proper_substring(str_list):
    if len(str_list) < 2:
        return False
        
    nth_minus_1 = str_list[-2]
    nth_str = str_list[-1]
    
    return nth_minus_1 in nth_str and len(nth_minus_1) < len(nth_str)

list1 = ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
print(f"List 1: {check_proper_substring(list1)}")  

list2 = ['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
print(f"List 2: {check_proper_substring(list2)}")  

list3 = ['a', 'abb', 'sfsdf', 'sfsdf']
print(f"List 3: {check_proper_substring(list3)}")  

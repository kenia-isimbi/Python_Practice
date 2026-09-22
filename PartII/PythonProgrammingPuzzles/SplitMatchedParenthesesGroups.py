def split_parentheses_groups(input_string):
    result = []
    current_group = []
    balance = 0
    
    for char in input_string:
        # Ignore all whitespace characters
        if char.isspace():
            continue
            
        if char == '(':
            balance += 1
            current_group.append(char)
        elif char == ')':
            balance -= 1
            current_group.append(char)
            
        # When balance hits 0, a perfectly matched group is completed
        if balance == 0 and current_group:
            result.append("".join(current_group))
            current_group = []
            
    return result

# --- Test Cases ---
if __name__ == "__main__":
    # Test Case 1
    str1 = "( ()) ((()()())) (()) ()"
    print(f"Input 1:  {str1}")
    print(f"Output 1: {split_parentheses_groups(str1)}\n")

    # Test Case 2
    str2 = "() (( ( )() ( )) ) ( ())"
    print(f"Input 2:  {str2}")
    print(f"Output 2: {split_parentheses_groups(str2)}")

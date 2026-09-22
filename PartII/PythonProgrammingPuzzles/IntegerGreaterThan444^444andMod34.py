def check_integer(num: int) -> bool:

    return num > 4**4 and num % 34 == 4

try:
    user_input = int(input("Enter an integer: "))
    result = check_integer(user_input)
    print(result)
except ValueError:
    print("Please enter a valid integer.")

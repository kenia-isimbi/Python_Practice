def convert_temperature(temp_str):
    degree = int(temp_str[:-1])
    convention = temp_str[-1].upper()

    if convention == "C":
        result = int(round((9 * degree) / 5 + 32))
        print(f"{degree}°C is {result} in Fahrenheit")
    elif convention == "F":
        result = int(round((degree - 32) * 5 / 9))
        print(f"{degree}°F is {result} in Celsius")
        
    else:
        print("Invalid input format. Use a number followed by 'C' or 'F'.")

convert_temperature("60C")
convert_temperature("45F")

def int_to_roman(num):
    val = {
        1000: "M", 900: "CM", 500: "D", 400: "CD",
        100: "C", 90: "XC", 50: "L", 40: "XL",
        10: "X", 9: "IX", 5: "V", 4: "IV",
        1: "I"
    }
    roman_num = ''
    for value, symbol in val.items():
        while num >= value:
            roman_num += symbol
            num -= value
    return roman_num

# Test the function
print(int_to_roman(int(input('Enter num'))))

def convert_to_hex_string(number):
    hex_string = ""
    for digit in str(number):
        hex_digit = hex(int(digit))[2:]
        hex_string += "\\x" + hex_digit.zfill(2)
    return hex_string

number = 181265777855
hex_string = convert_to_hex_string(number)
print(hex_string)
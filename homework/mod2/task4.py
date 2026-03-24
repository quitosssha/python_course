def decimal_to_any_notation(number, notation):
    if number == 0:
        return "0"
    universal_digits = "0123456789ABCDEF"
    result = ""
    while number > 0:
        result = universal_digits[number % notation] + result
        number //= notation
    return result

try:
    decimal = int(input())
    if decimal < 0:
        exit(1)
except:
    print("Неверный ввод")
    exit(1)

binary = decimal_to_any_notation(decimal, 2)
octal = decimal_to_any_notation(decimal, 8)
hexadecimal = decimal_to_any_notation(decimal, 16)

print(f"{binary}, {octal}, {hexadecimal}")
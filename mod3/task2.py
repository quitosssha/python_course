dec = [int(x) if x.isdecimal() else exit("Неверный ввод") for x in input().split()][0]
binary, octal, hexadecimal = [bin(dec)[2:], oct(dec)[2:], hex(dec)[2:]]
print(binary, octal, hexadecimal)

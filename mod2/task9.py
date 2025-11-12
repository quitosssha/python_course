symbols_to_exclude = ['-', '(', ')', ' ']

phone = input()
result = ""
for symbol in phone:
    if symbol in symbols_to_exclude:
        continue
    else:
        result += symbol

print (result)
phone = input()
clean_symbols = [x for x in phone if [' ', '-', '(', ')'].__contains__(x) == False]
print(str.join('', clean_symbols))

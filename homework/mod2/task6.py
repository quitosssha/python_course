digits = input()

zeros_count = 0
ones_count = 0

for digit in digits:
    if digit == '0':
        zeros_count += 1
    elif digit == '1':
        ones_count += 1

if zeros_count == ones_count:
    print('yes')
else:
    print('no')

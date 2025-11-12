s, i = [x.strip() for x in input().split(',')]

count = 0
for symbol in s:
    if symbol != i:
        break
    else:
        count += 1

print(count)
words = input().split()
result = [x[-1:] for x in words]
print(str.join('', result))

a, b, c = [int(x) for x in input().split()]

if a <= b <= c or c <= b <= a:
    print(b)
elif b <= a <= c or c <= a <= b:
    print(a)
else:
    print(c)

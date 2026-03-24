def gcd(a, b):
    """Рекурсивный алгоритм Евклида для поиска НОД"""
    if b == 0:
        return a
    return gcd(b, a % b)

a, b = [int(x) for x in input().split()]
print(gcd(a, b))

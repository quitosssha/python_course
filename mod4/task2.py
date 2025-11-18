def fast_pow(a: int, n: int) -> int:
    """Функция для быстрого возведения в степень. Сложность - O(log n)"""
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_pow(a * a, n // 2)
    else:
        return a * fast_pow(a, n - 1)


num, n = [int(x) for x in input().split()]
print(fast_pow(num, n))

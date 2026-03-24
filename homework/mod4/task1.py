def print_equality(*numbers: int):
    """Функция сравнивает входящие числа и печатает результат сравнения в стандартный поток вывода"""
    unique = set(numbers)
    if len(unique) == 1:
        print('Все числа равны')
        return
    if len(unique) == len(numbers):
        print('Все числа разные')
        return
    print('Есть равные и неравные числа')

ints = [int(x) for x in input().split()]
print_equality(*ints)
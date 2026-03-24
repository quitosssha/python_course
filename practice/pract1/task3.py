numbers_input = input("Введите числа через пробел: ")
numbers = [int(x) for x in numbers_input.split()]
K = int(input("Введите число K: "))

multiples = [num for num in numbers if num % K == 0]

print(f"Числа, кратные {K}:", multiples)
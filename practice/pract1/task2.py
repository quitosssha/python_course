N = int(input("Введите число N: "))

numbers = list(range(N, N**2 + 1))
sqrt_numbers = [round(x**0.5, 3) for x in numbers] # Округляем для удобства

print(f"Исходный список чисел от {N} до {N**2}: {numbers}")
print("Список квадратных корней:", sqrt_numbers)
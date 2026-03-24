prices_input = input("Введите цены товаров через пробел: ")
prices = [float(x) for x in prices_input.split()]
K = float(input("Введите число K (полные K рублей дают скидку): "))
M = float(input("Введите число M (размер скидки в рублях): "))

prices_with_discount = [price - (price // K) * M for price in prices]

print("Цены до применения скидки:", prices)
print("Цены после применения скидки:", prices_with_discount)
N = int(input("Введите количество имен: "))

names = []
print("Введите имена:")
for i in range(N):
    name = input()
    names.append(name)

existing_lengths = set()
uni = []
for name in names:
    length = len(name)
    if length in existing_lengths:
        continue
    existing_lengths.add(length)
    uni.append(name)

print("Исходный список names:", names)
print("Список uni (имена разной длины):", uni)

phrases_input = input("Введите фразы, разделенные символом ';': ")
phrases = [phrase.strip() for phrase in phrases_input.split(';')]

lengths = [len(phrase.split()) for phrase in phrases]

print("Исходный список фраз:", phrases)
print("Список количества слов в каждой фразе:", lengths)
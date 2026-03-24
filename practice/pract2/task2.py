import re

text = input("Введите текст для поиска email-адресов: ")

pattern = r'\b[a-zA-Z0-9.+\_\-#]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+\b'
emails = re.findall(pattern, text)

if emails:
    print("\nНайденные email-адреса:")
    for email in emails:
        print(email)
else:
    print("Email-адреса не найдены")
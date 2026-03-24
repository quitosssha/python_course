import re
from datetime import datetime

def find_datetime(text):
    pattern = r'\b(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})\b'
    results = []

    for match in re.finditer(pattern, text):
        try:
            dt_str = match.group(0)
            dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
            if 2000 <= dt.year <= 2099:
                results.append(dt_str)
        except ValueError:
            continue

    return results

text = input("Введите текст для поиска: ")
results = find_datetime(text)

if results:
    print("\nНайденные корректные даты и время:")
    for result in results:
        print(result)
else:
    print("\nКорректных дат и времени не найдено")
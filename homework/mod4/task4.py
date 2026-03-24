def make_palindrome(s: str) -> str:
    """Составляет палиндром из строки если это возможно"""
    chars_freq = dict()
    for char in s:
        chars_freq[char] = chars_freq.get(char, 0) + 1

    odd_counts = [x for x in chars_freq.values() if x % 2 == 1]
    if len(odd_counts) > 1:
        return "Нельзя составить палиндром"

    middle_char = ""
    straight_half = []

    for char, freq in sorted(chars_freq.items()):
        if freq % 2 == 1:
            middle_char = char
        straight_half.append(char * (freq // 2))

    left_part = str.join('', straight_half)
    right_part = left_part[::-1]

    return left_part + middle_char + right_part


s = input().strip()
print(make_palindrome(s))
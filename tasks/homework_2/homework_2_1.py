# пользователь вводит слово. Для простоты будем считать,
# что слово не меньше 3 символов

# Считайте ввод и распечатайте:
s = input("Введите слово: ")

# длину слова
print(len(s))

# слово без первой буквы
print(s[1:])

# последний символ слова
print(s[-1])

# слово без последних двух букв
print(s[:-2])

# слово в uppercase
print(s.upper())

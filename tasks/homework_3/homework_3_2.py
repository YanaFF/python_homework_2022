"""                Пользователь вводит строку. Найдите количество цифр и количество букв в строке
Вход: "абвгд 234"
Выход:
Цифры: 3
Буквы: 5                        """
user_input = input("Введите текст: ")
string = "абвгд 234"
symbol = {'Цифры': 0 , 'Буквы': 0}
for i in string:
    if i.isdigit():
        symbol['Цифры'] += 1
    elif i.isalpha():
        symbol['Буквы'] += 1

print("Цифры:", symbol['Цифры'])
print("Буквы:", symbol['Буквы'])
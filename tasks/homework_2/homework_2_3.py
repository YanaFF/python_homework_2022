# пользователь вводит строку

# Считайте ввод и если строка является числом, то напечатайте "Это число!"
# Если строка не является числом, то напечатайте "Это не число!"

user_input = input()
if user_input.isnumeric():
    print("Это число!")
else:
    print("Это не число!")

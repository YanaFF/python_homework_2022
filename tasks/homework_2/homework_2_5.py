CURRENT_YEAR = 2022

student = ('Иван Питонов', 2001, [8, 7, 7, 9, 6], True)

"""
Формат данных - ('имя', год рождения, [оценки])
Выполните пункты ниже, используя переменную student
"""

# выведите фамилию и имя Ивана в формате "Студент: {Фамилия}, {Имя}"

st_name = student[0]
split_st_name = st_name.split(" ")

print(f"Студент: {split_st_name[1]}, {split_st_name[0]}")

# Выведите возраст Ивана в формате "Возраст: {возраст}".
# Для определения текущего года используйте переменную CURRENT_YEAR

st_birth_year = student[1]
print(f"Возраст: {CURRENT_YEAR - st_birth_year}")

# напечатайте оценки Ивана через запятую в формате "Оценки: {оценка1}, {оценка2}"

st_all_marks = student[2]
st_mark1 = st_all_marks[0]
st_mark2 = st_all_marks[1]
st_mark3 = st_all_marks[2]
st_mark4 = st_all_marks[3]
st_mark5 = st_all_marks[4]
print(f"Оценки: {st_mark1}, {st_mark2}, {st_mark3}, {st_mark4}, {st_mark5}")

# напечатайте средний балл Ивана в формате "Средний бал: {бал}"
# Сумму элементов списка можно найти с помощью функции sum()

st_average_mark = sum(st_all_marks) / len(st_all_marks)
print(f"Средний бал: {st_average_mark}")

# Если средняя оценка Ивана больше или равна 8, то он получает повышенную стипендию.
# Выведите "Повышенная стипендия: есть/нет" в зависимости от его оценок

if st_average_mark >= 8:
    print("Повышенная стипендия: есть")
else:
    print("Повышенная стипендия: нет")

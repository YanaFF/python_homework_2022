"""

Напишите программу, которая объединяет значения из двух списков.
Структура всегда одна и та же - товар и количество

Ввод:

shops = [
    {'товар': 'яблоки', 'количество': 400},
    {'товар': 'конфеты', 'количество': 300},
    {'товар': 'яблоки', 'количество': 750}
]
Вывод:

{'яблоки': 1150, 'конфеты': 300}

"""

shops = [
    {'товар': 'яблоки', 'количество': 400},
    {'товар': 'конфеты', 'количество': 300},
    {'товар': 'яблоки', 'количество': 750}
]

shops_dict = dict(shops) # Не нашел решения
print(type(shops_dict))
#shops_dict["товар"]

for x in shops:
    print(index, element)
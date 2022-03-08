"""

Дан список из словарей
Напишите программу, которая объединяет значения в один словарь
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

total_apple = shops[0]['количество'] + shops[2]['количество']

shops[0]['количество'] = total_apple

shops.pop()

d_apple = [shops[0]['товар']]
d_candy = [shops[1]['товар']]
d_amount_apple = [shops[0]['количество']]
d_amount_candy = [shops[1]['количество']]

apple_dictionary = dict(zip(d_apple, d_amount_apple))
candy_dictionary = dict(zip(d_candy, d_amount_candy))

apple_and_candy = {**apple_dictionary, **candy_dictionary}
print(apple_and_candy)
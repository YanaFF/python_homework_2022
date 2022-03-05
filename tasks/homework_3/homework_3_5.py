"""

В математике существует так называемая последовательность чисел Фибоначчи
Выглядит она так: 1, 1, 2, 3, 5, 8, 13, ...

Каждое последующее число равно сумме двух предыдущих,
а первые два числа Фибоначчи - две единицы.

Запросите с клавиатуры число N и распечатайте через запятую первые N чисел Фибоначчи

Ввод: 6
Вывод: 1, 1, 2, 3, 5, 8

"""

N = int(input())

fibonachi = [1, 1]
if len(fibonachi) < N:
    while len(fibonachi) < N:
        extra = fibonachi[-1] + fibonachi[-2]
        fibonachi.append(extra)

elif N == 2:
    fibonachi = [1, 1]
else:
    fibonachi = [1]

print(fibonachi)


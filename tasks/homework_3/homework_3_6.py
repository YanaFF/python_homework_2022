"""

На вход принимается число N.

Выведите на печать следующий паттерн:

1
1 2
1 2 3
1 2 3 4
...
1 ... N

"""

N = int(input())

q = 1
s = 1
k = 0
while q <= N:
    print(q, end=' ')
    q = q + 1
    k = k + 1
    if k == s:
        print()
        s = s + 1
        k = 0
"""      Найти все числа от 1000 до 3000 включительно, все цифры которых четные.
Программа должна выдавать результат в виде разделенной запятыми строки """

#print([i for i in range(1000, 3000, 2) if len(set(str(i))) == len(str(i))])            #   1) решение

s = 0                                                                                   #   2) решение
for i in range(1000,3002, 2):

   print(i,end=" ")
   s += i + 2

print()


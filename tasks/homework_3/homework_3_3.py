chet_chisla = {0,2,4,6,8} # задаем множество четных чисел, с которым будем сверяться
even_list = [] # список, куда будем помещать правильные числа
for n in range(1000, 3001):# зададим рэндж. обращаем внимание,что там 3001, и начинаем перебор
     n_set = {int(a) for a in str(n)} # новое множество, в котором итерируем
     if n_set <= chet_chisla: #проверяем соотвествует ли элемент множеству четных чисел. Можно ли было это сделать по-другому? Через % 2?
        even_list.append(n) # добавляем элемент в пустое множество
print(even_list, sep = ", ")
   #Найти все числа от 1000 до 3000 включительно, все цифры которых четные.
# Программа должна выдавать результат в виде разделенной запятыми строки
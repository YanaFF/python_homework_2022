# Используя список dwarves, выведите на экран с помощью срезов следующие списки:
dwarves = ["Балин", "Двалин", "Бифур", "Бофур",
         "Бомбур", "Оин", "Глоин", "Дори", "Нори",
         "Ори", "Фили", "Кили", "Торин"]
# ["Двалин", "Бифур", "Бофур"]
dwarves1 = dwarves[1:4]
print(dwarves1)
# ["Балин", "Бифур", "Бомбур", "Глоин", "Нори", "Фили", "Торин"]
dwarves2 = dwarves[::2]
print(dwarves2)
# ["Оин", "Дори", "Ори", "Кили"]
dwarves3 = dwarves[5::2]
print(dwarves3)
# ["Торин", "Фили", "Нори", "Глоин"]
dwarves4 = dwarves[-1:5:-2]
print(dwarves4)

# Вам дан словарь, содержащий в себе списки словарей.
# Напишите код, который выведет на экран 'разработчик' из списка ключа Windows в первом словаре из списка 2

dict_of_lists = {
    'Список1': [
        {'Python': 'язык программирования'},
        {'R': 'язык программирования', 'LaTEX': 'язык верстки'}
    ],
    'Список2': [
        {'Windows': ['операционная система', 'разработчик'], 'UNIX': 'операционная система'},
        {'IBM': ['компания-производитель', 'разработчик'], 'IPv6': 'интернет-протокол'}
    ]
}

print(dict_of_lists['Список2'][0]['Windows'][1])
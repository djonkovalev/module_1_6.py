my_dict = {'Антона': 1987, 'Наташа': 1994, 'Кирил': 1999, 'Андрей': 1984, 'Людмила': 2000}
print('Словарь:', my_dict)
print('Год рождения Кирила:', my_dict['Кирил'])
print('Год рождения Людмилы:', my_dict.get('Людмила', 'нет такого ключа'))
my_dict.update({'Альберт': 1999, 'Валерия': 1996})
removed_year = my_dict.pop('Валерия')
print('Значение удалённого элемента \'Артём\':', removed_year)
print('Изменённый словарь:', my_dict)

print()

my_set = {2, 3, 3, 2, 5, True, True, False, True, 'list', 'set', 'list', 'list'}
print('Множество:', my_set)
my_set.add('string')
my_set.add('float')
my_set.discard(2)
print('Изменённое множество:', my_set)
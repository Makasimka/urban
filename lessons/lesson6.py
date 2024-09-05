my_dict = {
	'Россия'  : 'Москва',
	'Франция' : 'Париж',
	'Латвия'  : 'Рига',
	'Италия'  : 'Рим',
	'Швеция'  : 'Стокгольм',
	'Германия': 'Берлин',
}

print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict['Франция']}')
print(f'Not existing value: {my_dict.get('Сербия')}')

my_dict.update({
	'Австрия': 'Вена',
	'Бельгия': 'Брюссель',
})
print(f'Dict update: {my_dict}')

delete_val = my_dict.pop('Германия')
print(f'Deleted value:  {delete_val}')
print(f'Modified dictionary: {my_dict}')

my_set = { 0, 0, 0, 1, 1, 1, '1', '1', True, True, False, False, None, None, (1, 2), (3, 4), (1, 2), (3, 4), }
# True, False - удаляются (заменяются) на 1 и 0, хотя на уроке про это не сказали.

print(f'Set: {my_set}')

my_set.add(2)
my_set.update({ 3, 4, 5 })
print(f'Modified set: {my_set}')

my_set.remove(0)  # или .discard(), чтобы без ошибки
print(f'Modified set (2): {my_set}')

my_set2 = { 5, 6, 7, 8, (4, 5), (6, 7) }
print(f'Union set: {my_set.union(my_set2)}')

my_list = [42, 43]
my_dict = {
    "foo": {"a": 12, "b": (1, 2, 3, 4, my_list)},
    "bar": {"c": 12, "d": {5, 6, 7, 8}},
    "moo": {"e": 12, "f": {"Lol": ["L", "o", "l"]}},
}
# Выведите на консоль значение ключа ‘foo’.
print(my_dict['foo'])
# Выведите на консоль значение ключа ‘b’.
print(my_dict['foo']['b'])
# Добавьте в my_list 44.
my_list.append(44)
# Снова выведите на консоль значение ключа ‘b’.
print(my_dict['foo']['b'])
# Выведите множество.
print(my_dict['bar']['d'])
# Добавьте в множество элемент 9.
my_dict['bar']['d'].add(9)
# Снова выведите множество.
print(my_dict['bar']['d'])
# Удалите из списка элемент ‘o’.
my_dict['moo']['f']['Lol'].remove('o')
# Добавьте в словарь, который является значением ключа ‘f’ ключ ‘K’ со значением ['K', 'e', 'k'].
my_dict['moo']['f']['K'] = ['K', 'e', 'k']
print(my_dict)
# Очистите словарь my_dict.
my_dict.clear()
print(my_dict)
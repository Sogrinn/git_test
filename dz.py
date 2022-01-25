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
from random import randint
# 1


def nothing():
    pass

# 2


def fun_2(num):
    return num * 2

# 3


def fun_3(num):
    if num % 2 == 0:
        return print('yes')
    else:
        return print('no')

# 4


def fun_4(n_1, n_2):
    if n_1 > 10:
        return print('yes')
    else:
        return print('no')
'''# 5
fun_5 = lambda n_1, n_2: n_1%n_2
print(fun_5(5, 3))'''
'''# 6 • Создадим функцию с простыми командами. Обернём её в декоратор, который бы дополнял возможности функции.
def decor(f):
    def wr():
        print('//////////')
        f()
        print('!!!!!!!!!!')
    return wr

@decor
def Pirat():
    print('Arrr')

Pirat()'''
'''# 7 Использовать функцию map и filter
def check(num):
    return num % 2 == 0
numbers = [randint(1, 100) for i in range(10)]
print(numbers)
numbers_after = list(map(fun_2, numbers))
print(numbers_after, 'После map')
numbers_after = list(filter(check, numbers))
print(numbers_after, 'После filter')'''

# 8 Создадим чистую и нечистую функцию.


def fun_2(num):    # Чистая
    return num * 2


list_f = []


def fun_8(num): # Нечистая
    list_f.append(num)

'''# 9 Сделать функцию поиска минимума и максимума в списке.


def fun_min_and_max(list_f):
    min_f = list_f[0]
    max_f = list_f[0]
    for num in list_f:
        if num > max_f:
            max_f = num
        elif num < min_f:
            min_f = num
    return min_f, max_f


list_f = [1, 2, 3, 4, 5, 6, 88, -4, -20, 15, 0, -1]
print(fun_min_and_max(list_f))'''

# 10 Написать функцию, которая определяет, является ли год високосным. Пользователь вводит год, если он високосный,
# то функция возвращает True. Если нет, то False.


def fun_10(year):
    return (year - 1764) % 4 == 0


print(fun_10(1772))






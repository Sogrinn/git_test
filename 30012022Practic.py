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
        f
        print('!!!!!!!!!!')
    return wr

@decor
def Arrr():
    print('Arrr')

Arrr()
'''
# 7 Использовать функцию map и filter
def check(num):
    return num % 2 == 0
numbers = [randint(1, 100) for i in range(10)]
print(numbers)
numbers_after = list(map(fun_2, numbers))
print(numbers_after, 'После map')
numbers_after = list(filter(check, numbers))
print(numbers_after, 'После filter')





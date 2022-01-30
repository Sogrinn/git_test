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

# 5
fun_5 = lambda n_1, n_2: n_1%n_2
print(fun_5(5, 3))





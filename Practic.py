# 1 Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе
def is_prime(num):
    div = 2
    while num % div != 0:
        div += 1
    return num == div


# 2. Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата
def square(side):
    perimeter = side * 4
    area = side ** 2
    diagonal = ((side ** 2) * 2) ** 0.5
    return (perimeter, area, diagonal)


# 3 Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция,
# которая должна быть произведена над ними. Если третий аргумент +, сложить их;
# если —, то вычесть; * — умножить; / — разделить (первое на второе).
# В остальных случаях вернуть строку "Неизвестная операция".
def arithmetic(num_1, num_2, sign):
    if sign == '+':
        return num_1 + num_2
    elif sign == '-':
        return num_1 - num_2
    elif sign == '*':
        return num_1 * num_2
    elif sign == '/':
        return num_1 / num_2
    else:
        return 'Неизвестная операция'


# 4 Напишите функцию, которая проверяет, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.
def palindrome(string):
    string = string.lower().replace(' ', '')
    reverse_string = string[::-1]
    return string == reverse_string

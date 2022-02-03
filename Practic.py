# 1 Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе
def is_prime(num):
    div = 2
    while num % div != 0:
        div += 1
    return num == div


# 2. Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа: периметр квадрата, площадь квадрата и диагональ квадрата
def square(side):
    perimeter = side * 4
    area = side ** 2
    diagonal = ((side ** 2) * 2) ** 0.5
    return (perimeter, area, diagonal)






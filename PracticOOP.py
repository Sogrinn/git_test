from random import  randint
'''class Human:
    head = 1

    def __init__(self, eyecolor='brown'):
        self.eyecolor = eyecolor

nikita = Human(eyecolor='green')
print(nikita.head, nikita.eyecolor)'''
"""class Example:
    # global num_1, num_2
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    def __init__(self, num_3=2, num_4=10):
        self.num_3 = num_3
        self.num_4 = num_4

    def random_num(self):
        r_num = randint(0, 10000)
        return r_num


    '''def sum_global(self): # Использовать только с глобальными переменными
        return f"{num_1} + {num_2} = {num_1 + num_2}"'''


    def sum(self):
        return f'{self.num_1} + {self.num_2} = {self.num_1 + self.num_2}'


    def exponentiation(self):
        return self.num_3 ** self.num_4

task_1 = Example()
print(task_1.random_num())
print(task_1.sum())
print(task_1.exponentiation())
print(task_1.num_1)"""


class Calculator:

    def calc(self):
        num_1 = input('Num_1 :')
        num_2 = input('Num_2 :')
        sign = input('(+, -, *, /): ')
        if sign not in '+-*/':
            print('Неверная операция')
        else:
            try:
                return f'{num_1} {sign} {num_2} = {eval(num_1 + sign + num_2)}'
            except ZeroDivisionError:
                return 'На ноль делить нельзя'


calc = Calculator()
print(calc.calc())

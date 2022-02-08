from random import  randint
'''class Human:
    head = 1

    def __init__(self, eyecolor='brown'):
        self.eyecolor = eyecolor

nikita = Human(eyecolor='green')
print(nikita.head, nikita.eyecolor)'''
"""class Example:
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    def __init__(self, num_3=2, num_4=10):
        self.num_3 = num_3
        self.num_4 = num_4

    def random_num(self):
        r_num = randint(0, 10000)
        return r_num


    def sum(self):
        return f'{self.num_1} + {self.num_2} = {self.num_1 + self.num_2}'


    def exponentiation(self):
        return self.num_3 ** self.num_4

task_1 = Example()
print(task_1.random_num())
print(task_1.sum())
print(task_1.exponentiation())
print(task_1.num_1)"""
'''class Calculator:

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
'''
'''

class Task:
    vowels = 'уеыаоэяию'

    def __init__(self, user_input=input('!:'), long_of_input=None):
        self.user_input = user_input
        self.long_of_input = long_of_input

    def long(self):
        self.long_of_input = len(self.user_input)

    def fun(self):
        if self.user_input.isdigit:
            sum_num = 0
            for num in self.user_input[::2]:
                sum_num += int(num)
                return sum_num * self.long_of_input
        else:
            count_consonants = 0
            count_vowels = 0
            for_print_vowels = ''
            for_print_consonants = ''
            for l in self.user_input:
                if l in self.vowels:
                    count_vowels += 1
                    for_print_vowels += l
                else:
                    count_consonants += 1
                    for_print_consonants += l
            if count_vowels * count_consonants <= self.long_of_input:
                return for_print_vowels
            else:
                return for_print_consonants


task = Task()
task.long()
print(task.fun())
'''
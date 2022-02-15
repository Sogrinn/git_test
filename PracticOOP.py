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
'''

class Human():
    default_name = None
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'name = {self.name}\nage = {self.age}\nmoney = {self.__money}\nhouse = {self.__house}')

    @classmethod
    def default_info(cls):
        print(f'default name = {cls.default_name}\ndefault age = {cls.default_age}')

    def __make_deal(self, price, house):
        self.__money -= price
        self.__house = house

    def earn_money(self):
        self.__money += 5000

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(price, house)
        else:
            print('Not enough money')


class House():

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * discount / 100


class SmallHouse(House):

    def __init__(self, price, area=40):
        self._price = price
        self._area = area


Human.default_info()
cottage = SmallHouse(7000)
man = Human('a', 25)
man.info()
man.buy_house(cottage, 10)
man.earn_money()
man.earn_money()
man.buy_house(cottage, 10)
man.info()'''


class Tomato:
    states = {1: "didn't grow", 2: "did grow", 3: "ripe"}

    def __init__(self, index):
        self._index = index
        self._state = self.states[1]

    def grow(self):
        if self._state == "didn't grow":
            self._state = self.states[2]
        elif self._state == "did grow":
            self._state = self.states[3]

    def is_ripe(self):
        if self._state == "ripe":
            return True
        else:
            return False


class TomatoBush():

    def __init__(self, amount):
        self.amount = amount
        self.tomatoes = []
        for tomat in range(amount):
            tomat = Tomato(tomat)
            self.tomatoes.append(tomat)

    def grow_all(self):
        for tomat in self.tomatoes:
            tomat.grow()

    def all_are_ripe(self):
        for tomat in self.tomatoes:
            if not tomat.is_ripe():
                return False
                break
        else:
            return True

    def give_away_all(self):
        self.tomatoes = []


class Gardener():

    def __init__(self, name, bush):
        self.name = name
        self._plant = bush

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('The harvest has been harvested')
        else:
            print('not yet ripe')

    @staticmethod
    def knowledge_base():
        print('knowledge_base')


Gardener.knowledge_base()
tomato_bush = TomatoBush(17)
man = Gardener('Man', tomato_bush)
man.work()
man.harvest()
man.work()
man.harvest()


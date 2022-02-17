from random import choice

# 1
def hide_card_number(number):
    return (len(number) - 4) * '*' + number[-4:]


# 2
def palindrome(string):
    string = string.lower().replace(' ', '')
    reverse_string = string[::-1]
    return string == reverse_string

# 3 tic-tac-toe


class Field():

    def __init__(self):
        self.not_used_cells = [str(i) for i in range(1, 10)]
        self.field = {str(i) : str(i) for i in range(1, 10)}

    @staticmethod
    def decor(func):
        def wrapper(*args):
            print('--------------')
            func(*args)
            print('--------------')

        return wrapper

    @decor
    def _print_line_1(self):
        print(f'| {self.field["1"]} | {self.field["2"]} | {self.field["3"]} |')

    def _print_line_2(self):
        print(f'| {self.field["4"]} | {self.field["5"]} | {self.field["6"]} |')

    @decor
    def _print_line_3(self):
        print(f'| {self.field["7"]} | {self.field["8"]} | {self.field["9"]} |')

    def print_field(self):
        self._print_line_1()
        self._print_line_2()
        self._print_line_3()


class Player():

    def __init__(self, sign):
        self.sign = sign

    def step(self, *args):
        return input(f'Куда поставим {self.sign}?')

class AIPlayer(Player):

    def step(self, not_used_cells):
        return choice(not_used_cells)


class TicTacToe():

    __combination_for_win = (('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'), ('1', '4', '7'), ('2', '5', '8'),
                           ('3', '6', '9'), ('1', '5', '9'), ('3', '5', '9'))

    def __init__(self):
        self.player1 = Player('X')
        choise = input('1.PvP 2.PvE')
        if choise == '1':
            self.player2 = Player('O')
        elif choise == '2':
            self.player2 = AIPlayer('O')
        self.field = Field()

    def step(self, player):
        self.field.print_field()
        while True:
            cell = player.step(self.field.not_used_cells)
            if cell in self.field.not_used_cells:
                self.field.field[cell] == player.sign
                self.field.not_used_cells.remove(cell)
                break
            else:
                print('Неверный номер')

    def check_for_victory(self):
        for comb in self.__combination_for_win:
            if self.field.field[comb[0]] == self.field.field[comb[1]] == self.field.field[comb[2]]:
                return True

    def game(self):
        while True:
            self.step(player= self.player1)
            if self.check_for_victory():
                print('Win X')
                break
            self.step(player=self.player2)
            if self.check_for_victory():
                print('Win O')
                break

game = TicTacToe()
game.game()
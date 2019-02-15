print('Tic tac toe')

class Board:
    def __init__(self):
        self.grid = ' {} | {} | {} \n------------\n {} | {} | {} \n------------\n {} | {} | {} \n------------'
        self.state = [' ' for _ in range(9)]

    def draw(self, symbol, position):
        self.set_symbol(symbol, position)
        print(self.grid.format(*self.state))

    def set_symbol(self, symbol, position):
        if self.state[position - 1] != ' ':
            print('La celda esta ocupada')
        self.state[position - 1] = symbol

    def tic_tac_toe(self, symbol):
        return any([
            self.mark_horizontal(symbol),
            self.mark_vertical(symbol),
            self.mark_diagonal(symbol),
        ])

    def mark_horizontal(self, symbol):
        for i in [0, 3, 6]:
            if self.state[i] + self.state[i + 1] + self.state[i + 2] == symbol * 3:
                print('win horizontal')
                return True
        return False

    def mark_vertical(self, symbol):
        for i in [0, 1, 2]:
            if self.state[i] + self.state[i + 3] + self.state[i + 6] == symbol * 3:
                print('win vertical')
                return True
        return False

    def mark_diagonal(self, symbol):
        if self.state[0] + self.state[4] + self.state[8] == symbol * 3 or \
           self.state[2] + self.state[4] + self.state[6] == symbol * 3:
               print('win diagonal')
               return True
        return False


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def turn(self, board, position):
        board.draw(self.symbol, position)
        return board.tic_tac_toe(self.symbol)


board = Board()
playerX = Player('X')
player0 = Player('0')

while True:
    placingX = int(input('\nTurno de X: '))
    if playerX.turn(board, placingX):
        print('Player x win!')
        break

    placing0 = int(input('\nTurno de 0: '))
    if player0.turn(board, placing0):
        print('Player 0 win!')
        break


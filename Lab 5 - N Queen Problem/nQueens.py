class Square:
    def __init__(self):
        self.piece = '0'
        self.isAvailable = True
        self.isChecked = False
        self.threatened = 0


class Board:
    def __init__(self, n):
        self.n = n
        self.board = self.createBoard(n)

    def createBoard(self, n):
        board = []
        for i in range(n):
            row = []
            for j in range(n):
                newSquare = Square()
                row.append(newSquare)
            board.append(row)
        return board

    def printBoard(self):
        for row in self.board:
            for square in row:
                print(square.piece, end="  ")
            print()

    def placeQueen(self, row, column):
        square = self.board[row][column]
        square.isAvailable = False
        square.threatened += 1
        square.piece = 'Q'

        for i in range(n):
            square = self.board[row][i]
            square.isAvailable = False
            square.threatened += 1

        for i in range(n):
            square = self.board[i][column]
            square.isAvailable = False
            square.threatened += 1

        if row < column:
            i = 0
            j = abs(row-column)
            while j < n:
                square = self.board[i][j]
                square.isAvailable = False
                square.threatened += 1
                i += 1
                j += 1

            i = 0
            j = abs(row+column)
            if j >= n:
                j = n-1
                i = row + column - n + 1
            while j >= 0 and i < n:
                square = self.board[i][j]
                square.isAvailable = False
                square.threatened += 1
                i += 1
                j -= 1

        elif row > column:
            j = 0
            i = abs(row-column)
            while i < n:
                square = self.board[i][j]
                square.isAvailable = False
                square.threatened += 1
                i += 1
                j += 1

            j = 0
            i = abs(row+column)
            if i >= n:
                i = n-1
                j = row + column - n + 1
            while i >= 0 and j < n:
                square = self.board[i][j]
                square.isAvailable = False
                square.threatened += 1
                i -= 1
                j += 1

        else:
            i = 0
            j = abs(row-column)
            while j < n:
                square = self.board[i][j]
                square.isAvailable = False
                square.threatened += 1
                i += 1
                j += 1

            j = 0
            i = abs(row+column)
            if i >= n:
                i = n-1
                j = row + column - n + 1
            while i >= 0 and j < n:
                square = self.board[i][j]
                square.isAvailable = False
                square.threatened += 1
                i -= 1
                j += 1

    def removeQueen(self, row, column):
        square = self.board[row][column]
        square.piece = '0'
        square.threatened -= 1

        for i in range(n):
            square = self.board[row][i]
            square.isAvailable = False
            square.threatened -= 1

        for i in range(n):
            square = self.board[i][column]
            square.isAvailable = False
            square.threatened -= 1

        if row < column:
            i = 0
            j = abs(row-column)
            while j < n:
                square = self.board[i][j]
                square.isAvailable = False
                square.threatened -= 1
                i += 1
                j += 1

            i = 0
            j = abs(row+column)
            if j >= n:
                j = n-1
                i = row + column - n + 1
            while j >= 0 and i < n:
                square = self.board[i][j]
                square.isAvailable = False
                square.threatened -= 1
                i += 1
                j -= 1

        elif row > column:
            j = 0
            i = abs(row-column)
            while i < n:
                square = self.board[i][j]
                square.isAvailable = False
                square.threatened -= 1
                i += 1
                j += 1

            j = 0
            i = abs(row+column)
            if i >= n:
                i = n-1
                j = row + column - n + 1
            while i >= 0 and j < n:
                square = self.board[i][j]
                square.isAvailable = False
                square.threatened -= 1
                i -= 1
                j += 1

        else:
            i = 0
            j = abs(row-column)
            while j < n:
                square = self.board[i][j]
                square.isAvailable = False
                square.threatened -= 1
                i += 1
                j += 1

            j = 0
            i = abs(row+column)
            if i >= n:
                i = n-1
                j = row + column - n + 1
            while i >= 0 and j < n:
                square = self.board[i][j]
                square.isAvailable = False
                square.threatened -= 1
                i -= 1
                j += 1

    def solveBoard(self):
        solution = []
        queenPositions = []
        numberOfQueensPlaced = 0
        row = 0
        column = 0
        while numberOfQueensPlaced != n:
            if row >= n:
                for i in range(n):
                    square = self.board[i][column]
                    square.isChecked = False
                [row, column] = queenPositions[-1]
                self.removeQueen(row, column)
                queenPositions.pop(-1)
                numberOfQueensPlaced -= 1

            square = self.board[row][column]
            if not square.isChecked and square.threatened == 0:
                self.placeQueen(row, column)
                square.isChecked = True
                queenPositions.append([row, column])
                numberOfQueensPlaced += 1
                column += 1
                row = 0
            else:
                square.isChecked = True
                row += 1


if __name__ == '__main__':
    n = 4
    newBoard = Board(n)
    newBoard.solveBoard()
    newBoard.printBoard()

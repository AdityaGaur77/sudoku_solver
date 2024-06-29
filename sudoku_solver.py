class Board:
    def __init__(self):
        self.board = []

    def empty_board(self):
        for i in range(9):
            self.board.append([])

        for j in self.board:
            for x in range(3):
                j.append(["_", "_", "_"])

    def __str__(self):
        for m in self.board:
            print()
            for x in m:
                print(x, sep=" ", end=" ")
                print()

    def print_cell(self, number):
        cell = self.board[number-1]
        for k in cell:
            print(k)
            print()
    def add_num(self, num, row, column):
        if row <= 3:
            currentrow = [self.board[0][row-1], self.board[1][row-1], self.board[2][row-1]]
            if column <=3:
                currentrow[0][column-1] = num
            elif column <=6:
                currentrow[1][column-4] = num
            elif column <=9:
                currentrow[2][column-7] = num
        elif row <=6:
            currentrow = [self.board[0][row - 1], self.board[1][row - 1], self.board[2][row - 1]]
            if column <= 3:
                currentrow[0][column - 1] = num
            elif column <= 6:
                currentrow[1][column - 4] = num
            elif column <= 9:
                currentrow[2][column - 7] = num
test = Board()
test.empty_board()
test.add_num(2,2,2)
print(test)
class Board:
    def __init__(self):
        self.board = []

    def empty_board(self):
        for i in range(9):
            self.board.append([])

        for j in self.board:
            for x in range(3):
                j.append(["_", "_", "_"])

    def prettyprint(self):
        for m in self.board:
            print()
            for x in m:
                print(x, sep=" ", end=" ")
                print()

    def printcell(self, number):
            cell = self.board[number-1]
            for k in cell:
                print(k)
                print()
main_board = Board()
main_board.empty_board()
main_board.printcell(1)

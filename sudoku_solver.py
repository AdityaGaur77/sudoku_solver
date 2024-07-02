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
        for q in cell:
            print(q)
            print()
    def add_num(self, num, row, column):
        if row <= 3:
            currentrow = [self.board[0][row-1], self.board[1][row-1], self.board[2][row-1]]
            if column <=3:
                currentrow[0][column-1] = num
            elif 3 < column <=6:
                currentrow[1][column-4] = num
            elif 6 < column <=9:
                currentrow[2][column-7] = num
        elif 3 < row <=6:
            currentrow = [self.board[3][row - 4], self.board[4][row - 4], self.board[5][row - 4]]
            if column <= 3:
                currentrow[0][column - 1] = num
            elif 3 < column <= 6:
                currentrow[1][column - 4] = num
            elif 6 < column <= 9:
                currentrow[2][column - 7] = num
        elif 6 < row <=9:
            currentrow = [self.board[6][row - 7], self.board[7][row - 7], self.board[8][row - 7]]
            if column <= 3:
                currentrow[0][column - 1] = num
            elif 3 < column <= 6:
                currentrow[1][column - 4] = num
            elif 6 < column <= 9:
                currentrow[2][column - 7] = num
    def solve_board(self):
        numcounter = 0
        for b in self.board:
            for j in b:
                for p in j:
                    if type(p) == int:
                        numcounter +=1
        if numcounter < 17:
            print("not enough numbers in sudoku to solve")
            exit()
        queue = [1,2, 3, 4, 5, 6, 7, 8, 9]
        for z in range(len(self.board)):
                for l in range(len(self.board[z])):
                    for k in range(len(self.board[z][l])):
                        f = 0
                        while self.board[z][l][k] == "_":
                          if(queue[f] not in self.board[z][0]) and (queue[f] not in self.board[z][1]) and (queue[f] not in self.board[z][2]): #checking to see if number is in cell
                                if z == 0 or z==3 or z==6:
                                    if (queue[f] not in self.board[z][l]) and (queue[f] not in self.board[z+1][l]) and (queue[f] not in self.board[z+2][l]): #checking to see if num is in row
                                        if z < 3:
                                            if (queue[f] not in [r[k] for r in self.board[z]]) and (queue[f] not in [r[k] for r in self.board[z+3]]) and (queue[f] not in [r[k] for r in self.board[z+6]]):
                                                self.board[z][l][k] = queue[f]
                                            else:
                                              f +=1
                                              continue
                                        elif z < 6:
                                            if (queue[f] not in [r[k] for r in self.board[z]]) and (queue[f] not in [r[k] for r in self.board[z-3]]) and (queue[f] not in [r[k] for r in self.board[z+3]]):
                                                self.board[z][l][k] = queue[f]
                                            else:
                                                f+=1
                                                continue
                                        elif z < 9:
                                            if (queue[f] not in [r[k] for r in self.board[z]]) and (queue[f] not in [r[k] for r in self.board[z-3]]) and (queue[f] not in [r[k] for r in self.board[z-6]]):
                                                self.board[z][l][k] = queue[f]
                                            else:
                                                f+=1
                                                continue
                                    else:
                                        f+=1
                                        continue
                                
                                elif z == 1 or z==4 or z==7:
                                    if (queue[f] not in self.board[z][l]) and (queue[f] not in self.board[z-1][l]) and (queue[f] not in self.board[z+1][l]): #checking to see if num is in row
                                        if z < 3:
                                            if (queue[f] not in [r[k] for r in self.board[z]]) and (queue[f] not in [r[k] for r in self.board[z+3]]) and (queue[f] not in [r[k] for r in self.board[z+6]]):
                                                self.board[z][l][k] = queue[f]
                                            else:
                                              f +=1
                                              continue
                                        elif z < 6:
                                            if (queue[f] not in [r[k] for r in self.board[z]]) and (queue[f] not in [r[k] for r in self.board[z-3]]) and (queue[f] not in [r[k] for r in self.board[z+3]]):
                                                self.board[z][l][k] = queue[f]
                                            else:
                                                f+=1
                                                continue
                                        elif z < 9:
                                            if (queue[f] not in [r[k] for r in self.board[z]]) and (queue[f] not in [r[k] for r in self.board[z-3]]) and (queue[f] not in [r[k] for r in self.board[z-6]]):
                                                self.board[z][l][k] = queue[f]
                                            else:
                                                f+=1
                                                continue
                                    else:
                                        f+=1
                                        continue
                                elif z==2 or z==5 or z==8:
                                    if (queue[f] not in self.board[z][l]) and (queue[f] not in self.board[z-1][l]) and (queue[f] not in self.board[z-2][l]): #checking to see if num is in row
                                        if z < 3:
                                            if (queue[f] not in [r[k] for r in self.board[z]]) and (queue[f] not in [r[k] for r in self.board[z+3]]) and (queue[f] not in [r[k] for r in self.board[z+6]]):
                                                self.board[z][l][k] = queue[f]
                                            else:
                                              f +=1
                                              continue
                                        elif z < 6:
                                            if (queue[f] not in [r[k] for r in self.board[z]]) and (queue[f] not in [r[k] for r in self.board[z-3]]) and (queue[f] not in [r[k] for r in self.board[z+3]]):
                                                self.board[z][l][k] = queue[f]
                                            else:
                                                f+=1
                                                continue
                                        elif z < 9:
                                            if (queue[f] not in [r[k] for r in self.board[z]]) and (queue[f] not in [r[k] for r in self.board[z-3]]) and (queue[f] not in [r[k] for r in self.board[z-6]]):
                                                self.board[z][l][k] = queue[f]
                                            else:
                                                f+=1
                                                continue
                                    else:
                                        f+=1
                                        continue
                          else:
                              f +=1
                              continue
test = Board()
test.empty_board()
test.solve_board()
print(test)
class Board:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.winLength = 4
        self.board = [[0 for i in range(0,self.cols)] for j in range(0,self.rows)]
        self.searchDirections = [[1,-1],[1,0],[1,1],[0,1]]

    def display(self):
        for i in range(self.rows-1,-1,-1):
            for j in range(0,self.cols):
                if(self.board[i][j] == 0):
                    print('-', end = ' ')                    
                elif(self.board[i][j] == 1):
                    print('X', end = ' ')
                else:
                    print('O', end = ' ')
            print("")

    # At every square, look up-left, up, up-right, right for a win
    def isWon(self):

        # 0 means no winner. 1 means player 1, -1 means player 2
        winner = 0
        gameWon = False
        
        for i in range(0,self.rows):
            if(gameWon):
                break
            for j in range(0,self.cols):
                if(gameWon):
                    break
                if(self.board[i][j] != 0):
                    for dir in self.searchDirections:
                        gameWon = True
                        for len in range(1,self.winLength):
                            try:
                                if(self.board[i][j] != self.board[i+len*dir[0]][j+len*dir[1]]):
                                    gameWon = False
                                    break
                            except IndexError:
                                pass
                        if(gameWon):
                            winner = self.board[i][j]

        return winner

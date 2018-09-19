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
    # return 0 means no winner. 1 means player 1, -1 means player 2
    def isWon(self):
        
        for i in range(0,self.rows):
            for j in range(0,self.cols):
                if(self.board[i][j] != 0):
                    for dir in self.searchDirections:
                        # Check in given direction to see if we get 4 in a row.
                        gameWon = True
                        for len in range(1,self.winLength):
                            try:
                                if(self.board[i][j] != self.board[i+len*dir[0]][j+len*dir[1]]):
                                    gameWon = False
                                    break
                            except IndexError:
                                gameWon = False
                                break
                        if(gameWon):
                            return self.board[i][j]

        return 0

    # 1 means player 1, -1 means player 2.
    # Honestly that choice of 1 and -1 seems dumb but whatever
    def addPiece(self,player,col):
        # If this column is already full throw a IndexError
        # Idea: In the Game class use a try-except statement to place pieces
        if(self.board[self.rows-1][col] != 0):
            raise IndexError('Adding Piece to full column')

        row = self.rows-1
        while(row >= 0 and self.board[row][col] == 0):
            row = row - 1
        self.board[row+1][col] = player

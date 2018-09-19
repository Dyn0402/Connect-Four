from Board import Board

theBoard = Board()

theBoard.board[0][2] = 1
theBoard.board[0][3] = 1
theBoard.board[0][5] = 1
theBoard.board[1][4] = 1
theBoard.board[3][2] = 1
theBoard.board[0][5] = 1
theBoard.board[0][5] = 1

theBoard.display()
print(theBoard.isWon())

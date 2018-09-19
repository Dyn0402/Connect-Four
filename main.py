from Board import Board

theBoard = Board()

theBoard.addPiece(1,0)
theBoard.addPiece(-1,1)
theBoard.addPiece(1,1)
theBoard.addPiece(-1,2)
theBoard.addPiece(1,3)
theBoard.addPiece(-1,2)
theBoard.addPiece(1,2)
theBoard.addPiece(-1,2)
theBoard.addPiece(1,2)
theBoard.addPiece(-1,4)
theBoard.addPiece(1,5)
theBoard.addPiece(-1,3)
theBoard.addPiece(1,6)
theBoard.addPiece(-1,4)
theBoard.addPiece(1,4)
theBoard.addPiece(-1,5)

theBoard.display()
print(theBoard.isWon())

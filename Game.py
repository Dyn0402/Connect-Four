from HumanPlayer import HumanPlayer
from MachinePlayer import MachinePlayer
from Board import Board

## Well this is super duper unfinished but here's a start
class Game:
    def __init__(self,player1IsHuman = True, player2IsHuman = True, numRows = 6, numCols = 7, winLength = 4, displayTurns = False):
        if(player1IsHuman):
            self.player1 = HumanPlayer()
        else:
            self.player1 = MachinePlayer()

        if(player2IsHuman):
            self.player2 = HumanPlayer()
        else:
            self.player2 = MachinePlayer()
        
        if(player1IsHuman or player2IsHuman):
            self.displayTurns = True
        else:
            self.displayTurns = displayTurns
        self.gameBoard = Board(numRows,numCols,winLength)
        self.currentTurn = 1

    def takeTurn(self):
        if(self.displayTurns):
            self.gameBoard.display()
            if(self.currentTurn == 1):
                print("Player 1's turn")
            else:
                print("Player 2's turn")

        playSuccess = False
        while(not playSuccess):
            playCol = 0
        
            if(self.currentTurn == 1):
                playCol = self.player1.takeTurn()
            else:
                playCol = self.player2.takeTurn()

            try:
                self.gameBoard.addPiece(self.currentTurn,playCol)
                playSuccess = True
            except IndexError:
                print("Invalid Input, try again")
                continue
            
        self.currentTurn = -1*self.currentTurn

    def play(self):
        winner = 0
        while(winner == 0):
            self.takeTurn()
            winner = self.gameBoard.isWon()

        self.gameBoard.display()
        if(winner == 1):
            print("Player 1 wins!!!")
        else:
            print("Player 2 wins!!!")

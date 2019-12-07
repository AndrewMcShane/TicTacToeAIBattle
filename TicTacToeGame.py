import GameConstants as consts
import TicTacToeAI as AI

class GameBoard():
    def __init__(self):
        self.board = []
        self.resetBoard()
    
    def resetBoard(self):
        self.board = [[consts.EMPTY_SPACE]*3 for i in range(0,3)]

    def checkWin(self):
        for i in range(0,3):
            # Check row:
            if self.board[i][0] != consts.EMPTY_SPACE and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            # Check col:
            if self.board[0][i] != consts.EMPTY_SPACE and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]

        # Check diagonals:
        if self.board[1][1] != consts.EMPTY_SPACE:
            if self.board[0][0] == self.board[1][1] == self.board[2][2]:
                return self.board[1][1]
            elif self.board[2][0] == self.board[1][1] == self.board[0][2]:
                return self.board[1][1]
        # No winner
        return consts.EMPTY_SPACE

    def isFull(self):
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j] == consts.EMPTY_SPACE:
                    # Board is not full
                    return False
        # Board is full    
        return True
    # Helps the AI do first move
    def isEmpty(self):
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j] != consts.EMPTY_SPACE:
                    # Board is not empty
                    return False
        # Board is empty    
        return True

    def TryMove(self, row, col, playerType):
        # Safety check
        if row > 2 or col > 2 or row < 0 or col < 0:
            return False
        if self.board[row][col] == consts.EMPTY_SPACE:
            self.board[row][col] = playerType
            return True

        return False
    def GetCopy(self):
        boardCopy = GameBoard()
        for i in range(0,3):
            for j in range(0,3):
                boardCopy.board[i][j] = self.board[i][j]
        return boardCopy

class TicTacToeAIBattle():
    def __init__(self):
        self.xWins = 0
        self.oWins = 0
        self.draws = 0

        self.p1Turn = True
        self.gameOver = False

        self.p1 = AI.TicTacToeAI(consts.PLAYER_X)
        self.p2 = AI.TicTacToeAI(consts.PLAYER_O)

        self.board = GameBoard()
    
    def takeTurn(self):
        # Check if game is still playing:
        if self.gameOver == True:
            return False

        # Take Turn
        if self.p1Turn:
            self.p1.takeTurn(self.board)
            self.p1Turn = False
        else:
            self.p2.takeTurn(self.board)
            self.p1Turn = True
        # Check for a winner
        winner = self.board.checkWin()
        if winner != consts.EMPTY_SPACE:
            if winner == consts.PLAYER_O:
                self.oWins += 1
            else:
                self.xWins += 1
            self.gameOver = True

        # Check for a draw (board full)
        if self.board.isFull():
            self.draws += 1
            self.gameOver = True

    def resetGame(self):
        self.board.resetBoard()
        self.gameOver = False
        self.p1 = AI.TicTacToeAI(consts.PLAYER_X)
        self.p2 = AI.TicTacToeAI(consts.PLAYER_O)

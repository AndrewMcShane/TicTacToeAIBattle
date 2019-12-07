import GameConstants as consts
import random

class TicTacToeAI():
    def __init__(self, playerType):
        self.playerType = playerType
        self.turnsTaken = 0

    def takeTurn(self, board):
        opponent = consts.PLAYER_X
        if self.playerType == consts.PLAYER_X:
            opponent = consts.PLAYER_O
        # Make the first move in a corner or center
        if board.isEmpty():
            corner = random.randint(0,4)
            if corner == 0:
                board.TryMove(0,0, self.playerType)
            elif corner == 1:
                board.TryMove(0,2, self.playerType)
            elif corner == 2:
                board.TryMove(2,0, self.playerType)
            elif corner == 3:
                board.TryMove(2,2, self.playerType)
            else: # Center move
                board.TryMove(1,1, self.playerType)
            self.turnsTaken += 1
        # Continue algorithm
        # Not empty, but let's see how many moves have been taken:
        elif self.turnsTaken == 0:
            # Board isn't empty, but 0 turns taken: we are player 2
            # First, check center, otherwise pick a corner.
            if board.TryMove(1,1, self.playerType) == False:
                corner = random.randint(0,3)
                if corner == 0:
                    board.TryMove(0,0, self.playerType)
                elif corner == 1:
                    board.TryMove(0,2, self.playerType)
                elif corner == 2:
                    board.TryMove(2,0, self.playerType)
                else:
                    board.TryMove(2,2, self.playerType)
                self.turnsTaken += 1
                return
            else:
                # center move worked, increase turns taken. (Yeah, awkward syntax)
                self.turnsTaken += 1
                return
        # Neither player's first turn: 
        else:
            # 0. Edge case: opponent went first and did a "cross": need to counter with a side
            if self.turnsTaken == 1 and board.board[1][1] == self.playerType:
                # Check for the cross:
                if board.board[0][0] == opponent and board.board[2][2] == opponent:
                    # pick a side:
                    # 4. Check for any open side:
                    if board.TryMove(0,1, self.playerType) == True:
                        self.turnsTaken += 1
                        return
                    elif board.TryMove(1,2, self.playerType) == True:
                        self.turnsTaken += 1
                        return
                    elif board.TryMove(2,1, self.playerType) == True:
                        self.turnsTaken += 1
                        return
                    elif board.TryMove(1,0, self.playerType) == True:
                        self.turnsTaken += 1
                        return
                elif board.board[2][0] == opponent and board.board[0][2] == opponent:
                    if board.TryMove(0,1, self.playerType) == True:
                        self.turnsTaken += 1
                        return
                    elif board.TryMove(1,2, self.playerType) == True:
                        self.turnsTaken += 1
                        return
                    elif board.TryMove(2,1, self.playerType) == True:
                        self.turnsTaken += 1
                        return
                    elif board.TryMove(1,0, self.playerType) == True:
                        self.turnsTaken += 1
                        return
                # Else, no cross attempted, continue checking.

            # 1. Check for a winning move'
                ## easy out: less than 2 turns taken:
            if self.turnsTaken >= 2:
                boardCopy = board.GetCopy()
                ## Attempt a move at any place on the board to see if a win condition happens
                for i in range(0,3):
                    for j in range(0,3):
                        if boardCopy.TryMove(i,j,self.playerType) == True:
                            if boardCopy.checkWin() == self.playerType:
                                # Winning move, do the actual turn and exit:
                                board.TryMove(i, j, self.playerType)
                                self.turnsTaken += 1
                                return
                            else:
                                boardCopy.board[i][j] = consts.EMPTY_SPACE
            # 2. Check for a defensive move
                ## Essentially, check if any opponent move results in a win, then make that move with our piece.
            boardCopy = board.GetCopy()
            for i in range(0,3):
                for j in range(0,3):
                    if boardCopy.TryMove(i,j, opponent) == True:
                        if boardCopy.checkWin() == opponent:
                            # Opponent would have a winning move, cut them off:
                            board.TryMove(i, j, self.playerType)
                            self.turnsTaken += 1
                            return
                        else:
                            boardCopy.board[i][j] = consts.EMPTY_SPACE
            
            # 3. Check for an empty corner:
            if board.TryMove(0,0, self.playerType) == True:
                self.turnsTaken += 1
                return
            elif board.TryMove(0,2, self.playerType) == True:
                self.turnsTaken += 1
                return
            elif board.TryMove(2,0, self.playerType) == True:
                self.turnsTaken += 1
                return
            elif board.TryMove(2,2, self.playerType) == True:
                self.turnsTaken += 1
                return
                

            # 4. Check for any open side:
            if board.TryMove(0,1, self.playerType) == True:
                self.turnsTaken += 1
                return
            elif board.TryMove(1,2, self.playerType) == True:
                self.turnsTaken += 1
                return
            elif board.TryMove(2,1, self.playerType) == True:
                self.turnsTaken += 1
                return
            elif board.TryMove(1,0, self.playerType) == True:
                self.turnsTaken += 1
                return

            ## We shouldn't ever make it here, if we did, the ai has no move.

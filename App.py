import TicTacToeGame as TicTacToe
import tkinter as tk
from tkinter import StringVar
import time
import math

class TicTacToeGui(tk.Tk):
    def __init__(self, game, maxPlays=5):
        # Super init:
        tk.Tk.__init__(self)
        self.title("AI Tic-Tac-Toe")
        self.resizable(False, False)
        # Game ref
        self.gameRef = game
        self.gamesPlayed = 0
        self.maxPlays = maxPlays
        # Boxes
        self.boxes = []
        self.bindingVars = []
        self.configure(bg="#201f1e")
        
        fontStr = "verdana 36"
        boxColor = "#2d2d2d"
        fontCol = "#ffffff"
        
        boxPad = 15
        boxMargin = 5
        for dummyi in range(0,3):
            row = []
            bindRow = []
            for dummyj in range(0,3):
                v = StringVar()
                v.set("-")
                bindRow.append(v)
                row.append(tk.Label(self, textvariable=v, font=fontStr, bg=boxColor, padx=boxPad, pady=boxPad, fg=fontCol))
            self.boxes.append(row)
            self.bindingVars.append(bindRow)
            
        # Stats
            ## string vars for update
        self.xWinsStrV = StringVar()
        self.xWinsStrV.set("X: 0")
        self.oWinsStrV = StringVar()
        self.oWinsStrV.set("O: 0")
        self.drawsStrV = StringVar()
        self.drawsStrV.set("DRAWS: 0")
        self.xWins = tk.Label(self, textvariable=self.xWinsStrV, padx=boxPad, pady=boxPad, font=fontStr, bg=boxColor, fg=fontCol)
        self.oWins = tk.Label(self, textvariable=self.oWinsStrV, padx=boxPad, pady=boxPad, font=fontStr, bg=boxColor, fg=fontCol)
        self.draws = tk.Label(self, textvariable=self.drawsStrV, padx=boxPad, pady=boxPad, font=fontStr, bg=boxColor, fg=fontCol)

        # Bind
        for i in range(0,3):
            for j in range(0,3):
                self.boxes[i][j].grid(row=i, column=j, padx=boxMargin, pady=boxMargin, sticky='nsew')
            self.grid_columnconfigure(i, minsize=100)
            self.grid_rowconfigure(i, minsize=100)

                
        self.xWins.grid(row=3, column=0,padx=boxMargin, pady=boxMargin, sticky='nsew')
        self.oWins.grid(row=3, column=2, padx=boxMargin, pady=boxMargin, sticky='nsew')

        self.draws.grid(row=4, column=0, padx=boxMargin, pady=boxMargin, columnspan=3, sticky='nsew')

    def updateDisplay(self):
        # Update game:
        if self.gameRef.gameOver == False:
            self.gameRef.takeTurn()
        else:
            self.gamesPlayed += 1
            game.resetGame()
            
        # Bind
        for i in range(0,3):
            for j in range(0,3):
                txt = self.gameRef.board.board[i][j]
                self.bindingVars[i][j].set(txt.upper())
        
        self.xWinsStrV.set("X: " + str(self.gameRef.xWins))
        self.oWinsStrV.set("O: " + str(self.gameRef.oWins))
        self.drawsStrV.set("DRAWS: " + str(self.gameRef.draws))

        if self.gamesPlayed < self.maxPlays:
            self.after(1000, self.updateDisplay)



# Actual game:
game = TicTacToe.TicTacToeAIBattle()
#implement gui. math.inf == never ending unless interuppted. Makes for a nice desktop toy ;)
root = TicTacToeGui(game, math.inf)
# update the call after 1 second
root.after(1000, root.updateDisplay)
root.mainloop()


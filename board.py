# author: Sachin Jain
# date: 1 May, 2023
# file: board.py a Python program that implements board in a tic-tac-toe game
# input: Board
# output: prints Board

class Board:
       def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            # the winner's sign O or X
            self.winner = ""
       def get_size(self):
           return self.size
             # optional, return the board size (an instance size)
       def get_winner(self):
           return self.winner
            # return the winner's sign O or X (an instance winner)     
       def set(self, cell, sign):
            # mark the cell on the board waith the sign X or O
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            index = valid_choices.index(cell)
            self.board[index] = sign

       def isempty(self, cell):
           valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
           index = valid_choices.index(cell)
           if self.board[index] == ' ':
               return True
           else:
               return False


       def isdone(self):
           done = False
           self.winner = ''
           # check all game terminating conditions, if one of them is present, assign the var done to True
           # depending on conditions assign the instance var winner to O or X

           # check for a diagonal win (top-left to bottom-right)
           if self.board[0] == self.board[4] == self.board[8] != ' ':
               done = True
               self.winner = self.board[0]


           elif self.board[6] == self.board[4] == self.board[2] != ' ':
               done = True
               self.winner = self.board[6]

           elif self.board[0] == self.board[1] == self.board[2] != ' ':
               done = True
               self.winner = self.board[0]
           elif self.board[3] == self.board[4] == self.board[5] != ' ':
               done = True
               self.winner = self.board[3]
           elif self.board[6] == self.board[7] == self.board[8] != ' ':
               done = True
               self.winner = self.board[6]

           # check for a column win
           elif self.board[0] == self.board[3] == self.board[6] != ' ':
               done = True
               self.winner = self.board[0]
           elif self.board[1] == self.board[4] == self.board[7] != ' ':
               done = True
               self.winner = self.board[1]
           elif self.board[2] == self.board[5] == self.board[8] != ' ':
               done = True
               self.winner = self.board[2]

           # check for a tie
           elif ' ' not in self.board:
               done = True


           return done

       def show(self):
            # draw the board
            # need to complete the code
            print('   A   B   C') 
            print(' +---+---+---+')
            print('1| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2]))
            print(' +---+---+---+')
            print('2| {} | {} | {} |'.format(self.board[3], self.board[4], self.board[5]))
            print(' +---+---+---+')
            print('3| {} | {} | {} |'.format(self.board[6], self.board[7], self.board[8]))
            print(' +---+---+---+')

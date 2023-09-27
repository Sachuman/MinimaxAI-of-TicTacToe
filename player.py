# author: Sachin Jain
# date: 1 May, 2023
# file: player.py a Python program that implements a player class in a tic-tac-toe game
# input: Player
# output: finds the right outcome of the tic tac toe

import random


class Player:

      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            return self.sign
            # return an instance sign
      def get_name(self):
            return self.name
            # return an instance name
      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            while True: 
                  cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n').upper()
                  if cell in valid_choices:
                        if board.isempty(cell):
                              board.set(cell, self.sign)
                              break
                        else:
                              print("You did not choose correctly. ")
                  else:
                        print("You did not choose correctly. ")

class AI(Player):
      def __init__(self, name, sign, board):
            super().__init__(name, sign)
            self.board = board.board

      def get_sign(self):
            return self.sign
            # return an instance sign
      def get_name(self):
            return self.name

      def choose(self, board):
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']


            print(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ')
            while True:
                  cell = random.choice(valid_choices)


                  if board.isempty(cell):
                        board.set(cell, self.sign)
                        print(cell)
                        break

                  elif not board.isempty(cell):
                        valid_choices.remove(cell)



class MiniMax(AI):
      def choose(self, board):
            if self.sign == "O":
                  self.opponent_sign = "X"

            elif self.sign == "X":
                  self.opponent_sign = "O"
            print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
            cell = MiniMax.minimax(self, board, True, True)
            print(cell)
            board.set(cell, self.sign)


      def minimax(self, board, self_player, start):

            # check the base conditions
            if board.isdone():
                  if board.get_winner() == self.sign:
                        return 1
                  elif board.get_winner() == '':
                        return 0
                  else:
                        return -1

            maxscore = -1000  # any score < this
            minscore = 1000  # any score > this
                  # choose a cell & make a move
            moves = " "
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']

            for cell in valid_choices:
              if board.isempty(cell):
                    if self_player:
                          board.set(cell, self.sign)
                          score = self.minimax(board, False, False)
                          if score > maxscore:
                                maxscore = score
                                moves = cell

                    else:
                          board.set(cell, self.opponent_sign)
                          score = self.minimax(board, True, False)
                          if score < minscore:
                                minscore = score
                                moves = cell

                    board.set(cell, " ")

                    # for every move possible we do the algorithm
            if start:
                  return moves

            elif self_player:
                  return maxscore
            else:
                  return minscore


class SmartAI(AI):


      def choose(self, board):
            if self.sign == "O":
                  self.opponent_sign = "X"

            elif self.sign == "X":
                  self.opponent_sign = "O"

            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']


            print(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ')
            while True:

                  if self.board[0] == self.board[1] == self.sign and self.board[2] == " ":
                        board.set(valid_choices[2], self.sign)
                        print(valid_choices[2])
                        return True
                  elif self.board[1] == self.board[2] == self.sign and self.board[0] == " ":
                        board.set(valid_choices[0], self.sign)
                        print(valid_choices[0])
                        return True
                  elif self.board[0] == self.board[2] == self.sign and self.board[1] == " ":
                        board.set(valid_choices[1], self.sign)
                        print(valid_choices[1])
                        return True
                  elif self.board[0] == self.board[4] == self.sign and self.board[8] == " ":
                        board.set(valid_choices[8], self.sign)
                        print(valid_choices[8])
                        return True
                  elif self.board[4] == self.board[8] == self.sign and self.board[0] == " ":
                        board.set(valid_choices[0], self.sign)
                        print(valid_choices[0])
                        return True
                  elif self.board[0] == self.board[8] == self.sign and self.board[4] == " ":
                        board.set(valid_choices[4], self.sign)
                        print(valid_choices[4])
                        return True
                  elif self.board[3] == self.board[4] == self.sign and self.board[5] == " ":
                        board.set(valid_choices[5], self.sign)
                        print(valid_choices[5])
                        return True
                  elif self.board[3] == self.board[5] == self.sign and self.board[4] == " ":
                        board.set(valid_choices[4], self.sign)
                        print(valid_choices[4])
                        return True
                  elif self.board[4] == self.board[5] == self.sign and self.board[3] == " ":
                        board.set(valid_choices[3], self.sign)
                        print(valid_choices[3])
                        return True
                  elif self.board[4] == self.board[6] == self.sign and self.board[2] == " ":
                        board.set(valid_choices[2], self.sign)
                        print(valid_choices[2])
                        return True
                  elif self.board[4] == self.board[2] == self.sign and self.board[6] == " ":
                        board.set(valid_choices[6], self.sign)
                        print(valid_choices[6])
                        return True
                  elif self.board[2] == self.board[6] == self.sign and self.board[4] == " ":
                        board.set(valid_choices[4], self.sign)
                        print(valid_choices[4])
                        return True
                  elif self.board[7] == self.board[8] == self.sign and self.board[6] == " ":
                        board.set(valid_choices[6], self.sign)
                        print(valid_choices[6])
                        return True
                  elif self.board[6] == self.board[8] == self.sign and self.board[7] == " ":
                        board.set(valid_choices[7], self.sign)
                        print(valid_choices[7])
                        return True
                  elif self.board[6] == self.board[7] == self.sign and self.board[8] == " ":
                        board.set(valid_choices[8], self.sign)
                        print(valid_choices[8])
                        return True
                  elif self.board[2] == self.board[8] == self.sign and self.board[5] == " ":
                        board.set(valid_choices[5], self.sign)
                        print(valid_choices[5])
                        return True
                  elif self.board[2] == self.board[5] == self.sign and self.board[8] == " ":
                        board.set(valid_choices[8], self.sign)
                        print(valid_choices[8])
                        return True
                  elif self.board[5] == self.board[8] == self.sign and self.board[2] == " ":
                        board.set(valid_choices[2], self.sign)
                        print(valid_choices[2])
                        return True
                  elif self.board[1] == self.board[4] == self.sign and self.board[7] == " ":
                        board.set(valid_choices[7], self.sign)
                        print(valid_choices[7])
                        return True
                  elif self.board[4] == self.board[7] == self.sign and self.board[1] == " ":
                        board.set(valid_choices[1], self.sign)
                        print(valid_choices[1])
                        return True
                  elif self.board[1] == self.board[4] == self.sign and self.board[7] == " ":
                        board.set(valid_choices[7], self.sign)
                        print(valid_choices[7])
                        return True
                  elif self.board[3] == self.board[6] == self.sign and self.board[0] == " ":
                        board.set(valid_choices[0], self.sign)
                        print(valid_choices[0])
                        return True
                  elif self.board[0] == self.board[6] == self.sign and self.board[3] == " ":
                        board.set(valid_choices[3], self.sign)
                        print(valid_choices[3])
                        return True
                  elif self.board[0] == self.board[3] == self.sign and self.board[6] == " ":
                        board.set(valid_choices[6], self.sign)
                        print(valid_choices[6])
                        return True

                  if self.board[0] == self.board[1] == self.opponent_sign and self.board[2] == " ":
                        board.set(valid_choices[2], self.sign)
                        print(valid_choices[2])
                        return True
                  elif self.board[1] == self.board[2] == self.opponent_sign and self.board[0] == " ":
                        board.set(valid_choices[0], self.sign)
                        print(valid_choices[0])
                        return True
                  elif self.board[0] == self.board[2] == self.opponent_sign and self.board[1] == " ":
                        board.set(valid_choices[1], self.sign)
                        print(valid_choices[1])
                        return True
                  elif self.board[4] == self.board[6] == self.opponent_sign and self.board[2] == " ":
                        board.set(valid_choices[2], self.sign)
                        print(valid_choices[2])
                        return True
                  elif self.board[4] == self.board[2] == self.opponent_sign and self.board[6] == " ":
                        board.set(valid_choices[6], self.sign)
                        print(valid_choices[6])
                        return True
                  elif self.board[6] == self.board[2] == self.opponent_sign and self.board[4] == " ":
                        board.set(valid_choices[4], self.sign)
                        print(valid_choices[4])
                        return True
                  elif self.board[0] == self.board[4] == self.opponent_sign and self.board[8] == " ":
                        board.set(valid_choices[8], self.sign)
                        print(valid_choices[8])
                        return True
                  elif self.board[4] == self.board[8] == self.opponent_sign and self.board[0] == " ":
                        board.set(valid_choices[0], self.sign)
                        print(valid_choices[0])
                        return True
                  elif self.board[0] == self.board[8] == self.opponent_sign and self.board[4] == " ":
                        board.set(valid_choices[4], self.sign)
                        print(valid_choices[4])
                        return True

                  elif self.board[3] == self.board[4] == self.opponent_sign and self.board[5] == " ":
                        board.set(valid_choices[5], self.sign)
                        print(valid_choices[5])
                        return True
                  elif self.board[3] == self.board[5] == self.opponent_sign and self.board[4] == " ":
                        board.set(valid_choices[4], self.sign)
                        print(valid_choices[4])
                        return True
                  elif self.board[4] == self.board[5] == self.opponent_sign and self.board[3] == " ":
                        board.set(valid_choices[3], self.sign)
                        print(valid_choices[3])
                        return True

                  elif self.board[2] == self.board[8] == self.opponent_sign and self.board[5] == " ":
                        board.set(valid_choices[5], self.sign)
                        print(valid_choices[5])
                        return True
                  elif self.board[6] == self.board[8] == self.opponent_sign and self.board[7] == " ":
                        board.set(valid_choices[7], self.sign)
                        print(valid_choices[7])
                        return True
                  elif self.board[6] == self.board[7] == self.opponent_sign and self.board[8] == " ":
                        board.set(valid_choices[8], self.sign)
                        print(valid_choices[8])
                        return True
                  elif self.board[7] == self.board[8] == self.opponent_sign and self.board[6] == " ":
                        board.set(valid_choices[6], self.sign)
                        print(valid_choices[6])
                        return True
                  elif self.board[5] == self.board[8] == self.opponent_sign and self.board[2] == " ":
                        board.set(valid_choices[2], self.sign)
                        print(valid_choices[2])
                        return True
                  elif self.board[2] == self.board[5] == self.opponent_sign and self.board[8] == " ":
                        board.set(valid_choices[8], self.sign)
                        print(valid_choices[8])
                        return True
                  elif self.board[1] == self.board[4] == self.opponent_sign and self.board[7] == " ":
                        board.set(valid_choices[7], self.sign)
                        print(valid_choices[7])
                        return True
                  elif self.board[4] == self.board[7] == self.opponent_sign and self.board[1] == " ":
                        board.set(valid_choices[1], self.sign)
                        print(valid_choices[1])
                        return True
                  elif self.board[1] == self.board[4] == self.opponent_sign and self.board[7] == " ":
                        board.set(valid_choices[7], self.sign)
                        print(valid_choices[7])
                        return True
                  elif self.board[3] == self.board[6] == self.opponent_sign and self.board[0] == " ":
                        board.set(valid_choices[0], self.sign)
                        print(valid_choices[0])
                        return True
                  elif self.board[0] == self.board[6] == self.opponent_sign and self.board[3] == " ":
                        board.set(valid_choices[3], self.sign)
                        print(valid_choices[3])
                        return True
                  elif self.board[0] == self.board[3] == self.opponent_sign and self.board[6] == " ":
                        board.set(valid_choices[6], self.sign)
                        print(valid_choices[6])
                        return True


                  else:
                        if self.sign == "X":
                              if self.board[0] == " ":
                                    board.set(valid_choices[0], self.sign)
                                    print(valid_choices[0])
                              elif self.board[2] == " ":
                                    board.set(valid_choices[2], self.sign)
                                    print(valid_choices[2])
                              elif self.board[4] == " ":
                                    board.set(valid_choices[4], self.sign)
                                    print(valid_choices[4])
                              elif self.board[6] == " ":
                                    board.set(valid_choices[6], self.sign)
                                    print(valid_choices[6])
                              elif self.board[8] == " ":
                                    board.set(valid_choices[8], self.sign)
                                    print(valid_choices[8])
                              break
                        else:
                              if self.board[4] == " ":
                                    board.set(valid_choices[4], self.sign)
                                    print(valid_choices[4])
                              elif self.board[2] == " ":
                                    board.set(valid_choices[2], self.sign)
                                    print(valid_choices[2])
                              elif self.board[6] == " ":
                                    board.set(valid_choices[6], self.sign)
                                    print(valid_choices[6])
                              elif self.board[8] == " ":
                                    board.set(valid_choices[8], self.sign)
                                    print(valid_choices[8])
                              elif self.board[1] == " ":
                                    board.set(valid_choices[1], self.sign)
                                    print(valid_choices[1])
                              elif self.board[3] == " ":
                                    board.set(valid_choices[3], self.sign)
                                    print(valid_choices[3])
                              elif self.board[5] == " ":
                                    board.set(valid_choices[5], self.sign)
                                    print(valid_choices[5])
                              elif self.board[7] == " ":
                                    board.set(valid_choices[7], self.sign)
                                    print(valid_choices[7])

                              else:
                                    board.set(valid_choices[0], self.sign)
                                    print(valid_choices[0])
                              break



from wsgiref.simple_server import WSGIRequestHandler
from Game.game import Game, BoardException


class UI:

    def __init__(self):
        # Initializing our game with none, as no size of the board has been read
        self.__game = None

    def welcome(self):
        # Introduction prompt
        print("\tWelcome to the Obstruction game, where rules are pretty simple.\n" +
              "First player puts a piece, which blocks all of the surroundings of that piece for the second player and so on.\n")
        ans = input("Are you ready to play?(y/n) ")
        if ans.lower() == "y" or ans.lower() == "yes":
            # Initializing the size arg for the game
            size = input("Enter a size for the board (must be >= 6)")
            while size.isnumeric() is False:
                size = input("Wrong input, try again!")
            size = int(size)
            try:
                self.__game = Game(size)
                return size
            except BoardException as be:
                print(be)
                return

        print("Ok then, maybe later!")
        return None

    def start(self):
        # Allows player to choose a place to position their move
        player = 0
        while True:
            print(self.__game.__str__())
            if player == 0:
                pos = input("Position of player 1: ")
                player = 1
            else:
                pos = input("Position of player 2: ")
                player = 0
            pos_cor = pos.split(sep=" ")

            # Checking if positions are inputed correctly
            while (pos_cor[0].isnumeric() is False and pos_cor[1].isnumeric() is False) or len(pos_cor) < 2:
                pos = input("Wrong coordinates fam, try again: ")
                pos_cor = pos.split(sep=" ")

            # After the checks, the move is made
            position = (int(pos_cor[0]), int(pos_cor[1]))

            # Prints the error message in case one of the players tries to put a piece in the wrong place
            try:
                self.__game.put_piece(position)
            except BoardException as be:
                print(be)

            # Checking if there is a winner
            if self.__game.check_win() == 0:
                print(self.__game.__str__())
                print("Player 2 won!")
                return
            elif self.__game.check_win() == 1:
                print(self.__game.__str__())
                print("Player 1 won!")
                return
            else:
                continue

from Board.board import Board, BoardException

class Game:
    """
        Wrapper for the game, here all the functionalities will be listed.
    """

    def __init__(self, bd_size:int):
        self.__board = Board(bd_size)
        self.__player = 0 # will be used to determine which player is moving

    def put_piece(self, position:tuple):
        # Case when the first player puts a piece
        if(self.__player == 0):
            self.__board.setPosition(position, "O") 
            self.__player = 1

        # Case when the second player puts a piece
        else:
            self.__board.setPosition(position, "Y")
            self.__player = 0

    def check_win(self):
        # Checking if there are still free spots
        for i in range(self.__board.getSize()):
            for j in range(self.__board.getSize()):
                if self.__board.getPosition((i,j)) == '- ':
                    return None

        # In case of no free spots, it should return the player's number
        return self.__player

    def __str__(self):
        return self.__board.__str__()

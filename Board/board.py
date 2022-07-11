from Exceptions.exceptions import BoardException


class Board:
    """
        The board for the obstruction game, size of the board is given.
        Size must be greater or equal to 6, because otherwise none of the players can move.
    """
    def __init__(self, size):
        if size <= 6:
            raise BoardException("Size of board is not enough")
        self.__size = size
        self.__bd = list()
        for i in range(self.__size):
            self.__bd.append(list())
            for j in range(self.__size):
                self.__bd[i].append('- ')

    def setPosition(self, position:tuple, player:int):
        """
            Setter, throws error in case of wrong input.
        """
        if position[0] < 0 or position[0] >6:
            raise BoardException("Invalid positions")
        if position[1] < 0 or position[1] > 6:
            raise BoardException("Invalid positions")
        self.__bd[position[0]-1][position[1]-1]=player
    

    def __str__(self):
        final_str = ""
        for i in range(self.__size):
            for j in range(self.__size):
                final_str=final_str+str(self.__bd[i][j])
            final_str+='\n'
        return final_str

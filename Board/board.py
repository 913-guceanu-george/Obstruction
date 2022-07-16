from Exceptions.exceptions import BoardException


class Board:
    """
        The board for the obstruction game, size of the board is given.
        Size must be greater or equal to 6, because otherwise none of the players can move.
    """

    def __init__(self, size: int):
        if size < 6:
            raise BoardException("Size of board is not enough")
        self.__size = size
        self.__bd = list()
        for i in range(self.__size):
            self.__bd.append(list())
            for j in range(self.__size):
                self.__bd[i].append('- ')

    def getSize(self):
        """
            Getter function
        """
        return self.__size

    def getPosition(self, position: tuple):
        """
            Getter function
        """
        return self.__bd[position[0]][position[1]]

    def setPosition(self, position: tuple, player):
        """
            Setter, throws error in case of wrong input.
        """
        x = position[0] - 1
        y = position[1] - 1
        if position[0] < 1 or position[0] > self.__size:
            raise BoardException("Invalid positions")
        if position[1] < 1 or position[1] > self.__size:
            raise BoardException("Invalid positions")
        if self.__bd[x][y] != 'x ' and self.__bd[x][y] != "O " and self.__bd[x][y] != "Y ":
            self.__bd[x][y] = str(player) + " "

            # Checking corner cases

            if x == 0 and y == 0:  # Top left corner
                self.__bd[x+1][y] = "x "
                self.__bd[x+1][y+1] = "x "
                self.__bd[x][y+1] = "x "
                return

            if x == 0 and y == self.__size - 1:  # Top right corner
                self.__bd[x][y-1] = "x "
                self.__bd[x+1][y] = "x "
                self.__bd[x+1][y-1] = "x "
                return

            if x == self.__size - 1 and y == 0:  # Bottom left corner
                self.__bd[x-1][y] = "x "
                self.__bd[x][y+1] = "x "
                self.__bd[x-1][y+1] = "x "
                return

            if x == self.__size - 1 and y == self.__size - 1:  # Bottom right corner
                self.__bd[x-1][y-1] = "x "
                self.__bd[x-1][y] = "x "
                self.__bd[x][y-1] = "x "
                return

            # Checking rail cases
            if x == 0 and y != 0 and y != self.__size - 1:  # Top rail
                self.__bd[x][y-1] = "x "
                self.__bd[x+1][y-1] = "x "
                self.__bd[x+1][y] = "x "
                self.__bd[x+1][y+1] = "x "
                self.__bd[x][y+1] = "x "
                return

            if x == self.__size - 1 and y != 0 and y != self.__size - 1:  # Bottom rail
                self.__bd[x][y-1] = "x "
                self.__bd[x-1][y] = "x "
                self.__bd[x-1][y+1] = "x "
                self.__bd[x-1][y-1] = "x "
                self.__bd[x][y+1] = "x "
                return

            if y == 0 and x != 0 and x != self.__size - 1:  # Left rail
                self.__bd[x-1][y] = "x "
                self.__bd[x][y+1] = "x "
                self.__bd[x-1][y+1] = "x "
                self.__bd[x+1][y+1] = "x "
                self.__bd[x+1][y] = "x "
                return

            if y == self.__size - 1 and x != 0 and x != self.__size - 1:  # Right rail
                self.__bd[x-1][y] = "x "
                self.__bd[x+1][y] = "x "
                self.__bd[x-1][y-1] = "x "
                self.__bd[x+1][y-1] = "x "
                self.__bd[x][y-1] = "x "
                return

            # The rest of the pieces
            self.__bd[x-1][y-1] = "x "   # Top left box
            self.__bd[x-1][y] = "x "     # Top box
            self.__bd[x-1][y+1] = "x "   # Top right box
            self.__bd[x][y-1] = "x "     # Left box
            self.__bd[x][y+1] = "x "    # Right box
            self.__bd[x+1][y-1] = "x "   # Bottom left box
            self.__bd[x+1][y] = "x "     # Bottom box
            self.__bd[x+1][y+1] = "x "   # Bottom right box
            return

        raise BoardException("Wrong position fam")

    def __str__(self):
        """
            Overriding the __str__ function so that we can use str(Board) to print it.
        """
        final_str = ""
        for i in range(self.__size):
            if i == 0:
                final_str += "  "
                for k in range(self.__size):
                    final_str += str(k+1) + " "
                final_str += "\n"
            final_str += str(i+1) + " "
            for j in range(self.__size):
                final_str = final_str+str(self.__bd[i][j])
            final_str += '\n'
        return final_str

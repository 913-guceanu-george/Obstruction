from Board.board import Board

def __main__():
    b = Board(6)
    b.setPosition((2, 3), 1)
    print(b.__str__())


if __name__=="__main__":
    __main__()

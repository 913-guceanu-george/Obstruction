from Board.board import Board

def __main__():
    b = Board(6)
    b.setPosition((2, 3), 1)
    b.setPosition((4,2), 2)
    print(b.__str__())
    b.setPosition((2,4), 1)


if __name__=="__main__":
    __main__()

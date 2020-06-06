import board as b


def startBoardCorrect():

    if type(b.startBoard()) != list:
        return print('Wrong board.')
    else:
        pass

startBoardCorrect()

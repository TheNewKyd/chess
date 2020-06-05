import board as b

def makeBoardCorrect():
    if type(b.makeBoard()) != list:
        return print("Sth is wrong in makeBoard.")
    else:
        pass

makeBoardCorrect()

def fillUpBoardCorrect():
    cortb_ = [['BR', 'BKN', 'BB', 'BQ', 'BK', 'BB', 'BKN', 'BR'],
              ['BP0', 'BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6', 'BP7'],
              [None, None, None, None, None, None, None, None],
              [None, None, None, None, None, None, None, None],
              [None, None, None, None, None, None, None, None],
              [None, None, None, None, None, None, None, None],
              ['WP0', 'WP1', 'WP2', 'WP3', 'WP4', 'WP5', 'WP6', 'WP7'],
              ['WR', 'WKN', 'WB', 'WQ', 'WK', 'WB', 'WKN', 'WR']]

    if b.fillUpBoard() != cortb_:
        print(b.fillUpBoard())
        return print('Wrong board.')
    else:
        pass

fillUpBoardCorrect()

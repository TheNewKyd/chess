#python3!
#Chess
#Game allows:
#   - to move figures accordingly to rules
#   - to "take" opponent's figures
#   - not to "take" yourselfs
#   - to win/lose the match
#   - to castle
#   - can/can't jump above other figures

import pyinputplus as pyip
import knight as kn
import rook as r
import bishop as bp
import queen as q
import king as k
import board as b
import figures as f
import pawn_w0 as pw0
import pawn_w1 as pw1
import pawn_w2 as pw2
import pawn_w3 as pw3
import pawn_w4 as pw4
import pawn_w5 as pw5
import pawn_w6 as pw6
import pawn_w7 as pw7
import pawn_b0 as pb0
import pawn_b1 as pb1
import pawn_b2 as pb2
import pawn_b3 as pb3
import pawn_b4 as pb4
import pawn_b5 as pb5
import pawn_b6 as pb6
import pawn_b7 as pb7

from tabulate import tabulate

chess_figures_ = ['BR1', 'BKN', 'BB1', 'BQ', 'BK', 'BB2', 'BKN2', 'BR2',
                  'BP0', 'BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6', 'BP7',
                  'WP0', 'WP1', 'WP2', 'WP3', 'WP4', 'WP5', 'WP6', 'WP7',
                  'WR1', 'WKN1', 'WB1', 'WQ', 'WK', 'WB2', 'WKN2', 'WR2']

moves_ = {"A1": (7, 1), "A2": (6, 1), "A3": (5, 1), "A4": (4, 1),
          "A5": (3, 1), "A6": (2, 1), "A7": (1, 1), "A8": (0, 1),
          "B1": (7, 2), "B2": (6, 2), "B3": (5, 2), "B4": (4, 2),
          "B5": (3, 2), "B6": (2, 2), "B7": (1, 2), "B8": (0, 2),
          "C1": (7, 3), "C2": (6, 3), "C3": (5, 3), "C4": (4, 3),
          "C5": (3, 3), "C6": (2, 3), "C7": (1, 3), "C8": (0, 3),
          "D1": (7, 4), "D2": (6, 4), "D3": (5, 4), "D4": (4, 4),
          "D5": (3, 4), "D6": (2, 4), "D7": (1, 4), "D8": (0, 4),
          "E1": (7, 5), "E2": (6, 5), "E3": (5, 5), "E4": (4, 5),
          "E5": (3, 5), "E6": (2, 5), "E7": (1, 5), "E8": (0, 5),
          "F1": (7, 6), "F2": (6, 6), "F3": (5, 6), "F4": (4, 6),
          "F5": (3, 6), "F6": (2, 6), "F7": (1, 6), "F8": (0, 6),
          "G1": (7, 7), "G2": (6, 7), "G3": (5, 7), "G4": (4, 7),
          "G5": (3, 7), "G6": (2, 7), "G7": (1, 7), "G8": (0, 7),
          "H1": (7, 8), "H2": (6, 8), "H3": (5, 8), "H4": (4, 8),
          "H5": (3, 8), "H6": (2, 8), "H7": (1, 8), "H8": (0, 8),
         }

def newCoor(coor):
    return moves_[coor]

def isChessFigure(figure):
    while True:
        if figure in chess_figures_:
            return figure
            break
        else:
            return print("Try again")
            break
def isCoordinates(coor):
    if coor[0].isalpha() and coor[0].isupper():
        if coor[1].isdigit():
            return coor
        else:
            return print("Second coordinate is incorrect. It must be an intiger number")
    else:
        return print("First coordinate is incorrect. It must be an upper, english alphabeth letter.")

if __name__ == "__main__":

    mvcounts = 0
    fmlist_ = []
    fmk = 0
    fmlist_.append(fmk)
    fmr1 = 0
    fmlist_.append(fmr1)
    fmr2 = 0
    fmlist_.append(fmr2)
    fm_pw0 = 0
    fmlist_.append(fm_pw0)
    fm_pw1 = 0
    fmlist_.append(fm_pw1)
    fm_pw2 = 0
    fmlist_.append(fm_pw2)
    fm_pw3 = 0
    fmlist_.append(fm_pw3)
    fm_pw4 = 0
    fmlist_.append(fm_pw4)
    fm_pw5 = 0
    fmlist_.append(fm_pw5)
    fm_pw6 = 0
    fmlist_.append(fm_pw6)
    fm_pw7 = 0
    fmlist_.append(fm_pw7)
    fm_pb0 = 0
    fmlist_.append(fm_pb0)
    fm_pb1 = 0
    fmlist_.append(fm_pb1)
    fm_pb2 = 0
    fmlist_.append(fm_pb2)
    fm_pb3 = 0
    fmlist_.append(fm_pb3)
    fm_pb4 = 0
    fmlist_.append(fm_pb4)
    fm_pb5 = 0
    fmlist_.append(fm_pb5)
    fm_pb6 = 0
    fmlist_.append(fm_pb6)
    fm_pb7 = 0
    fmlist_.append(fm_pb7)

    nb_ = b.table()
    nbinfo_ = b.startBoard()

    while True:
        print(tabulate(nb_, tablefmt="grid"))
        figure = pyip.inputCustom(isChessFigure, "Figure: ")
        coor = pyip.inputCustom(isCoordinates, "Coordinates: ")
        nc_ = list(newCoor(coor))
        new_fmlist_ = []

        #king
        if figure == 'WK' or figure == 'BK':
            dict_, nb_, mate, draw, pat, check, mate = k.king(figure,
                                                                 fmlist_,
                                                                 mvcounts,
                                                                 nc_,
                                                                 nbinfo_,
                                                                 nb_)
            fmk += 1
            new_fmlist_.append(fmk)

            if mate:
                print(f'End of game, {f.whoseMove(mvcounts)} is the winner.')
                break

            if draw:
                print('Game ended with draw.')
                break

            if pat:
                print(f'End of game, {f.whoseMove(mvcounts)} is the winner.',
                        '\nGame ends with pat.')
                break

            if check:
                if figure == 'WK':
                    print('Blacks must move or cover king.')
                elif figure == 'BK':
                    print('WHites must move or cover king.')

        #queen
        elif figure == 'WQ' or figure == 'BQ':
            dict_, nb_ = q.queen(figure, mvcounts, nc_, nbinfo_, nb_)

        #bishop
        elif (figure == 'WB1' or figure == 'WB2' or
                figure == 'BB1' or figure == 'BB2'):
                dict_, nb_ = bp.bishop(figure, mvcounts, nc_, nbinfo_, nb_)

        #knight
        elif (figure == 'WKN1' or figure == 'WKN2' or
                figure == 'BKN1' or figure == 'BKN2'):
                dict_, nb_ = kn.knight(figure, mvcounts, nc_, nbinfo_, nb_)

        #rook
        elif (figure == 'WR1' or figure == 'WR2' or
            figure == 'BR1' or figure == 'BR2'):
            dict_, nb_ = r.rook(figure, mvcounts, nc_, nbinfo_, nb_)
            if '1' in figure:
                fmr1 += 1
                new_fmlist_.append(fmr1)
                new_fmlist_.append(fmr2)
            else:
                fmr2 += 1
                new_fmlist_.append(fmr1)
                new_fmlist_.append(fmr2)

        #pawn white 0
        elif figure == 'WP0':
            dict_, nb_ = pw0.pawn(nc_, nbinfo_, fm_pw0, nb_)
            fm_pw0 += 1
            new_fmlist_.append(fm_pw0)

        #pawn white 1
        elif figure == 'WP1':
            dict_, nb_ = pw1.pawn(nc_, nbinfo_, fm_pw1, nb_)
            fm_pw1 += 1
            new_fmlist_.append(fm_pw1)

        #pawn white 2
        elif figure == 'WP2':
            dict_, nb_ = pw2.pawn(nc_, nbinfo_, fm_pw2, nb_)
            fm_pw2 += 1
            new_fmlist_.append(fm_pw2)

        #pawn white 3
        elif figure == 'WP3':
            dict_, nb_ = pw3.pawn(nc_, nbinfo_, fm_pw3, nb_)
            fm_pw3 += 1
            new_fmlist_.append(fm_pw3)

        #pawn white 4
        elif figure == 'WP4':
            dict_, nb_ = pw4.pawn(nc_, nbinfo_, fm_pw4, nb_)
            fm_pw4 += 1
            new_fmlist_.append(fm_pw4)

        #pawn white 5
        elif figure == 'WP5':
            dict_, nb_ = pw5.pawn(nc_, nbinfo_, fm_pw5, nb_)
            fm_pw5 += 1
            new_fmlist_.append(fm_pw5)

        #pawn white 6
        elif figure == 'WP6':
            dict_, nb_ = pw6.pawn(nc_, nbinfo_, fm_pw6, nb_)
            fm_pw6 += 1
            new_fmlist_.append(fm_pw6)

        #pawn white 7
        elif figure == 'WP7':
            dict_, nb_ = pw7.pawn(nc_, nbinfo_, fm_pw7, nb_)
            fm_pw7 += 1
            new_fmlist_.append(fm_pw7)

        #pawn black 1
        elif figure == 'BP0':
            dict_, nb_ = pb0.pawn(nc_, nbinfo_, fm_pb0, nb_)
            fm_pb0 += 1
            new_fmlist_.append(fm_pb0)

        #pawn black 1
        elif figure == 'BP1':
            dict_, nb_ = pb1.pawn(nc_, nbinfo_, fm_pb1, nb_)
            fm_pb1 += 1
            new_fmlist_.append(fm_pb1)

        #pawn black 2
        elif figure == 'BP2':
            dict_, nb_ = pb2.pawn(nc_, nbinfo_, fm_pb2, nb_)
            fm_pb2 += 1
            new_fmlist_.append(fm_pb2)

        #pawn black 3
        elif figure == 'BP3':
            dict_, nb_ = pb3.pawn(nc_, nbinfo_, fm_pb3, nb_)
            fm_pb3 += 1
            new_fmlist_.append(fm_pb3)

        #pawn black 4
        elif figure == 'BP4':
            dict_, nb_ = pb4.pawn(nc_, nbinfo_, fm_pb4, nb_)
            fm_pb4 += 1
            new_fmlist_.append(fm_pb4)

        #pawn black 5
        elif figure == 'BP5':
            dict_, nb_ = pb5.pawn(nc_, nbinfo_, fm_pb5, nb_)
            fm_pb5 += 1
            new_fmlist_.append(fm_pb5)

        #pawn black 6
        elif figure == 'BP6':
            dict_, nb_ = pb6.pawn(nc_, nbinfo_, fm_pb6, nb_)
            fm_pb6 += 1
            new_fmlist_.append(fm_pb6)

        #pawn black 7
        elif figure == 'BP7':
            dict_, nb_ = pb7.pawn(nc_, nbinfo_, fm_pb7, nb_)
            fm_pb7 += 1
            new_fmlist_.append(fm_pb7)

        mvcounts += 1
        nbinfo_ = dict_
        fmlist_.clear()
        fmlist_ = new_fmlist_
        new_fmlist_.clear()

import figures as f
import pyinputplus as pyip

def pawn(nc_, nbinfo_, firstMove, nb_):

    nbi_ = nbinfo_
    cc_ = nbi_.setdefault('BP0')

    pm_ = possibleMoves(cc_, nb_, firstMove)

    if nc_ in pm_:
        nbi_['BP0'] = nc_
        nb_[nc_[0]][nc_[1]] = 'BP0'
        if nc_[0] == 7:
            pawnTransform(nb_, nc_)
        nb_[cc_[0]][cc_[1]] = None

    return nbi_, nb_

def possibleMoves(cc_, nb_, firstMove):

    pm_ = []
    #1. UP - ONE
    if nb_[cc_[0] + 1][cc_[1]] == None:
        n = [cc_[0] + 1, cc_[1]]
        pm_.append(n)

    if firstMove == 0:
    #2. UP - TWO
        if nb_[cc_[0] + 2][cc_[1] ] == None:
            n = [cc_[0] + 2, cc_[1]]
            pm_.append(n)

    #3. PAWN TAKES RIGHT
    if 9 > cc_[0] + 1 >= 0 and 9 > cc_[1] + 1 >= 1:
        if crush([cc_[0] + 1, cc_[1] + 1], nb_):
            n = [cc_[0] + 1, cc_[1] + 1]
            pm_.append(n)

    #4. PAWN TAKES LEFT
    if 9 > cc_[0] + 1 >= 0 and 9 > cc_[1] - 1 >= 1:
        if crush([cc_[0] + 1, cc_[1] - 1], nb_):
            n = [cc_[0] + 1, cc_[1] - 1]
            pm_.append(n)

    return pm_

def pawnTransform(nb_, nc_):

    new_figure = pyip.inputCustom(whatFigure, 'New figure:\n- queen = BQ\n')
    nb_[nc_[0]][nc_[1]] = new_figure

    return nb_

def whatFigure(new_figure):

    well_figure = ['BQ']
    if new_figure in well_figure:
        return new_figure
    else:
        print('Wrong Figure')

def crush(nc_, nb_):

    if nb_[nc_[0]][nc_[1]] != None:
        if "W" in nb_[nc_[0]][nc_[1]]:
            return True
    else:
        return False

import figures as f

def knight(chess_piece, mvcounts, nc_, nbinfo_, nb_):

    nbi_ = nbinfo_

    if f.whoseMove(mvcounts) == "White" and chess_piece == 'WKN1':
        cc_ = nbi_.setdefault('WKN1')
        pm_ = possibleMovesWhite(cc_, nb_)

        if nc_ in pm_:
            nbi_['WKN1'] = nc_
            nb_[nc_[0]][nc_[1]] = 'WKN1'
            nb_[cc_[0]][cc_[1]] = None

    elif f.whoseMove(mvcounts) == "White" and chess_piece == 'WKN2':
        cc_ = nbi_.setdefault('WKN2')
        pm_ = possibleMovesWhite(cc_, nb_)

        if nc_ in pm_:
            nbi_['WKN2'] = nc_
            nb_[nc_[0]][nc_[1]] = 'WKN2'
            nb_[cc_[0]][cc_[1]] = None


    elif f.whoseMove(mvcounts) == "Black" and chess_piece == 'BKN1':
        cc_ = nbi_.setdefault('BKN1')
        pm_ = possibleMovesBlack(cc_, nb_)

        if nc_ in pm_:
            nbi_['BKN1'] = nc_
            nb_[nc_[0]][nc_[1]] = 'BKN1'
            nb_[cc_[0]][cc_[1]] = None

    elif f.whoseMove(mvcounts) == "Black" and chess_piece == 'BKN2':
        cc_ = nbi_.setdefault('BKN2')
        pm_ = possibleMovesBlack(cc_, nb_)

        if nc_ in pm_:
            nbi_['BKN2'] = nc_
            nb_[nc_[0]][nc_[1]] = 'BKN2'
            nb_[cc_[0]][cc_[1]] = None

    return nbi_, nb_

def possibleMovesWhite(cc_, nb_):

    pm_ = []
    #1. UP -LEFT
    if 8 > cc_[0] - 2 >= 0 and 8 > cc_[1] - 1 >= 1:
        n = [cc_[0] - 2, cc_[1] - 1]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushWhite([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #2. UP - RIGHT
    if 8 > cc_[0] - 2 >= 0 and 8 >= cc_[1] + 1 > 1:
        n = [cc_[0] - 2, cc_[1] + 1]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushWhite([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #3. lEFT - UP
    if 8 > cc_[0] - 1 >= 0 and 7 > cc_[1] - 2 >= 1:
        n = [cc_[0] - 1, cc_[1] - 2]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushWhite([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #4. LEFT - DOWN
    if 8 > cc_[0] + 1 >= 0 and 7 > cc_[1] - 2 >= 1:
        n = [cc_[0] + 1, cc_[1] - 2]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushWhite([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #5. RIGHT - UP
    if 8 > cc_[0] - 1 >= 0 and 8 >= cc_[1] + 2 > 2:
        n = [cc_[0] - 1, cc_[1] + 2]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushWhite([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #6.RIGHT - DOWN
    if 8 > cc_[0] + 1 >= 0 and 8 >= cc_[1] + 2 > 2:
        n = [cc_[0] + 1, cc_[1] + 2]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushWhite([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #7. DOWN - RIGHT
    if 8 > cc_[0] + 2 >= 0 and 8 >= cc_[1] + 1 > 2:
        n = [cc_[0] + 1, cc_[1] + 2]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushWhite([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #8. DOWN - LEFT
    if 8 > cc_[0] - 2 >= 0 and 7 > cc_[1] - 1 >= 1:
        n = [cc_[0] - 2, cc_[1] - 1]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushWhite([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    return pm_

def possibleMovesBlack(cc_, nb_):

    pm_ = []
    #1. UP -LEFT
    if 8 > cc_[0] - 2 >= 0 and 8 > cc_[1] - 1 >= 1:
        n = [cc_[0] - 2, cc_[1] - 1]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushBlack([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #2. UP - RIGHT
    if 8 > cc_[0] - 2 >= 0 and 8 >= cc_[1] + 1 > 1:
        n = [cc_[0] - 2, cc_[1] + 1]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushBlack([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #3. lEFT - UP
    if 8 > cc_[0] - 1 >= 0 and 7 > cc_[1] - 2 >= 1:
        n = [cc_[0] - 1, cc_[1] - 2]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushBlack([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #4. LEFT - DOWN
    if 8 > cc_[0] + 1 >= 0 and 7 > cc_[1] - 2 >= 1:
        n = [cc_[0] + 1, cc_[1] - 2]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushBlack([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #5. RIGHT - UP
    if 8 > cc_[0] - 1 >= 0 and 8 >= cc_[1] + 2 > 2:
        n = [cc_[0] - 1, cc_[1] + 2]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushBlack([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #6.RIGHT - DOWN
    if 8 > cc_[0] + 1 >= 0 and 8 >= cc_[1] + 2 > 2:
        n = [cc_[0] + 1, cc_[1] + 2]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushBlack([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #7. DOWN - RIGHT
    if 8 > cc_[0] + 2 >= 0 and 8 >= cc_[1] + 1 > 2:
        n = [cc_[0] + 1, cc_[1] + 2]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushBlack([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #8. DOWN - LEFT
    if 8 > cc_[0] - 2 >= 0 and 7 > cc_[1] - 1 >= 1:
        n = [cc_[0] - 2, cc_[1] - 1]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushBlack([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    return pm_


def crushWhite(nc_, nb_):

    if "W" in nb_[nc_[0]][nc_[1]]:
            return True
    else:
        return False

def crushBlack(nc_, nb_):

    if "W" not in nb_[nc_[0]][nc_[1]]:
        return True
    else:
        return False

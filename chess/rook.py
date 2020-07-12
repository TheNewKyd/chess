import figures as f

def rook(chess_piece, mvcounts, nc_, nbinfo_, nb_):

    nbi_ = nbinfo_

    if f.whoseMove(mvcounts) == "White" and chess_piece == "WR1":
        cc_ = nbi_.setdefault('WR1')
        pm_ = possibleMovesWhite(cc_, nb_)
        
        if nc_ in pm_:
            nbi_['WR1'] = nc_
            nb_[nc_[0]][nc_[1]] = 'WR1'
            nb_[cc_[0]][cc_[1]] = None

    elif f.whoseMove(mvcounts) == "White" and chess_piece == "WR2":
        cc_ = nbi_.setdefault('WR2')
        pm_ = possibleMovesWhite(cc_, nb_)

        if nc_ in pm_:
            nbi_['WR2'] = nc_
            nb_[nc_[0]][nc_[1]] = 'WR2'
            nb_[cc_[0]][cc_[1]] = None

    elif f.whoseMove(mvcounts) == "Black" and chess_piece == "BR1":
        cc_ = nbi_.setdefault('BR1')
        pm_ = possibleMovesBlack(cc_, nb_)

        if nc_ in pm_:
            nbi_['BR1'] = nc_
            nb_[nc_[0]][nc_[1]] = 'BR1'
            nb_[cc_[0]][cc_[1]] = None

    elif f.whoseMove(mvcounts) == "Black" and chess_piece == "BR2":
        cc_ = nbi_.setdefault('BR1')
        pm_ = possibleMovesBlack(cc_, nb_)

        if nc_ in pm_:
            nbi_['BR2'] = nc_
            nb_[nc_[0]][nc_[1]] = 'BR2'
            nb_[cc_[0]][cc_[1]] = None

    return nbi_, nb_

def possibleMovesWhite(cc_, nb_):

    pm_ = []

    for i in range(1, 9):
        #1. HORIZONTAL - LEFT
        if 8 >= cc_[1] - i >= 1:
            n = [cc_[0], cc_[1] - i]
            if nb_[n[0]][n[1]] == None:
                pm_.append(n)
            elif crushWhite([n[0], n[1]], nb_):
                break
            else:
                pm_.append(n)
                break

    for i in range(1, 9):
        #2. HORIZONTAL - RIGHT
        if 8 >= cc_[1] + i >= 1:
            n = [cc_[0], cc_[1] + i]
            if nb_[n[0]][n[1]] == None:
                pm_.append(n)
            elif crushWhite([n[0], n[1]], nb_):
                break
            else:
                pm_.append(n)
                break

    for i in range(1, 8):
        #3. VERITCAL - DOWN
        if 8 > cc_[0] + i >= 0:
            n = [cc_[0] + i, cc_[1]]
            if nb_[n[0]][n[1]] == None:
                pm_.append(n)
            elif crushWhite([n[0], n[1]], nb_):
                break
            else:
                pm_.append(n)
                break

    for i in range(1, 8):
        #4. VERTICAL - UP
        if 8 > cc_[0] - i >= 0:
            n = [cc_[0] - i, cc_[1]]
            if nb_[n[0]][n[1]] == None:
                pm_.append(n)
            elif crushWhite([n[0], n[1]], nb_):
                break
            else:
                pm_.append(n)
                break

    return pm_

def possibleMovesBlack(cc_, nb_):

    pm_ = []

    for i in range(1, 9):
        #1. HORIZONTAL - LEFT
        if 8 >= cc_[1] - i >= 1:
            n = [cc_[0], cc_[1] - i]
            if nb_[n[0]][n[1]] == None:
                pm_.append(n)
            elif crushBlack([n[0], n[1]], nb_):
                break
            else:
                pm_.append(n)
                break

    for i in range(1, 9):
        #2. HORIZONTAL - RIGHT
        if 8 >= cc_[1] + i >= 1:
            n = [cc_[0], cc_[1] + i]
            if nb_[n[0]][n[1]] == None:
                pm_.append(n)
            elif crushWhite([n[0], n[1]], nb_):
                break
            else:
                pm_.append(n)
                break

    for i in range(1, 8):
        #3. VERITCAL - DOWN
        if 8 > cc_[0] + i >= 0:
            n = [cc_[0] + i, cc_[1]]
            if nb_[n[0]][n[1]] == None:
                pm_.append(n)
            elif crushWhite([n[0], n[1]], nb_):
                break
            else:
                pm_.append(n)
                break

    for i in range(1, 8):
        #4. VERTICAL - UP
        if 8 > cc_[0] - i >= 0:
            n = [cc_[0] - i, cc_[1]]
            if nb_[n[0]][n[1]] == None:
                pm_.append(n)
            elif crushWhite([n[0], n[1]], nb_):
                break
            else:
                pm_.append(n)
                break

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

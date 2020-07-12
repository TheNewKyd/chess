import figures as f

def bishop(chess_piece, mvcounts, nc_, nbinfo_, nb_):

    nbi_ = nbinfo_
    nc_ = nc_

    if f.whoseMove(mvcounts) == "White" and chess_piece == "WB1":
        cc_ = nbi_.setdefault('WB1')
        pm_ = possibleMovesWhite(cc_, nb_)

        if nc_ in pm_:
            nbi_['WB1'] = nc_
            nb_[nc_[0]][nc_[1]] = 'WB1'
            nb_[cc_[0]][cc_[1]] = None

    elif f.whoseMove(mvcounts) == "White" and chess_piece == "WB2":
        cc_ = nbi_.setdefault('WB2')
        pm_ = possibleMovesWhite(cc_, nb_)

        if nc_ in pm_:
            nbi_['WB2'] = nc_
            nb_[nc_[0]][nc_[1]] = 'WB2'
            nb_[cc_[0]][cc_[1]] = None


    elif f.whoseMove(mvcounts) == "Black" and chess_piece == "BB1":
        cc_ = nbi_.setdefault('BB1')

        pm_ = possibleMovesBlack(cc_, nb_)

        if nc_ in pm_:
            nbi_['BB1'] = nc_
            nb_[nc_[0]][nc_[1]] = 'BB1'
            nb_[cc_[0]][cc_[1]] = None

    elif f.whoseMove(mvcounts) == "Black" and chess_piece == "BB2":
        cc_ = nbi_.setdefault('BB2')

        pm_ = possibleMovesBlack(cc_, nb_)

        if nc_ in pm_:
            nbi_['BB2'] = nc_
            nb_[nc_[0]][nc_[1]] = 'BB2'
            nb_[cc_[0]][cc_[1]] = None


    return nbi_, nb_

def possibleMovesWhite(cc_, nb_):

    pm_ = []

    for i in range(1, 9):
        #1. CROSS - UP - LEFT
        if 8 > cc_[0] - i >= 0 and 8 >= cc_[1] - i >= 1:
            n = [cc_[0] - i, cc_[1] - i]
            if nb_[n[0]][n[1]] == None:
                pm_.append(n)
            elif crushWhite([n[0], n[1]], nb_):
                break
            else:
                pm_.append(n)
                break

    for i in range(1, 9):
        #2. CROSS - UP - RIGHT
        if 8 > cc_[0] - i >= 0 and 8 >= cc_[1] + i >= 1:
            n = [cc_[0] - i, cc_[1] + i]
            if nb_[n[0]][n[1]] == None:
                pm_.append(n)
            elif crushWhite([n[0], n[1]], nb_):
                break
            else:
                pm_.append(n)
                break

    for i in range(1, 9):
        #3. CROSS - DOWN - LEFT
        if 8 > cc_[0] + i >= 0 and 8 >= cc_[1] - i >= 1:
            n = [cc_[0] + i, cc_[1] - i]
            if nb_[n[0]][n[1]] == None:
                pm_.append(n)
            elif crushWhite([n[0], n[1]], nb_):
                break
            else:
                pm_.append(n)
                break

    for i in range(1, 9):
        #4. CROSS - DOWN - RIGHT
        if 8 > cc_[0] + i >= 0 and 8 >= cc_[1] + i >= 1:
            n = [cc_[0] + i, cc_[1] + i]
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
        #1. CROSS - UP - LEFT
        if 8 > cc_[0] - i >= 0 and 8 >= cc_[1] - i >= 1:
            n = [cc_[0] - i, cc_[1] - i]
            if nb_[n[0]][n[1]] == None:
                pm_.append(n)
            elif crushBlack([n[0], n[1]], nb_):
                break
            else:
                pm_.append(n)
                break

    for i in range(1, 9):
        #2. CROSS - UP - RIGHT
        if 8 > cc_[0] - i >= 0 and 8 >= cc_[1] + i >= 1:
            n = [cc_[0] - i, cc_[1] + i]
            if nb_[n[0]][n[1]] == None:
                pm_.append(n)
            elif crushBlack([n[0], n[1]], nb_):
                break
            else:
                pm_.append(n)
                break

    for i in range(1, 9):
        #3. CROSS - DOWN - LEFT
        if 8 > cc_[0] + i >= 0 and 8 >= cc_[1] - 1 >= 1:
            n = [cc_[0] + 1, cc_[1] - i]
            if nb_[n[0]][n[1]] == None:
                pm_.append(n)
            elif crushBlack([n[0], n[1]], nb_):
                break
            else:
                pm_.append(n)
                break

    for i in range(1, 9):
        #4. CROSS - DOWN - RIGHT
        if 8 > cc_[0] + i >= 0 and 8 >= cc_[1] + 1 >= 1:
            n = [cc_[0] + i, cc_[1] + i]
            if nb_[n[0]][n[1]] == None:
                pm_.append(n)
            elif crushBlack([n[0], n[1]], nb_):
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

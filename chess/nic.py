def bigCastleWhite(fmr, fmk, nb_):

    if fmr == 0 and fmk == 0:
        if nb_[7][2] == nb_[7][3] == nb_[7][4] == None:
            nb_[7][2] == "WK"
            nb_[7][3] == "WR1"

    return nb_

def littleCastleWhite(fmr, fmk, nb_):

    if fmr == 0 and fmk == 0:
        if nb_[7][7] == nb_[7][6] == None:
            nb_[7][7] == "WK"
            nb_[7][6] == "WR2"

    return nb_

def bigCastleBlack(fmr, fmk, nb_):

    if fmr == 0 and fmk == 0:
        if nb_[2][0] == nb_[3][0] == nb_[4][0] == None:
            nb_[2][0] == "BK"
            nb_[3][0] == "BR1"

    return nb_

def littleCastleBLack(fmr, fmk, nb_):

    if fmr == 0 and fmk == 0:
        if nb_[6][0] == nb_[7][0] == None:
            nb_[7][0] == "BK"
            nb_[6][0] == "BR2"

    return nb_



def forbiddenMoveWhite(movesWhite_, nb_, pm_):

    forbiddenMoves_ = movesWhite_

    for i in range(len(pm_)):
        for val_ in forbiddenMoves_:
            if pm_[i] in val_:
                pm_.pop(i)
                pm_.append(None)

    return pm_

def forbiddenMoveBlack(movesBlack_, nb_, pm_):

    forbiddenMoves_ = movesBlack_

    for i in range(len(pm_)):
        for val_ in forbiddenMoves_:
            if pm_[i] in val_:
                pm_.pop(i)
                pm_.append(i)
                print(pm_)

    return pm_

def checkWhite(cc_, movesWhite_, nb_):

    incheck_ = movesWhite_

    for val_ in incheck_:
        if cc_ in val_:
            return True
            break

    return False


def checkBlack(cc_, movesBlack_, nb_):

    incheck_ = movesBlack_

    for val_ in incheck_:
        if cc_ in val_:
            return True
            break

    return False

def mate():
    return True


def draw(nb_):

    for row in nb_:
        for col in row:
            if ("Q" not in col and
                "KN" not in col and
                "B" not in col and
                "R" not in col and
                "P" not in col):
                return True
            else:
                return False

def patWhite(nb_, movesWhite_):

    for row in nb_:
        for col in row:
            if ("WQ" not in col and
                "WKN" not in col and
                "WB" not in col and
                "WR" not in col and
                "WP" not in col):
                if checkWhite(cc_, movesWhite_, nb_):
                    return True
            else:
                return False

def patBlack(nb_, movesBlack_):

    for row in nb_:
        for col in row:
            if ("BQ" not in col and "BKN" not in col and "BB" not in col and
                "BR" not in col and "BP" not in col):
                if checkBlack(cc_,movesBlack_, nb_):
                    return True
            else:
                return False

import figures as f
import queen as q
import knight as kn
import bishop as bi
import rook as r
import pawn_w1 as pw1
import pawn_w2 as pw2
import pawn_w3 as pw3
import pawn_w4 as pw4
import pawn_w5 as pw5
import pawn_w6 as pw6
import pawn_w7 as pw7
import pawn_b1 as pb1
import pawn_b2 as pb2
import pawn_b3 as pb3
import pawn_b4 as pb4
import pawn_b5 as pb5
import pawn_b6 as pb6
import pawn_b7 as pb7


def king(chess_piece, fmlist_, mvcounts, nc_, nbi_, nb_):

    if f.whoseMove(mvcounts) == "White" and chess_piece == 'WK':
        cc_ = nbi_.setdefault('WK')

        try:
            ccq_ = nbi_.setdefault('WQ')
            q_exists = True
        except:
            q_exists = False

        try:
            cckn1_ = nbi_.setdefault('WKN1')
            kn1_exists = True
        except:
            kn1_exists = False

        try:
            ccbi1_ = nbi_.setdefault('WB1')
            bi1_exists = True
        except:
            bi1_exists = False

        try:
            ccr1_ = nbi_.setdefault('WR1')
            r1_exists = True
        except:
            r1_exists = False

        try:
            cckn2_ = nbi_.setdefault('WKN2')
            kn2_exists = True
        except:
            kn2_exists = False

        try:
            ccbi2_ = nbi_.setdefault('WB2')
            bi2_exists = True
        except:
            bi2_exists = False

        try:
            ccr2_ = nbi_.setdefault('WR2')
            r2_exists = True
        except:
            r2_exists = False

        try:
            ccpw1_ = nbi_.setdefault('WP1')
            pw1_exists = True
        except:
            pw1_exists = False

        try:
            ccpw2_ = nbi_.setdefault('WP2')
            pw2_exists = True
        except:
            pw2_exists = False

        try:
            ccpw3_ = nbi_.setdefault('WP3')
            pw3_exists = True
        except:
            pw3_exists = False

        try:
            ccpw4_ = nbi_.setdefault('WP4')
            pwr_exists = True
        except:
            pw4_exists = False

        try:
            ccpw5_ = nbi_.setdefault('WP5')
            pw5_exists = True
        except:
            pw5_exists = False

        try:
            ccpw6_ = nbi_.setdefault('WP6')
            pw6_exists = True
        except:
            pw6_exists = False

        try:
            ccpw7_ = nbi_.setdefault('WP7')
            pw7_exists = True
        except:
            pw7_exists = False

        movesWhite_ = []

        #QUEEN
        if q_exists:
            movesWhite_.append(q.possibleMovesWhite(ccq_, nb_))
        #HORSES
        if kn1_exists:
            movesWhite_.append(kn.possibleMovesWhite(cckn1_, nb_))
        if kn2_exists:
            movesWhite_.append(kn.possibleMovesWhite(cckn2_, nb_))
        #BISHOPS
        if bi1_exists:
            movesWhite_.append(bi.possibleMovesWhite(ccbi1_, nb_))
        if bi2_exists:
            movesWhite_.append(bi.possibleMovesWhite(ccbi2_, nb_))
        #ROOKS
        if r1_exists:
            movesWhite_.append(r.possibleMovesWhite(ccr1_, nb_))
        if r2_exists:
            movesWhite_.append(r.possibleMovesWhite(ccr2_, nb_))
        #PAWNS
        if pw1_exists:
            movesWhite_.append(pw1.possibleMoves(ccpw1_, nb_, fmlist_[3]))
        if pw2_exists:
            movesWhite_.append(pw1.possibleMoves(ccpw1_, nb_, fmlist_[4]))
        if pw3_exists:
            movesWhite_.append(pw1.possibleMoves(ccpw1_, nb_, fmlist_[5]))
        if pw4_exists:
            movesWhite_.append(pw1.possibleMoves(ccpw1_, nb_, fmlist_[6]))
        if pw5_exists:
            movesWhite_.append(pw1.possibleMoves(ccpw1_, nb_, fmlist_[7]))
        if pw6_exists:
            movesWhite_.append(pw1.possibleMoves(ccpw1_, nb_, fmlist_[8]))
        if pw7_exists:
            movesWhite_.append(pw1.possibleMoves(ccpw1_, nb_, fmlist_[9]))

        pm_ = forbiddenMovesWhite(movesWhite_, cc_, nb_)

        check = checkWhite(movesWhite_, cc_)
        mate = mateWhite(movesWhite_, cc_)
        draw = draw(nbi_)
        pat = patWhite(nbi_, pm_)


        if nc_== [7, 7] and not check:
            if (checkWhite(movesWhite_, [7, 7]) and
                checkWhite(movesWhite_, [7, 6])):
                if fmlist_[2] == 0 and fmlist_[0] == 0:
                    nb_, nbi_ = littleCastleWhite(nb_, nbi_)

                    return nbi_, nb_, mate, draw, pat, check

        if nc_ == [7, 2] and not check:
            if (checkWhite(movesWhite_, [7, 2]) and
                checkWhite(movesWhite_, [7, 3]) and
                checkWhite(movesWhite_, [7, 4])):
                if fmlist_[1] == 0 and fmlist_[0] == 0:
                    nb_, nbi_ = bigCastleWhite(nb_, nbi_)

                    return nbi_, nb_, mate, draw, pat, check

        if mate:
            return nbi_, nb_, mate, draw, pat, check

        if draw:
            return nbi_, nb_, mate, draw, pat, check

        if pat:
            return nbi_, nb_, mate, draw, pat, check

        elif nc_ in pm_:
            nbi_['WK'] = nc_
            nb_[nc_[0]][nc_[1]] = 'WK'
            nb_[cc_[0]][cc_[1]] = None

            return nbi_, nb_, mate, draw, pat, check

    elif f.whoseMove(mvcounts) == "Black" and chess_piece == 'BK':
        cc_ = nbi_.setdefault('BK')

        try:
            ccq_ = nbi_.setdefault('BQ')
            q_exists = True
        except:
            q_exists = False

        try:
            cckn1_ = nbi_.setdefault('BKN1')
            kn1_exists = True
        except:
            kn1_exists = False

        try:
            ccbi1_ = nbi_.setdefault('BB1')
            bi1_exists = True
        except:
            bi1_exists = False

        try:
            ccr1_ = nbi_.setdefault('BR1')
            r1_exists = True
        except:
            r1_exists = False

        try:
            cckn2_ = nbi_.setdefault('BKN2')
            kn2_exists = True
        except:
            kn2_exists = False

        try:
            ccbi2_ = nbi_.setdefault('BB2')
            bi2_exists = True
        except:
            bi2_exists = False

        try:
            ccr2_ = nbi_.setdefault('BR2')
            r2_exists = True
        except:
            r2_exists = False

        try:
            ccpw1_ = nbi_.setdefault('BP1')
            pw1_exists = True
        except:
            pw1_exists = False

        try:
            ccpw2_ = nbi_.setdefault('BP2')
            pw2_exists = True
        except:
            pw2_exists = False

        try:
            ccpw3_ = nbi_.setdefault('BP3')
            pw3_exists = True
        except:
            pw3_exists = False

        try:
            ccpw4_ = nbi_.setdefault('BP4')
            pwr_exists = True
        except:
            pw4_exists = False

        try:
            ccpw5_ = nbi_.setdefault('BP5')
            pw5_exists = True
        except:
            pw5_exists = False

        try:
            ccpw6_ = nbi_.setdefault('BP6')
            pw6_exists = True
        except:
            pw6_exists = False

        try:
            ccpw7_ = nbi_.setdefault('BP7')
            pw7_exists = True
        except:
            pw7_exists = False

        movesBlack_ = []

        #QUEEN
        if q_exists:
            movesBlack_.append(q.possibleMovesBlack(ccq_, nb_))
        #HORSES
        if kn1_exists:
            movesBlack_.append(kn.possibleMovesBlack(cckn1_, nb_))
        if kn2_exists:
            movesBlack_.append(kn.possibleMovesBlack(cckn2_, nb_))
        #BISHOPS
        if bi1_exists:
            movesBlack_.append(bi.possibleMovesBlack(ccbi1_, nb_))
        if bi2_exists:
            movesBlack_.append(bi.possibleMovesBlack(ccbi2_, nb_))
        #ROOKS
        if r1_exists:
            movesBlack_.append(r.possibleMovesBlack(ccr1_, nb_))
        if r2_exists:
            movesBlack_.append(r.possibleMovesBlack(ccr2_, nb_))
        #PAWNS
        if pw1_exists:
            movesBlack_.append(pw1.possibleMoves(ccpw1_, nb_, fmlist_[3]))
        if pw2_exists:
            movesBlack_.append(pw1.possibleMoves(ccpw1_, nb_, fmlist_[4]))
        if pw3_exists:
            movesBlack_.append(pw1.possibleMoves(ccpw1_, nb_, fmlist_[5]))
        if pw4_exists:
            movesBlack_.append(pw1.possibleMoves(ccpw1_, nb_, fmlist_[6]))
        if pw5_exists:
            movesBlack_.append(pw1.possibleMoves(ccpw1_, nb_, fmlist_[7]))
        if pw6_exists:
            movesBlack_.append(pw1.possibleMoves(ccpw1_, nb_, fmlist_[8]))
        if pw7_exists:
            movesBlack_.append(pw1.possibleMoves(ccpw1_, nb_, fmlist_[9]))

        pm_ = forbiddenMovesBlack(movesBlack_, nb_, nb_)

        check = checkBlack(movesBlack_, cc_)
        mate = mateBlack(movesBlack_, cc_)
        draw = draw(nbi_)
        pat = patBlack(nbi_, pm_)


        if nc_== [7, 7] and not check:
            if (checkBlack(movesWhite_, [7, 7]) and
                checkBlack(movesWhite_, [7, 6])):
                if fmlist_[2] == 0 and fmlist_[0] == 0:
                    nb_, nbi_ = littleCastleBLack(nb_, nbi_)

                    return nbi_, nb_, mate, draw, pat, check

        if nc_ == [7, 2] and not check:
            if (checkBlack(movesWhite_, [7, 2]) and
                checkBlack(movesWhite_, [7, 3]) and
                checkBlack(movesWhite_, [7, 4])):
                if fmlist_[1] == 0 and fmlist_[0] == 0:
                    nb_, nbi_ = bigCastleBlack(nb_, nbi_)

                    return nbi_, nb_, mate, draw, pat, check

        if mate:
            return nbi_, nb_, mate, draw, pat, check

        if draw:
            return nbi_, nb_, mate, draw, pat, check

        if pat:
            return nbi_, nb_, mate, draw, pat, check

        elif nc_ in pm_:
            nbi_['WK'] = nc_
            nb_[nc_[0]][nc_[1]] = 'WK'
            nb_[cc_[0]][cc_[1]] = None

            return nbi_, nb_, mate, draw, pat, check

def possibleMovesWhite(cc_, nb_):

    pm_ = []

    #1. UP -LEFT
    if 8 > cc_[0] - 1 >= 0 and 8 > cc_[1] - 1 >= 1:
        n = [cc_[0] - 1, cc_[1] - 1]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushWhite([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #2. UP - MID
    if 8 > cc_[0] - 1 >= 0:
        n = [cc_[0] - 1, cc_[1]]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushWhite([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #3. UP - RIGHT
    if 8 > cc_[0] - 1 >= 0 and 8 >= cc_[1] + 1 > 1:
        n = [cc_[0] - 1, cc_[1] + 1]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushWhite([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #4. MID - LEFT
    if 8 > cc_[1] - 1 >= 1:
        n = [cc_[0], cc_[1] - 1]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushWhite([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #5. MID - RIGHT
    if 8 >= cc_[1] + 1 > 1:
        n = [cc_[0], cc_[1] + 1]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushWhite([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #6. DOWN - LEFT
    if 8 > cc_[0] + 1 >= 0 and 8 > cc_[1] - 1 >= 1:
        n = [cc_[0] + 1, cc_[1] - 1]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushWhite([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #7. DOWN - MID
    if 8 > cc_[0] + 1 >= 0:
        n = [cc_[0] + 1, cc_[1]]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushWhite([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #8. DOWN - RIGHT
    if 8 > cc_[0] + 1 >= 0 and 8 >= cc_[1] + 1 > 1:
        n = [cc_[0] + 1, cc_[1] + 1]
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
    if 8 > cc_[0] - 1 >= 0 and 8 > cc_[1] - 1 >= 1:
        n = [cc_[0] - 1, cc_[1] - 1]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushBlack([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #2. UP - MID
    if 8 > cc_[0] - 1 >= 0:
        n = [cc_[0] - 1, cc_[1]]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushBlack([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #3. UP - RIGHT
    if 8 > cc_[0] - 1 >= 0 and 8 >= cc_[1] + 1 > 1:
        n = [cc_[0] - 1, cc_[1] + 1]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushBlack([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #4. MID - LEFT
    if 8 > cc_[1] - 1 >= 1:
        n = [cc_[0], cc_[1] - 1]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushBlack([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #5. MID - RIGHT
    if 8 >= cc_[1] + 1 > 1:
        n = [cc_[0], cc_[1] + 1]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushBlack([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #6. DOWN - LEFT
    if 8 > cc_[0] + 1 >= 0 and 8 > cc_[1] - 1 >= 1:
        n = [cc_[0] + 1, cc_[1] - 1]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushBlack([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #7. DOWN - MID
    if 8 > cc_[0] + 1 >= 0:
        n = [cc_[0] + 1, cc_[1]]
        if nb_[n[0]][n[1]] == None:
            pm_.append(n)
        elif crushBlack([n[0], n[1]], nb_):
            pass
        else:
            pm_.append(n)

    #8. DOWN - RIGHT
    if 8 > cc_[0] + 1 >= 0 and 8 >= cc_[1] + 1 > 1:
        n = [cc_[0] + 1, cc_[1] + 1]
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

def bigCastleWhite(nb_, nbi_):

    if nb_[7][2] == nb_[7][3] == nb_[7][4] == None:
        nb_[7][2] = "WK"
        nb_[7][3] = "WR1"
        nbi_['WK'] = [7, 2]
        nbi_['WR1'] = [7, 3]

    return nb_, nbi_

def littleCastleWhite(nb_, nbi_):

    if nb_[7][7] == nb_[7][6] == None:
        nb_[7][7] = "WK"
        nb_[7][7] = "WR2"
        nbi_['WK'] = [7, 7]
        nbi_['WR2'] = [7, 6]

    return nb_, nbi_

def bigCastleBlack(nb_, nbi_):

    if nb_[0][2] == nb_[0][3] == nb_[0][4] == None:
        nb_[0][2] = "BK"
        nb_[0][3] = "BR1"
        nbi_['BK'] = [0, 2]
        nbi_['BR1'] = [0, 3]

    return nb_, nbi_

def littleCastleBLack(nb_, nbi_):

    if nb_[0][6] == nb_[0][7] == None:
        nb_[0][7] = "BK"
        nb_[0][6] = "BR2"
        nbi_['BK'] = [0, 7]
        nbi_['BR2'] = [0, 6]

    return nb_, nbi_

def forbiddenMovesWhite(movesWhite_, cc_, nb_):

    pm_ = possibleMovesWhite(cc_, nb_)

    for val_ in movesWhite_:
        for mv_ in pm_:
            if mv_ in val_:
                pm_.remove(mv_)
    return pm_

def forbiddenMovesBlack(movesBlack_, cc_, nb_):

    pm_ = possibleMovesWhite(cc_, nb_)

    for val_ in movesBlack_:
        for mv_ in pm_:
            if mv_ in val_:
                pm_.remove(mv_)
    return pm_

def checkWhite(movesWhite_, cc_):

    for val_ in movesWhite_:
        if cc_ in val_:
            return True

    return False


def checkBlack(cc_, movesBlack_, nb_):

    for val_ in incheck_:
        if cc_ in val_:
            return True
            break

    return False

def mateWhite(movesWhite_, cc_, nb_):

    if (checkWhite(movesWhite_, cc_) and
        len(forbiddenMovesWhite(movesWhite_, cc_, nb_)) == 0):
        return True

    return False

def mateBlack(movesBlack_, cc_, nb_):

    if (checkBlack(movesBlack_, cc_) and
        len(forbiddenMovesBlack(movesBlack_, cc_, nb_)) == 0):
        return True

    return False

def draw(nbi_):

    for figure in nbi_.keys():
        if ("Q" not in figure and
            "KN" not in figure and
            "B" not in figure and
            "R" not in figure and
            "P" not in figure):
            return True

    return False

def patWhite(nbi_, pm_):

    for figure in nbi_.keys():
        if ("WQ" not in figure and
            "WKN" not in figure and
            "WB" not in figure and
            "WR" not in figure and
            "WP" not in figure):
            if len(pm_) == 0:
                return True

    return False

def patBlack(nbi_, pm_):

    for figure in nbi_.keys():
        if ("BQ" not in figure and
            "BKN" not in figure and
            "BB" not in figure and
            "BR" not in figure and
            "BP" not in figure):
            if len(pm_) == 0:
                return True

    return False

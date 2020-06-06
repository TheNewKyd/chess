#python3!
#Chess
#Figures and perchs:
#   1. King:
#       Can move in any direction, but only one sqr.
#       Attack on King equals check. If the King has no move to run away
#       or possibility to be saved by other figure it is checkmate and the match
#       is over. King can castle with rooks,unless King is being checked
#       or castle is in a way of the chack.
#   2. Queen:
#       Can move in any direction, as many sqrs as possible, but can't jump obove
#       other figures - Queen can "take" it.
#   3. Bishop:
#       Can in move only on cross, as many sqrs as possible, but can't jump obove
#       other figures - Bishop can "take" it. Bishop can't change color of sqrs.
#   4. Knight:
#       Can move in shape of an L and is the only figure that is allowed to
#       jump above other figures.
#   5. Rook:
#       Can move verticaly and horizontaly, as many sqrs as possible
#       ,can't jump over figures. Rook can castle with King,
#       unless King is being checked or castle is in a way of the chack.
#   6. Pawn:
#       Pawn can move one sqr vertically, but "takes" crosses before it.
#       If it is pawn's first move end there is space, it can take two sqrs vert.
#       Pawn has a superpower - beating in passing.
#       If the opponent's pawn made sqrs move and is now directly on any side
#       of yours, You can "take" it, by crossing one sqr.

import board as b
from tabulate import tabulate

class Figures():

    def __init__(self):
        nbinfo_ =  b.startBoard()
        self.nb_ = nbinfo_[3]
        self.nbc_ = nbinfo_[0]
        self.nbr_ = nbinfo_[1]
        self.nbv_ = nbinfo_[2]

    def crushesAndTakes(self):
        """Is the move possible(crushes) and takes"""
        pass

    def kingPossibleMoves(cc_=[self.nbc_[5], self.nbr_[5]]):
        possibleMoves_ = []
        cc0 = cc_[0]
        cc1 = cc_[1]

        #1.Górny lewy
        try:
            n = [cc0 - 1, cc1 - 1]
            possibleMoves_.append(n)

        except IndexError:
            pass
        #2. Górny środkowy
        try:
            n = [cc0, cc1 - 1]
            possibleMoves_.append(n)

        except IndexError:
            pass
        #3. Górny prawy
        try:
            n = [cc0 + 1, cc1 - 1]
            possibleMoves_.append(n)

        except IndexError:
            pass
        #4. Środek lewy
        try:
            n = [cc0 - 1, cc1]
            possibleMoves_.append(n)

        except IndexError:
            pass
        #5. Środek prawy
        try:
            n = [cc0 + 1, cc1]
            possibleMoves_.append(n)

        except IndexError:
            pass
        #6. Dół lewy
        try:
            n = [cc0 - 1, cc1 + 1]
            possibleMoves_.append(n)

        except IndexError:
            pass
        #7. Dół środek
        try:
            n = [cc0 - 1, cc1 + 1]
            possibleMoves_.append(n)

        except IndexError:
            pass
        #8. Dół prawy
        try:
            n = [cc0 + 1, cc1 + 1]
            possibleMoves_.append(n)

        except IndexError:
            pass

        return possibleMoves_

    def king(self, cc_, nc_):
        """Moves"""
        pm_ = [] # possbile moves

        if nc_ in pm_: #nc_ - new coor
            cc_ = nc_ #cc_ - current coor

        pass

    def queen(self):
        pass

    def bishop(self):
        pass

    def knight(self):
        pass

    def rook(self):
        pass

    def pawn(self):
        pass

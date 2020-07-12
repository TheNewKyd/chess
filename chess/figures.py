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

def whoseMove(mvcounts):
    firstMove = "White"
    if mvcounts == 0 or mvcounts % 2 == 0:
        return firstMove
    elif mvcounts % 2 != 0:
        firstMove = "Black"
        return firstMove

def checkmate():
    pass

def pat():
    pass

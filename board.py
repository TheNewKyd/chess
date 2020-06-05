#!python3
#Chess
#Chess board

import figures
from tabulate import tabulate


start_board_black = {"WRR": [0, 7],
                     "WKNR": [0, 6],
                     "WBR": [0, 5],
                     "WK": [0, 4],
                     "WQ": [0, 3],
                     "WBL": [0, 2],
                     "WKNL": [0, 1],
                     "WRL": [0, 0],
                     "WP0": [1, 0],
                     "WP1": [1, 1],
                     "WP2": [1, 2],
                     "WP3": [1, 3],
                     "WP4": [1, 4],
                     "WP5": [1, 5],
                     "WP6": [1, 6],
                     "WP7": [1, 7]
                     }

start_board_white = {"BRR": [7, 7],
                     "BKNR": [7, 6],
                     "BBR": [7, 5],
                     "BK": [7, 4],
                     "BQ": [7, 3],
                     "BBL": [7, 2],
                     "BKNL": [7, 1],
                     "BRL": [7, 0],
                     "BP0": [7, 0],
                     "BP1": [7, 1],
                     "BP2": [7, 2],
                     "BP3": [7, 3],
                     "BP4": [7, 4],
                     "BP5": [7, 5],
                     "BP6": [7, 6],
                     "BP7": [7, 7]
                     }

def makeBoard():
    cols_ = [None for col in range(8)]
    return [cols_ for row in range(8)]


def fillUpBoard():
    nb_ = makeBoard()
    sbbk_ = []
    sbbv_ = []

    for k, v in start_board_black.items():
        sbbk_.append(k)
        sbbv_.append(v)

    for k in sbbk_:
        for c1, c0 in sbbv_:
            nb_[c0][c1] = k
            
    sbwk_ = []
    sbwv_ = []

    for k, v in start_board_white.items():
        sbwk_.append(k)
        sbwv_.append(v)

    for k in sbwk_:
        for c1, c0 in sbwv_:
            nb_[c0][c1] = k

    return tabulate(nb_)

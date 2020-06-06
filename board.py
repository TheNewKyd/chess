#!python3
#Chess
#Chess board

import figures
from tabulate import tabulate


nb_ = [['BR', 'BKN', 'BB', 'BQ', 'BK', 'BB', 'BKN', 'BR'],
       ['BP0', 'BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6', 'BP7'],
       [None, None, None, None, None, None, None, None],
       [None, None, None, None, None, None, None, None],
       [None, None, None, None, None, None, None, None],
       [None, None, None, None, None, None, None, None],
       ['WP0', 'WP1', 'WP2', 'WP3', 'WP4', 'WP5', 'WP6', 'WP7'],
       ['WR', 'WKN', 'WB', 'WQ', 'WK', 'WB', 'WKN', 'WR']]


def startBoard():
    nbc_ = []
    nbr_ = []
    nbv_ = []
    nbinfo_ = []

    for c0 in range(8):
        for c1 in range(8):
            nbc_.append(c0)
            nbr_.append(c1)
            nbv_.append(nb_[c0][c1])

    nbinfo_.append(nbc_)
    nbinfo_.append(nbr_)
    nbinfo_.append(nbv_)
    nbinfo_.append(nb_)

    return nbinfo_

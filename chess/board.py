#!python3
#Chess
#Chess board

import figures

def table():
    nb_ = [['8', 'BR1', 'BKN1', 'BB1', 'BQ', 'BK', 'BB2', 'BKN2', 'BR2'],
           ['7', 'BP0', 'BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6', 'BP7'],
           ['6', None, None, None, None, None, None, None, None],
           ['5', None, None, None, None, None, None, None, None],
           ['4', None, None, None, None, None, None, None, None],
           ['3', None, None, None, None, None, None, None, None],
           ['2', 'WP0', 'WP1', 'WP2', 'WP3', 'WP4', 'WP5', 'WP6', 'WP7'],
           ['1', 'WR1', 'WKN1', 'WB1', 'WQ', 'WK', 'WB2', 'WKN2', 'WR2'],
           [None, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']]

    return nb_

def startBoard():
    nb_ = table()
    nbc_ = []
    nbr_ = []
    nbv_ = []
    nbinfo_ = {}

    for c0 in range(9):
        for c1 in range(9):
            nbc_.append(c0)
            nbr_.append(c1)
            nbv_.append(nb_[c0][c1])

    for i in range(81):
        nbinfo_[nbv_[i]] = [nbc_[i], nbr_[i]]

    return nbinfo_

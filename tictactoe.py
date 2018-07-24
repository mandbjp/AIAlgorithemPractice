#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TicTacToe(object):
    X = 1  # TicTac
    O = 2  # Toe
    N = 0
    WIN_O = None
    WIN_X = None
    DRAW = "draw"
    ON_PROGRESS = "none"

    def __init__(self):
        self.board = None
        self.reset()
        pass

    def reset(self):
        self.board = [self.N for _ in range(9)]

    def copy(self, board):
        self.board = board[:]

    def print_board(self, show_index=False):
        s = ""
        for i, t in enumerate(self.board):
            n = "-" if not show_index else "%d" % (i+1)
            s += _stringify(t, n=n)
            if (i % 3) == 2:
                s += "\n"
            else:
                s += " | "
        return s.rstrip("\n")

    def set(self, position, t):
        self.board[position-1] = t

    def get(self, position):
        return self.board[position-1]

    def eval(self):
        b = self.board

        if (b[0] != self.N) and (b[0] == b[1] == b[2]):
            return _wins(b[0])
        if (b[3] != self.N) and (b[3] == b[4] == b[5]):
            return _wins(b[3])
        if (b[6] != self.N) and (b[6] == b[7] == b[8]):
            return _wins(b[6])
        if (b[0] != self.N) and (b[0] == b[3] == b[6]):
            return _wins(b[0])
        if (b[1] != self.N) and (b[1] == b[4] == b[7]):
            return _wins(b[1])
        if (b[2] != self.N) and (b[2] == b[5] == b[8]):
            return _wins(b[2])
        if (b[0] != self.N) and (b[0] == b[4] == b[8]):
            return _wins(b[0])
        if (b[2] != self.N) and (b[2] == b[4] == b[6]):
            return _wins(b[2])

        if len([_ for _ in self.board if _ == self.N]) == 0:
            return TicTacToe.DRAW

        return TicTacToe.ON_PROGRESS


def _parse_t(t):
    t = t.upper()
    return TicTacToe.O if t == "O" else TicTacToe.X if t == "X" else TicTacToe.N


def _stringify(t, n="-"):
    return "O" if t == TicTacToe.O else "X" if t == TicTacToe.X else n if t == TicTacToe.N else "?"


def _wins(t):
    return "win %s" % _stringify(t)


TicTacToe.WIN_O = _wins(TicTacToe.O)
TicTacToe.WIN_X = _wins(TicTacToe.X)


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tictactoe import TicTacToe
from .base import Base
import random


class AnywhereCanSet(Base):
    """
    何も考えずに、ランダムで設置できるところに設置する
    """
    def play(self):
        if self.ttt.eval() != TicTacToe.ON_PROGRESS:
            return
        while True:
            position = random.randrange(1, 10)
            if self.ttt.get(position) == TicTacToe.N:
                break
            continue
        self.ttt.set(position, self.t)
        return position


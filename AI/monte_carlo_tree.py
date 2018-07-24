#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tictactoe import TicTacToe
from . import Base


class MonteCarloTree(Base):
    """
    ターンが来た状態からゲーム終了になるまでランダムに打ち続ける。
    数パターン行って、その中から自分が勝つ位置を答える
    """
    def __init__(self, *args, **kwargs):
        super(MonteCarloTree, self).__init__(*args, **kwargs)
        self.order_count = 0

    def play(self):
        if self.ttt.eval() != TicTacToe.ON_PROGRESS:
            return

        self.order_count = 0

        result = self.monte_carlo(self.ttt.board, self.t)
        print "order count:" , self.order_count
        return

    def monte_carlo(self, board, t, depth=None):
        self.order_count += 1

        if depth is None:
            depth = []

        ttt = TicTacToe()
        ttt.copy(board)

        # ランダムに自分の一手を行う
        position = _pick_one(ttt)
        ttt.set(position, t)

        t_enemy = TicTacToe.O if t == TicTacToe.X else TicTacToe.X

        depth = depth + [(t, position)]

        # 結果を判定。決着がつかないなら再帰的に繰り返す
        status = ttt.eval()
        if status != TicTacToe.ON_PROGRESS:
            result = {
                "game_result": status,
                "moves": depth,
                TicTacToe.WIN_O: 0,
                TicTacToe.WIN_X: 0,
                TicTacToe.DRAW: 0,
            }
            result[status] += 1
            return result

        result = {
            "position": position,
            TicTacToe.WIN_O: 0,
            TicTacToe.WIN_X: 0,
            TicTacToe.DRAW: 0,
        }
        mc_results = [self.monte_carlo(ttt.board, t_enemy, depth) for _ in range(1)]
        for mc_result in mc_results:
            result[TicTacToe.WIN_O] += mc_result[TicTacToe.WIN_O]
            result[TicTacToe.WIN_X] += mc_result[TicTacToe.WIN_X]
            result[TicTacToe.DRAW] += mc_result[TicTacToe.DRAW]
        return result


def _pick_one(ttt):
    import random

    if ttt.eval() != TicTacToe.ON_PROGRESS:
        return
    while True:
        position = random.randrange(1, 10)
        if ttt.get(position) == TicTacToe.N:
            break
        continue
    return position


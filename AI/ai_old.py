#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tictactoe import TicTacToe


class TicTacToeAIBase:
    def __init__(self, ttt, t):
        self.t = t
        self.ttt = ttt

    def play(self):
        raise Exception("Override this!")


class TicTacToeAIRandom(TicTacToeAIBase):
    def play(self):
        if self.ttt.eval() != TicTacToe.ON_PROGRESS:
            return
        import random
        while True:
            position = random.randrange(0, 8)
            if self.ttt.get(position) == TicTacToe.N:
                break
            continue
        self.ttt.set(position, self.t)
        return position


class TicTacToeAIMonteCarlo(TicTacToeAIBase):
    def play(self):
        if self.ttt.eval() != TicTacToe.ON_PROGRESS:
            return

        results = [self.monte_carlo(self.ttt.board) for _ in range(10)]

        # TODO: 結果の一覧から 自分が勝つ > draw > 負け の優先度で選びたい
        # TODO: 更にこのpositionは勝率が高い を優先したい
        # TODO: この確率の処理をmonte_carlo内で実行して、それぞれの手から数通り分岐していく。そこから、win O / win X / draw の確率を出したい

        # 勝つ > draw > 負け の順番に並び替え。それぞれは、手の少ない順に並び替え
        results2 = []
        results2.extend(sorted([x for x in results if x["game_result"] == TicTacToe.WIN_X], key=lambda y: len(y["moves"])))
        results2.extend(sorted([x for x in results if x["game_result"] == TicTacToe.DRAW] , key=lambda y: len(y["moves"])))
        results2.extend(sorted([x for x in results if x["game_result"] == TicTacToe.WIN_O], key=lambda y: len(y["moves"])))

        print "AI step to win:", " → ".join([str(x) for x in results2[0]["moves"]])
        position = results2[0]["position"]
        self.ttt.set(position, self.t)
        return position

    def monte_carlo(self, board, depth=None):
        if depth is None:
            depth = []

        ttt = TicTacToe()
        ttt.copy(board)

        # ランダムに自分の一手を行う
        position = self.pick_one(ttt)
        ttt.set(position, self.t)

        if ttt.eval() == TicTacToe.ON_PROGRESS:
            # 敵の手もランダムに一手を行う
            t_enemy = TicTacToe.O if self.t == TicTacToe.X else TicTacToe.X
            position_enemy = self.pick_one(ttt)
            ttt.set(position_enemy, t_enemy)

        depth = depth + [position]

        # 結果を判定。決着がつかないなら再帰的に繰り返す
        result = ttt.eval()
        if result != TicTacToe.ON_PROGRESS:
            return {
                "position": depth[0],
                "game_result": result,
                "moves": depth
            }

        return self.monte_carlo(ttt.board, depth)

    def pick_one(self, ttt):
        import random

        if ttt.eval() != TicTacToe.ON_PROGRESS:
            return
        while True:
            position = random.randrange(1, 10)
            if ttt.get(position) == TicTacToe.N:
                break
            continue
        return position
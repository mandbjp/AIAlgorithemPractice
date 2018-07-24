#!/usr/bin/env python
# -*- coding: utf-8 -*-


def TicTacToeGame():
    from tictactoe import TicTacToe
    from AI import AnywhereCanSet, RandomUntilEnd, MonteCarloTree

    game = TicTacToe()

    # AIを選ぶ
    ai = RandomUntilEnd(game, TicTacToe.X)

    while True:
        print "\n----"
        print game.print_board(True)
        cmd = raw_input("move?:")
        if cmd == "q":
            break
        if cmd == "r":
            game.reset()
            print game.print_board()
            continue

        try:
            position = int(cmd)
            game.set(position, TicTacToe.O)
        except Exception as e:
            print e.message
            continue
        # print game.print_board()
        # print "status:", game.eval()

        print ai.play()
        print game.print_board()
        print "status:", game.eval()

        if game.eval() != TicTacToe.ON_PROGRESS:
            game.reset()
            print "\n\nnew game!"
            print game.print_board()


def GenericAlgorithemText():
    """
    概要: 特定のアルファベットの単語(文字列)に近づける
    手法として遺伝的アルゴリズムを使う
    1. ランダム生成
    2. それぞれの評価(fitness)
    3. 親の選択と交叉する(crossover)
    4. 突然変異(mutation)
    """
    target = "HelloWorldJapan"
    print "Target is:", target
    import random

    def calc_distance(src, target):
        """
        文字の距離を計算する。
        距離ゼロ＝一致
        桁数が違う += 桁数*100
        同じ位置の文字が異なる += (大文字小文字が違うだけなら+10), (全く違うなら+50)

        :param src:
        :param target: 合わせに行く文字
        :return:
        """
        distance = 0
        distance += abs(len(src) - len(target)) * 100
        length = max([len(src), len(target)])
        for i in range(length):
            s = src[i] if i < len(src) else ""
            t = target[i] if i < len(target) else ""
            if s == t:
                score = 0
            elif s.lower() == t.lower():
                score = 10
            else:
                score = 50

            # print "compare %s <--> %s: %d" % (s, t, score)
            distance += score

        return distance

    def create_random_text():
        """
        大小アルファベットから1~2文字ランダムな文字列を生成する。
        @see https://qiita.com/kakk_a/items/3aef4458ed2269a59d63#comment-31254f0dbeeef2dc7f68
        :return:
        """
        import string
        length = random.randrange(0, 2)
        s = ""
        for _ in range(length):
            s += random.choice(string.ascii_letters)
        return s

    def mutate_text(src):
        """
        文字列に突然変異の可能性を与える。
        低い確率で文字置き換え
        低い確率で文字削除
        高い確率で現状維持
        :return:
        """
        import string
        s = ""
        for _ in range(len(src)):
            s += random.choice(string.ascii_letters) if (random.randrange(1000) <= 5) else \
                    "" if (random.randrange(1000) < 5) else \
                    src[_]
        return s

    def crossover(src1, src2):
        """
        交叉する。二点交叉を用いる
        :param src1:
        :param src2:
        :return:
        """
        m = max([len(src1), len(src2)])
        m1 = int(m/3)
        m2 = m - m1
        return src1[:m1]+src2[m1:m2]+src1[m2:], src2[:m1]+src1[m1:m2]+src2[m2:]

    counts_on_single_generation = 20
    results = ["" for _ in range(counts_on_single_generation)]
    for generation in range(1, 10000):
        # 生成
        results = [_ + create_random_text() for _ in results]

        # 評価
        results = sorted(results, key=lambda x: calc_distance(x, target))

        # 交叉
        next_results = []
        for _ in range(counts_on_single_generation / 2):
            # next_results.extend(list(crossover(*random.sample(results[:10], 2))))  # 上位10からランダムに2つ取り出して交差
            next_results.extend(list(crossover(results[_/2], *random.sample(results[:10], 1))))
            # for __ in range(10):
            #     crossed = list(crossover(results[_], *random.sample(results[:10], 1)))
            #     if crossed[0] not in next_results and crossed[1] not in next_results:
            #         break
            # next_results.extend(crossed)

        # 突然変異
        results = [mutate_text(_) for _ in next_results]

        current = sorted([(_, calc_distance(_, target)) for _ in results], key=lambda x: x[1])
        if (generation % 500) == 0:
            print "%d generation" % generation
            for _ in current[:3]:
                print "  %4d %s" % (_[1], _[0])
            print ""
        if current[0][1] <= 10:
            break

    print "%d generation" % generation
    for _ in current[:3]:
        print "  %4d %s" % (_[1], _[0])

    pass


if __name__ == '__main__':
    # TicTacToeGame()
    GenericAlgorithemText()

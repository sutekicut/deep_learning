import unittest
from functools import reduce

CARD = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
CARD_VALUE = {
    'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10
}


class Player:
    def __init__(self):
        self.cards = []
        self.score = 0

    # 手札から、スコアを計算する
    def update_score(self):
        # スコアをリセット
        self.score = 0

        # スコアを加算する
        for hand in self.cards:
            self.score += CARD_VALUE[hand]

        # print(self.score)

        # aceを持った状態で、自分の手札の合計値が21を超えた場合
        if 'A' in self.cards and self.score > 21:
            # 手札のAだけ抽出する。
            aces = filter(lambda hand: hand == 'A', self.cards)

            # カードの合計値が21以上なら、Aは1つずつ1に変更する
            for ace in aces:
                self.score -= 10

                # 　途中で21を下回ったら、ブレイクする
                if self.score <= 21:
                    break

    # カードを引く。
    # スコアを更新する
    # @return: なし
    def hit(self, card: str):
        # カードを手札に加える
        self.cards.append(card)

        # スコアを更新する
        self.update_score()


class TestBlackJackMethods(unittest.TestCase):
    def test_roles(self):
        player = Player()

        # A, JならA = 11として、スコア21
        player.cards = ['A', 'J']
        player.update_score()
        # print(player.score)
        self.assertEqual(player.score, 21, 'message')

        # A, 8, 3ならA = 1として、スコア12
        player.cards = ['A', '8', '3']
        player.update_score()
        self.assertEqual(player.score, 12, 'message')

        # A, A, 9なら、片方は11、残りを1として、スコア21
        player.cards = ['A', 'A', '9']
        player.update_score()
        self.assertEqual(player.score, 21, 'message')

        player.cards = ['4', '9', '9']
        player.update_score()
        self.assertEqual(player.score, 22, 'message')


if __name__ == '__main__':
    unittest.main()

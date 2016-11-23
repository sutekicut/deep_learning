from .blackjack import BlackJack
from .action_value import ActionValue
from .policy import Policy

import random


class MCESMethod:
    def __init__(self, action_value, policy):
        self.action_value = action_value
        self.policy = policy

    # 1ゲーム行い、価値と方策を更新する
    def simulate(self, verbose=False):
        game = BlackJack()

        player_total_queue = []
        player_has_ace_queue = []
        player_hit_queue = []
        # dealer_face_value

        # エピソード生成
        while True:
            player_total = game.player.score
            player_has_ace = game.player.has_ace

            # 1番最初の行動は、開始点探査の仮定を満たすために、ランダムに選択する
            if not player_hit_queue:
                player_hit = random.choice([True, False])
            else:
                player_hit = self.policy.hit()


            player_total_queue.append(player_total)
            player_has_ace_queue.append(player_has_ace)
            player_hit_queue.append(player_hit)

            if player_hit:

            else:



            # 価値関数の更新

            # 方策の更新

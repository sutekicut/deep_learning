from .blackjack import BlackJack


class Policy:
    def __init__(self):
        self.policy = [{}, {}]

    def hit(self, player_total, player_has_ace, dealer_face_value):
        ace_index = 0 if player_has_ace else 1
        self.policy[ace_index][player_total][dealer_face_value]

    def set(self, player_total, player_has_ace, dealer_face_value, hit):
        ace_index = 0 if player_has_ace else 1
        self.policy[ace_index][player_total][dealer_face_value] = hit

    def print(self):
        return ""

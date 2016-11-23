from libs.blackjack import BlackJack


class ActionValue:
    def __init__(self):
        self.value = [{}, {}]
        self.count = [{}, {}]

    def get(self, player_total, player_has_ace, dealer_face_value, player_hit):
        ace_index = 0 if player_has_ace else 1
        action_index = 0 if player_hit else 1
        self.value[ace_index][player_total][dealer_face_value][action_index]

    def update(self, player_total, player_has_ace, dealer_face_value, player_hit, reward):
        ace_index = 0 if player_has_ace else 1
        action_index = 0 if player_hit else 1

        count = self.count[ace_index][player_total][dealer_face_value][action_index]
        count += 1

        self.count[ace_index][player_total][dealer_face_value][action_index] = count

        value = self.value[ace_index][player_total][dealer_face_value][action_index]
        value += 1
        self.value[ace_index][player_total][dealer_face_value][action_index] = value

    def print(self):
        return ""

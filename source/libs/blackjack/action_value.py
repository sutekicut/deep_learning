from .blackjack_correct import BlackJack
import re

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
        value += 1 / count * (reward - value)
        self.value[ace_index][player_total][dealer_face_value][action_index] = value

    print_bar = "---" + "---------" * len(range(12, 21+1))
    print_header = "  |" + "  %2d(h/s)  " * len(range(12, 21+1)) % tuple(range(12, 21+1))
    print_format = "%2d|" + "%4.2f / %4.2f" * len(range(12, 21+1)) + "\n"

    def print(self):
        print(re.sub(r'-', '[ace]', ActionValue.print_bar, 1))
        print(ActionValue.print_header)
        print(ActionValue.print_bar)

        for dealer_face_value in range(2, 11+1):
            print(ActionValue.print_format)



        return ""

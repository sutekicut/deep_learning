import random

class BlackJack:
    #カードとその価値
    # Aceについては21を超えない限り21として扱う
    CARD = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    CARD_VALUE = {
        'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10
    }

    def __init__(self):
        self.player_cards = []
        self.player_ace = 0
        self.player_total = 0

        self.dealer_cards = []
        self.dealer_ace = 0
        self.dealer_total = 0

        while self.player_total < 12:
            self.player_draw()

        for _ in range(0, 2):
            self.dealer_draw()

        self.finish = False

    def player_has_ace(self):
        return self.player_ace > 0

    def dealer_face_value(self):
        return BlackJack.CARD_VALUE[self.dealer_cards[0]]

    def player_hit(self):
        if self.finish:
            raise NameError("game has finished.")

        self.player_draw()

        self.finish = self.player_total > 21

    def player_stand(self):
        if self.finish:
            raise NameError("Game has finished.")

        self.dealer_draw_all()

        self.finish = True

    #　ゲームの結果を返す
    def result(self):
        if not self.finish:
            raise NameError("Game hasn't finished")

        if self.player_total > 21:
            ret = -1
        elif self.dealer_total > 21:
            ret = 1
        elif self.player_total > self.dealer_total:
            ret = 1
        elif self.player_total < self.dealer_total:
            ret = -1
        else:
            ret = 0

        return ret

    def print(self):
        print("--" * 10)

        print("Player (total: {player_total}) [{player_cards}]".format(
            player_total=self.player_total,
            player_cards=', '.join(self.player_cards)
        ))

        if self.finish:
            print("Dealer (total: {dealer_total}) [{dealer_cards}]".format(
                dealer_total=self.dealer_total,
                dealer_cards=', '.join(self.dealer_cards)
            ))
        else:
            print("Dealer (total: ??) [{dealer_card}, ??]".format(
                dealer_card=self.dealer_cards[0],
            ))

        print("--" * 10)

    def draw_card(self):
        return random.choice(BlackJack.CARD)

    def has_finished(self):
        return  self.finish

    def player_draw(self):
        card = self.draw_card()
        self.player_cards.append(card)
        self.player_total += BlackJack.CARD_VALUE[card]

        if card == 'A':
            self.player_ace += 1

        if self.player_total > 21 and self.player_ace > 0:
            self.player_total -= 10
            self.player_ace -= 1

    def dealer_draw(self):
        card = self.draw_card()
        self.dealer_cards.append(card)
        self.dealer_total += BlackJack.CARD_VALUE[card]

        if card == 'A':
            self.dealer_ace += 1

        if self.dealer_total > 21 and self.dealer_ace > 0:
            self.dealer_total -= 10
            self.dealer_ace -= 1

    def dealer_draw_all(self):
        while self.dealer_total < 17:
            self.dealer_draw()

if __name__ == '__main__':
    game = BlackJack()

    while True:
        game.print()
        print("select…")
        print("[h] hit")
        print("[s] stand")
        print("[q] quit")

        selected = input()

        if selected == 'h':
            game.player_hit()
        elif selected == 's':
            game.player_stand()
        elif selected == 'q':
            exit()
        else:
            print("wrong input")

        if game.has_finished():
            break

    game.print()
    result = game.result()

    if result > 0:
        print("Player Win!!")
    elif result < 0:
        print("Player lose!!")
    else:
        print("Draw")

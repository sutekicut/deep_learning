import random


CARD = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
CARD_VALUE = {
  'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10
}

class Player:
  def __init__(self):
    self.cards = []
    self.score = 0
    self.has_ace = 0

  # 手札から、スコアを計算する
  def update_score(self, card: str):
    #スコアをリセット
    self.score = 0

    # もしaceなら、カウントをあげる
    if card == 'A':
      self.has_ace += 1

    # スコアを計算する
    for hand in self.cards:
      self.score += CARD_VALUE[hand]

    # aceを持った状態で、自分の手札の合計値が21を超えた場合
    if 'A' in self.cards and self.score > 21:
      # 手札のAだけ抽出する。
      aces = filter(lambda hand: hand == 'A', self.cards)

      # カードの合計値が21以上なら、Aは1つずつ1に変更する
      for ace in aces:
        self.score -= 10

        #　途中で21を下回ったら、ブレイクする
        if self.score <= 21:
          break

  # カードを引く。
  # スコアを更新する
  # @return: なし
  def hit(self, card: str):
    # カードを手札に加える
    self.cards.append(card)

    #スコアを更新する
    self.update_score(card)

  def check_my_cards(self):
    print(self.cards)



class Dealer:
  def __init__(self):
    self.cards = []
    self.score = 0
    self.has_ace = 0

  def hit(self, card: str):
    #手札をカードに加える
    self.cards.append(card)

    #スコアを更新する
    self.update_score(card)

  def update_score(self, card: str):
    # スコアをリセット
    self.score = 0

    # もしaceなら、カウントをあげる
    if card == 'A':
      self.has_ace += 1

    # スコアを計算する
    for hand in self.cards:
      self.score += CARD_VALUE[hand]

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

  def open_dealer_card(self):
    print("dealer[{first_card} : ??]".format(first_card=self.cards[0]))


class BlackJack:
  def __init__(self):
    self.player = Player()
    self.dealer = Dealer()


  def draw_card(self):
    return CARD[random.randint(0, 12)]


  def deal(self):
    result = 0

    #burstしたら負け
    if self.player.score > 21:
      result = -1
    elif self.dealer.score > 21:
      result = 1
    elif self.player.score > self.dealer.score:
      result = 1
    elif self.player.score < self.dealer.score:
      result = -1
    else:
      result = 0

    return result

  def start_game(self):
    #席に座る
    self.player = Player()
    self.dealer = Dealer()
    self.finished = False
    self.result = 0

    # スコア12以上になるまでhitする
    while self.player.score < 12:
      self.player.hit(self.draw_card())
    self.player.check_my_cards()

    # ディーラーは2枚ドローする
    for _ in range(0, 2):
      self.dealer.hit(self.draw_card())

    # 1枚目は見せる
    self.dealer.open_dealer_card()

    while self.finished == False:
      player_input = input()

      if player_input == 'hit':
        self.player.hit(self.draw_card())
        self.player.check_my_cards()
        #21を超えたらburst
        if self.player.score > 21:
          self.finished = True
          break

        continue

      elif player_input == 'stand':
        # dealerはスコア17以上になるまでカードを引いた後
        while self.dealer.score <= 17:
          self.dealer.hit(self.draw_card())

        # 勝敗をつける
        self.deal()
        break

      elif player_input == 'check':
        self.player.check_my_cards()

      else:
        print("one more")
        continue

    self.finish_game()

  def finish_game(self):
    print("player's hands: {player_hands}. player's score: {player_score}".format(player_hands=self.player.cards, player_score=self.player.score))
    print("dealer's hands: {dealer_hands}. dealer's score: {dealer_score}".format(dealer_hands=self.dealer.cards, dealer_score=self.dealer.score))

    result = self.deal()

    if result == 1:
      print("player win!!!")
    elif result == 0:
      print("draw")
    else:
      print("player loose…")
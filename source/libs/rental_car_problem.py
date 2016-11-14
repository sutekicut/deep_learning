from math import exp
from functools import reduce

class ENV(object):
  _instance = None

  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = object.__new__(cls, *args, **kwargs)
    return cls._instance

  def __init__(self, rental_car_max: int = 20, move_max: int = 5):
    self.RENTAL_CAR_MAX = rental_car_max
    self.MOVE_MAX = move_max

  def RENTAL_CAR_AMX(self):
    return self.RENTAL_CAR_MAX

  def MOVE_MAX(self):
    return self.MOVE_MAX


class StatusValue():
  #状態価値の初期値は0
  def __init__(self):
    env = ENV()
    self.value = [0.0 for i in range(0, env.RENTAL_CAR_AMX()) for j in range(0, env.RENTAL_CAR_AMX())]

  def get(self, x, y):
    return self.value[x][y]

  def set(self, x ,y , new_value):
    self.value[x][y] = new_value

  env = ENV()
  print_header = "  |" + "  {size}".format(size=len(range(0, env.RENTAL_CAR_AMX())))
  print_bar = "----" + "----" * len(range(0, env.RENTAL_CAR_AMX()))
  #print_format = "" +

  def print(self):
    print(StatusValue.print_bar)

    print(StatusValue.print_bar)


    print(StatusValue.print_bar)


  # 期待値がexpectでのポアソン分布P(X=n)の確率を返す
  def poisson(self, n, expect):
    if n > 0:
      return  (expect ** n) * (exp(-expect)) / reduce(lambda x, y: x * y, range(0, n))
    else:
      return exp(-expect)

  # 第一営業所の貸し出し台数がnに成る確率を返す
  def x_rental_probability(self, n: int):
    return StatusValue.poisson(n, 3)

  # 第二営業所ん貸し出し台数がnに成る確率
  def y_rental_probability(self, n: int):
    return StatusValue.poisson(n, 4)

  #　第一営業所の返却台数がnに成る確率
  def x_return_probability(self, n: int):
    return StatusValue.poisson(n, 3)

  #　第二営業所の返却台数がnになる確率
  def y_return_probability(self, n: int):
    return StatusValue.poisson(n, 2)

  # 状態(x, y)からmoveだけ動かした時の状態価値を計算する
  # moveが不正な場合、例外を投げる
  def value_of_move(self, x: int, y: int, move: int):
    env = ENV()
    value = 0.0

    #次の状態とは
    next_x_start = x - move
    next_y_start = y - move

    keep_for_x_rental = (next_x_start < 0) or (next_x_start > env.RENTAL_CAR_AMX())
    keep_for_y_rental = (next_y_start < 0) or (next_y_start > env.RENTAL_CAR_AMX())

    if keep_for_x_rental or keep_for_y_rental:
      return print("move is invalid")

    # 第一で貸し出せるのは、0 = next_x_startまで
    # 第二で貸し出せるのは、0 = next_y_startまで
    for x_rental in range(0, next_x_start):
      for y_rental in range(0, next_y_start):
        x_rest = next_x_start - x_rental
        y_rest = next_y_start - y_rental

        # 第一に返される台数は、0 ~ (RENTAL_CAR_MAX - x_rest)まで
        # 第二に返される台数は、0 ~ (RENTAL_CAR_MAX - y_rest)まで
        for x_return in range(0, env.RENTAL_CAR_AMX() - x_rest):
          for y_return in range(0, env.RENTAL_CAR_AMX() - y_rest):
            probability = (
              StatusValue.x_rental_probability(x_rental) *
              StatusValue.y_rental_probability(y_rental) *
              StatusValue.x_return_probability(x_return) *
              StatusValue.y_return_probability(y_return)
            )
            reward = (x_rental + y_rental) * 10 - move * 2
            next_x = next_x_start - x_rental + x_return
            next_y = next_y_start - y_rental + y_return
            value += probability * (reward + 0.9 * self.value[next_x][next_y])
    return value


  def get_most_valuable_move(self, x, y, *move_list):
    move_value_hash = move_list.












if __name__ == '__main__':

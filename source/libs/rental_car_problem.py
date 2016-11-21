from math import exp
from prettytable import PrettyTable

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
    self.value = [[0.0 for i in range(0, env.RENTAL_CAR_AMX())] for j in range(0, env.RENTAL_CAR_AMX())]

  def get(self, x: int, y: int):
    return self.value[x][y]

  def set(self, x ,y , new_value):
    self.value[x][y] = new_value

  def print(self):
    env = ENV()
    t = PrettyTable(list(range(0, env.RENTAL_CAR_AMX())))
    for i in range(0, env.RENTAL_CAR_AMX()):
      t.add_row(list(map(lambda j: float(self.value[i][j]), list(range(0, env.RENTAL_CAR_AMX())))))

    print(t)

  # 期待値がexpectでのポアソン分布P(X=n)の確率を返す
  def poisson(self, actual, mean):

    p = exp(-mean)
    for i in range(actual):
      p *= mean
      p /= i+1

    return p


    # if n > 0:
    #   denominator = reduce(lambda x, y: x * y, range(0, n))
    #   return  (expect ** n) * (exp(-expect)) / denominator if denominator != 0 else 0
    # else:
    #   return exp(-expect)

  # 第一営業所の貸し出し台数がnに成る確率を返す
  def x_rental_probability(self, n: int):
    return self.poisson(n, 3)

  # 第二営業所ん貸し出し台数がnに成る確率
  def y_rental_probability(self, n: int):
    return self.poisson(n, 4)

  #　第一営業所の返却台数がnに成る確率
  def x_return_probability(self, n: int):
    return self.poisson(n, 3)

  #　第二営業所の返却台数がnになる確率
  def y_return_probability(self, n: int):
    return self.poisson(n, 2)

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
    for x_rental in range(0, int(next_x_start)):
      for y_rental in range(0, int(next_y_start)):
        x_rest = next_x_start - x_rental
        y_rest = next_y_start - y_rental

        # 第一に返される台数は、0 ~ (RENTAL_CAR_MAX - x_rest)まで
        # 第二に返される台数は、0 ~ (RENTAL_CAR_MAX - y_rest)まで
        for x_return in range(0, int(env.RENTAL_CAR_AMX() - x_rest)):
          for y_return in range(0, int(env.RENTAL_CAR_AMX() - y_rest)):
            probability = (
              self.x_rental_probability(x_rental) *
              self.y_rental_probability(y_rental) *
              self.x_return_probability(x_return) *
              self.y_return_probability(y_return)
            )
            reward = (x_rental + y_rental) * 10 - move * 2
            next_x = next_x_start - x_rental + x_return
            next_y = next_y_start - y_rental + y_return
            value += probability * (reward + 0.9 * self.value[int(next_x)][int(next_y)])

    print(value)
    return value

  def get_most_valuable_move(self, x, y, *move_list):
    move_value_hash = {}
    for key, move in list(move_list):
      move_value_hash[move] = self.value_of_move(x, y, move)

    highest_value = max(move_value_hash.values())
    most_valuable_move = max((v, k) for (k, v) in move_value_hash.items())[1]

    return most_valuable_move, highest_value

class Policy:
  # 方策の初期値は0
  def __init__(self):
    env = ENV()
    self.policy = [[0.0 for i in range(0, env.RENTAL_CAR_AMX())] for j in range(0, env.RENTAL_CAR_AMX())]

  def get(self, x, y):
    return self.policy[x][y]

  def set(self, x, y, move):
    self.policy[x][y] = move

  env = ENV()
  print_header = "  |" + "  %d" * len(range(0, env.RENTAL_CAR_AMX()))
  print_bar = "----" + "----" * len(range(0, env.RENTAL_CAR_AMX()))
  print_format = "%d  |" + " %f  " * len(range(0, env.RENTAL_CAR_AMX()))

  def print(self):
    env = ENV()
    t = PrettyTable(list(range(0, env.RENTAL_CAR_AMX())))

    # print(Policy.print_bar)
    # print(Policy.print_header % tuple(range(0, env.RENTAL_CAR_AMX())))
    # print(Policy.print_bar)


    # value_table = ""
    # for i in range(0, env.RENTAL_CAR_AMX()):
    #   for j in range(0, env.RENTAL_CAR_AMX()):
    #     value_table += Policy.print_format % self.policy[i][j]
    # print(value_table)
    #
    # value_table = ""
    # for i in range(0, env.RENTAL_CAR_AMX()):
    #   policy_map = map(lambda j: self.policy[i][j], list(range(0, env.RENTAL_CAR_AMX())))
    #   print(Policy.print_format % (i, policy_map))
    # print(Policy.print_bar)
    #
    # print(Policy.print_bar)

class PolicyIterationMethod:
  delta_max = 0.1

  # 方策反復法
  def __init__(self, value: StatusValue, policy: Policy, verbose=False):
    self.value = value
    self.policy = policy
    self.verbose = verbose

  def execute(self):
    i = 0
    while True:
      self.evaluate_policy()

      if self.verbose:
        self.value.print()

      improved = self.improved_policy()

      if self.verbose:
        self.policy.print()

      if improved:
        i += 1
      else:
        break

  # 2. 方策評価
  def evaluate_policy(self):
    env = ENV()

    # 1. 以下を繰り返す
    while True:
      # 1-1. delta <- 0
      delta = 0.0
      # 1-2. 各状態sについて
      for x in range(0, env.RENTAL_CAR_AMX()):
        for y in range(0, env.RENTAL_CAR_AMX()):
          # 1-2-1. v <- V(s)
          old_value = self.value.get(x, y)

          # 1-2-2. V(s) <- Σs' Pss'*(Rss' + γV(s'))
          new_value = self.value.value_of_move(x, y, self.policy.get(x, y))

          # 1-2-3. delta <- max{delta, | Vs - v |}
          delta = max([delta, abs(new_value - old_value)])

      # 1-3. delta < epsilon なら、繰り返し完了
      if delta < PolicyIterationMethod.delta_max:
        break

      if self.verbose:
        self.value.print()

  # 3. 方策評価
  # 状態価値valueを使って方策改善を行う
  # 改善された場合、trueを返す
  def improved_policy(self):
    env = ENV()

    # 1. updated = false
    policy_improved = False

    # 2. 各状態sについて
    for x in range(0, env.RENTAL_CAR_AMX()):
      for y in range(0, env.RENTAL_CAR_AMX()):
        # 2-1. old <- pi(s)
        old_policy = self.policy.get(x, y)

        # 2-2. pi(s) <- arg max Σs' P(ss')*(R(ss') + γV(s'))
        new_policuy, max_value = self.value.get_most_valuable_move(x, y, list(range(-env.MOVE_MAX, env.MOVE_MAX)))

        # 2-2. old != pi(s))なら、updated=true
        # 3. updated=trueなら、2へ戻る。そうでなければ終了
        if old_policy != new_policuy:
          policy_improved = True
          self.policy.set(x, y, new_policuy)

    return policy_improved


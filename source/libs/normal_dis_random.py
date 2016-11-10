import random
from math import cos, log, pi, sin, sqrt

#正規分布に従った乱数を生成する関数
class NormalDistRandom:
  #期待値exp, 分散varの正規分布に従った乱数を生成
  #乱数生成器を作成
  def __init__(self, exp=1.0, var=1.0):
    self.exp = exp
    self.var = var
    self.values = []

  def get_random(self):
    if len(self.values) == 0:
      #　ボックス・ミュラー法で乱数を生成する
      a = 1.0 - random.random()
      b = 1.0 - random.random()
      z1 = sqrt(-2.0 * log(a)) * cos(2 * pi * b)
      z2 = sqrt(-2.0 * log(a)) * sin(2 * pi * b)
      rand1 = z1 * sqrt(self.var) + self.exp
      rand2 = z2 * sqrt(self.var) + self.exp

      self.values.append(rand1)
      self.values.append(rand2)
    return self.values.pop(0)

  def __str__(self):
    print(self.exp)
    print(self.var)
    return "did"

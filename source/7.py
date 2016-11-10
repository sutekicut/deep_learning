#!/usr/bin/env python
from libs.bandit import Bandit
from libs.greedy_method import GreedyMethod

class TestRunnner:
  def __init__(self, bandit: Bandit, method: GreedyMethod):
    self.bandit = bandit
    self.method = method
    self.count = 0
    self.total_reward = 0

  def exec(self, count):
    for i in range(0, count):
      selected_arm = self.method.select()

  def average(self):
    return (self.total_reward)

  def max_exp(self):
    return max(self.bandit.reward_exp)

if __name__ == "__main__":
  size = 10
  bandit = Bandit(size=size)
  test_runner = TestRunnner(bandit, GreedyMethod(size=size))
  print(test_runner.exec(10))


import re

from source.libs import normal_dis_random as ndr


class Bandit:
  # size: 腕の数
  # reward_exp_avg: 各行動に対する報酬の期待値の平均
  # reward_exp_var: 各行動に対する報酬の期待値の分散
  # reward_var: 各行動に対する報酬の分散
  def __init__(self, size=10, reward_exp_avg=0.0, reward_exp_var=1.0, reward_var=1.0):
    self.size = size
    self.rand_generator = []
    self.reward_exp = []
    random = ndr.NormalDistRandom(reward_exp_avg, reward_exp_var)

    for i in range(0, self.size):
      print(i)
      reward_exp = random.get_random()
      self.reward_exp.append(reward_exp)
      self.rand_generator.append(ndr.NormalDistRandom(reward_exp, reward_var))

  def select(self, i):
    return self.rand_generator[i].get_random()

if __name__ == "__main__":
  bandit = Bandit()
  print("input 0 - {last_num}, or q".format(last_num=bandit.size - 1.0))
  while True:
    line = input()
    if re.match(r"[0-9]+", line):
      print(bandit.select(int(line)))
    elif "q" == line:
      print(line)
      break
    else:
      print("input 0 - {last_num}, or q".format(last_num=bandit.size - 1.0))
  print("expected value")
  print(bandit.reward_exp)

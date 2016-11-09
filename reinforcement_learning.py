import normal_dis_random as ndr

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

    for i in self.size:
      print(i)
      reward_exp = random.get_random()
      self.reward_exp.append(reward_exp)
      self.rand_generator.append(ndr.NormalDistRandom(reward_exp, reward_var))

  def select(self, i):
    return self.rand_generator[i].get_random()


bandit = Bandit()
print("input %f" %bandit.size)
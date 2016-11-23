#!/usr/bin/env python
from libs.bandit import Bandit
from libs.bandit.greedy_method import GreedyMethod
from libs.bandit.softmax_mehod import SoftMaxMethod


class TestRunnner:
    def __init__(self, bandit: Bandit, method):
        self.bandit = bandit
        self.method = method
        self.count = 0
        self.total_reward = 0

    def exec(self, count):
        for i in range(0, count):
            selected_arm = self.method.select()
            # 選んだ腕の報酬
            reward = self.bandit.select(selected_arm)
            self.total_reward += reward
            self.method.reflect(selected_arm, reward)
        self.count += count

    # 得られた報酬の平均値
    def average(self):
        return (self.total_reward * 1.0) / self.count if self.count != 0 else 0

    # 報酬の期待値の最大値
    def max_exp(self):
        return max(self.bandit.reward_exp)

    # 最適度
    def optimality(self):
        return self.average() / self.max_exp()


if __name__ == "__main__":
    size = 10
    bandit = Bandit(size=size)

    test = []
    test.append(TestRunnner(bandit, GreedyMethod(size=size)))
    test.append(TestRunnner(bandit, GreedyMethod(size=size, epsilon=0.1)))
    test.append(TestRunnner(bandit=bandit, method=SoftMaxMethod(size=size, temperature=0.3)))

    for runner in test:
        print("----------------------------------")
        print("time   reward avg.   optimality")
        print("----------------------------------")
        for i in range(0, 20):
            runner.exec(100)
            print("{count}   {avg}  {optimality}".format(count=runner.count, avg=runner.average(),
                                                         optimality=runner.optimality()))

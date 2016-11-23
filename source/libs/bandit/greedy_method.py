import random as Random


class GreedyMethod:
    # size: n本腕バンディット問題のサイズ
    # epsilon: グリーディではなくランンダムに選択する確率
    # stepsize: nil以外を指定した場合、ステップサイズとして扱う
    def __init__(self, size=10, epsilon=0.0, stepsize=None):
        self.size = size
        self.epsilon = epsilon
        self.stepsize = stepsize
        self.times = [0] * size
        self.values = [0] * size

    # グリーディ法で腕を選ぶ
    # --
    # @return int i番目の選んだ腕

    # epsilonの確率でランダムに選択を行う
    # そうでない場合には、最も確率の高いと推定される行動を選ぶ
    def select(self):
        if Random.random() < self.epsilon:
            return Random.randint(0, self.size - 1)
        else:
            return self.values.index(max(self.values))

    # 得られた報酬を反映し、学習する
    # --
    # selected: 選んだ腕
    # value: 得られた報酬
    def reflect(self, selected: int, value: float):
        self.times[selected] += 1
        stepsize = self.stepsize if self.stepsize != None else (1.0 / self.times[selected])
        self.values[selected] += stepsize * (value - self.values[selected])

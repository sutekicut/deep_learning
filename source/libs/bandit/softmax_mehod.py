import random as Random
from math import exp


class SoftMaxMethod:
    # size: n本腕バンディット問題のサイズ
    # temperature: 温度(学習パラメータ)
    # stepsize: nil以外を指定した場合、stepsizeとして扱う
    def __init__(self, size=10, temperature=1.0, stepsize=None):
        self.size = size
        self.temperature = temperature
        self.stepsize = stepsize
        self.times = [0] * size
        self.values = [0] * size
        self.weights = [1.0] * size

    # ソフトマックス法で腕を選ぶ
    # ----------------------
    # 各腕の重みをexp(values[i]/temperature)として、重みに従った確率で腕を選ぶ
    # 価値が高いほど、重みが大きくなるので選ばれやすい
    # ただし、温度が高い場合、重みは相対的に小さくなり、他の行動が選ばれる確率が高くなる
    def select(self):
        total_weights = sum(self.weights)
        rand = Random.random() * total_weights
        selected = 0
        for i in range(0, self.size):
            if rand <= self.weights[i]:
                selected = i
                break
            else:
                rand -= self.weights[i]

        return selected

    # 得られた報酬を反映し、学習する
    # --------------------------
    # selected: 選んだ腕
    # value: 得られた報酬
    def reflect(self, selected: int, value: float):
        self.times[selected] += 1
        stepsize = self.stepsize if self.stepsize != None else (1.0 / self.times[selected])
        self.values[selected] += stepsize * (value - self.values[selected])
        self.weights[selected] = exp(self.values[selected] / self.temperature)
